#!/usr/bin/env python3
"""echo_hypothesis_test.py — pin down MA3's OSC echo routing.

Two hypotheses about what MA3 v2.3 does when EchoOutput=Yes on an OSC line:
  H1: MA3 sends echo to the line's DestinationIP:PORT (configured destination).
      → On loopback with our setup (Dest=127.0.0.1, PORT=8000) this loops back
        to MA3 itself, never reaching us.
  H2: MA3 sends echo back to the source IP:port of the inbound packet.
      → A single socket bound to a known port that BOTH sends AND listens
        will see the echo arrive on that same port.

This test binds ONE UDP socket to a known source port, sends /cmd "Echo TEST"
from it, then waits up to 1.5s for any incoming OSC packet.

  echo received  → H2 is correct. Fix is to make osc_client.py use a single
                   shared socket for send + receive.
  nothing        → H1 is correct (or some other issue). Need a different
                   topology — possibly a second outbound-only OSC line on a
                   port the MCP server isn't binding.

Run:
  cd WORKING/gma3-mcp-server-py
  source .venv/bin/activate
  python echo_hypothesis_test.py
"""
from __future__ import annotations

import socket
import struct
import sys
import time


def osc_string(s: str) -> bytes:
    """OSC-encoded string: null-terminated, padded to 4 bytes."""
    raw = s.encode("utf-8") + b"\x00"
    pad = (-len(raw)) % 4
    return raw + b"\x00" * pad


def build_cmd_message(command: str) -> bytes:
    """Build a single OSC message: address '/cmd', type 's', payload <command>."""
    return osc_string("/cmd") + osc_string(",s") + osc_string(command)


def parse_osc_packet(data: bytes) -> tuple[str, list[str]]:
    """Minimal OSC parse: read address, type tag string, and any string args."""
    def read_str(buf: bytes, off: int) -> tuple[str, int]:
        end = buf.index(b"\x00", off)
        s = buf[off:end].decode("utf-8", errors="replace")
        # advance past null + padding
        pad_end = ((end + 4) // 4) * 4
        return s, pad_end
    addr, off = read_str(data, 0)
    type_tag, off = read_str(data, off)
    args: list[str] = []
    if type_tag.startswith(","):
        for tag in type_tag[1:]:
            if tag == "s":
                a, off = read_str(data, off)
                args.append(a)
            elif tag in ("i", "f"):
                args.append(repr(struct.unpack(">i" if tag == "i" else ">f", data[off:off+4])[0]))
                off += 4
            else:
                args.append(f"<{tag}?>")
                break
    return addr, args


def main() -> int:
    target_host = "127.0.0.1"
    target_port = 8000        # MA3 OSC line PORT
    local_port  = 8001        # source port (same as in_port we want echo on)
    payload     = 'Echo "alchemease-hypothesis-test"'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("0.0.0.0", local_port))
    except OSError as e:
        print(f"FAIL: can't bind UDP/{local_port}: {e}")
        print("Hint: another process is holding it (the MCP server probe? a stale listener?). Kill and retry.")
        return 2

    print(f"single socket bound on 0.0.0.0:{local_port}")
    print(f"sending /cmd \"{payload}\" → {target_host}:{target_port}")
    msg = build_cmd_message(payload)
    t_send = time.monotonic()
    sock.sendto(msg, (target_host, target_port))

    sock.settimeout(1.5)
    received: list[tuple[float, tuple, bytes]] = []
    deadline = t_send + 1.5
    while time.monotonic() < deadline:
        try:
            sock.settimeout(max(0.05, deadline - time.monotonic()))
            data, addr = sock.recvfrom(8192)
            received.append((time.monotonic() - t_send, addr, data))
        except socket.timeout:
            break
        except OSError as e:
            print(f"recv error: {e}")
            break

    print()
    print("== result ==")
    if received:
        print(f"H2 SUPPORTED — MA3 echoed back to the sender's source port.")
        for rtt, addr, data in received:
            try:
                osc_addr, args = parse_osc_packet(data)
                print(f"  +{rtt*1000:6.1f} ms   from {addr[0]}:{addr[1]}   osc {osc_addr}  args={args}")
            except Exception as e:
                print(f"  +{rtt*1000:6.1f} ms   from {addr[0]}:{addr[1]}   raw={data!r} ({e})")
        return 0
    else:
        print("H2 NOT SUPPORTED — no packet arrived at the sender's source port.")
        print("Likely H1: MA3 sends echo to DestinationIP:PORT (configured destination),")
        print("which on loopback with our setup is 127.0.0.1:8000 — MA3's own listen port.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

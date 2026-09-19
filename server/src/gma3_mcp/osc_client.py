"""OSC client for grandMA3 — outbound `/cmd` + optional echo diagnostics.

MA3 OSC contract (live-verified 2026-05-27 on onPC 2.3.2.0; re-verify points
for 2.4.x tracked in NEXT_ACTIONS):

  * Server → MA3: UDP message, address `/cmd`, type 's', payload = command
    string. Single messages only — OSC Bundles are unsupported.
  * MA3 → Server: **event-driven only** (mapped Page/Fader/Key changes on the
    OSC line). There is NO built-in echo of command results —
    `EchoInput`/`EchoOutput` are System Monitor diagnostics, not transport.
  * A UDP send succeeding proves NOTHING about liveness (verified 2026-06-29:
    onPC closed, send still "succeeds"). Real liveness/queries live in
    roundtrip.py (Lua-file round-trip).

The echo listener below is therefore OPTIONAL diagnostics for two-machine
topologies where MA3's event-driven output is mapped at us. It is off by
default (config `ma3.osc.echo_listener`); on single-machine loopback it's
useless by construction (MA3 binds every OSC line's port once a session is
active, and no command results are ever emitted anyway).
"""
from __future__ import annotations

import logging
import threading
import time
from collections import deque
from contextlib import suppress

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

log = logging.getLogger(__name__)


class OSCClient:
    def __init__(self, host: str, out_port: int, in_port: int, cmd_address: str = "/cmd",
                 rate_per_sec: int = 50):
        self.host = host
        self.out_port = out_port
        self.in_port = in_port
        self.cmd_address = cmd_address
        self.client = SimpleUDPClient(host, out_port)
        self._rate_per_sec = rate_per_sec
        self._last_send_t = 0.0
        self._send_lock = threading.Lock()

        # Optional event-stream capture (two-machine diagnostics only)
        self._echo: deque[tuple[float, str, list]] = deque(maxlen=2000)  # (recv_time, address, args)
        self._echo_lock = threading.Lock()
        self._server: ThreadingOSCUDPServer | None = None
        self._server_thread: threading.Thread | None = None

    # ----- send -----

    def _rate_limit(self) -> None:
        min_gap = 1.0 / max(self._rate_per_sec, 1)
        with self._send_lock:
            dt = time.monotonic() - self._last_send_t
            if dt < min_gap:
                time.sleep(min_gap - dt)
            self._last_send_t = time.monotonic()

    def send_cmd(self, command: str) -> None:
        """Send a single MA3 command-line string. Single message, no bundles.

        Returning without an exception means ONLY that the datagram left this
        machine. It does NOT mean MA3 received or executed anything.
        """
        self._rate_limit()
        log.debug("OSC out → %s %r", self.cmd_address, command)
        self.client.send_message(self.cmd_address, command)

    # ----- optional event-stream listener (diagnostics) -----

    def start_echo_listener(self) -> bool:
        """Capture MA3's event-driven OSC output (mapped faders/keys) on in_port.

        NOT a command-result channel — see module docstring. Two-machine
        topologies only; on loopback the port is typically already bound by MA3.
        """
        if self._server is not None:
            return True
        try:
            dispatcher = Dispatcher()
            dispatcher.set_default_handler(self._on_message)
            bind_host = self.host if self.host != "127.0.0.1" else "0.0.0.0"
            self._server = ThreadingOSCUDPServer((bind_host, self.in_port), dispatcher)
            self._server_thread = threading.Thread(target=self._server.serve_forever, daemon=True, name="osc-events")
            self._server_thread.start()
            log.info("OSC event listener up on UDP %s:%d", bind_host, self.in_port)
            return True
        except OSError as e:
            log.warning("OSC event listener could not start: %s", e)
            self._server = None
            return False

    def stop_echo_listener(self) -> None:
        if self._server is not None:
            with suppress(Exception):
                self._server.shutdown()
            self._server = None
            self._server_thread = None

    def _on_message(self, address: str, *args) -> None:
        with self._echo_lock:
            self._echo.append((time.monotonic(), address, list(args)))

    def drain_echo_lines(self, since_t: float) -> list[tuple[str, list]]:
        with self._echo_lock:
            return [(addr, args) for (t, addr, args) in self._echo if t > since_t]

    # ----- diagnostics -----

    def udp_ping(self) -> dict:
        """Fire a harmless Echo and report ONLY that the datagram left.

        `udp_sent` is not liveness — a closed onPC still yields True. For real
        reachability use LuaFileRoundtrip.probe().
        """
        result: dict = {
            "udp_sent": False,
            "event_listener_up": self._server is not None,
            "note": "udp_sent≠liveness — UDP is connectionless; use the Lua-file round-trip probe",
        }
        try:
            self.send_cmd('Echo "alchemease-mcp-ping"')
            result["udp_sent"] = True
        except Exception as e:
            log.warning("OSC udp_ping failed: %s", e)
            result["error"] = str(e)
        return result

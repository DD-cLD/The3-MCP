"""Lua-file round-trip — the REAL reachability/query channel for grandMA3.

Why this exists (paid-for lessons, 2026-05-27 + 2026-06-29, see WORKING/MEMORY.md):

  * MA3 has NO built-in OSC echo of command results. `EchoInput`/`EchoOutput`
    on the OSC line are System Monitor diagnostics, not transport behavior.
    Outbound OSC is event-driven (fader/key mappings), never command replies.
  * A UDP send never raises whether or not onPC is listening, so "the send
    worked" (`udp_sent`) can NEVER prove liveness. Verified 2026-06-29: onPC
    fully closed still yielded out_ok:true in the old probe.
  * The one channel that genuinely requires MA3 to execute code is the
    Lua-file pattern proven by the alchemease_snapshot plugin: send a
    `Lua "..."` command that writes a sentinel file into the console's
    gma3_library folder; poll-read it from Python; nonce ties response
    to request; wall-clock delta = RTT.

Topology constraint: this only works when the MCP server and MA3 share a
filesystem — single-machine onPC dev (the current setup), or a mounted
console share. On a two-machine rig (console at FOH, server on laptop)
round-trip queries need the Phase-2 push-channel plugin instead.

Generated-Lua ground rules (MA3 CLI quoting is unforgiving):
  * The whole payload rides inside `Lua "<code>"` — so the code may contain
    NO double quotes. Lua single quotes + string.char(34) cover everything.
  * No semicolons — `;` batches commands at the MA3 command line (verified
    2.4.2.2, 2026-07-04); a semicolon inside the code would split it.
    Lua needs no statement separators — whitespace is enough.
  * No backslashes — nothing in the payload should need CLI escaping.
  * Single line, and keep it well under one UDP datagram.

File format (plain text, NOT JSON — deliberately: emitting valid JSON from
generated one-line Lua means escaping arbitrary tostring() output, which is
exactly the kind of fragile quoting this module exists to avoid; the MCP
tools return JSON to the agent, the wire format stays dumb):

    ALCHE_RT_V1
    nonce=<12 hex chars>
    ok=<true|false>            <- pcall success of the user expression
    value=<tostring(result)>   <- everything to EOF, may span lines

Only Enums/functions verified in the live api dump (2026-05-27, 242 globals)
are used in generated code: GetPath, Enums.PathType.Library, Version,
HostType, HostOS, HostRevision. Path separator is a hardcoded '/' — Lua's
io.open accepts it on Windows as well, and it removes a failure mode.
"""
from __future__ import annotations

import logging
import os
import re
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

log = logging.getLogger(__name__)

PROTOCOL_TAG = "ALCHE_RT_V1"
BASENAME = "alchemease_rt.txt"

# Expression that identifies the console — every call is inside pcall, so a
# missing function on some build degrades to ok=false + error text, while the
# file write (the liveness proof) still happens.
PROBE_EXPR = (
    "'v='..tostring(Version())"
    "..' host='..tostring(HostType())"
    "..' os='..tostring(HostOS())"
    "..' rev='..tostring(HostRevision())"
    "..' lua='.._VERSION"
)

_FORBIDDEN = (
    ('"', 'double quote — MA3 CLI wraps the code in `Lua "..."`; use Lua single quotes'),
    (";", "semicolon — the MA3 command line batches on `;` and would split the code"),
    ("\n", "newline — generated command must be a single line"),
    ("\\", "backslash — no CLI escaping is safe on this transport"),
)

MAX_EXPR_LEN = 1800  # loopback MTU is 16k; 1800 leaves rich experiments room while staying sane


def validate_expr(expr: str) -> None:
    """Raise ValueError if a Lua expression can't ride the /cmd transport."""
    if not expr or not expr.strip():
        raise ValueError("empty Lua expression")
    for ch, why in _FORBIDDEN:
        if ch in expr:
            raise ValueError(f"Lua expression contains forbidden {why}")
    if len(expr) > MAX_EXPR_LEN:
        raise ValueError(f"Lua expression too long ({len(expr)} > {MAX_EXPR_LEN} chars)")


def build_roundtrip_lua(nonce: str, expr: str, basename: str = BASENAME) -> str:
    """One-line Lua: evaluate `expr` under pcall, write the sentinel file.

    Statements are separated by spaces only (valid Lua; no `;` allowed on this
    transport). tmp-write + os.remove + os.rename ≈ atomic replace on POSIX
    and survives Windows' no-overwrite rename.
    """
    validate_expr(expr)
    if not re.fullmatch(r"[0-9a-f]{12}", nonce):
        raise ValueError("nonce must be 12 lowercase hex chars")
    return (
        "local d=GetPath(Enums.PathType.Library) "
        "local n=string.char(10) "
        f"local ok,v=pcall(function() return ({expr}) end) "
        "if d then "
        f"local p=d..'/{basename}' "
        "local f=io.open(p..'.tmp','w') "
        "if f then "
        f"f:write('{PROTOCOL_TAG}'..n..'nonce={nonce}'..n..'ok='..tostring(ok)..n..'value='..tostring(v)) "
        "f:close() "
        "pcall(os.remove,p) "
        "os.rename(p..'.tmp',p) "
        "end end"
    )


@dataclass
class RoundtripResult:
    roundtrip_ok: bool          # file arrived with our nonce → console EXECUTED code (liveness)
    ok: bool                    # pcall of the expression succeeded
    value: str | None
    rtt_ms: float | None
    udp_sent: bool
    error: str | None
    nonce: str
    lua_sent: str | None = field(default=None, repr=False)


class LuaFileRoundtrip:
    """Send `Lua "..."` via a provided sender; poll the shared exchange file."""

    def __init__(self, send_cmd: Callable[[str], None], exchange_dir: str,
                 out_port: int | None = None, basename: str = BASENAME):
        self._send = send_cmd
        self.exchange_dir = str(Path(os.path.expanduser(exchange_dir)))
        self.basename = basename
        self.out_port = out_port  # for diagnostics text only

    # ----- internals -----

    @property
    def exchange_path(self) -> Path:
        return Path(self.exchange_dir) / self.basename

    def _checklist(self, timeout: float) -> str:
        port = self.out_port if self.out_port is not None else "<out_port>"
        return (
            f"no round-trip file within {timeout:.1f}s. Checklist: "
            "(1) onPC/console running? "
            "(2) Session ACTIVE in the Network window (loopback session is fine — "
            "without a session the OSC subsystem stays dormant)? "
            "(3) Menu > In & Out > OSC master: Enable Input=Yes AND Interface set to a real "  # scrub-ok: In & Out
            "NIC (lo0/127.0.0.1 for local), not <None>? "
            f"(4) OSC line: Receive=Yes, ReceiveCommand=Yes, Port={port}? "
            f"(5) exchange dir really the console's gma3_library ({self.exchange_dir})?"
        )

    @staticmethod
    def _parse(text: str) -> dict | None:
        lines = text.split("\n")
        if not lines or lines[0].strip() != PROTOCOL_TAG:
            return None
        out: dict = {}
        for i, line in enumerate(lines[1:], start=1):
            if line.startswith("nonce="):
                out["nonce"] = line[len("nonce="):].strip()
            elif line.startswith("ok="):
                out["ok"] = line[len("ok="):].strip() == "true"
            elif line.startswith("value="):
                out["value"] = "\n".join([line[len("value="):]] + lines[i + 1:])
                break
        if "nonce" not in out:
            return None
        return out

    def _consume_if_match(self, nonce: str) -> dict | None:
        p = self.exchange_path
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except (FileNotFoundError, OSError):
            return None
        parsed = self._parse(text)
        if parsed is None or parsed.get("nonce") != nonce:
            # stale or foreign response — clear it so it can't mask a timeout
            try:
                p.unlink()
            except OSError:
                pass
            return None
        try:
            p.unlink()
        except OSError:
            pass
        return parsed

    # ----- public -----

    def query(self, expr: str, *, timeout: float = 4.0, poll_interval: float = 0.03) -> RoundtripResult:
        """Evaluate a Lua EXPRESSION on the console; return its tostring()."""
        nonce = uuid.uuid4().hex[:12]
        lua = build_roundtrip_lua(nonce, expr, self.basename)  # raises ValueError on bad expr
        cmd = f'Lua "{lua}"'

        # clear any leftover file so a stale response can't win
        try:
            self.exchange_path.unlink()
        except OSError:
            pass

        udp_sent = False
        t0 = time.monotonic()
        try:
            self._send(cmd)
            udp_sent = True
        except Exception as e:  # UDP raising at all is unusual — config-level problem
            return RoundtripResult(
                roundtrip_ok=False, ok=False, value=None, rtt_ms=None,
                udp_sent=False, error=f"OSC send failed: {e}", nonce=nonce, lua_sent=cmd,
            )

        deadline = t0 + timeout
        while time.monotonic() < deadline:
            parsed = self._consume_if_match(nonce)
            if parsed is not None:
                rtt = (time.monotonic() - t0) * 1000.0
                return RoundtripResult(
                    roundtrip_ok=True,
                    ok=bool(parsed.get("ok")),
                    value=parsed.get("value"),
                    rtt_ms=round(rtt, 1),
                    udp_sent=udp_sent,
                    error=None if parsed.get("ok") else f"Lua pcall failed: {parsed.get('value')}",
                    nonce=nonce,
                    lua_sent=cmd,
                )
            time.sleep(poll_interval)

        return RoundtripResult(
            roundtrip_ok=False, ok=False, value=None, rtt_ms=None,
            udp_sent=udp_sent, error=self._checklist(timeout), nonce=nonce, lua_sent=cmd,
        )

    def probe(self, *, timeout: float = 2.5) -> dict:
        """Liveness + identity probe. `lua_roundtrip_ok` is THE liveness bit;
        `udp_sent` only means the datagram left this machine (NOT liveness —
        a closed onPC still yields udp_sent=true)."""
        r = self.query(PROBE_EXPR, timeout=timeout)
        return {
            "udp_sent": r.udp_sent,
            "lua_roundtrip_ok": r.roundtrip_ok,
            "rtt_ms": r.rtt_ms,
            "console_info": r.value if r.roundtrip_ok and r.ok else None,
            "exchange_file": str(self.exchange_path),
            "error": r.error,
        }

"""Lua-file round-trip tests — run against a fake MA3 console.

The fake binds a real UDP socket and parses real OSC datagrams, so the whole
Python-side path (OSC send → poll → parse → nonce check → cleanup) is
exercised end-to-end. What it can NOT prove is that the generated Lua runs on
a real console — that's the live-wire test in the working notes (onPC 2.4.2.2,
loopback session).
"""
from __future__ import annotations

import re
import threading
import time
from pathlib import Path

import pytest
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer

from gma3_mcp.osc_client import OSCClient
from gma3_mcp.roundtrip import (
    BASENAME,
    PROBE_EXPR,
    PROTOCOL_TAG,
    LuaFileRoundtrip,
    build_roundtrip_lua,
    validate_expr,
)

NONCE_RE = re.compile(r"nonce=([0-9a-f]{12})")


class FakeMA3:
    """Receives `/cmd` OSC datagrams and answers the way the generated Lua
    would: writes the sentinel file (tmp + rename) into the exchange dir."""

    def __init__(self, exchange_dir: Path):
        self.exchange_dir = exchange_dir
        self.mode = "respond"          # respond | lua_error | silent | wrong_nonce
        self.value = "FAKE v2.4.2.2 host=onPC os=mac"
        self.delay = 0.02
        self.received: list[str] = []
        dispatcher = Dispatcher()
        dispatcher.map("/cmd", self._on_cmd)
        self._server = ThreadingOSCUDPServer(("127.0.0.1", 0), dispatcher)
        self.port = self._server.server_address[1]
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def close(self):
        self._server.shutdown()

    # -- behavior --

    def _on_cmd(self, address: str, *args):
        payload = args[0] if args else ""
        self.received.append(payload)
        if self.mode == "silent":
            return
        m = NONCE_RE.search(payload)
        if not m:
            return
        nonce = "beefbeefbeef" if self.mode == "wrong_nonce" else m.group(1)
        ok = "false" if self.mode == "lua_error" else "true"
        value = "attempt to call a nil value (global 'Nope')" if self.mode == "lua_error" else self.value
        time.sleep(self.delay)
        tmp = self.exchange_dir / (BASENAME + ".tmp")
        tmp.write_text(f"{PROTOCOL_TAG}\nnonce={nonce}\nok={ok}\nvalue={value}", encoding="utf-8")
        tmp.replace(self.exchange_dir / BASENAME)


@pytest.fixture()
def fake(tmp_path):
    f = FakeMA3(tmp_path)
    yield f
    f.close()


@pytest.fixture()
def rt(fake, tmp_path):
    osc = OSCClient(host="127.0.0.1", out_port=fake.port, in_port=fake.port + 1)
    return LuaFileRoundtrip(send_cmd=osc.send_cmd, exchange_dir=str(tmp_path), out_port=fake.port)


# ---------- generator / validator (pure) ----------

def test_generated_lua_is_transport_safe():
    lua = build_roundtrip_lua("0123456789ab", "1+1")
    assert '"' not in lua
    assert ";" not in lua
    assert "\\" not in lua
    assert "\n" not in lua
    assert "0123456789ab" in lua
    assert BASENAME in lua
    assert PROTOCOL_TAG in lua
    # the safety net: expression rides inside pcall
    assert "pcall(function() return (1+1) end)" in lua


def test_probe_expr_is_itself_transport_safe():
    validate_expr(PROBE_EXPR)  # must not raise


@pytest.mark.parametrize("bad,why", [
    ('tostring("x")', "double quote"),
    ("a=1; b=2", "semicolon"),
    ("1+\n1", "newline"),
    ("'a\\n'", "backslash"),
    ("", "empty"),
    ("x" * 1801, "too long"),  # MAX_EXPR_LEN raised 600->1800 (2026-07-04); fixture must exceed it
])
def test_validate_expr_rejections(bad, why):
    with pytest.raises(ValueError):
        validate_expr(bad)


def test_bad_nonce_rejected():
    with pytest.raises(ValueError):
        build_roundtrip_lua("SHOUTYNONCE!", "1+1")


# ---------- end-to-end against the fake ----------

def test_probe_happy(fake, rt):
    result = rt.probe(timeout=2.0)
    assert result["udp_sent"] is True
    assert result["lua_roundtrip_ok"] is True
    assert result["rtt_ms"] is not None and result["rtt_ms"] >= 0
    assert "FAKE" in result["console_info"]
    assert result["error"] is None
    # the wire saw exactly one transport-safe Lua command
    assert len(fake.received) == 1
    inner = fake.received[0]
    assert inner.startswith('Lua "') and inner.endswith('"')
    assert ";" not in inner[5:-1] and '"' not in inner[5:-1]


def test_probe_timeout_reports_checklist_and_fails(fake, rt):
    fake.mode = "silent"
    result = rt.probe(timeout=0.3)
    assert result["udp_sent"] is True          # datagram left — proves nothing
    assert result["lua_roundtrip_ok"] is False  # THE liveness bit
    assert "Checklist" in result["error"]
    assert str(fake.port) in result["error"]    # names the port to check
    assert result["console_info"] is None


def test_query_lua_error_still_proves_liveness(fake, rt):
    fake.mode = "lua_error"
    r = rt.query("Nope()", timeout=2.0)
    assert r.roundtrip_ok is True   # file arrived → console executed code
    assert r.ok is False            # but the expression failed
    assert "pcall failed" in r.error
    assert "nil value" in r.error


def test_stale_file_is_cleared_and_fresh_response_wins(fake, rt, tmp_path):
    stale = tmp_path / BASENAME
    stale.write_text(f"{PROTOCOL_TAG}\nnonce=deaddeaddead\nok=true\nvalue=STALE", encoding="utf-8")
    r = rt.query("1+1", timeout=2.0)
    assert r.roundtrip_ok is True
    assert r.value != "STALE"
    assert not stale.exists()       # consumed after read


def test_exchange_file_consumed_after_success(fake, rt, tmp_path):
    r = rt.query("2+2", timeout=2.0)
    assert r.roundtrip_ok is True
    assert not (tmp_path / BASENAME).exists()


def test_multiline_value_roundtrips(fake, rt):
    fake.value = "line one\nline two\nline three"
    r = rt.query("1+1", timeout=2.0)
    assert r.ok is True
    assert r.value == "line one\nline two\nline three"


def test_wrong_nonce_never_matches(fake, rt):
    fake.mode = "wrong_nonce"
    r = rt.query("1+1", timeout=0.4)
    assert r.roundtrip_ok is False
    assert "Checklist" in r.error


def test_unsafe_expr_never_hits_the_wire(fake, rt):
    with pytest.raises(ValueError):
        rt.query('tostring("boom")', timeout=0.2)
    time.sleep(0.05)
    assert fake.received == []

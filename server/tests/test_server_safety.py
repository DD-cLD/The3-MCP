"""Exercise exposed tool gates with fake transports; never contact a console."""
import asyncio
import os
import time
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from gma3_mcp import server
from gma3_mcp.config import Config, SafetyConfig


@pytest.fixture
def app_factory(monkeypatch):
    sent = []
    results = {}

    class FakeOSC:
        def __init__(self, **kwargs):
            pass

        def send_cmd(self, command):
            sent.append(command)

    class FakeRoundtrip:
        def __init__(self, **kwargs):
            pass

        def query(self, expression, *, timeout):
            sent.append(expression)
            return SimpleNamespace(
                **{
                    "udp_sent": True, "roundtrip_ok": True, "ok": True,
                    "value": "fake-response", "rtt_ms": 0, "error": None,
                    **results,
                },
            )

    monkeypatch.setattr(server, "OSCClient", FakeOSC)
    monkeypatch.setattr(server, "LuaFileRoundtrip", FakeRoundtrip)

    def make(*, roundtrip_result=None, **safety):
        if roundtrip_result:
            results.update(roundtrip_result)
        app = server.build_app(Config(safety=SafetyConfig(**safety)))

        def call(name, **kwargs):
            tool = asyncio.run(app.get_tool(name))
            return tool.fn(**kwargs)

        return call, sent

    return make


def test_raw_lua_reports_roundtrip_send_failure(app_factory, tmp_path):
    enable_file = tmp_path / "LIVE_ENABLE"
    enable_file.touch()
    call, sent = app_factory(
        default_mode="rehearsal", live_enable_file=str(enable_file),
        roundtrip_result={
            "udp_sent": False, "roundtrip_ok": False, "ok": False,
            "value": None, "rtt_ms": None, "error": "OSC send failed: fake failure",
        },
    )
    call("confirm_gate", command='Lua "1+1"')
    out = call("send_lua", code="1+1")
    assert out["sent"] is False and out["udp_sent"] is False
    assert out["roundtrip_ok"] is False and out["ok"] is False
    assert out["error"] == "OSC send failed: fake failure"
    assert sent == ["1+1"]  # one attempted query; fake transport has no network
    assert call("send_lua", code="1+1")["needs_confirm"] is True


@pytest.mark.parametrize("code", [
    "tostring(Version())",
    "Cmd('store Group 101')",
    "Cmd('delete Group 101')",
    "SetVar (UserVars(),'example',1)",
    "_G['Cmd']('Go+ Sequence 1')",
    "os.remove('example.txt')",
])
@pytest.mark.parametrize("want_result", [True, False])
def test_dry_run_never_transports_caller_lua(app_factory, code, want_result):
    call, sent = app_factory()
    out = call("send_lua", code=code, want_result=want_result)
    assert out["sent"] is False and out["dry_run"] is True
    assert out["tier"] == 3
    assert sent == []


@pytest.mark.parametrize("mode", ["rehearsal", "live"])
def test_raw_lua_needs_fresh_interlock_and_exact_single_use_grant(app_factory, tmp_path, mode):
    enable_file = tmp_path / "LIVE_ENABLE"
    call, sent = app_factory(
        default_mode=mode, live_enable_file=str(enable_file),
        require_confirm_for_tier2=False, require_confirm_for_tier3=False,
    )
    code = "tostring(Version())"
    command = f'Lua "{code}"'
    assert call("send_lua", code=code)["needs_live_enable"] is True
    enable_file.touch()
    assert call("send_lua", code=code)["needs_confirm"] is True
    call("confirm_gate", command='Lua "1+1"')
    assert call("send_lua", code=code)["needs_confirm"] is True
    call("confirm_gate", command=command)
    assert call("send_lua", code=code)["sent"] is True
    assert call("send_lua", code=code)["needs_confirm"] is True
    assert sent == [code]


@pytest.mark.parametrize("file_state", ["missing", "stale", "future", "directory"])
def test_invalid_live_enable_blocks_even_with_grant(app_factory, tmp_path, file_state):
    enable_file = tmp_path / "LIVE_ENABLE"
    if file_state == "directory":
        enable_file.mkdir()
    elif file_state != "missing":
        enable_file.touch()
        stamp = time.time() + (300 if file_state == "future" else -300)
        os.utime(enable_file, (stamp, stamp))
    call, sent = app_factory(default_mode="live", live_enable_file=str(enable_file))
    call("confirm_gate", command='Lua "1+1"')
    out = call("send_lua", code="1+1", want_result=False)
    assert out["sent"] is False and out["needs_live_enable"] is True
    assert sent == []


@pytest.mark.parametrize("values", [
    {"default_mode": "dry-run"},
    {"default_mode": "unrestricted"},
    {"live_enable_freshness_seconds": 0},
    {"live_enable_freshness_seconds": -1},
])
def test_invalid_safety_configuration_is_rejected(values):
    with pytest.raises(ValidationError):
        SafetyConfig(**values)

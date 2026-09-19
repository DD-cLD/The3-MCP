"""install_plugin flow + hook host surface (P1 remainder, 2026-07-05).

Pure-logic tests: injected senders, tmp dirs, fake clock. No OSC, no console.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from gma3_mcp.plugins import (
    HOOK_HOST_LUA,
    HOOK_HOST_NAME,
    InstallGovernor,
    approval_command,
    hook_call_expr,
    install_plugin_flow,
    plan_steps,
    render_plugin_xml,
    scan_lua_source,
    slot_warnings,
    validate_plugin_name,
)
from gma3_mcp.safety import classify

DENY = ["LoadShow", "Delete User", "Network", "Reset"]
LUA_OK = "local function Main() Printf('hi') end\nreturn Main\n"


# ---------- validation ----------

def test_name_rules():
    assert validate_plugin_name("alchemease_hooks") is None
    assert validate_plugin_name("A1_b2") is None
    for bad in ("", "1abc", "has space", "dash-name", "x" * 65, "dot.name"):
        assert validate_plugin_name(bad) is not None


def test_gpdf_is_blocked_any_case():
    assert any("GetPresetDataFast" in p for p in scan_lua_source("x = GetPresetDataFast(1)", DENY))
    assert scan_lua_source("y = getpresetdatafast(2)", DENY)  # case-insensitive


def test_deny_words_word_boundary_in_source():
    # Cmd('Reset ...') embedded in a plugin body must block…
    assert scan_lua_source("Cmd('Reset Output')", DENY)
    # …but 'Preset' must NOT trip the 'Reset' entry (the live 2026-07-04 lesson)
    assert scan_lua_source("Cmd('Store Preset 4.101')", DENY) == []


def test_empty_source_blocked():
    assert scan_lua_source("   ", DENY)


# ---------- rendering + gate ----------

def test_xml_shape_is_userplugin():
    xml = render_plugin_xml("foo", data_version="2.4.2.2")
    assert "<UserPlugin " in xml and "<Plugin " not in xml  # concept plugin-xml-schema
    assert 'Path="foo"' in xml
    assert 'FileName="foo.lua"' in xml
    assert 'DataVersion="2.4.2.2"' in xml


def test_gated_install_dry_run_preview_threads_data_version():
    """Review nit 2026-07-05: DataVersion comes from config via the tool layer —
    the preview must carry the caller's value, and dry_run must not consult
    approvals at all."""
    from gma3_mcp.plugins import gated_install

    class _BoomApprovals:
        def consume(self, command, tier):  # pragma: no cover - must never run
            raise AssertionError("approvals consulted in dry_run")

    out = gated_install(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=False,
        install_dir="/nonexistent", default_mode="dry_run", require_confirm=True,
        deny_words=DENY, approvals=_BoomApprovals(),
        governor=InstallGovernor(cooldown_seconds=5.0, now=lambda: 0.0),
        send_cmd=lambda c: (_ for _ in ()).throw(AssertionError("sent in dry_run")),
        query=None, data_version="9.8.7.6",
    )
    assert out["dry_run"] is True and out["sent"] is False
    assert 'DataVersion="9.8.7.6"' in out["xml_preview"]


def test_flow_written_xml_carries_data_version(tmp_path):
    """Live-path counterpart to the dry_run preview pin: the .xml actually
    written to disk must carry the threaded DataVersion (review test-gap #2)."""
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=None, run_after=False,
        install_dir=str(tmp_path), send_cmd=lambda c: None, query=None,
        governor=InstallGovernor(cooldown_seconds=5.0, now=lambda: 0.0),
        deny_words=DENY, data_version="9.8.7.6",
    )
    assert r.ok
    xml_text = (tmp_path / "foo" / "foo.xml").read_text()
    assert 'DataVersion="9.8.7.6"' in xml_text


def test_approval_command_binds_content_hash():
    a = approval_command("foo", 5, False, "src-one")
    b = approval_command("foo", 5, False, "src-two")
    c = approval_command("foo", 6, False, "src-one")
    d = approval_command("foo", 5, False, "src-one", xml_source="<UserPlugin/>")
    assert len({a, b, c, d}) == 4  # source, slot, AND xml all change the gate (review M1)
    assert a.startswith("InstallPlugin foo Slot 5 Run 0 Sha ")


def test_classifier_knows_synthetic_installplugin():
    cls = classify(approval_command("foo", 5, True, LUA_OK), DENY)
    assert cls.tier == 2


# ---------- governor ----------

def test_governor_cooldown():
    t = {"now": 100.0}
    g = InstallGovernor(cooldown_seconds=5.0, now=lambda: t["now"])
    assert g.check() == 0.0
    g.mark()
    t["now"] = 102.0
    assert g.check() == pytest.approx(3.0)
    t["now"] = 105.1
    assert g.check() == 0.0


# ---------- plan + warnings ----------

def test_plan_steps_shapes():
    assert plan_steps("foo", None, False) == ["ReloadAllPlugins"]
    assert plan_steps("foo", 7, False) == ["ReloadAllPlugins", 'Import Plugin 7 "foo"']
    assert plan_steps("foo", 7, True) == ["ReloadAllPlugins", 'Import Plugin 7 "foo"', "Plugin 7"]


def test_slot_reservation_warnings():
    assert any("1-20" in w for w in slot_warnings("alchemease_x", 30))
    assert any("21+" in w for w in slot_warnings("showplugin", 3))
    assert any("EMPTY" in w for w in slot_warnings("alchemease_x", 5))
    assert any("files-only" in w for w in slot_warnings("foo", None))


# ---------- flow ----------

def _fake_query_ok(name="foo"):
    def q(lua, *, timeout):
        value = "false" if "~= nil" in lua else name
        return SimpleNamespace(roundtrip_ok=True, ok=True, value=value, rtt_ms=30.0, error=None)
    return q


def test_flow_writes_pair_and_sends_in_order(tmp_path):
    sent: list[str] = []
    g = InstallGovernor(cooldown_seconds=5.0, now=lambda: 0.0)
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=True,
        install_dir=str(tmp_path), send_cmd=sent.append, query=_fake_query_ok(),
        governor=g, deny_words=DENY,
    )
    assert r.ok
    assert (tmp_path / "foo" / "foo.lua").read_text() == LUA_OK
    assert "<UserPlugin " in (tmp_path / "foo" / "foo.xml").read_text()
    assert sent == ["ReloadAllPlugins", 'Import Plugin 7 "foo"', "Plugin 7"]
    assert r.verify and r.verify["materialized"] is True


def test_flow_files_only_when_no_slot(tmp_path):
    sent: list[str] = []
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=None, run_after=False,
        install_dir=str(tmp_path), send_cmd=sent.append, query=_fake_query_ok(),
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert r.ok and sent == ["ReloadAllPlugins"] and r.verify is None


def test_flow_verifies_before_optional_run(tmp_path):
    events = []

    def query(lua, *, timeout):
        preflight = "~= nil" in lua
        events.append("preflight" if preflight else "verify")
        return SimpleNamespace(roundtrip_ok=True, ok=True, value="false" if preflight else "foo")

    result = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=True,
        install_dir=str(tmp_path), send_cmd=events.append, query=query,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert result.ok
    assert events == ["preflight", "ReloadAllPlugins", 'Import Plugin 7 "foo"', "verify", "Plugin 7"]


@pytest.mark.parametrize("state", ["occupied", "unreachable", "query-error", "no-query"])
def test_flow_preflight_failure_prevents_install_changes(tmp_path, state):
    sent = []

    def query(lua, *, timeout):
        if state == "query-error":
            raise OSError("fake read failure")
        return SimpleNamespace(roundtrip_ok=state != "unreachable", ok=True, value="true")

    result = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=True,
        install_dir=str(tmp_path), send_cmd=sent.append,
        query=None if state == "no-query" else query,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not result.ok and result.error
    assert sent == [] and list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("state", ["wrong-name", "empty", "timeout", "lua-error", "query-error"])
def test_flow_failed_post_verify_never_runs_slot(tmp_path, state):
    sent = []

    def query(lua, *, timeout):
        if "~= nil" in lua:
            return SimpleNamespace(roundtrip_ok=True, ok=True, value="false")
        if state == "query-error":
            raise OSError("fake verify failure")
        value = {"wrong-name": "other", "empty": "nil"}.get(state, "foo")
        return SimpleNamespace(roundtrip_ok=state != "timeout", ok=state != "lua-error", value=value)

    result = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=True,
        install_dir=str(tmp_path), send_cmd=sent.append, query=query,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not result.ok and "not run" in result.error
    assert sent == ["ReloadAllPlugins", 'Import Plugin 7 "foo"']


def test_flow_refuses_gpdf_before_touching_disk(tmp_path):
    r = install_plugin_flow(
        name="killer", lua_source="GetPresetDataFast()", xml_source=None, slot=1,
        run_after=False, install_dir=str(tmp_path), send_cmd=lambda c: None,
        query=None, governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and "GetPresetDataFast" in r.error
    assert not (tmp_path / "killer").exists()


def test_flow_respects_cooldown(tmp_path):
    t = {"now": 100.0}
    g = InstallGovernor(cooldown_seconds=5.0, now=lambda: t["now"])
    g.mark()
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=None, run_after=False,
        install_dir=str(tmp_path), send_cmd=lambda c: None, query=None,
        governor=g, deny_words=DENY,
    )
    assert not r.ok and "cooldown" in r.error
    assert not (tmp_path / "foo").exists()


def test_flow_verify_reports_empty_slot(tmp_path):
    def q(lua, *, timeout):
        value = "false" if "~= nil" in lua else "nil"
        return SimpleNamespace(roundtrip_ok=True, ok=True, value=value, rtt_ms=30.0, error=None)
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=False,
        install_dir=str(tmp_path), send_cmd=lambda c: None, query=q,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and r.verify["materialized"] is False


def test_flow_send_failure_stops_sequence(tmp_path):
    calls: list[str] = []

    def bad_send(cmd: str) -> None:
        calls.append(cmd)
        if cmd.startswith("Import"):
            raise OSError("socket down")

    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=True,
        install_dir=str(tmp_path), send_cmd=bad_send, query=_fake_query_ok(),
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and "Import" in r.error
    assert calls == ["ReloadAllPlugins", 'Import Plugin 7 "foo"']  # Plugin 7 never sent


# ---------- hook host ----------

def test_hook_host_source_is_clean_and_transport_safe():
    assert scan_lua_source(HOOK_HOST_LUA, DENY) == []
    assert HOOK_HOST_NAME == "alchemease_hooks"
    assert "HookObjectChange(" in HOOK_HOST_LUA and "Unhook(" in HOOK_HOST_LUA
    assert "UnhookObjectChange" not in HOOK_HOST_LUA  # does not exist (concept hook-api-surface)


def test_hook_call_expr_shapes():
    e = hook_call_expr("add", "Sequence 2")
    assert e == "tostring(_G.alchemease_hooks_api and _G.alchemease_hooks_api.add('Sequence 2') or 'host-not-active')"
    assert ";" not in e and '"' not in e and "\\" not in e and "\n" not in e
    assert hook_call_expr("list") is not None
    assert hook_call_expr("drop", "x") is None            # unknown fn
    assert hook_call_expr("add", "bad;ref") is None       # transport-unsafe ref
    assert hook_call_expr("add", "quote'ref") is None     # would need escaping
    assert hook_call_expr("add", "Sequence 2\n") is None  # fullmatch (review m3)


# ---------- review fixes 2026-07-05 (B1, M1, M2, m1-m5) ----------

def test_classify_gpdf_denied_everywhere():
    # B1: the console-killer must die at the classifier, not just in source scans
    assert classify('Lua "tostring(GetPresetDataFast(1))"', DENY).tier == 99
    assert classify("Lua 'getpresetdatafast()'", DENY).tier == 99
    assert classify("GetPresetDataFast", DENY).tier == 99


def test_name_rejects_trailing_newline():
    assert validate_plugin_name("foo\n") is not None  # m3: match→fullmatch


def test_xml_source_must_uphold_pair_contract(tmp_path):
    from gma3_mcp.plugins import validate_xml_source
    good = render_plugin_xml("foo")
    assert validate_xml_source("foo", good) is None
    assert validate_xml_source("foo", None) is None
    assert validate_xml_source("foo", good.replace('Path="foo"', 'Path="bar"')) is not None
    assert validate_xml_source("foo", good.replace('FileName="foo.lua"', 'FileName="evil.lua"')) is not None
    assert validate_xml_source("foo", "<Plugin ContentType='Usercontent'/>") is not None
    # and the flow refuses it before touching disk
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=good.replace('Path="foo"', 'Path="bar"'),
        slot=None, run_after=False, install_dir=str(tmp_path), send_cmd=lambda c: None,
        query=None, governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and not (tmp_path / "foo").exists()


def test_verify_occupied_slot_reports_not_materialized(tmp_path):
    # M2: read-back finding a different occupant must NOT count as materialized
    def q(lua, *, timeout):
        value = "false" if "~= nil" in lua else "squatter"
        return SimpleNamespace(roundtrip_ok=True, ok=True, value=value, rtt_ms=30.0, error=None)
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=False,
        install_dir=str(tmp_path), send_cmd=lambda c: None, query=q,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and r.verify["materialized"] is False
    assert "occupied" in r.verify.get("warning", "")


def test_slot_out_of_range_blocks(tmp_path):
    for bad in (0, -3, 10000):
        r = install_plugin_flow(
            name="foo", lua_source=LUA_OK, xml_source=None, slot=bad, run_after=False,
            install_dir=str(tmp_path), send_cmd=lambda c: None, query=None,
            governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
        )
        assert not r.ok and "out of range" in r.error  # m1: block, not warn


def test_flow_write_failure_is_structured_not_raised(tmp_path):
    squatter = tmp_path / "foo"
    squatter.write_text("i am a file, not a folder")  # mkdir will fail
    r = install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=None, run_after=False,
        install_dir=str(tmp_path), send_cmd=lambda c: None, query=None,
        governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and "filesystem write failed" in r.error  # m2


def test_flow_refuses_hook_host_run_after(tmp_path):
    r = install_plugin_flow(
        name=HOOK_HOST_NAME, lua_source=HOOK_HOST_LUA, xml_source=None, slot=5,
        run_after=True, install_dir=str(tmp_path), send_cmd=lambda c: None,
        query=None, governor=InstallGovernor(cooldown_seconds=0.0), deny_words=DENY,
    )
    assert not r.ok and "never be auto-run" in r.error  # m5
    assert not (tmp_path / HOOK_HOST_NAME).exists()


def test_governor_marks_after_send_failure(tmp_path):
    # pins current behavior: a failed attempt still starts the cooldown window
    t = {"now": 100.0}
    g = InstallGovernor(cooldown_seconds=5.0, now=lambda: t["now"])

    def bad_send(cmd: str) -> None:
        raise OSError("down")

    install_plugin_flow(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=False,
        install_dir=str(tmp_path), send_cmd=bad_send, query=_fake_query_ok(),
        governor=g, deny_words=DENY,
    )
    assert g.check() > 0


# ---------- gated_install: the tool-layer ordering contract ----------

from gma3_mcp.approvals import ApprovalRegistry
from gma3_mcp.plugins import gated_install


class _NeverConsult:
    def consume(self, command: str, tier: int) -> bool:
        raise AssertionError("approvals consulted in dry_run — its block must be absolute")


def _gi(tmp_path, *, mode="supervised", approvals=None, governor=None, sent=None, **kw):
    args = dict(
        name="foo", lua_source=LUA_OK, xml_source=None, slot=7, run_after=False,
        install_dir=str(tmp_path), default_mode=mode, require_confirm=True,
        deny_words=DENY, approvals=approvals or ApprovalRegistry(),
        governor=governor or InstallGovernor(cooldown_seconds=0.0),
        send_cmd=(sent.append if sent is not None else (lambda c: None)),
        query=_fake_query_ok(),
    )
    args.update(kw)
    return gated_install(**args)


def test_gated_dry_run_writes_nothing_never_consults_approvals(tmp_path):
    out = _gi(tmp_path, mode="dry_run", approvals=_NeverConsult())
    assert out["dry_run"] is True and out["sent"] is False
    assert "gate_command" in out and "<UserPlugin " in out["xml_preview"]
    assert list(tmp_path.iterdir()) == []  # nothing written


def test_gated_cooldown_block_leaves_grant_pending(tmp_path):
    t = {"now": 100.0}
    g = InstallGovernor(cooldown_seconds=5.0, now=lambda: t["now"])
    g.mark()
    reg = ApprovalRegistry()
    gate = approval_command("foo", 7, False, LUA_OK, None)
    reg.grant(gate, tier_max=2)
    out = _gi(tmp_path, approvals=reg, governor=g)
    assert "cooldown" in out["error"] and "grant not consumed" in out["error"]
    assert len(reg.pending()) == 1  # invariant 6: the single-shot grant survived


def test_gated_grant_not_replayable_for_different_source(tmp_path):
    reg = ApprovalRegistry()
    reg.grant(approval_command("foo", 7, False, "other source", None), tier_max=2)
    out = _gi(tmp_path, approvals=reg)
    assert out.get("needs_confirm") is True and out["sent"] is False
    assert list(tmp_path.iterdir()) == []


def test_gated_single_shot_second_install_reblocked(tmp_path):
    reg = ApprovalRegistry()
    gate = approval_command("foo", 7, False, LUA_OK, None)
    reg.grant(gate, tier_max=2)
    sent: list[str] = []
    first = _gi(tmp_path, approvals=reg, sent=sent)
    assert first["ok"] is True and sent[0] == "ReloadAllPlugins"
    second = _gi(tmp_path, approvals=reg, sent=sent)
    assert second.get("needs_confirm") is True  # grant was consumed by first


def test_gated_hook_host_run_after_refused_before_any_gate(tmp_path):
    out = _gi(tmp_path, name=HOOK_HOST_NAME, lua_source=HOOK_HOST_LUA, slot=5, run_after=True)
    assert out["sent"] is False and "never be auto-run" in out["error"]
    assert "needs_confirm" not in out  # refused outright, no gate offered

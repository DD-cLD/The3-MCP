"""confirm_gate approval registry + new Tier-2 classifier prefixes (P1, 2026-07-04)."""
from __future__ import annotations

import time

from gma3_mcp.approvals import ApprovalRegistry
from gma3_mcp.safety import classify


# ---------- ApprovalRegistry ----------

def test_grant_then_consume_single_shot():
    r = ApprovalRegistry(ttl_seconds=300)
    r.grant('Lua "Store Preset 4.106"', tier_max=2)
    assert r.consume('Lua "Store Preset 4.106"', tier=2) is True
    # single-shot: second use fails
    assert r.consume('Lua "Store Preset 4.106"', tier=2) is False


def test_consume_ignores_only_surrounding_whitespace():
    r = ApprovalRegistry()
    r.grant('  Lua "Store Preset 4.106"  ')
    assert r.consume('Lua "Store Preset 4.106"', tier=2) is True
    r.grant('Lua "Store Preset 4.106"')
    assert r.consume('Lua "Store Preset 4.107"', tier=2) is False


def test_approval_preserves_whitespace_inside_lua_strings():
    r = ApprovalRegistry()
    command = "Lua \"ObjectList('Sequence named  with  spaces')[1]:Addr()\""
    r.grant(command, tier_max=3)
    assert r.consume(command.replace('  ', ' '), tier=3) is False
    assert r.consume(command, tier=3) is True


def test_approval_preserves_whitespace_between_tokens_too():
    r = ApprovalRegistry()
    r.grant('Lua  "Printf(1)"', tier_max=3)
    assert r.consume('Lua "Printf(1)"', tier=3) is False
    assert r.consume('Lua  "Printf(1)"', tier=3) is True


def test_expired_grant_is_rejected_and_pruned():
    r = ApprovalRegistry(ttl_seconds=300)
    g = r.grant("SaveShow /Enumerate /NoConfirmation", ttl_seconds=0)
    time.sleep(0.01)
    assert time.monotonic() > g.expires_at
    assert r.consume("SaveShow /Enumerate /NoConfirmation", tier=2) is False
    assert r.pending() == []


def test_tier3_command_not_covered_by_tier2_grant():
    r = ApprovalRegistry()
    r.grant("Go+ Sequence 5", tier_max=2)
    assert r.consume("Go+ Sequence 5", tier=3) is False


def test_revoke_and_pending_view():
    r = ApprovalRegistry(ttl_seconds=300)
    r.grant("Store Macro 11")
    assert len(r.pending()) == 1
    assert r.revoke("Store  Macro 11") is False
    assert r.revoke(" Store Macro 11 ") is True
    assert r.pending() == []
    assert r.revoke("Store Macro 11") is False


# ---------- classifier P1 additions ----------

def test_reload_all_plugins_is_tier2():
    c = classify("ReloadAllPlugins")
    assert c.tier == 2


def test_plugin_run_is_tier2():
    c = classify("Plugin 5")
    assert c.tier == 2


def test_import_plugin_is_tier2():
    c = classify('Import Plugin 5 "alchemease_hello"')
    assert c.tier == 2


def test_lua_wrapping_reload_escalates():
    c = classify("Lua \"Cmd('ReloadAllPlugins')\"")
    assert c.tier == 3
    assert c.needs_confirm


def test_preset_reads_still_pass_word_boundary_deny():
    # regression guard for the substring "Reset"-blocks-"Preset" bug
    c = classify("Lua \"tostring(ObjectList('Preset 4.101')[1]:Addr())\"", deny_list=["Reset"])
    assert c.tier == 3
    assert c.matched_rule == "lua-arbitrary"


def test_lua_setvar_requires_tier3_review():
    c = classify("Lua \"SetVar(UserVars(),'x',1)\"")
    assert c.tier == 3
    assert c.matched_rule == "lua-arbitrary"


def test_lua_getvar_also_requires_tier3_review():
    c = classify("Lua \"tostring((GetVar(UserVars(),'x')))\"")
    assert c.tier == 3
    assert c.needs_confirm

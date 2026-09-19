"""Test matrix from MA3_MCP_Server_Spec_v2.1 §11 — safety classifier rows."""
from __future__ import annotations

from gma3_mcp.safety import classify


def test_harmless_selection():
    c = classify("Fixture 1 Thru 10")
    assert c.tier == 99  # unknown selection — deny for writes


def test_go_plus_is_tier3():
    c = classify("Go+ Sequence 2")
    assert c.tier == 3
    assert c.needs_confirm


def test_store_is_tier2():
    c = classify("Store Sequence 47 Cue 1")
    assert c.tier == 2
    assert c.needs_confirm


def test_delete_is_tier2_confirm():
    c = classify("Delete Sequence 47")
    assert c.tier == 2
    assert c.needs_confirm


def test_loadshow_denied():
    c = classify("LoadShow foo.show3")
    assert c.tier == 99
    assert c.matched_rule == "deny-prefix"


def test_lua_read_is_tier1():
    c = classify('Lua "Printf(ObjectList(\\"Master 1\\")[1]:Addr())"')
    assert c.tier == 1


def test_lua_wrapping_store_is_tier2():
    c = classify('Lua "Cmd(\\"Store Sequence 1 Cue 1\\")"')
    assert c.tier == 2


def test_oops_is_tier1():
    c = classify("Oops")
    assert c.tier == 1


def test_echo_is_tier0():
    c = classify('Echo "ping"')
    assert c.tier == 0


def test_saveshow_is_tier2_since_0704():
    c = classify('SaveShow "cLD_BENCH_WORK" /NoConfirmation')
    assert c.tier == 2
    assert c.needs_confirm


def test_loadshow_still_denied():
    assert classify("LoadShow foo").tier == 99


def test_deny_is_word_boundary_not_substring():
    # "Reset" in the deny list must not match "Preset" (live catch 2026-07-04)
    c = classify('Lua "ObjectList(\'Preset 4.101\')"', ["Reset"])
    assert c.tier != 99


def test_reset_still_denied_as_word():
    assert classify("Reset", ["Reset"]).tier == 99

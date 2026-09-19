"""Test matrix from MA3_MCP_Server_Spec_v2.1 §11 — safety classifier rows."""
from __future__ import annotations

import pytest

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


def test_apparently_read_only_lua_still_requires_tier3_review():
    c = classify('Lua "Printf(ObjectList(\\"Master 1\\")[1]:Addr())"')
    assert c.tier == 3
    assert c.needs_confirm


def test_lua_wrapping_store_requires_tier3_review():
    c = classify('Lua "Cmd(\\"Store Sequence 1 Cue 1\\")"')
    assert c.tier == 3
    assert c.needs_confirm


@pytest.mark.parametrize("command", [
    'lua "Cmd(\'store sequence 1\')"',
    'LuA\t"SetVar (UserVars(), \'x\', 1)"',
    'Lua "Cmd(\'Delete Sequence 1\')"',
    'Lua "_G[\'C\'..\'md\'](\'Go+ Sequence 1\')"',
    'Lua "(function() local f = Cmd return f(\'store sequence 1\') end)()"',
    'Lua "ObjectList(\'Sequence 1\')[1]:Set(\'name\', \'changed\')"',
    'Lua "_G[\'GetPreset\'..\'DataFast\'](1)"',
])
def test_lua_never_gets_a_read_only_exemption_from_spelling(command):
    c = classify(command)
    assert c.tier == 3
    assert c.needs_confirm
    assert c.matched_rule == "lua-arbitrary"


def test_lua_prefix_requires_keyword_boundary():
    assert classify('LuaSomething "Printf(1)"').tier == 99


def test_lua_hard_denies_still_take_precedence():
    assert classify('Lua "getpresetdatafast (1)"').tier == 99
    assert classify('Lua "Cmd(\'reset\')"', ["Reset"]).tier == 99


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

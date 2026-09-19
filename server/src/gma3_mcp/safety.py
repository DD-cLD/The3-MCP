"""Tier classifier + confirm-gate stub.

Per MA3_MCP_Server_Spec_v2.1 §5: every command string passes through a
classifier before transport. Defaults are deny-on-unknown for writes.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Classification:
    tier: int       # 0 read, 1 reversible, 2 showfile, 3 live
    reason: str
    needs_confirm: bool
    matched_rule: str | None = None


_TIER_3_PREFIXES = (
    "Go+", "Go-", "Goto ", "Top ", "Pause", "Release", "Off ", "On ",
    "Flash ", "Kill ", "Solo ", "Temp ", "GrandMaster ", "Blackout",
)
# SaveShow reclassified deny→Tier 2 (2026-07-04, owner decision — save-before-
# big-moves discipline). LoadShow stays denied: loading nukes the session context.
# ReloadAllPlugins + "Plugin <n>" (runs Main() = executes code) added 2026-07-04
# per spec §5 P1 — both are steps of the install_plugin Tier-2 flow.
# "InstallPlugin" is SYNTHETIC (2026-07-05): never sent to the console — it is
# the confirm_gate approval key for the composite install_plugin tool (write
# pair + ReloadAllPlugins + Import + optional run). One grant = one install.
_TIER_2_PREFIXES = ("Store ", "Update ", "Move ", "Copy ", "Insert ", "Set ", "Assign ", "Label ", "Import ", "Export ", "SaveShow", "ReloadAllPlugins", "Plugin ", "InstallPlugin")
_DENY_PREFIXES = ("LoadShow ", "Network ", "Reset ", "Shutdown ", "Restart ")
_DELETE = re.compile(r"^\s*Delete\b", re.I)
# ⛔ Hard rule 1 (concept gpdf-console-killer): segfaults 2.4.2.2, pcall can't
# catch it. Was only enforced for plugin SOURCES until 2026-07-05 review (B1):
# a `Lua "...GetPresetDataFast(...)"` expression classified Tier 1 and would
# have sailed through send_lua ungated — in dry_run too. Deny at the
# classifier so every present and future tool inherits the ban.
_GPDF = re.compile(r"GetPresetDataFast", re.I)


def classify(command: str, deny_list: list[str] | None = None) -> Classification:
    cmd = command.strip()
    lo = cmd.lower()

    if _GPDF.search(cmd):
        return Classification(
            tier=99,
            reason="GetPresetDataFast is banned — segfaults 2.4.2.2 (concept gpdf-console-killer)",
            needs_confirm=False,
            matched_rule="gpdf-ban",
        )

    deny_list = deny_list or []
    for entry in deny_list:
        # Word-boundary match — naive substring denied every mention of
        # "Preset" via the "Reset" entry (caught live 2026-07-04).
        if re.search(rf"(?<![A-Za-z]){re.escape(entry)}(?![A-Za-z])", cmd, re.I):
            return Classification(tier=99, reason=f"deny-list match: {entry!r}", needs_confirm=False, matched_rule="deny")

    for p in _DENY_PREFIXES:
        if cmd.startswith(p):
            return Classification(tier=99, reason=f"denied prefix {p!r}", needs_confirm=False, matched_rule="deny-prefix")

    if _DELETE.match(cmd):
        return Classification(tier=2, reason="Delete-style mutation", needs_confirm=True, matched_rule="delete")

    if cmd.startswith("Lua "):
        # Lua is a read-channel by convention if the snippet just uses Printf/ObjectList/GetPath
        # — but conservative: classify as 1 unless it contains Cmd("...") with a Tier 2+ op.
        for p in _TIER_3_PREFIXES:
            if p in cmd:
                return Classification(tier=3, reason=f"Lua wraps Tier-3 op {p!r}", needs_confirm=True, matched_rule="lua-fires")
        for p in _TIER_2_PREFIXES:
            if p in cmd:
                return Classification(tier=2, reason=f"Lua wraps Tier-2 op {p!r}", needs_confirm=True, matched_rule="lua-stores")
        # Lua API write functions — prefix rules miss these ("Set " has a
        # trailing space; "SetVar(" doesn't). Found live 2026-07-04.
        for fn in ("SetVar(", "DelVar(", "CreateUndo(", "Delete(", "Acquire(", "SetAttribute(", "SetFader("):
            if fn in cmd:
                return Classification(tier=2, reason=f"Lua calls write API {fn!r}", needs_confirm=True, matched_rule="lua-api-write")
        return Classification(tier=1, reason="Lua read-channel (Printf/ObjectList/GetPath)", needs_confirm=False, matched_rule="lua-read")

    for p in _TIER_3_PREFIXES:
        if cmd.startswith(p):
            return Classification(tier=3, reason=f"Tier-3 playback op {p!r}", needs_confirm=True, matched_rule="t3")
    for p in _TIER_2_PREFIXES:
        if cmd.startswith(p):
            return Classification(tier=2, reason=f"Tier-2 showfile op {p!r}", needs_confirm=True, matched_rule="t2")

    if cmd.startswith("Echo ") or cmd.startswith("Printf "):
        return Classification(tier=0, reason="read-only print", needs_confirm=False, matched_rule="read")
    if cmd.startswith("Get") or cmd.startswith("List") or cmd.startswith("Help"):
        return Classification(tier=0, reason="read-only query", needs_confirm=False, matched_rule="read")
    if cmd.startswith("Clear") or cmd.startswith("Oops"):
        return Classification(tier=1, reason="programmer-state op", needs_confirm=False, matched_rule="t1")

    return Classification(tier=99, reason="unknown command — deny for writes", needs_confirm=False, matched_rule="unknown")

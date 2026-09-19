---
id: gpdf-console-killer
title: "GetPresetDataFast() segfaults onPC 2.4.2.2 on a freshly built preset/phaser — banned from generated Lua"
role: programmer
tags: [lua, mcp, crash, v2.4, onpc]
when_to_load: "Before generating any Lua that reads preset internals; when an MCP round-trip times out unexpectedly after a fresh Store"
status: active
source: "MEMORY §Console-crash paid-for lessons — GetPresetDataFast() is a console-killer over the wire, 2026-07-04, onPC 2.4.2.2, MCP-driven, live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Two hard crashes this session (11:34 + 11:42),** each the instant `GetPresetDataFast(handle,...)` ran on a **freshly built preset/phaser**.

Crash logs at `~/MALightingTechnology/gma3_2.4.2/onpc/temp/crashlogs/processed/` show identical **`_sigtramp` (signal/segfault) faults in the LUA thread**, with a recursive native stack — this is a **C-side crash, NOT a Lua error**, so:
- **`pcall` cannot catch it.**
- The MCP round-trip just **times out** (the console dies before writing the sentinel file) — see `segfault-manifests-as-mcp-timeout` for the diagnostic signature this produces.

**Ban `GetPresetDataFast()` from generated Lua entirely.** Verify stored phasers with SAFE reads only (`.Name`, `.Addr()`, pool-slot counts) or inspect the exported showfile XML offline instead.

**Likely root cause (investigate, not yet confirmed):** boot log shows `attribute import error 'PresetMode'='Default' : illegal value` during preset compression. CLI-stored presets may carry an illegal v2.4 `PresetMode` that sends GPDF's recursive serializer off a cliff — v2.4 removed the "Auto" preset mode (see `v24-migration-facts`), and "Default" may also be an illegal value now. Check `PresetMode` on `Store Preset` before trusting programmatic preset builds.

**Investigation update (2026-07-05, read-only probe):** a CLI-stored color preset, `cLD Red` (4.101), reads `PresetMode=Global` — a **LEGAL** value. The boot-log's illegal `'Default'` did **NOT** reproduce on this object. Root-cause hypothesis is therefore not yet confirmed by this probe; still needs a fresh phaser-candidate probe (SAFE property reads only — **never GPDF**) during the next attended console session to actually catch an illegal `PresetMode` in the wild.

**Enforcement update (2026-07-05): classify() now denies GPDF at the classifier, closing a B1 hole.** Until today, `GetPresetDataFast` classified as **Tier 1** ("Lua read-channel") and would pass `send_lua` **ungated — even in `dry_run`** — because the console-killer ban above lived only in a plugin-source scan, which the classifier path never reached. **Fix:** `classify()` now denies GPDF tier-99 (hard-deny) before any other rule is evaluated (`safety.py` gpdf-ban). Every current and future tool that routes through `classify()` inherits the ban. Found by a second-look Fable cross-check subagent review — not by the 67-green unit test suite in place at the time.

History: first-observed, live, 2026-07-04 (standalone crash-avoidance rule; escalated as a bug report to MA Lighting/ACT support, see project task list). 2026-07-05: classifier-level enforcement added after a cross-check review found the ban wasn't reaching `send_lua`'s gating path; fixed same session, suite now 80 green.

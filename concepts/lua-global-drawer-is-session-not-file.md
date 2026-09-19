---
id: lua-global-drawer-is-session-not-file
title: "The Lua _G drawer belongs to the RUNNING SESSION, not the file — quit/relaunch or a show reload empties it, and it has NO window from the desk; SetGlobalVariable is a different cabinet that DOES have one"
role: programmer
tags: [ma3, lua, plugin, uservariable, v2.4, tourshow]
when_to_load: "Before relying on anything held in Lua globals across a reload, or when trying to inspect what a plugin has left in memory — and before confusing the Lua drawer with the console's user-variable store"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-5cLD] 2026-08-08 — live _G census, Tier-1 read"
supersedes: []
superseded_by: null
---

## Persistence

**The drawer is session-scoped.** onPC quit and relaunch = empty drawer, **even on the same saved file**. A show load or reload = empty drawer. A PSR carries the plugin **code** (the pool object) but it arrives **unfired**.

**This is not a problem**, because load re-runs every plugin's top-level code and rebuilds the drawer (`plugin-code-runs-at-showfile-load`). **SaveShow saves the recipe, never the meal.**

## Two drawers, different cabinets

| | Console user variables | Lua `_G` |
|---|---|---|
| Written by | `SetGlobalVariable` | plugin top-level code |
| Visible from the desk | **yes** — `List Global Variable` | **no window at all** |
| Read by | CLI and Lua | Lua only |

The song-fire chain uses both: the token and BPM go into **user variables** (visible, inspectable), while the toolbox functions live in **`_G`** (invisible unless you ask Lua).

## What a live census looks like

Roughly **34 tables**, of which the named toolboxes map one-to-one onto plugin pool slots, alongside the stock ones (`Enums`, `ButtonApi`, `LedApi`, `lfs`, `__CallbacksRegistry`…). 279 functions, 3 userdata.

**The jewel in the census:** a plugin's **configuration constants sit in `_G` as plain globals** — the song macro range, the song page range, the song timecode range, the song view and view-button numbers, the sequence range, the pool number, plus a debug flag. **Decoding an inherited plugin's numbering scheme can be a memory read rather than a source read.** Assorted crumbs also accumulate there (current image pool name, element numbers, counters) — useful, unreliable, not a contract.

**Resident vs parked:** hooks and timers are the genuinely-running class (the MCP hook host is one). The song path has none — it is a pure native chain. **An audit lane for "is anything actually running" is reading plugin source**, not reading `_G`.

**Offered artifact:** a one-press census macro that prints the inventory to the System Monitor — the drawer gets a window.

**Relation:** `plugin-code-runs-at-showfile-load` · `uservariable-cli-and-lua-surface` · `lua-api-surface-inventory` · `hook-api-surface` · `automator-tc-architecture`.

History: none — censused live 2026-08-08.

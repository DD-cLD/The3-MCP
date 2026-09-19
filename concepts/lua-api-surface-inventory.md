---
id: lua-api-surface-inventory
title: "Lua API surface: 242 global functions + 617 enums on stock MA3 onPC 2.3.2.0"
role: programmer
tags: [lua, mcp]
when_to_load: "When you need the full inventory of available MA3 Lua globals/enums, or want to confirm a function/enum exists before using it"
status: active
source: "MEMORY §MCP v2.1 Build — Lua API surface, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Live-captured on a stock MA3 onPC 2.3.2.0 install: **242 global functions** + **617 enums**.

Full inventory: `WORKING/generated/ma3/snapshots/api_dump_*.json` (produced by the `alchemease_api_dump` plugin, pool slot 3 — see `plugin-pool-slot-reservations`).

Notable named functions/objects worth remembering directly (rather than searching the dump every time): `Cmd*` family, `HookObjectChange`/`Unhook`, `CreateUndo`/`CloseUndo`, `CallRealtimeLockedProtected`, `ChannelTable`, `ConfigTable`, `SelectionTable`, `CurrentUser`, `CurrentProfile`.

History: none — captured 2026-05-27 against onPC 2.3.2.0; the count may drift under v2.4 (2.4.2.2) but no corpus entry re-ran the dump against that build.

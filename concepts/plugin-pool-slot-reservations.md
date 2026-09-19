---
id: plugin-pool-slot-reservations
title: "Plugin pool slot reservations — alchemease_* in 1-20, production show plugins 21+"
role: programmer
tags: [lua, mcp]
when_to_load: "Before assigning a new plugin to a pool slot on Dave's onPC — check this reservation convention first to avoid collisions"
status: active
source: "MEMORY §MCP v2.1 Build — Plugin pool slot reservations, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Currently on Dave's onPC:
- Slot 1: `alchemease_hello` (probe)
- Slot 2: `alchemease_snapshot` (state export)
- Slot 3: `alchemease_api_dump` (API inventory)
- Slot 4: `alchemease_hook_demo` (lifecycle probe)

**Convention:** keep the `alchemease_*` namespace in slots **1–20**; production show plugins (PatchExport, PhaseCalc, ShowShuffle) get **21+**.

History: none — established 2026-05-27; no later corpus entry records additional slot assignments beyond these four.

---
id: undo-and-realtime-safety-primitives
title: "CreateUndo/CloseUndo and CallRealtimeLockedProtected — required safety wrappers for generated Lua"
role: programmer
tags: [lua, mcp]
when_to_load: "Before generating any Lua that mutates console state, especially Phasers, MAtricks live values, or executor state — these wrappers are mandatory for Tier 2 generated Lua"
status: active
source: "MEMORY §MCP v2.1 Build — Undo + realtime safety primitives, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **`CreateUndo("description")` / `CloseUndo()`** — wrap mutations to make them a single `Oops` step. **Tier 2 generated Lua MUST use this.**
- **`CallRealtimeLockedProtected(fn)`** — protected entry point for code that touches realtime output (Phasers, MAtricks live values, executor state).

History: none — recorded 2026-05-27, no later corrections found in corpus.

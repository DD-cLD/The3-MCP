---
id: hook-api-surface
title: "Hook API (v2.3.2) — HookObjectChange, Unhook (not UnhookObjectChange), UnhookMultiple, DumpAllHooks"
role: programmer
tags: [lua, mcp]
when_to_load: "Before writing code that registers or removes an object-change hook — the unhook function name is easy to get wrong"
status: active
source: "MEMORY §MCP v2.1 Build — Hook API, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

| Function | Status |
|---|---|
| `HookObjectChange(callback, handle)` | returns a token |
| `Unhook(token)` | correct unhook call — **NOT** `UnhookObjectChange`, which does not exist |
| `UnhookMultiple(...)` | batch remove |
| `DumpAllHooks()` | inspection — useful for debugging |
| `PatchFixturesChangedCallback`, `PatchGridColumnFilterChangedCallback`, `PatchSettingsChangedCallback` | specialized patch-domain hooks |

Recall also: any hook registered inside a `Plugin <N>` invocation's `Main()` is unhooked automatically the instant that invocation ends (see `plugin-lifecycle-autocleanup`) — this Hook API is for use in persistent-lifecycle plugins, not one-shot `Plugin <N>` calls.

History: none — recorded 2026-05-27, no later corrections found in corpus.

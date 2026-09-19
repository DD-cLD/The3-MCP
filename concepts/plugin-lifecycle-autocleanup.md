---
id: plugin-lifecycle-autocleanup
title: "Plugin <N> auto-runs Cleanup() immediately after Main() — kills persistent state same call"
role: programmer
tags: [lua, mcp]
when_to_load: "Before writing a plugin that needs to persist state across command invocations (hooks, retained handles, coroutines, push channels, observers) — one-shot plugins are unaffected"
status: active
source: "MEMORY §MCP v2.1 Build — Plugin lifecycle gotcha, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

When invoked via `Plugin <N>` from the command line, MA3 runs `Main()` and then **immediately runs `Cleanup()`** in the same synchronous call. Consequences:

- Persistent state (registered hooks, retained handles, coroutines) is torn down before the next command runs.
- `HookObjectChange` registered inside `Main` will be **unhooked by the time the user changes the target** — a hook set up this way is already dead.
- For **persistent** plugins (push channels, observers) you need a different lifecycle: the v2.3 plugin pool's **`Toggle`** pool-action, or `Execute(type, ...)` with a long-lived registry, or registration at showfile-load time.
- For **one-shot** plugins (snapshot, API dump, codegen), the auto-Cleanup is exactly the behavior you want — no special handling needed.

History: none — recorded 2026-05-27, no later corrections found in corpus.

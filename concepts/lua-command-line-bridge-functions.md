---
id: lua-command-line-bridge-functions
title: "Lua → command-line bridge functions (Cmd, CmdIndirect, CmdIndirectWait, CmdObj)"
role: programmer
tags: [lua, mcp]
when_to_load: "Before deciding how a generated Lua artifact should invoke MA3 command-line strings — synchronous vs async vs object-scoped"
status: active
source: "MEMORY §MCP v2.1 Build — Lua → command-line bridge, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

| Function | Use |
|---|---|
| `Cmd("…")` | Execute MA3 command-line string synchronously; result available in System Monitor |
| `CmdIndirect("…")` | Async / queued |
| `CmdIndirectWait("…")` | Async with wait barrier |
| `CmdObj(obj, "…")` | Execute command in the context of a specific object handle |

Prefer these over OSC round-trips when codegen targets a Lua artifact — no UDP latency, no echo parsing.

History: none — recorded 2026-05-27, no later corrections found in corpus.

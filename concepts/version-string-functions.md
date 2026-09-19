---
id: version-string-functions
title: "Getting the real MA3 version from Lua: BuildDetails().BigVersion (HostRevision() is just a build tag)"
role: programmer
tags: [lua, ma3]
when_to_load: "Before writing Lua that needs to detect or report the running MA3 version programmatically"
status: active
source: "MEMORY §MCP v2.1 Build — Version strings, 2026-05-27, onPC 2.3.2.0; live-verified via MCP round-trip 2026-07-04 on onPC 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- `HostRevision()` returns a short string (e.g. **"Rev1"**) — **NOT** the user-facing version.
- `_VERSION` returns **"Lua 5.4"** — confirms the Lua runtime only, not the MA3 build.
- **`BuildDetails()` is the real answer** (live-verified 2026-07-04, onPC 2.4.2.2, over the MCP wire, 34.9 ms RTT): returns a table —
  `BigVersion=2.4.2.2` (the user-facing version) · `SmallVersion=2.4.0.0` · `GitHash` · `GitDate` · `CompileDate` / `CompileTime` · `CodeType=Release` · `IsRelease=true` · `HostType=onPC` · `HostSubType=Undefined`.
- Programmatic version check: **`BuildDetails().BigVersion`**.

History: was `status: verify` ("BuildDetails() in the api dump — try it", 2026-05-27). Cleared live 2026-07-04 — the first concept verified through the library's own loop (index flagged it → one Tier-1 Lua expression → active).

---
id: plugin-install-loop
title: "Full plugin install → run sequence (write files, ReloadAllPlugins, Import Plugin, Plugin N)"
role: programmer
tags: [lua, mcp]
when_to_load: "Before installing or refreshing a Lua plugin on-console — the exact 4-step sequence and its two common failure modes"
status: active
source: "MEMORY §MCP v2.1 Build — Plugin install loop (live-verified), 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The full install → run sequence, live-verified:

1. Write `<name>.lua` + `<name>.xml` pair to `~/MALightingTechnology/gma3_library/datapools/plugins/<name>/`. Folder name must match `<UserPlugin Path="…">` in the XML; the `.lua` filename must match `<ComponentLua FileName="…"/>`.
2. `ReloadAllPlugins` — refreshes pool entries already present; does **NOT** auto-import new ones from disk.
3. `Import Plugin <slot> "<folder_name>"` — materializes into pool slot. Slot must be empty (`Delete Plugin <slot> /NoConfirmation` first if needed).
4. `Plugin <slot>` — runs `Main(display_handle, arguments)`.

Failures to remember:
- `Import "name" At Plugin <slot>` → returns **"Illegal object"**. This is wrong syntax — use step 3's form instead.
- `Enums.PathType.UserPlugin` → **does not exist**. Use **`CustomPluginLibrary`** (user-level) or **`PluginLibrary`** (system-level).
- Path resolution at runtime: `Lua "for k,v in pairs(Enums.PathType) do Printf(k..'='..tostring(GetPath(v))) end"`.

See `plugin-xml-schema` for the XML shape referenced in step 1, and `plugin-lifecycle-autocleanup` for what happens the instant `Plugin <slot>` finishes running.

History: none — live-verified 2026-05-27, no later corrections found in corpus.

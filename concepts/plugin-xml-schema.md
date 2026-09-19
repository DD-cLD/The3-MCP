---
id: plugin-xml-schema
title: "Plugin XML schema (v2.3.2) — UserPlugin element, not Plugin"
role: programmer
tags: [lua, mcp]
when_to_load: "Before writing the .xml companion file for a Lua plugin"
status: active
source: "MEMORY §MCP v2.1 Build — Plugin XML schema, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GMA3 DataVersion="2.3.2.2">
  <UserPlugin Name="<name>" Author="…" Version="0.1.0.0" Path="<folder>">
    <ComponentLua Name="<name>" FileName="<name>.lua"/>
  </UserPlugin>
</GMA3>
```

The root plugin element is **`<UserPlugin>`**, not `<Plugin>`. `<Plugin ContentType="Usercontent">` is a *different* shape used for the showfile-embedded portability form of a plugin — do not confuse the two.

History: none — recorded 2026-05-27, no later corrections found in corpus.

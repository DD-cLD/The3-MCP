---
id: web-remote-is-video-stream
title: "MA3 Web Remote is a rendered video stream over WebSocket, not a JSON-RPC scheme — MCP routes around it"
role: programmer
tags: [mcp, osc]
when_to_load: "Before considering MA3 Web Remote as an automation transport — it is not scriptable the way MA2's Web Remote was"
status: active
source: "MEMORY §MCP v2.1 Build — Web Remote stance, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

MA3 Web Remote is a **video stream** — a remote-rendered framebuffer sent over WebSocket on port **8080** — not a JSON-RPC scheme like MA2's Web Remote was. As of May 2026, no third party has published a working reverse-engineered MA3 WebSocket client.

**Implication:** MCP automation routes through **OSC + Lua plugins** instead of Web Remote. If DOM-level access to Web Remote is ever needed, the fallback is **read-only Playwright scraping** of the rendered stream — not a real API integration.

History: none — recorded 2026-05-27, still the architecture as of the latest corpus entries.

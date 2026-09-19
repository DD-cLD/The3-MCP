---
id: mcp-fastmcp-framework-pins
title: "MCP spec + FastMCP version pins (May 2026): 2025-11-25 spec, FastMCP >=3.3,<4, streamable-HTTP"
role: operational-meta
tags: [mcp]
when_to_load: "Before upgrading or debugging the MCP server's protocol/framework dependencies"
status: active
source: "MEMORY §MCP v2.1 Build — MCP / FastMCP framework pins, 2026-05-27"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- MCP spec revision **`2025-11-25`** — async Tasks, URL-mode elicitation, tool annotations (`readOnlyHint` / `destructiveHint` / `idempotentHint` / `openWorldHint`).
- **FastMCP `>=3.3,<4`** — Providers + Transforms composition; CIMD-default auth; use **`require_scopes`**, not `require_auth`.
- SSE transport deprecated since 2025; **streamable-HTTP** is current.

Related, later-dated dependency facts: see `mcp-server-venv-python-trap` for the Python-version/pip trap encountered building this server's venv (2026-06-29), and the confirmed working dependency versions there (`fastmcp 3.4.2`, `python-osc 1.10.2`, `pydantic 2.13.4`).

History: none — pinned 2026-05-27, consistent with the later 2026-06-29 rebuild's resolved versions.

---
id: reread-tool-description-on-misbehavior
title: "When an MCP tool misbehaves, re-read its OWN description before building a deeper diagnostic theory — the fix is often already documented there"
role: operational-live
tags: [mcp, process, debugging]
when_to_load: "The moment any MCP tool starts behaving unexpectedly (timeouts, silent no-ops, wrong results) — before chasing a deeper root cause, re-read that tool's current description first"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The reloaded `send_lua` tool description states the expression-only rule plainly:** send a single Lua EXPRESSION, single quotes only, no semicolons, no backslashes, with a separate `want_result=false` lane for statements. This was documented and available the entire time.

**It still cost six failed calls and a live console-echo debug session** (see `send-lua-expression-payload-rule`) to rediscover behavior that was already written down in the tool's own schema.

**Standing rule: RE-READ THE TOOL DESCRIPTION at the start of any debugging session for an MCP tool that's misbehaving, before diagnosing deeper.** A tool's description can change between sessions (server updates, reloaded schemas); don't diagnose against a remembered/assumed contract when the current one is one read away.

Card-candidate line for `CARD_DESK` bring-up.

**Relation:** `send-lua-expression-payload-rule` — the concrete case this lesson came from.

History: none — captured 2026-07-29, same session as the send_lua expression-rule discovery.

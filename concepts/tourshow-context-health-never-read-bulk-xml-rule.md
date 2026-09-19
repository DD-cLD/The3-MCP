---
id: tourshow-context-health-never-read-bulk-xml-rule
title: "Never Read a {LD} or export-back XML file into context — bulk analysis runs through committed, re-runnable scripts that print short summaries; sessions die from reading, not from working"
role: operational-live
tags: [context-health, tooling, process, desk-hygiene, tourshow]
when_to_load: "Before reading any {LD} source export or a cLD export-back XML file directly into a session's context — these run 6-17 MB each; use a committed script instead and let it print a short summary"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Context-health rule, now written into the standing lock/run plan and load-bearing: never `Read` a {LD} or export-back XML file into context** — these files run **6-17 MB each**. Every 08-03 finding in this corpus instead came from **committed scripts printing <=30 summary lines**, with full detail routed to a sheet on disk rather than into the conversation.

**All bulk analysis is a committed, re-runnable script** (kept under `recipe_sheets/` or equivalent), run via a process-launching tool rather than read directly. **One state file + one plan file is what a fresh session needs to read** to pick up where the last one left off — not the underlying XML.

**Findings hit `INBOX.md` as they happen, not only at wrap** — a HELD session that never formally wraps still keeps its findings this way, since capture is decoupled from the wrap event.

**The standing reason: sessions die from reading, not from working.** A single large-file `Read` can burn the context budget a whole song's worth of mechanical work would otherwise fit inside.

**Relation:** `low-credit-cli-mcp-first-authoring-doctrine` (a related context-economy doctrine for MCP/CLI authoring). `tourshow-songbuild-kit-and-runbook` (the committed-script kit this rule assumes exists and gets extended, not replaced by ad-hoc reads).

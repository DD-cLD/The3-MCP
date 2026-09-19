---
id: lua-body-write-api-classifier-gate
title: "Classifier scans Lua bodies for embedded write-API calls to force Tier 2 — prefix rules alone let writes slip Tier 1"
role: programmer
tags: [mcp, safety, lua]
when_to_load: "When modifying or auditing the MCP command classifier's Tier 1/Tier 2 rules, or wondering why a Lua payload landed in Tier 1"
status: active
source: "findings/INBOX.md, 2026-07-05, found+fixed"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Gap found:** `SetVar(` and similar write calls could slip Tier 1 classification because the classifier's prefix rules require a **trailing space** to match — a call written without one (or embedded mid-Lua-body rather than as a bare command prefix) wasn't caught.

**Fix applied:** the classifier now additionally **scans the body of Lua payloads** for write-API call signatures and forces **Tier 2** if any are found, regardless of the top-level prefix match. Scanned call signatures (verbatim from the fix):

```
SetVar(
DelVar(
CreateUndo(
Delete(
Acquire(
SetAttribute(
SetFader(
```

This closes the gap where a Lua string could carry a mutating call past the surface-level prefix check. Complements — does not replace — the mandatory `CreateUndo`/`CloseUndo` wrapping already required for Tier 2 Lua (`undo-and-realtime-safety-primitives`) and the word-boundary deny-list fix (`saveshow-discipline-and-mcp-tier`): those two govern *what Tier 2 must do*; this concept governs *what gets routed to Tier 2 in the first place*.

History: none — found and fixed same session, 2026-07-05.

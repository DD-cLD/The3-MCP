---
id: classifier-plugin-token-false-positive-block
title: "MCP classifier gap: a READ-ONLY ObjectList('Plugin *') call auto-blocks as Tier 2 purely on the 'Plugin ' token — a false positive on a census-only, non-mutating call"
role: programmer
tags: [mcp, safety, classifier]
when_to_load: "When a plainly read-only Lua call unexpectedly gets classified Tier 2/blocked — check whether it contains the literal 'Plugin ' token before assuming the call itself is dangerous"
status: verify
source: "findings/{FESTIVAL}/FESTIVAL_FINDINGS_v0.1.md [0722cLD] 2026-07-22, live 2.4.2.2, MCP classifier"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The gap:** a read-only census call, `ObjectList('Plugin *')`, auto-blocks at the MCP classifier as if it were a Tier-2 (write/dangerous) operation — purely because the literal token `Plugin ` appears in the command string, not because the call does anything mutating. `ObjectList` itself is a pure read/enumeration function.

**Distinction from other classifier gaps in the corpus:** this is neither the `lua-body-write-api-classifier-gate` mechanism (write-API calls like `SetVar(`/`Delete(` inside a Lua body) nor the `classifier-tier-gap-edit-and-bare-layer-keywords` ruling (CLI-native mutating keywords under-classified as Tier 1) — this is the OPPOSITE failure shape: a harmless read call OVER-classified as Tier 2 because of a keyword substring match, most likely because `Plugin` also appears in genuinely dangerous plugin-install/-run commands and the classifier's word-list isn't scoped to the verb position.

**Status:** `verify` — flagged as a gap during a live session, not yet triaged against the classifier's actual word-list logic or fixed. Queue for the same classifier word-list review that `classifier-tier-gap-edit-and-bare-layer-keywords` and the [0723cLD] Delete-inside-Cmd gap (see `delete-command-classifier-tier-gap`) are already queued against.

History: none — observed live in one session, 2026-07-22, attempting a plugin-pool census on {LD}'s AR showfile.

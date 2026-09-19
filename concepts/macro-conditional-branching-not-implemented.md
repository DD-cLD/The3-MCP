---
id: macro-conditional-branching-not-implemented
title: "True if/then/else branching does NOT exist in native macro CLI syntax — Lua is the only path; If/EndIf is scope-restriction, not branching"
role: programmer
tags: [ma3, macro, lua, v2.4]
when_to_load: "Before trying to build conditional (if/then/else) logic into a macro using native CLI syntax — it isn't possible; before assuming If/EndIf in a macro branches execution"
status: active
source: "findings/INBOX.md, 2026-07-17 (MA staff confirmed 2020 and again 2022)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**True conditional branching (if/then/else) is NOT implemented in native macro CLI syntax.** MA staff gave the same answer twice, three years apart (confirmed 2020, confirmed again 2022) — a settled, repeatedly-confirmed limitation, not a one-off forum opinion. **Lua is the only path** to real conditional branching in MA3.

**What `If`/`EndIf` actually does in a macro:** it's **scope-restriction** — a WHERE clause limiting which objects a subsequent command applies to — **not branching**. Don't read an `If` line in a macro as a programming-language conditional.

Cross-reference: the If family is also covered structurally (command surface + scoping-stack model) in `IF_AT_FILTERS_WORLDS_STUDY_v0.1.md` — see `at-filters-worlds-manual-gap-and-study-doc` for that doc's manual-gap findings on At/Filters/Worlds.

**Workarounds exist, but don't contradict this ruling (added 2026-07-19):** MA's own shipped macros use two operator/Lua-assisted idioms that approximate control structures without any native branching primitive — a self-referential Go-loop for iteration, and a self-gating Lua `Confirm()` for a real yes/no gate. See `macro-control-structure-workaround-idioms` for both. Both still require an operator Go+ or a one-line Lua evaluation to advance; neither is native macro-CLI branching, so MA staff's ruling above stands unchanged.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: cross-referenced the two factory control-structure workaround idioms (`macro-control-structure-workaround-idioms`) — they work around this limit, they don't lift it.

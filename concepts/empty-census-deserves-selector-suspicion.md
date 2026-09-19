---
id: empty-census-deserves-selector-suspicion
title: "An empty census result is a selector bug until proven otherwise — check the SELECTOR before believing the absence"
role: operational-live
tags: [diagnosis, crosscheck, census, selector-bug, sequence-xml]
when_to_load: "Before trusting a census/report/query that comes back ZERO or unexpectedly empty — especially any 'first matching X' selector (first cue, first row, first non-blank field) — check what the selector actually matched before believing the absence"
status: active
source: "BACKLOG_pass3.md [0803-2cLD]; worked case: Mark-cue position grid, generated/desk_pack/MARK_CUE_POSITION_GRID.csv, first pass"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**An EMPTY census result deserves the same suspicion as a surprising one.** A query that returns zero hits reads exactly like a real finding ("no song positions at Mark") — but zero is not self-verifying. Before accepting an empty result, check the SELECTOR that produced it, the same way you would check a surprising non-empty one.

## Worked case — the Mark-cue position grid's first pass (L7, 2026-08-03)

Building the show-wide Mark-cue position grid, the first pass took "the first cue with a non-empty `No`" as its definition of the Mark cue, and returned **ZERO positions for all 16 songs** — a result that reads exactly like a real finding. It was actually selecting **OffCue / CueZero**: per `sequence-xml-ordered-header-law`, the first two `Cue` children of any sequence ARE `OffCue` and `CueZero`, both of which carry a non-empty `No` but neither of which carries the show's content.

**Correct rule: take the first cue that actually HAS `StandardRecipes`, preferring one literally named `Mark`.** Applied correctly, this produced the real grid: 156 rows, 16 songs, 10 distinct Mark positions show-wide (see `tourshow-mark-position-grid-flow-pass-signal`).

## The family

This is the same shape as two standing hazards, both selector bugs disguised as findings of absence:
- `glob-false-negative-on-drive-synced-dirs` — a directory reads empty/stale because the LISTING tool served a stale or wrong view, not because the directory is actually empty.
- `stripped-group-membership-recipe-uncooked-diagnosis` — a group reads as having no members because the CENSUS METHOD (`Count()`/`Children()`) is structurally blind, not because the group is actually empty.

All three share the same corrective: **don't trust zero. Interrogate what produced the zero before treating it as a finding.**

**Relation:** `sequence-xml-ordered-header-law` (the header law that explains why "first non-empty No" mis-selects), `tourshow-mark-position-grid-flow-pass-signal` (the real result once the selector was fixed), `glob-false-negative-on-drive-synced-dirs`, `stripped-group-membership-recipe-uncooked-diagnosis` (sibling instances of the same family).

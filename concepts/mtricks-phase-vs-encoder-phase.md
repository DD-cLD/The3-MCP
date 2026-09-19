---
id: mtricks-phase-vs-encoder-phase
title: "MAtricks Phase is a literal manual value; Encoder Bar Phase auto-calculates"
role: programmer
tags: [ma3, phase-math]
when_to_load: "Before setting Phase on any MAtricks pool object destined for preset/cue storage — do not trust encoder-bar-derived values for pool storage"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules / Patterns We Use, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Phase in MAtricks = LITERAL degree value** — you must apply the `360 − 360/N` (and related) formulas manually; the console does not do this math for a MAtricks pool object.

**Phase in the Encoder Bar = AUTO-CALCULATED** — the console does compute it there, live, during interactive fanning.

Pattern this drives: **phase math is always applied manually before storing to a MAtricks pool object** — never trust encoder-bar-derived values when the destination is MAtricks pool storage, because the two surfaces do not share the same computation path.

See `phase-math-formulas` for the actual formulas.

History: none — stable rule since 2026-04-01.

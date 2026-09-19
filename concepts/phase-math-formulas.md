---
id: phase-math-formulas
title: "MAtricks phase math formulas — full spread, line-by-line, wings/group/block effective N"
role: programmer
tags: [ma3, phase-math]
when_to_load: "Before generating any Lua or CLI syntax that sets MAtricks Phase values for a phaser/preset — full-spread, line-by-line X/Y, or wings/group/block distributions"
status: active
source: "MEMORY §Phase Math Formulas, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Phase in MAtricks is a **LITERAL degree value** — the console does NOT auto-calculate it there (contrast with the Encoder Bar, which does auto-calculate; see `mtricks-phase-vs-encoder-phase` concept). These formulas must be applied manually before storing.

| Pattern | Formula |
|---------|---------|
| Full spread | `PhaseTo = 360 - (360 / N)` |
| Line-by-line X | `PhaseToX = (360 / Y) × ((X - 1) / X)` |
| Line-by-line Y | `PhaseToY = 360 - (360 / Y)` |
| Wings effective N | `ceil(total / wings)` |
| Group effective N | `= group_count` |
| Block effective N | `ceil(total / block_size)` |

`N` in the full-spread formula is the effective fixture count for the distribution being built — computed via the wings/group/block sub-formulas above depending on which structure you're phasing across.

Concrete worked example (from the v2.4 sandbox, `CLAUDE_SETUP_V0.1.show`): a 1×10 line of generic fixtures, full-spread phase for N=10 = **324°** (i.e. `360 - 360/10`).

History: none — stable since 2026-04-01, reused as the worked-example check in the 2026-07-04 v2.4 sandbox session.

**[0805-2cLD] SCOPE RULING (Dave + message-board history): flat ±360 MAtricks phase literals STAND.** The `360 − 360/N` stop-short law stays scoped to HAND-BAKED per-fixture phases; the formula lane is for pin-specific phase on a fixture set. Do not "correct" a flat ±360 MAtricks knob literal to stop-short.

History: extended 2026-08-05 [0805-2cLD] — stop-short scoped to hand-baked per-fixture phases; flat ±360 MAtricks literals attested and standing (Dave, message-board history).

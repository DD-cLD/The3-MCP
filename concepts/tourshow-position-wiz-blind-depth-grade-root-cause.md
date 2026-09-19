---
id: tourshow-position-wiz-blind-depth-grade-root-cause
title: "Blind depth-grade root cause: a 1-wide Thru selection degenerates Grid Rotate's spread to uniform tilt — depth grading needs a real 2D grid group"
role: programmer
tags: [tourshow, grid, macro, v2.4]
when_to_load: "Before running POSITION_WIZ's (or any Grid-Rotate-based) Blind/depth-grade block against a selection — a plain Thru range across one truss row will NOT depth-grade; only a true 2D grid selection will"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], Dave live console data + grid mechanics; ARTIST_TOURSHOW_GROUP_CONTRACT_v0.1.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Root cause (live-confirmed):** a plain `Fixture A Thru B` selection auto-fills as a **1-wide grid strip** (single X row, see `grid-cursor-cli-recipe-for-2d-group-layouts`). Running `Grid 'Rotate' 'Right'` against a 1-wide selection makes a width-1 column — there's nothing for the subsequent `Tilt` `Thru` spread to distribute across, so it collapses to one uniform value instead of grading. This is exactly what happened on cLD POSITION WIZ's whole-rig run (see `cld-position-wiz-generic-v01-authored-and-deployed`): the DS-row run (already effectively 1D) worked fine, but the whole-rig Blind block produced no depth grade.

**Depth grading REQUIRES a selection carrying a real 2D grid.** MA's own demo groups have grids baked in already; {TOUR}'s category groups don't yet (as of this session).

**The fix:** build each category as a proper **12×4 2D grid group** (one row per truss position: DS/MS1/MS2/US) via the already-proven `Grid X/Y` + `Fixture Thru` one-paste recipe (see `grid-cursor-cli-recipe-for-2d-group-layouts`). This is exactly what `tourshow-group-contract-v01`'s per-category ALL groups (x01, the 28×4 frame) are built to provide — its own "Consequences" note ties the two together directly: whole-category POSITION WIZ runs against the x01 groups should produce real depth-graded Blind, DS→US.

**[INFERRED, verify at desk] Mechanism detail for WHY Grid Rotate produces this specific effect:** `Thru` spreads distribute along grid X. Rotating 90° via `Grid 'Rotate' 'Right'` reassigns which stage axis a subsequent spread walks — turning a left-to-right Pan-style spread into a front-to-back (DS→US) Tilt spread, i.e. depth-graded tilt, uniform per row. In POSITION_WIZ's Blind block specifically, Pan is fanned BEFORE the rotate and Tilt is spread AFTER it — two perpendicular spread axes composed into one look. This explanation is consistent with everything observed live (rotate itself confirmed running; the degeneracy on a 1-wide selection matches the theory) but the exact axis-reassignment mechanics haven't been isolated at the desk yet. Dave's "Next" framing (stepping through the grid) is believed to walk the same grid-X mechanism, unconfirmed.

**Consequence for cLD's own macro:** run the Blind block only against full-category 2D grid groups (12×4, all 4 truss rows) — per-row/per-truss runs are fine for everything else in the wizard, just not Blind.

History: none — root cause diagnosed live 2026-07-19 from the whole-rig POSITION WIZ run's failure mode; fix designed the same session as the geometric justification for `tourshow-group-contract-v01`'s per-category frame shape.

---
id: grid-cursor-cli-recipe-for-2d-group-layouts
title: "Grid x/y cursor moves batch inline via CLI — one-paste recipe bakes a 2D fixture layout into a recallable Group"
role: programmer
tags: [ma3, cli, v2.4]
when_to_load: "Before building a 2D selection-grid layout (rows/columns of fixtures) from the CLI in one shot, or when you need a recallable Group that preserves 2D grid positions"
status: active
source: "findings/INBOX.md, 2026-07-10, console live-verified 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Verified one-paste recipe (2.4.2.2, live):**

```
ClearAll ; Grid 0/0 ; Fixture 1 Thru 5 ; Grid 0/1 ; Fixture 6 Thru 10 ; Store Group 106 "cLD 5x2" ; ClearAll ; Group 106
```

This builds a 5×2 grid in one semicolon-batched paste (interactive CLI batches `;` — see `macro-line-syntax-and-batching-rule`):
- `Grid X/Y` moves the grid cursor to that cell before the next `Fixture` selection lands there.
- Each `Fixture ... Thru ...` selection is stamped into the current grid cursor position.
- `Store Group 106 "cLD 5x2"` **bakes the 2D positions into the Group** — the grid shape is stored, not just the fixture list.
- `Group 106` (recall) **restores the 2D positions**, confirming the bake round-trips correctly.

Ties to `selection-grid-and-fixture-cell-model` (X/Y/Z axis convention, one-fixture-one-cell-per-sequence rule) — this recipe is the concrete CLI mechanism for populating that grid model.

**Caveat found the same session:** grid coordinates set this way persist through Group storage and later transforms (e.g. MAtricks XWidth re-wrap) — see `matricks-xwidth-wraps-on-absolute-grid-x` for a case where a non-zero grid origin from a build like this produced uneven wrapped rows.

**Further verified 2026-07-14 (grid drill session):** a bare `Fixture A Thru B` with no `Grid X/Y` cursor calls at all auto-fills one X row in FID order (48-wide, live-verified) — the simplest possible case, a single one-wide plane. Grid-cursor placement is only needed once a shape stops being a single line. The recipe also holds for sparse, non-contiguous rows: single-fixture `Grid X/Y` + selection calls can build multiple aligned rows at different step intervals over one shared window, and `Store Group` bakes that sparse 2D arrangement exactly — recall round-trips pixel-identical. Worked exemplars: Groups 121-124, see `grid-drill-exemplar-groups-121-124`.

**Further verified 2026-07-15 (multi-instance session):** the same Grid-cursor + `Fixture ... Thru ...` composition pattern holds unchanged at the SUBFIXTURE level — `Grid 0/2 ; Fixture 301.17 Thru 32 ; Grid 0/1 ; Fixture 301.33 Thru 48` lands each sub-range at its cursor row and selections accumulate across calls (48 subs selected total, live 2.4.2.2). See `subfixture-thru-range-syntax` for the dot-notation Thru rules this composes with, and `gridstore-keyword-and-fixture-type-write` for baking a sub-level layout into the fixture TYPE itself (a stronger, type-wide alternative to the per-instance Group bake this recipe produces).

**Further verified 2026-07-21 (pixel-cell sandwich, live):** the recipe bakes correct per-fixture 2D coords for ACME pixel-line cells. `ClearAll ; Grid X/0 ; Fixture <fid>.1 Thru 16 ; Grid X/1 ; Fixture <fid>.17 Thru 32 ; ... ; Store Group n` — export confirms `301.1`–`16` @X0–15/Y0, `302.1`–`16` @X16–31/Y0 (per-fixture tiling continues across the truss), `301.17`–`32` @X0–15/Y1 (second row). A per-truss ACME cell group thus lands top color subs 1–16 @Y0, bottom color 17–32 @Y1, beam 33–48 @Y0, 16 cols/fixture, FID→X. Generator: `build/gen_pix_cells.py`. The physical convention (top/bottom rows, FID→X direction) is still warehouse-verify — see `acme-pixel-line-ip-anatomy`. This is now the RELIABLE cell-layout lane, after the GS type-bake was found not to survive the v11 repatch (`gridstore-keyword-and-fixture-type-write`).

**Ad-hoc composition is exploration only (Dave, live console, 2026-07-19):** recalling groups/selections with an existing selection appends per the append rules — see `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle` for what `Preserve GridPositions` does to that combined recall. A manual grid-cell click places the cursor where the NEXT recall lands (see `selection-grid-and-fixture-cell-model`), so recall→click→recall builds ad-hoc composite grids live. But this is a sketching tool, not a recipe input: recipes bind Selection to a stored Group object, so anything that's going to enter a repeatable recipe has to be Stored as a Group first. Sketch live, store before it enters a cue — see `tourshow-gesture-groups-on-demand-doctrine` for the doctrine this feeds (gesture groups specifically get stored at first real use, not pre-built).

**Depth-grade corollary (2026-07-19):** this recipe's 2D output isn't just cosmetic — a `Grid Rotate`-based depth-grade effect (e.g. POSITION_WIZ's Blind block) requires a real 2D grid selection to work at all; a flat 1-wide `Thru` selection degenerates it to a uniform value. See `tourshow-position-wiz-blind-depth-grade-root-cause` for the full diagnosis and `tourshow-group-contract-v01` for the 12×4-per-category frame built specifically to satisfy this requirement.

History: first verified live 2026-07-10. Extended and reverified 2026-07-14 with the flat auto-fill and sparse-aligned-row variants (grid drill session — see `grid-drill-exemplar-groups-121-124`). Extended again 2026-07-15 confirming the recipe composes unchanged at the subfixture/dot-range level (multi-instance session). Extended 2026-07-19: added the ad-hoc-composition-is-exploration-only doctrine and the depth-grade corollary (2D selection required for Grid-Rotate-based effects). Extended 2026-07-21: added the ACME pixel-cell sandwich build (per-fixture tiling FID→X, top/bottom color rows, beam center) — the reliable cell-layout lane since GS type-bakes don't survive a repatch.

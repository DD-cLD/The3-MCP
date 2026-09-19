---
id: selection-grid-and-fixture-cell-model
title: "Selection Grid axis convention and one-fixture-one-cell-per-sequence rule"
role: programmer
tags: [ma3]
when_to_load: "Before building or reasoning about MAtricks grid layouts, or when a fixture appears to occupy more than one cell in a single sequence; also check when reading a grid-window screenshot, since zoom level and FID-label readability shift with selection extent"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Selection Grid axis convention:**
- X = horizontal (red)
- Y = vertical (blue)
- Z = depth (green)

**Cell occupancy rule:** each fixture occupies exactly **one cell per sequence**. Multiple sequences can place multiple grids on the same fixtures, resolved by LTP/HTP priority — i.e. cross-sequence overlap is legitimate and expected; it is *intra*-sequence duplication that is the invariant being guarded.

**Grid window render behavior (added 2026-07-14, live drill observation):** the grid window auto-fits its zoom to the current selection's extent. Narrow-to-medium builds render with large cells and readable FID labels — confirmed readable at 16 columns and again at 31 columns; wider builds shrink to a thin, label-illegible strip — confirmed unreadable at 46 columns. The exact threshold between 31 and 46 wasn't pinned down. Practical rule: verify a wide build by its overall shape, verify a narrow-to-medium build by reading the FID labels, and confirm contents by readback when either is in doubt. Separately: clicking anywhere on the grid canvas moves the grid cursor to that cell — normal behavior, but worth knowing because a fullscreen grid window exposes much more canvas area, so incidental/stray clicks land on it (and silently relocate the cursor) far more easily than in a windowed view.

**Grid Rotate (added 2026-07-19):** `Grid 'Rotate' 'Right'` rotates the grid — since `Thru` spreads distribute along grid X, rotating changes which axis a subsequent spread walks (e.g. turning a left-right spread into a front-back one). Live-confirmed running; the precise axis-reassignment mechanics are still being pinned down at the desk — see `tourshow-position-wiz-blind-depth-grade-root-cause` for the worked diagnosis of what happens when this runs against a selection that isn't a real 2D grid.

**Cursor + recall (added 2026-07-19):** confirms and extends the canvas-click note above — clicking a grid cell doesn't just move the cursor, the NEXT recalled Group or selection lands wherever the cursor currently sits. Chaining click→recall→click→recall builds ad-hoc composite grids live (see `grid-cursor-cli-recipe-for-2d-group-layouts` for the storage discipline that governs when an ad-hoc composite needs to become a real stored Group).

History: stable axis/occupancy rule since 2026-04-01. Render-behavior notes (auto-fit zoom, canvas-click-moves-cursor) added 2026-07-14 from live grid-drill observation. Extended 2026-07-19: added Grid Rotate's axis-swap behavior and the recall-lands-at-cursor mechanic, both from live console observation.

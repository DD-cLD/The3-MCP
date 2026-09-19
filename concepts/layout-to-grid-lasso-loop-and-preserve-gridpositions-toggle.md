---
id: layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle
title: "Lasso-selecting in a Layout view puts the full 2D shape into the selection grid — Preserve GridPositions toggles compact-pack vs literal sparse coordinates"
role: programmer
tags: [ma3, v2.4, layout]
when_to_load: "Before building a Group from a Layout's visual arrangement — this is the fast lane for turning a shaped Layout selection into a 2D Group via the selection grid"
status: active
source: "findings/INBOX.md, 2026-07-14, Dave-demonstrated, screenshot-confirmed"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**LAYOUT→GRID LOOP CLOSED (Dave-demonstrated, screenshot-confirmed, 2026-07-14):** lasso-selecting fixtures/elements inside a Layout view puts the **full 2D layout shape** into the selection grid — the grid isn't limited to manually-typed `Grid X/Y` moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`); a visual lasso in Layout carries its shape straight into grid coordinates.

**`Preserve GridPositions` toggle controls how:**
- **OFF** → **tight compact pack**: gaps between elements are compressed while the overall shape is kept (observed result: the DS+wings line plus 3 truss rows packed tight).
- **ON** → **literal sparse layout coordinates**: the grid preserves the actual (gappy) layout spacing as-is.

**This is the fast lane for shaped selections → Grid → Store Group** — lasso the shape in Layout, then `Store Group` captures the 2D arrangement without hand-typing `Grid X/Y` moves. Per Dave: "the quick-and-easy way."

Relevant to the pending `tourshow-festival-group-theory` work item ("groups off the layout") — this is the mechanism that ratifies the "layout/plot first, then group contract" workflow order.

**Extended beyond Layout-lasso, 2026-07-19 (Dave, console live):** the same append/`Preserve GridPositions` mechanics govern plain group-recall composition, not just a Layout lasso selection. Recalling groups with an existing selection appends per the normal append rules — with nothing selected first, multiple rows (e.g. DS+MS, or more) can be built up together grid-fashion one recall at a time. With `Preserve GridPositions` OFF, the combined recall COLLAPSES to a single compact grid — no sparse offset cells at the start of the grid, same compaction behavior as the Layout-lasso case above.

History: none — demonstrated and screenshot-confirmed live, 2026-07-14. Extended 2026-07-19: confirmed the same mechanics apply to plain group-recall composition, not just a Layout-view lasso selection.

---
id: subfixture-grid-compact-collapse-technique
title: "[VERIFY] Collapsing a spread sub-layout to compact: remove grid coordinates from the selection, or via toolbar commands — mechanics UNKNOWN"
role: programmer
tags: [ma3, grid, multi-instance, v2.4, verify]
when_to_load: "Before attempting to collapse/compact a spread-out sub-fixture grid selection back down — this names the technique Dave described, but the exact mechanics are not yet drilled; don't assume a specific command sequence from this file alone"
status: verify
source: "findings/INBOX.md, 2026-07-15 (Dave's layout-ratify dictation), carried forward undigested to the 2026-07-16 librarian run"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

From Dave's layout-ratify dictation: a spread sub-layout can apparently be collapsed back to compact either by **REMOVING THE GRID COORDINATES** from the selection, or **via toolbar commands**.

**Mechanics are UNKNOWN.** This is a named technique, not yet drilled. Do not assume a specific command sequence from this note — it names the destination (spread → compact) and two candidate approaches (coordinate removal vs. toolbar), not verified steps.

**Verifies with:** drill this alongside the toolbar pass (Dave's task 6).

**Not to be confused with** `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle`'s `Preserve GridPositions` toggle — that toggle controls compact-vs-sparse at the moment a Layout-view lasso selection is CAPTURED into the selection grid. This note is about collapsing a selection that's already spread out on the grid — a different (though related-sounding) operation, and on the sub-fixture/multi-instance grid rather than the Layout system.

History: none — dictated 2026-07-15, split off from the same INBOX line that already yielded `jdc-look-a-poppy-and-look-b-paired-beams` and `gridstore-keyword-and-fixture-type-write`. This last remaining fragment was carried forward undigested until the 2026-07-16 run since mechanics were never drilled — flagged, not fabricated.

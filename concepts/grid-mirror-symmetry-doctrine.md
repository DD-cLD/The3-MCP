---
id: grid-mirror-symmetry-doctrine
title: "Grid builds should be mirror-symmetric by default — mirror gap positions about center, seam at the SR/SL boundary"
role: programmer
tags: [ma3, doctrine, grid, v2.4]
when_to_load: "Before finalizing any grid layout with gaps or dropped columns — check whether the gap pattern is mirrored about center before storing the Group"
status: active
source: "findings/INBOX.md, 2026-07-14, Dave dictated + hand-demonstrated"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Standing default: **grid builds should be mirror-symmetric unless there's a deliberate reason to be asymmetric.** When a layout has gaps or dropped/skipped columns, mirror their positions about the grid's center axis, and land the seam (the center drop, or the point of symmetry) at the physical stage-right/stage-left boundary.

Dave demonstrated this live rather than just describing it: the first pass at Group 123 used a flat, unmirrored skip pattern (dropping columns 3/7/11/15 to fit 12 spots against 16 wing columns). Dave rebuilt it by hand into a mirrored triplet pattern and stored his edit directly over Group 123 (`Store /Overwrite` — no confirmation dialog fires on `/Overwrite`).

This generalizes past the single Group 123 fix: any time a grid build has to drop, skip, or otherwise unevenly distribute cells, the default assumption should be a mirrored solution, with asymmetry treated as an exception that needs its own justification.

History: none — dictated + hand-demonstrated live 2026-07-14, applied to Group 123 "cLD DS WING PAIRED16." The same principle governs Group 124's bounce pattern — see `grid-bounce-pattern`.

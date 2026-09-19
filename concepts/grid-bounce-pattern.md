---
id: grid-bounce-pattern
title: "The bounce pattern — two fixture types on alternating columns fire alternately; drop the surplus in mirrored triplet gaps"
role: programmer
tags: [ma3, doctrine, grid, v2.4]
when_to_load: "Before building a two-type alternating-column grid chase, or when a fixture count doesn't evenly divide the available alternating slots"
status: active
source: "findings/INBOX.md, 2026-07-14, Dave-specced, drill-verified"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The bounce**: put two fixture types on alternating columns of the same grid row-set so an X-sweeping effect alternates fire between them, step by step — Dave's term for the feel is "bouncing between each step."

Drill case (Group 124 "cLD DS WING BOUNCE"): wings placed on every even column (0-30, 16 columns), leaving 15 odd-column gaps for 12 stage spots. 15 gaps for 12 fixtures doesn't divide evenly, so 3 columns go unfilled. Per the mirror doctrine (`grid-mirror-symmetry-doctrine`), those 3 dropped columns aren't arbitrary — they're mirrored drops at columns 7/15/23, which preserves a 3-3-3-3 triplet rhythm on both sides and lands the center drop exactly on the physical SR/SL seam.

Verified round-trip; all FIDs readable at the drill's 31-column zoom level (see the render-behavior note in `selection-grid-and-fixture-cell-model`).

History: none — specced by Dave and drill-verified live 2026-07-14. Fourth and final member of the 2026-07-14 canonical two-part alignment set — see `grid-drill-exemplar-groups-121-124`.

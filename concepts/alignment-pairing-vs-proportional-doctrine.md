---
id: alignment-pairing-vs-proportional-doctrine
title: "Aligning rig parts with different fixture counts on the grid — pair when counts are close, spread proportionally only when they're far apart"
role: programmer
tags: [ma3, doctrine, grid, matricks, v2.4]
when_to_load: "Before building a shared-X grid layout for two rig parts with different fixture counts — decide whether to pair or proportionally spread before placing anything"
status: active
source: "findings/INBOX.md, 2026-07-14, Dave dictated + drill-verified"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Two techniques exist for lining up rig parts that have different fixture counts onto one shared X window, and Dave's doctrine is about which one to reach for.

**Proportional spread** (the general mechanism): place each part's fixtures across one shared X window at its own step interval (step = window span ÷ fixture count). Any X-axis effect then sweeps all rows at proportionally the same rate, keeping the parts in sync across the window even though their per-fixture spacing differs. Workflow: think through the look, place it on the grid, `Store Group` — chase recipes come later.

**Pairing** (the taste call, drill-verified): when two parts have counts that are *close* (drill case: 16 wings vs. 12 spots), a proportional spread reads as chaotic — the two step intervals only line up at occasional coincidence columns and drift everywhere else. Dave's preferred alternative: align the parts so partnered fixtures share a column and fire together, then place the leftover unpaired fixtures on evenly-spaced columns (drill case: every 4th column). This reads as intentional and clean.

**The rule: pairing beats proportionality when counts are close.** Proportional spreads are reserved for cases with a genuinely large density gap between the two parts (Dave's example: pixel leafs vs. spots), where pairing isn't practical because one part vastly outnumbers the other.

History: none — dictated + drill-verified live 2026-07-14. Worked examples: Group 122 "cLD DS WING ALIGN" (proportional, 12@step4/16@step3 — kept as the density-gap exemplar) vs. Group 123 "cLD DS WING PAIRED16" (paired; later hand-rebuilt mirrored by Dave — see `grid-mirror-symmetry-doctrine`). Full catalog in `grid-drill-exemplar-groups-121-124`.

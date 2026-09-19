---
id: speed-distribution-bpm-hz-decimal-trap
title: "Speed distribution values need decimal adjustment converting BPM to Hz"
role: programmer
tags: [ma3]
when_to_load: "Before setting speed/rate distribution values in MAtricks or a phaser — check whether the value is being entered as BPM or Hz"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Speed distribution values in MA3 need **decimal adjustment** when converting between BPM and Hz representations — the two units are not interchangeable 1:1 and a naive pass-through will be wrong by a scaling factor. Treat any speed value as unit-tagged (BPM vs Hz) and convert explicitly before entry.

History: none — stable note since 2026-04-01. No conversion constant/formula was recorded in the corpus; flagged for future verification if the exact factor is needed.

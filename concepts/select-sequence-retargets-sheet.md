---
id: select-sequence-retargets-sheet
title: "`Select Sequence <n>` retargets the Sequence Sheet view to that sequence"
role: programmer
tags: [ma3, cli, sequence, sheet, v2.4]
when_to_load: "Before assuming the visible Sequence Sheet matches the sequence you're working on via CLI — the sheet stays pinned to Seq 1 Default until explicitly retargeted"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Verified live:** `Select Sequence 101` retargets the visible **Sequence Sheet** to Sequence 101 — before this call the sheet stayed pinned to **Sequence 1 Default** regardless of which sequence was being built via CLI/recipe work. Relevant any time a sheet view needs to follow a non-default sequence (e.g. the recipe build in `recipe-lane-end-to-end-verified`, which used Sequence 101).

History: none — confirmed live in one session, 2026-07-15, during the first recipe build.

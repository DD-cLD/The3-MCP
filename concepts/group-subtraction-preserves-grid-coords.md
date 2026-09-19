---
id: group-subtraction-preserves-grid-coords
title: "Group selection subtraction (`Group A - Group B`) preserves the surviving fixtures' original grid coordinates — gaps show as hollow rows, not a repack"
role: programmer
tags: [ma3, cli, group, grid, v2.4]
when_to_load: "Before using Group subtraction to build a section Group from a larger recalled Group — the result keeps its source grid shape (useful when the grid layout itself is meaningful, e.g. a time-map design), it does not compact-pack the survivors"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Verified live:** `Group 125 - Group 126 ; Store Group 127` → **384 selected** (576 − 192, exact) — the surviving fixtures **keep their original grid coordinates** from the recalled group they came from. Where the subtracted members had occupied a row (a strobe row in this build), that row renders **hollow** in the resulting selection rather than the remaining fixtures repacking to fill the gap.

**Ratified as a design-relevant behavior (Dave, 2026-07-15):** the fact that subtractive group math preserves shape (rather than compacting) matters because the grid doubles as a time-map (see `grid-is-a-time-map-doctrine`) — a hollow row left by subtraction is a different, meaningful thing from a repacked one, and Dave confirmed this is the wanted behavior, not a bug to work around.

**Companion method, ratified same session:** direct dot-range entry (`Fixture 301 Thru 312.33 Thru 48 ; Store Group x`, see `subfixture-thru-range-syntax`) is the primary lane for building section Groups directly; subtractive group math is the complementary lane for carving a section back OUT of an already-recalled larger group.

History: none — subtraction behavior and its design-relevance both confirmed live in one session, 2026-07-15.

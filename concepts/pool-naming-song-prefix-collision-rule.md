---
id: pool-naming-song-prefix-collision-rule
title: "Spell the song prefix out when a short code collides — 'SONG_M' not 'SN', since 'NS' is already SONG_D"
role: programmer
tags: [naming, pools, tourshow]
when_to_load: "Before choosing a short song-prefix code for a pool object name (preset/phaser/MAtricks) — check it doesn't collide with another song's existing short code first"
status: active
source: "findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation, G=0.3 PREFERENCE)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**PREFERENCE (G=0.3).** When a song's short abbreviation code would collide with another
song's, spell the prefix out in full rather than inventing a second short form: **`SONG_M`**
for SONG_M, not `SN` — `NS` is already SONG_D, and `SN` reads as its natural but
wrong sibling.

**Relation:** `pool-labeling-doctrine-inherited-risk` (the sibling risk — renaming/labeling
pools without provenance) · `tourshow-songbuild-kit-and-runbook` (the per-song build line
this naming discipline serves).

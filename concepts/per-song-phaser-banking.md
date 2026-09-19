---
id: per-song-phaser-banking
title: "Phasers are banked per song, not from one big template library — a small shared 'punt page' of basics is the only commons"
role: programmer
tags: [ma3, doctrine, phasers, process, v2.4, tourshow]
when_to_load: "When deciding where a finished phaser/recipe should live, or whether to build a general-purpose effect library — the storage-structure ruling"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Each song's phasers get DESCRIBED during that song's exploration pass (the beatgrid + description layer, per `phaser-story-doctrine`) — programming then means building the pre-described set for that song, and the result is **banked per track**, not pooled into a general library.

Dave's explicit ruling: **no big template bank.** The only shared resource is a small **"punt page"** — basic effect stacks kept as commons for quick starts, not a comprehensive catalogue. Programming enters each song already knowing what it's going to write.

**Relation:** extends `phaser-story-doctrine` — this is what happens to the phaser AFTER the story is written and the recipe is built. Together the two describe the full per-song loop: plan (`phaser-story-doctrine`) → store (this concept).

History: none — doctrine stated 2026-07-16.

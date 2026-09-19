---
id: tourshow-fixture-type-recipe-authoring-gotchas
title: "Fixture-type recipe gotchas: Wash (Dimmer+Color as CHILDREN) needs recipe mode STRICT; QX40 has no Tilt — never give it a Position part"
role: programmer
tags: [tourshow, festival, recipes, fixture-types]
when_to_load: "Before authoring or copying a cue-part recipe onto a Wash or QX40 fixture on any {TOUR} song — Wash needs STRICT recipe mode, QX40 must never get a Position part"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29 (Dave, console fact)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**WASH RECIPES = STRICT.** The Wash fixture type carries Dimmer and Color as **CHILDREN (subfixtures)**, so any recipe touching it must be set to **STRICT** mode — already applied to SONG_T. Card-candidate: an authoring self-verify lint line.

**QX40 HAS NO TILT.** The Position part of the recipe was **DISABLED** on SONG_T for this reason — **never include a Position part for QX40 on any other song.** Card-candidate: an authoring lint line.

**Relation:** `tourshow-floor-package` (QX40 MKII ×7 patched at FID 1401-1407, 25ch mode) · `tourshow-authoring-contract-v01` (the general recipe-authoring contract these are exceptions within).

History: none — captured live 2026-07-29, SONG_T build.


## WASH STRICT law covers phaser lines too, not just value lines — kit needs a post-pass — 2026-07-31 [0731-3cLD]

SONG_D's main sequence landed 12 Strict all-wash sites, **including 3 phaser lines** —
confirming the WASH-recipe-needs-STRICT law (above) applies to **phaser lines, not only
value lines**. The build kit (`ns_emit.py` / the songbuild kit) **only Stricts value lines
by default**; a manual **post-pass** was needed to also Strict the phaser lines targeting
Wash. Future kit work should extend the auto-Strict pass to cover phaser lines on Wash
fixtures, not just value lines.

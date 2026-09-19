---
id: measure-attribute-show-wide-census
title: "Measure attribute, show-wide census: only 28 of 166 figure rows carry one at all, and Measure 4 (one bar) is the ONLY real value anywhere in {LD}'s file"
role: programmer
tags: [ma3, phasers, measure, census, tourshow]
when_to_load: "Before assuming a song's figures need a Measure fixup, or before treating Measure as a common attribute — it is rare and concentrated on one figure class; check the song's own figure data before asserting a Measure action is owed"
status: active
source: "findings/INBOX.md [0805cLD] 2026-08-05, off FIGURE_HASH_SHOWWIDE_v2.csv"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Show-wide census, off `FIGURE_HASH_SHOWWIDE_v2.csv`: only 28 of 166 figure rows carry a
Measure attribute at all.** Of those 28: **7 read `16777216`** — the fixed-point encoding of
literal `1`, i.e. the DEFAULT (not a real measure) — and **21 read `67108864`** — Measure
**4**, one bar.

**Measure 4 is the only real Measure value anywhere in {LD}'s file**, and it lands
specifically on the breathe/swell-class Dim figures: SONG_G `Intro 1/1 Dim`, SONG_D `Swell`,
SONG_J `Swell Dim#3`, SONG_A `Intro 1/1 Strike M US RGB Dim`.

**SONG_L carries ZERO Measure across all 10 of its figure rows** — proven by this census,
not by absence of contrary evidence.

**Consequence — do not reflex a Measure fixup from doctrine.** `phaser-copy-does-not-carry-
measure` documents that a `Copy` doesn't bring a source's Measure along, but that rule only
bites when the SOURCE actually carried one. Check the song's own figure data before asserting
a Measure fixup is owed — see the caution folded into that concept.

**Relation:** `phaser-copy-does-not-carry-measure` (the mechanism this census scopes),
`tourshow-seq2210-song-l-build-record` (the build this census was run for, which the
result cleared of any Measure debt).

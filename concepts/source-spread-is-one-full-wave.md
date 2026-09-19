---
id: source-spread-is-one-full-wave
title: "{LD}'s 6 SONG_T phasers all bake the SAME spatial figure — one full wave, endpoint-exclusive (360×(N-1)/N) — except the Prechorus build, which is deliberate phase-0 unison"
role: programmer
tags: [tourshow, festival, song-t, phaser, matricks, source]
when_to_load: "Before reading or replacing any of {LD}'s SONG_T phasers' spatial spread — all six use one convention, already matched by our own stock MAtricks, so the spatial layer needs no new authoring"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, decoded from Sequence 1500 export; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**All six of {LD}'s SONG_T phasers bake exactly ONE spatial figure: one full wave, endpoint-exclusive** — `PhaseToX = 360 × (N-1)/N` for a group of N fixtures, the standard "don't collide the last fixture with the first" convention (`recipe-phase-endpoint-convention`) applied consistently:

- **Spots (14 fixtures):** `360 × 13/14`, step **25.714°**.
- **Cells (162 fixtures):** `360 × 161/162`, step **3.158°**.

**Exception: the Prechorus build phaser is phase-0 UNISON by design** — every fixture at the same phase, not spread. (Consistent with `cue-structure-is-tonal-harmony`: the Prechorus is the pre-dominant/build, and unison reads as "everyone rising together," distinct from the spread figure used elsewhere.)

**Consequence — nothing new needs authoring for the spatial layer.** The whole spread story is already served by **Dave's existing `MAtricks 101 'cLD Full Spread'`** (0→324°, i.e. `360 × 9/10` — the exact same endpoint-exclusive convention, computed for a different N). It is bound at **10 of the phaser recipe lines**; the **BUILD** phaser stays bare (no MAtricks), matching the unison reading above.

**Relation:** this is the spatial half of the phaser-figure/MAtricks split in `tourshow-authoring-contract-v01`; `source-timing-is-the-tempo-grid` is the temporal half of the same six-phaser decode. `no-baked-n-portable-phaser-doctrine` is the standing doctrine this figure confirms — {LD}'s own file uses the generic endpoint-exclusive convention rather than a hand-tuned literal, on top of the one case (`Intro 1/1 Spot Dim`) already on file as the baked-N failure exemplar.

History: none — decoded in one pass, 2026-07-28, from the Sequence 1500 (SONG_T) export.

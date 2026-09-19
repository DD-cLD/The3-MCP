---
id: beatgrid-treatment-transfer-layer-model
title: "Treatment-transfer layer model: album treatment is expensive (human+cLD); show-version derivation is a 4-layer pipeline, 3 of which are automatable"
role: tools
tags: [beatgrid, process]
when_to_load: "When planning how a song's album lighting treatment becomes its show-edit treatment — or when scoping the 'Transfer treatment' Beatgrid feature"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Proven end-to-end on the SONG_G SHOW bundle (2026-07-07; see `tourshow-days-show-edit-map`), the pipeline splits into 4 layers:

- **Layer 0 — scan:** free. Running BPM/sections/hits detection on the source audio costs nothing extra.
- **Layer 1 — edit-map:** automatable. Deriving the show edit's cut list against the album (offsets, cut boundaries) is mechanical once the paid-for pitfalls are avoided (see `chorus-aliasing-lesson`). Next build step: **port `align_days2.py` into Beatgrid as a "Transfer treatment" feature.**
- **Layer 2 — re-timing:** bookkeeping. Once the edit-map exists, shifting the album treatment's cues onto the show's timeline is arithmetic, not judgment.
- **Layer 3 — edit judgment:** stays human. Deciding what a cut *means* for the design (e.g. the Ember-image question in `tourshow-days-show-edit-map`) is not automatable.

**Implication for sequencing future work: treat albums first — show versions become cheap derivatives** once Layer 1 is built as a Beatgrid feature.

**Edit-map taxonomy (3 classes identified, 2026-07-08):** the Layer-1 edit-map output now has known shapes — **flat-bounce cut** (album cut down with a clean seam; Genius, SONG_G — see `tourshow-genius-show-edit-map`, `tourshow-days-show-edit-map`), **restructured ending** (body maps linearly but the ending is rebuilt from different album material; SONG_N — see `tourshow-song-n-ground-truth-and-edit-map`), and **straight-through** (no cuts at all, just placed in its slot; SONG_T — see `tourshow-song-t-show-edit-map`). Recognizing which class a new song falls into early narrows the Layer-1 search space.

History: none — pipeline articulated and proven same session, 2026-07-07. 2026-07-08: 3-class edit-map taxonomy added, cross-referencing the four song-specific edit-map concepts built so far. 2026-07-16: `phaser-story-doctrine` extends this pipeline past Layer 3 (edit judgment) — per-song phaser stories carry the treatment plan through to console handoff.

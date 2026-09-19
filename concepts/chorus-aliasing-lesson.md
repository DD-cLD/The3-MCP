---
id: chorus-aliasing-lesson
title: "Chorus-aliasing lesson (paid-for): energy-envelope cross-correlation can map repeated choruses onto the WRONG instance at high correlation — trust arithmetic over correlation on repetitive songs"
role: tools
tags: [audio-dsp]
when_to_load: "Before aligning a show/edit bounce against its album source using envelope cross-correlation on a song with repeated choruses or other structurally repetitive sections"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Paid-for lesson (SONG_G edit-map build, 2026-07-07):** a **10Hz energy-envelope cross-correlation** mapped the show's choruses onto the **wrong album instances** — at a correlation of **0.95**, high enough to look confidently correct while being wrong.
- **Why it fails:** repeated choruses in the same song are near-identical in coarse energy shape, so envelope xcorr alone can't distinguish which instance is which — it will happily lock onto the wrong one with a high score.
- **Fix:** **4-band spectral features + a total-length checksum** to break the tie between candidate instances.
- **General principle: trust arithmetic over correlation scores on repetitive songs.** If cut lengths/offsets can be derived and checked by exact addition (as in `tourshow-days-show-edit-map`), that arithmetic closure is stronger evidence than a high correlation score — a wrong-but-plausible correlation match will not, in general, also close arithmetically.

History: none — first paid-for instance of this failure mode, 2026-07-07, during the SONG_G edit-map build (see `tourshow-days-show-edit-map`).

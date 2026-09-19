---
id: bar-math-corroboration-method
title: "Bar-math corroboration method: check 8/16-bar phrase quantization before splitting a machine-merged block — but it validates the offset anchor, not the tempo octave"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before splitting, merging, or otherwise second-guessing a machine-detected section boundary — run the bar-math check first, and before citing a clean bar count as evidence for which tempo octave is correct"
status: active
source: "findings/INBOX.md 2026-07-07 + fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Method:** before inventing a split (or corroborating a merge) in a machine-detected block, check whether the block's duration quantizes cleanly to an 8- or 16-bar (occasionally 4-bar) phrase at the grid tempo. A clean quantization is corroborating evidence for a structural decision; a messy one is evidence against inventing one.

**Positive examples:**
- **SONG_N:** a 57.1s block = *exactly* 32 bars at grid tempo → read as a clean 16+16 verse pair, conf 0.55 (builder A).
- **1 of 1:** a merged 43.5s block (11.59 bars, no clean quantization as a whole) was split at t=47.4 into two sub-blocks landing within ~1s of clean 8-bar and 4-bar phrases respectively — inside the brief's own "adequate, not perfect" tolerance — done specifically so the song's one rationed Impact could land on a real transient instead of an arbitrary boundary.
- **Candy:** Chorus 3 (22.0s) lands at 7.87 bars — essentially a clean 8, supporting its identity as a distinct callback rather than a shapeless continuation of Chorus 2. The full music region spans 64.01 bars — about as clean as this check gets.

**Negative/null examples (equally valid outcomes — absence of quantization is itself information):** SONG_H, SONG_L, Candy's other seven sections, From Scratch (all ten sections), Pilot (all nine), and 1 of 1's Chorus 2 all failed to quantize cleanly at any candidate tempo and were kept as single, un-split regions. A verse-phrased R&B/soul song not quantizing to square EDM-style phrasing is itself an expected, informative result, not a failure of the method.

**Important caveat (surfaced by the Candy build, 2026-07-07): bar-math cleanliness does NOT resolve tempo-octave ambiguity.** When candidate tempos are exact integer/octave multiples of one another (e.g. Candy's 42.93 / 85.86 / 171.72), a block that quantizes cleanly at one candidate will quantize *equally cleanly* at the others (32 bars at one octave = an equally clean 16 or 64 bars at the neighboring octaves). **This method validates the offset/phase anchor** (that the grid's zero-point is real and well-placed) **— it does not tell you which octave is the felt tempo.** Don't overclaim a clean bar count as tempo-resolving evidence; see `bpm-ambiguous-margin-policy` for how octave ambiguity actually gets resolved (or explicitly left flagged).

See also `beatgrid-region-scoped-detection` (the underlying per-region measurement this check consumes).

History: none — method used repeatedly across the bake-off and six-song fleet batch, 2026-07-07; the octave-blindness caveat surfaced and recorded the same day via the Candy build.

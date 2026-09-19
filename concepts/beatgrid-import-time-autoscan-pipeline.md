---
id: beatgrid-import-time-autoscan-pipeline
title: "Beatgrid 0.4.1 import-time autoScan: music region → scoped BPM → sections v2 (hits pulled out, manual-only per Dave's verdict)"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before relying on (or debugging) what beatgrid.html automatically analyzes when a tour bounce is opened or reattached — what runs, what doesn't, and why hits aren't in the chain"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Pre-0.4.1 baseline (the bug this release fixes):** opening a fresh tour bounce auto-ran NOTHING but the TC split + DSP pass. The "slim scan" Dave first saw on SONG_G was actually **manual** Detect-sections running fixed **0.30/0.55 energy banding** — an EDM-shaped heuristic that merges R&B song bodies into one blob (SONG_G: **4 regions, one 2:28 long**).
- That comparison was invalid on top of being slim: the rich SONG_G section map Dave had already seen was **authored content** (`source:"claude"`, an offline librosa + storytelling pass), **never the scanner's own output**. Raw-import vs. rich-map was apples/oranges until autoScan existed to produce a real scanner baseline.
- **0.4.1 ships autoScan:** on file load, the chain is **music region → scoped BPM → sections v2 → hits**, each stage feeding the next. Guarded: **any edited/non-dsp event on the session skips the whole chain** — reattaching audio to an existing session can never bury already-authored work under fresh suggestions.
- **musicRegions** (the first stage): a region is "active" when smoothed energy is **>5% of the file's p95**; regions **merge across gaps <4s**; regions **<12s are dropped**. This trims bounce leaders and splits multi-song files into separate regions — e.g. `01_INTRO.GENIUS`'s spoken intro shows up as its own low-band region, separate from the song body.
- **Dave's verdict on 0.4.1 first contact:** auto-sprayed hits were noise ("no rhyme or reason") — **sections are the deliverable**. Result: autoScan is now **region + BPM + sections only**; **Detect hits is strictly manual**. A persisted **"on open" checkbox** (`localStorage bg_autoOnOpen`) lets Dave disable import-time scanning entirely.
- Release hygiene: the established pre-version backup convention held for this ship — `_rubbish/beatgrid_v0.4_pre-0.4.1_2026-07-07.html`.

See `beatgrid-bpm-estimator-octave-fix` and `beatgrid-sections-v2-novelty-segmentation` for the scoped-BPM and sections-v2 stages in detail.

History: none — designed, shipped, and immediately corrected (hits pulled from the chain) same session, 2026-07-07.

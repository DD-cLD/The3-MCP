---
id: beatgrid-sections-v2-novelty-segmentation
title: "Sections v2: novelty-primary segmentation (rank-normalized energy+spectral-tilt, adaptive terciles, rubato-safe bar-snap) replaces the fixed-grid detector"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before trusting or extending beatgrid's automatic section-boundary detection, especially on rubato/non-4-bar-rigid material"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Sections v2 = novelty-primary segmentation:** rank-normalized **energy + spectral-tilt**, **8s averaging**, **0.5s boundary refine**, and **snap-to-4-bar only when the snap distance is ≤1.25s** (rubato-safe — fixed 4-bar grids were drifting off the music on SONG_G). Uses **adaptive terciles** and a **42s blob failsafe** (guards against one giant undifferentiated section).
- **Validated against the curated SONG_G map:** **9 of 11** curated boundaries landed within drag distance, vs. roughly **2 of 11** before v2.
- **Validated on the real bounces:** `09_SONG-G` auto-scan produced **10 sections with verse-chorus alternation**, vs. the old detector's **4 blobs**; `21_SONG-G SHORT` produced **6 sections**. (Confirms tour SONG_G is already a cutdown of the 243s album track — 190s and 123s edits — see `tourshow-days-show-edit-map` for the edit itself.)

See `beatgrid-import-time-autoscan-pipeline` for where this sits in the autoScan chain, and `beatgrid-dsp-reality-check` for the earlier "structure lives at 4–8s timescale" finding this design builds on.

History: none — designed and shipped 2026-07-07, validated same session against both curated and real-bounce material.

---
id: measure-layer-math
title: "Measure layer — definition (official manual) and runtime-scale math (MA forum 68396)"
role: programmer
tags: [ma3, recipes, measures, math, v2.4]
when_to_load: "Before setting a Measure value on a phaser/recipe layer, or before predicting how long a step/loop will actually take once Measure is set — the repo manual does not define this layer, this is the forum-sourced formula"
status: active
source: "findings/INBOX.md, 2026-07-16 (official MA_V2.4.2_MANUAL for the definition; MA forum thread 68396, Andreas/MA, for the math)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Definition (official 2.4 manual):** Measure is an optional phaser layer = the number of **beats** in one loop. Combined with Speed, it fixes the loop's real time (e.g. `Measure 4 @ 120 BPM = 2s`). Knocking in Measure with **no value** adopts the current step count. Speed, Speedmaster, Phase, and Measure are all **per-attribute-per-fixture**, and stay **constant across steps**.

**Runtime-scale math (Andreas/MA, forum thread 68396):**
- With **no Measure set**, loop length = `Σwidths / 100` beats.
- With **Measure set**, runtime scale = `Measure ÷ (Σwidths / 100)`. Widths are **NOT rewritten** — proportions are preserved, only the playback rate scales.
- Per-step time: `step_beats = Measure × width ÷ Σwidths`.
- Reading: widths compose the note values (relative proportions within the loop); Measure is the bar — the absolute time budget the widths get stretched or compressed to fit.

**Why this had to be forum-sourced:** the repo manual has **no definition of the Measure layer** (column label only — repo-manual gap #4+). The full manual-vs-live study (15-test matrix) is written up in `PHASER_MEASURES_STUDY_v0.1.md` (WORKING/).

Cross-reference: `stock-measures-grammar-census` for how MA's own stock recipe library actually uses Measure per effect category; `wipe-in-thru-range-anatomy` for a full worked example of widths distributing inside one `Measure=1` loop; `phasers-via-measures-curriculum` for the teaching approach that produced this study.

History: created 2026-07-16, merging the official-manual definition with the forum-sourced runtime formula (two parts of one Measure-math concept) plus the repo-manual-gap provenance note.

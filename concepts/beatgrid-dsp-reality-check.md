---
id: beatgrid-dsp-reality-check
title: "Beatgrid DSP reality check — energy-threshold drops, hit detection, structure timescale, and BPM-grid drift, all against a real non-EDM track"
role: tools
tags: [audio-dsp]
when_to_load: "Before trusting the beatgrid prototype's drop-detector, onset/hit-detector, or fixed-BPM grid on a real (especially non-EDM) track, or before analyzing a multi-segment tour bounce with whole-file stats instead of a scoped region — read this before relying on any of the findings below"
status: active
source: "MEMORY §Paid-for lessons 2026-06-29 — Beatgrid DSP reality; findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Test track: "001 No Stopping - Inland Knights.mp3" (deep house, 6:09, ~122 BPM). Live in `WORKING/beatgrid/`.

- **Energy-threshold drop detection is mostly false on non-EDM.** The suck-out/drop detector fired **11 false drops** — all 0.08–0.12s sidechain/kick micro-gaps inside the loud peak sections — and **missed the real 3:19 breakdown entirely** (its floor threshold is 12% of peak, but the breakdown sits ~16%, and it rejects floors longer than 2.5s). Don't trust this detector outside clean EDM build/drop material.
- **"Hits" track silence, not importance.** Top-30 broadband onsets ≥ mean+3.5σ clustered in the quiet intro/outro and vanished in the dense middle (nothing clears 3.5σ in a compressed loud mix). Loudness ≠ musical hit.
- **Structure IS cheaply detectable — at the right timescale.** A coarse (4–8s) energy-envelope segmentation recovers the true arc cleanly (intro / pullback / build / peak / breakdown / rebuild / peak / outro). The lesson: musical structure lives in **sustained** energy change over seconds, not 0.1s gaps. This is what `detectSections()` does.
- **A rigid single-BPM grid drifts.** Even with the right tempo (~122), autocorrelation at hop=512 only resolves ~0.7 BPM/step; over a 6-min track the grid walks off the music by ~2 beats by the end. A real beat-tracker (or frequent hand re-anchoring) is needed for long tracks; don't trust the grid in the back half.

- **Global (whole-file) statistics fail across heterogeneous/multi-segment material — even with clean audio.** Diagnosed 2026-07-07 on the first real tour bounce (`01_INTRO.GENIUS`, TC-split, LTC channel confirmed clean — see `tc-split-bounces-and-ltc-tools`): the file is ~100s of intro material bolted onto the Genius album track, and a single global σ/eMax/top-30 computed across both segments produced weak-looking results. Not an LTC/split artifact — a global-threshold-on-heterogeneous-material artifact, same family as the false-positive/false-negative findings above, just triggered by segment structure instead of genre. **Cure shipped 2026-07-07: region-scoped detection** — see `beatgrid-region-scoped-detection`. Tour-bounce workflow going forward: punch song regions, then detect per song.

History: none — the first four findings are from one test-track session, 2026-06-29, and are best loaded together (same evidentiary basis, same "don't trust the naive version of this analysis" theme). 2026-07-07: a 5th finding added from real tour-bounce material — same theme, different trigger (multi-segment files, not genre); the cure is a separate concept, `beatgrid-region-scoped-detection`.

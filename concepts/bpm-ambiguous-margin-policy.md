---
id: bpm-ambiguous-margin-policy
title: "Ambiguous-margin BPM policy: sub-50 winners by <0.1 contrast margin get the proto pick + an ear flag, not a forced resolution"
role: tools
tags: [beatgrid, audio-dsp, process]
when_to_load: "When a beatgrid/proto BPM contrast table shows two or more candidates within ~0.1 of each other — decide whether to force a tempo call or flag it"
status: active
source: "findings/INBOX.md 2026-07-08 + fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Policy:** when the top BPM-contrast candidates score within roughly **<0.1 of each other**, take the **proto/grid_final pick as-is**, carry a **✎ ear-check flag** into every deliverable, and do **not** force a resolution by judgment call. This is how the fleet build batch handled genuine ambiguity rather than manufacturing false confidence.

**Tactus-trap catalogue (growing; see `beatgrid-bpm-estimator-octave-fix` for the underlying estimator mechanism):**
- **SONG_G** (existing catalogue entry) — felt-half tempo, gridded high.
- **SONG_N** (bake-off) — proto's tactus-band preference promoted 134.58 over the comb-winning 67.29; see `tourshow-song-n-ground-truth-and-edit-map`.
- **SONG_H** — grid 78.43, contrast 0.408; alternate 39.22 at 0.349 — close enough to flag (both builds carried the ✎ flag into every file).
- **Candy** — grid_final 85.86 (contrast 0.416) is *not even the top scorer*: 42.93 scores 0.502, and 171.72 scores 0.43 — 85.86 was promoted by tactus-band preference, not raw contrast. Carried as an open ✎ flag, unedited from `grid_final` per house rule.
- **1 of 1** — **decisive counter-example**, not a trap: 63.96 wins at 0.792 vs. 0.126@127.92 — the proto pick correctly resisted the doubling here, and the file documents this explicitly as "the third such catch in the catalogue" (i.e. the contrast table catching what a naive tactus-band preference would have doubled). No ✎ flag needed.
- **SONG_L** — different shape: *both* readings are weak (149.59→0.187, 74.8→0.122), not just close to each other — carried as an open ✎ flag per house rule (grid uses 149.59 unedited).

**Rule of thumb this establishes:** a decisive win (large contrast gap, as in 1 of 1 or From Scratch's 97.0@0.896) needs no flag. A close-margin or uniformly-weak contrast table gets the grid's own pick honored verbatim, plus a mandatory ✎ flag through every deliverable (analysis JSON, cuelist footer, moodboard, CSV revision notes) — never silently resolved either direction.

See also `bar-math-corroboration-method` (a second, independent check that can corroborate the *offset/phase* anchor but does **not** resolve octave ambiguity) and `librosa-triplet-subdivision-lock` (a related but mathematically distinct 2:3 confusion class).

History: none — policy and catalogue compiled 2026-07-07→08 across the bake-off and the six-song fleet batch.

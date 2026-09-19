---
id: librosa-triplet-subdivision-lock
title: "librosa locks onto the 2:3 TRIPLET pulse on soul shuffles, not just octave doubles — treat 2:3 relatives as subdivision suspects, not tempo candidates"
role: tools
tags: [audio-dsp]
when_to_load: "When a librosa-based BPM estimate on a shuffle/swing-feel track keeps returning a value that is exactly 1.5x (or 2/3x) another plausible candidate"
status: active
source: "findings/INBOX.md 2026-07-07, bake-off (both builders independently)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

On SONG_N (slow soul shuffle), **librosa stubbornly locks onto the TRIPLET pulse** — **99.4 BPM = 67.3 × 1.5** — and this holds across `beat_track`, `tempo`, and `autocorr`, and across multiple random seedings. Both bake-off builders converged on this independently.

**This is a distinct failure class from octave doubling** (see `beatgrid-bpm-estimator-octave-fix` and `bpm-ambiguous-margin-policy`, both about ×½/×1/×2 confusion). A 2:3 (or 3:2) relative is a **subdivision** relationship — shuffle/swing feel naturally has a strong triplet subdivision that a beat tracker can mistake for the primary pulse.

**Rule:** when a BPM candidate is a clean 2:3 or 3:2 ratio of another plausible candidate on shuffle/swing material, treat it as a **subdivision suspect**, not as an independent tempo candidate to weigh on equal footing. Don't let it enter contrast tables as if it were an octave relative.

History: none — first documented instance, 2026-07-07 bake-off (SONG_N), both builders.

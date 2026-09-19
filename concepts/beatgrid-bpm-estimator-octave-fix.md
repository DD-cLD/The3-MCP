---
id: beatgrid-bpm-estimator-octave-fix
title: "estimateBPM's EDM-octave fold (80–180 range) doubled slow soul tempos — fixed with scored octave candidates + a 90–150 tactus preference"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before trusting a beatgrid BPM readout on a non-EDM or slow-tempo track, or when validating the estimator against known/written tempos"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Bug:** `estimateBPM`'s 80–180 BPM "EDM octave" fold doubled slow soul tempos (e.g. **76 → 152**).
- **Fix:** score octave candidates (**×½ / ×1 / ×2**) by **on-beat onset support**, and **prefer the 90–150 BPM tactus band when it holds ≥50% support** — rather than blindly folding everything into 80–180.
- **Validated album↔bounce (2026-07-07):** SONG_T **139.13 / 139.17**; Genius **118.95 / 118.97** — **0.04 BPM agreement**.
- **Correctly does NOT over-correct:** SONG_E's bounce honestly reads **58 BPM** (it's a true slow-jam) — **116** is offered as a **typed alternate**, not forced. The band preference doesn't force fast octaves onto ballads.
- **SONG_G real-bounce validation:** `09_SONG-G` auto-scan BPM **114.96** (= Dave's programmed **115**); `21_SONG-G SHORT` — same BPM.
- **Cross-validated against the written tour TC sheet** (see `tourshow-artist-tc-sheet` for the full sheet record): **5 of 6** estimator readings match written BPMs (Genius 119, SONG_T 139, SONG_D 94, SONG_C 120, SONG_G 115 all agree; SONG_E's 116 is the sheet-confirmed typed alternate). **SONG_B is the one open discrepancy: sheet says 142, heard/estimated ~113.6** — flagged, needs a written-vs-felt check on console open, not yet resolved.

**Residual failure mode found in the 90–150 tactus-band preference itself (2026-07-07, bake-off):** on SONG_N (slow soul shuffle), the band preference promoted **134.58** over the comb-contrast-winning **67.29** (0.245 vs 0.400) — the same EDM-tactus assumption that motivated the original fix can itself misfire on slow soul when a sub-90 candidate actually wins on raw contrast. **JS-port fix queued (not yet shipped):** surface the sub-90 alternate whenever it out-scores the band-preferred pick on raw comb contrast, rather than trusting the band preference unconditionally. See `bpm-ambiguous-margin-policy` for how the fleet build handled ambiguous cases in the meantime, and `tourshow-song-n-ground-truth-and-edit-map` for the full SONG_N grid.

History: none — algorithm fixed and validated same session, 2026-07-07 (fix + first validation set); song-g-bounce and TC-sheet cross-validation landed later the same session. 2026-07-07 (bake-off, later same day): a residual misfire in the 90–150 tactus-band preference documented on SONG_N — a queued JS-port fix (surface the sub-90 alternate on contrast win) is not yet shipped.

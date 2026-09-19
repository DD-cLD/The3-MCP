---
id: birds-eye-batch2-grids-and-tempo-flags
title: "Bird's Eye fleet-batch grids: BPM/offset/meter per song, tempo-contrast confidence, and where each song's one Impact landed"
role: design
tags: [tourshow, audio-dsp]
when_to_load: "When you need a specific Bird's Eye song's grid (bpm/offset/meter/fps), its tempo-ambiguity status, or where its rationed Impact landed"
status: active
source: "fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Grid facts as built (`grid_final`, unedited from ground truth per house rule — see `bpm-ambiguous-margin-policy`). **Meter is 4/4 across all six** — GT states no meter on this batch; explicitly flagged ASSUMED in the Candy/From Scratch/Pilot builds, consistently applied across the batch. **FPS is 30 across all six.**

| Song | Track # | bpm | offset | Tempo confidence | Impact landed at | Palette |
|---|---|---|---|---|---|---|
| SONG_H | — | 78.43 | 1.07 | Ambiguous: 0.408 vs alt 39.22@0.349 (close) | 1:44 / `01:01:44:24` (climax exit of the sanctioned strobe window) | ASSIGNED — see `tourshow-palette-and-groove-v2` June-1 table |
| SONG_L | 04 | 149.59 | 0.33 | Soft both readings: 0.187 vs alt 74.8@0.122 | Verse 3, t=164.2s (hottest of 5 flagged transients) | ASSIGNED but tension-flagged — see `birds-eye-unassigned-song-palette-proposals` |
| Candy | 05 | 85.86 | 0.79 | NOT top contrast: 42.93 scores highest (0.502); 85.86=0.416; 171.72=0.43 — promoted by tactus preference, not raw contrast | Chorus 2, t=95.9s (11.6s in; GT's own highest transient) | PROPOSED — see `birds-eye-unassigned-song-palette-proposals` |
| From Scratch | 08 | 97.0 | 0.33 | Clean/decisive: 0.896 vs 48.5@0.662, 194.0@0.27 | Verse 5, 158.7–176.3s (no transient support — corroborated only by two independent loudness measures) | PROPOSED — see `birds-eye-unassigned-song-palette-proposals` |
| 1 of 1 | — | 63.96 | 0.58 | Decisive: 0.792 vs 127.92@0.126, 255.84@0.094 — tactus-trap 3rd catalogue instance, correctly resisted | Split region at t=47.4 (Chorus 1 / Impact sub-split — see `bar-math-corroboration-method`) | PROPOSED — see `birds-eye-unassigned-song-palette-proposals` |
| Pilot | 10 | 85.84 | 0.67 | Clean/decisive: 0.375 vs 42.92@0.238, 171.68@0.15 | Chorus, 1:52.5 (9.2s into the section; second-hottest onset, corroborated by RMS) | PROPOSED — see `birds-eye-unassigned-song-palette-proposals` |

See `bpm-ambiguous-margin-policy` for the ambiguous-margin handling rule these tempo-confidence values follow, and `impact-placement-heuristic` for the reasoning pattern behind the Impact column.

History: none — all six grids measured/built same overnight fleet session, 2026-07-07.

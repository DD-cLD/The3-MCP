---
id: birds-eye-unassigned-song-palette-proposals
title: "Four Bird's Eye songs have no June-1 palette assignment — ◆ PROPOSED palettes built from the lock's own anchor set, all pending Dave's ratify"
role: design
tags: [tourshow, design]
when_to_load: "Before treating Candy, From Scratch, 1 of 1, or Pilot's palette as settled — these are proposals, not assignments; also before touching SONG_L's palette, which is assigned but has an open tension flag"
status: active
source: "fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Candy, From Scratch, 1 of 1, and Pilot are **not among the 18 songs in `ARTIST_TOURSHOW_PALETTE_LOCK_v0.1.md`'s June-1 table** — each build proposed a palette from the lock's own anchor set (axis logic, existing family names/hexes) rather than inventing new colors. **All four are flagged ◆ PROPOSED throughout their bundles (analysis JSON, moodboard, cuelist chips, QCaller header) — none of this is load-bearing until Dave ratifies it.**

- **Candy:** Neutral White (frame) + **Blush Pink `#CC7598`** (GROUND-leaning, "the candy itself," carries the front three-quarters) + **Deep Sat Purple `#5B4B8A`** (AIR-axis "plum," enters only at the Breakdown/comedown). Deliberately not the same pair as SONG_H (Neutral + Blush/Pastel Pink) so the two songs don't wear the same signature.
- **From Scratch:** **Warm White** (frame, the lock's "ground white — skin, intimacy") + **Amber / Gold** (single punch family, matches the base HTML template's default punch color `#E6A23C`). Grounded in two live web searches (track position/runtime + general lyric theme — a plain-spoken commitment song) rather than the title alone; no lyric text reproduced. Ember/Burnt Orange, Deep Sat Red, and the pink family were considered and rejected (reasoning in `fromscratch_analysis.json.palette_proposal.alternatives_considered`).
- **1 of 1:** 5-swatch proposal — **Warm White** (frame, all of it — no cool family introduced even for the brighter Intro/Bridge) + **Blush Pink** (signature) + **Amber/Gold** (secondary), plus one derived pale tint (**Rose Glow**) and one small coda accent (**Dusk Plum**, outro's last few seconds only). Grounded in verified real lyrics/credits (readdork.com/LRCLIB) confirming a devotion-song theme, cited by URL in the analysis file.
- **Pilot:** **Deep Sat Blue `#1E3454`** + **Haze Blue `#7FA8C9`** (punches, rationed to the Build/Chorus where both tilt and RMS climb together) with **Warm White `#FFD9A0`** + **Cool White `#DCE8FF`** (frame) — read as a progression across the song's arc (pattern precedent: SONG_E's "Amber → Ember," SONG_G' "Gold → Deep Desaturated Orange" in the lock), not layered in one cue. Warm White carries her on the floor throughout per the axis law ("warm lives low, cool lives high") even though the song overall leans cool.

**SONG_L is different: it IS assigned (June-1 row 13 = Neutral White + Deep Sat Blue), but carries an open tension flag, not a proposal.** The Position note calls SONG_L an AIR-pole song (cool, distance, night), which would pair more naturally with **Cool White** (~7500K, the lock's own "air" white) than the assigned **Neutral White** (~4800K, daytime-stark default). Built literally as written (Neutral White) per house rule — flag conflicts, don't smuggle a fix — noted in `song-l_analysis.json.palette_tension_flag`. A Cool-White swap, if ratified, is a one-line change across the bundle.

See `tourshow-palette-and-groove-v2` for the palette lock itself, and `birds-eye-batch2-grids-and-tempo-flags` for these songs' grid facts.

History: none — all five flags (4 proposals + 1 tension) raised same overnight fleet session, 2026-07-07.

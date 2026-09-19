---
id: tourshow-crosswalk-prework-alias-gap
title: "18-song crosswalk prework DONE — the SONG_T substitution map holds everywhere, but the other 17 bind a RENAMED group layer; a NAME-ALIAS extension + 3 rulings are owed before it's usable"
role: programmer
tags: [tourshow, festival, crosswalk, setlist]
when_to_load: "Before starting crosswalk work on any of the 18 remaining songs — the prework is done, where its tables live, what the NAME-ALIAS extension + 3 owed rulings are, and which songs (SONG_S, maybe SONG_R) are full-authors rather than crosswalk jobs"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29 (prework COMPLETE — 6 smiths, 18 songs, ~928k tokens); wraps/2026-07-29-song-t-complete-fills-cutover-prework.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Prework complete.** Tables and per-song detail live in **`SETLIST_CROSSWALK_PREP_v0.1.md`** (WORKING root) + **19 sheets** in `generated/crosswalk_prep/` — **load those for the actual data; this concept is the headline and pointer, not a duplicate of the tables.**

## Headline

The SONG_T substitution map (the crosswalk that closed SONG_T) **holds everywhere** — but the other 17 songs bind a **RENAMED group layer** that SONG_T didn't have to deal with:

- **JDC1 US/DS/SW** = the **old Strike M rows**, now pointing at **QX40** / groups `511`/`512`.
- **CL** = **PL, renamed** — ghost-group + phaser-binding proof on file.
- **Spots + Beam `[Sym]` combos** also need the renamed-layer treatment.

**A NAME-ALIAS extension (mapping the renamed layer back to the substitution map) closes an estimated 50-70% of currently-"unmapped" bindings without needing any new Dave rulings.**

## Genuinely-new rulings still owed (not closeable by aliasing alone)

- **Sym treatment** — how `[Sym]` combos resolve.
- **Beam-pool MM walls** — `RateFast`/`Open` 12-19-group walls, a pattern that repeats across the setlist.
- **Dimmer `'20'`/`'30'` slots.**

## SONG_R (2800) — status uncertain, needs a desk check

**SONG_R's main sequence is an EMPTY SKELETON:** 17 named cues, zero content, and no other SONG_R sequence appears anywhere in the TC exports. Needs a **console-side content check** — if there's genuinely nothing there, SONG_R joins SONG_S as a full-author song rather than a crosswalk job. (Separately, SONG_R's **aux-layer count is 0** per the per-song architecture decode — see `tourshow-fill-layer-rebuild-method` — consistent with either reading.)

## SONG_S builds LAST — the other full-author song

**SONG_S has no {LD} TC to retarget at all** — it's authored (song + timecode) entirely from scratch, and is scheduled as the **final slot** in the 19-song build order specifically because of that. The TC-authoring lane needed for it is already proven: cLD's SONG_G TC was hand-authored and imported clean, and the beatgrid `startSec` → `CmdEvent Time` bridge is banked (`tc-bump-button-architecture`, `export-timecode-tc-event-xml-schema`).

## Cross-song structural facts (confirmed across the 19-export scan)

- **Mono-part cues: the P1-P8 per-fixture-class part scheme is OURS**, not inherited.
- **`Note` attribute = BPM**, consistently.
- **Beat-locked fades** throughout (consistent with the SONG_T timing decode, `source-timing-is-the-tempo-grid`).
- **Phaser gears ÷1/÷2/÷4/÷8** appear in the defs across songs (see the speed decode in `tourshow-fill-layer-rebuild-method` for the mechanism).
- **`Active=No` on 70-89% of objects** — a cook-state artifact, not a meaningful flag.
- **`Strict` on MM marks**, consistently.
- **Hazard labels observed:** `U+221A JDC1 DS MM` · `'Guitar Swell '` (trailing space) · `'I I'`.

## Design-input pipeline

**COLORS FROM {DESIGNER}:** per-song color palettes come from {DESIGNER}'s simplified design handoff sheets; Dave is pulling them. This is the design-side input the 18 rebuilds are waiting on — the sheets carry per-song distinct-color-slot counts to author against.

**Relation:** `tourshow-fill-layer-rebuild-method` (the per-song build method this crosswalk feeds) · `inherited-file-membership-is-ground-truth` (why a renamed-but-truthful group layer is expected, not a surprise) · `tc-track-target-cutover` (the cutover mechanic each crosswalked song will use once its groups resolve).

History: none — prework completed and headline captured in one session, 2026-07-29.


## ⭐ WHOLE-SHOW CROSSWALK NOW EFFECTIVELY LOCKED 2026-08-03 [0803-1cLD] — 100% group coverage, zero unmapped

**All 18 {LD} song sequences run against the ratified submap, file-side, zero console contact: 2,636 sequence recipe lines across 384 cues — 100.0% of groups MAPPED, ZERO unmapped.** The crosswalk is effectively already locked at the group layer for the ENTIRE show, not just the 10 songs built so far — this is the fact that makes a "lock the crosswalk, then speed-run the remaining builds" plan viable rather than aspirational.

**Show-wide inventory, same pass:** 2,636 lines · 384 cues · 106 phaser figure uses · 17 distinct {LD} colours. Biggest colours by line count: Deep Saturated Blue 86 (8 songs) · Soft Desaturated Blue 63 (4) · Pastel Pink 33 (3) · Lite Blue 33 (2) · Saturated Pink 33 (2) · Neutral White 32 (6) · Lavender 32 (1). The Key CTB / Key White / Key CTO trio appears in 5-7 songs each at 1 line per song — these ride the HELD Follow Spots lane.

**Repo debt found by the same pass:** only 4 preset gaps exist show-wide, and **3 of them have been getting patched LOCALLY, per-song, instead of promoted into `cld_submap.PRESETS_FIXED`**: `Position.I I` (14 songs, 17 lines), `Position.Side Wash [Forte SW]` (17 songs, 17 lines), `Position.Stage Wash [VL3600 + Strike M SW]` (17 songs, 17 lines). Every build so far has carried these as a per-song local dict rather than a promoted fix — promote once, delete the local patches. (The 4th gap, `Position.Release Relative`, is not debt — it is the release-dialect exemplar, see `release-relative-universal-preset-exemplar-proven`.)

**Template-mapping precedent (Dave), keep separate templates for near-identical-looking source phasers:** {LD}'s `Dim_PWM` maps to **cLD WIPE IN** (`21.71`); `Dim_PWM_THIN` maps to **cLD TRAPEZE** (`21.56`). The two PWM variants deliberately map to DIFFERENT templates — plain PWM is a 50/50 square Dave reads as a travelling wipe ("it's a good look"), THIN is the sliver. **Do not collapse them into one template.**

## ⛔ RULED 2026-08-03 [0803-1cLD] — SONG_R is confirmed empty, and SONG_R + SONG_S are NOT full-authored from scratch after all; the crosswalk key for both is TIME, not groups

**SONG_R ({LD} 2800) is confirmed EMPTY: 0 cues, 0 recipe lines** (the export is a 6 KB stub) — this settles the "status uncertain, needs a desk check" open item above; either it was never programmed or the export didn't capture it, and Dave confirmed before it was counted as a build target.

**RULED (Dave) — SONG_R and SONG_S are NOT authored from scratch. Crosswalk a like song instead; the crosswalk key this time is TIME, not groups.** Method as planned: SONG_R keeps its own 17-cue NAMED skeleton ({LD}'s 2800 cue names, though contentless, ARE the section map) -> a donor song's content maps on by SECTION NAME -> then re-time everything to SONG_R's own target beatgrid, with fades regenerated from the target BPM, never copied as raw seconds. **SONG_S has no skeleton at all**, so it needs a donor AND an all-new cue spine — it remains the one genuinely new build in the setlist, now with a defined method (donor content + built spine) rather than pure invention. Donor selection for both is Dave's call, not yet made as of this backlog.


## SONG_S donor decision deferred, 2026-08-03 [0803-2cLD]

Dave picks the donor later. Source line does not elaborate what "donor" refers to beyond the deferral itself — flagged, not inferred further. **No change to run order:** SONG_S stays LAST (see "SONG_S builds LAST," above); no other work blocks on the deferred decision.

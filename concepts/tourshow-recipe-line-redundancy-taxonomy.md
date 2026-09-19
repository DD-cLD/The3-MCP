---
id: tourshow-recipe-line-redundancy-taxonomy
title: "Recipe-line redundancy taxonomy: the emitter does not dedup by design (crosswalk collapse); parent+child group overlap is invisible to an identity-dupe census; same value in two century PARTS is not a duplicate"
role: programmer
tags: [redundancy, duplicate, crosswalk, groups, tourshow]
when_to_load: "Before deleting an apparent duplicate recipe line at the desk, or before trusting an identity-duplicate (group,value) census as a complete redundancy check — several redundancy shapes exist and only some of them are real bugs"
status: active
source: "BACKLOG.md 2026-08-01 [0801-2cLD], 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Three distinct redundancy shapes exist in the crosswalked output, and they need different responses. Conflating them is exactly what almost cost SONG_J its wash layer (some songs' wash content landed on a beam target and was hand-deleted at the desk as an apparent duplicate — an open, Dave-owned action item, not detailed further here).

## Shape 1 — identity-duplicate lines (emitter does not dedup, and that is expected)

**The emitter does not dedup, and the shipped SONG_J file carried 38 EXCESS DUPLICATE RECIPE LINES across 22 (cue, group, value) groups — {LD}'s source has ZERO.** Every one is a **crosswalk COLLAPSE**: several distinct {LD} groups map onto one cLD group and happen to carry the same value in the same cue (e.g. `JDC1 US [MM]` + `[MMRGB]` + `[MMSTB]` all -> `cLD QX40 MM ALL @ Beam.RateFast`). Harmless to output — the same value is simply written twice — **but this is exactly what a doubled line looks like at the desk**, the same shape as the wash-defect failure mode. SONG_J's specific desk-edit outcome: 26 of the 38 cleared by Dave (the cue 21/22/23 `Beam.RateFast`/`Beam.Open` pile-ups collapsed ×3->×1 and ×2->×1); **12 excess still stand** (cue 21 BEAMS DS/MS + PLINE UPPER/BAND + QX40 MM; cue 23 QX40 MM; cue 27.1 BEAMS DS + MS).

## Shape 2 — parent + child GROUP overlap (invisible to the identity-dupe census)

**A redundancy class the identity-dupe census cannot see, because the group NAMES differ:** e.g. `cLD BEAMS ALL` alongside `cLD BEAMS DS` and `US` + `cLD BEAMS MS1` + `2` — same fixtures, same ingredient, same cue, but a (group, value) repeat count is blind to it since the names don't match. 3 sites in SONG_J (c20.1 `Dimmer.0`; c27.1 `Ultra Cool White` and `Dimmer.0`).

**⚠ The same test does NOT hold for JDC:** `cLD PLATES GRID` and `cLD TUBES GRID` are **different SUBFIXTURE ENGINES on the same physical bodies**, so a `JDC ALL` line beside a `PLATES GRID` line can both be legitimately real at once — do not flag JDC parent/child pairs as automatic overlap. Containment is currently INFERRED from `ARTIST_TOURSHOW_GROUP_CONTRACT` (row scopes DS/MS1/MS2/US tile a category) — a live Group membership census would make this provable and is still owed.

**Removal direction is a taste call, not a mechanical collapse — do not automate it.** Observed case: Dave's Mark-cue beam edit was NOT "collapse to the parent" (the natural-sounding shorthand). He instead removed `cLD BEAMS ALL`'s Position and Colour and KEPT the per-child lines, then repositioned MS1+2 (Stage Wash Base -> cLD Mid) and RIVALE (Pan X 1 -> Pan Fan) — because the children needed DIFFERENT positions (DS/US at Lowest, MS1+2 at Mid), so the PARENT's blanket position was the line that had to go. **Rule as observed: remove whichever line is redundant or in conflict given what the children actually need — direction depends on the cue.**

**⚑ Open question for Dave, same redundancy family:** at SONG_J cue 23.1 Dave removed `cLD QX40 MM ALL @ Dimmer.Full` (an expansion line, see `tourshow-stb-white-release-ruling`) and `cLD QX40 COLOR @ Dimmer.0` ({LD}'s own line, which fought the expansion's `Dimmer.Full`) — reading as a deliberate rule that when the MM engine also carries a phaser, the expansion's `Dimmer.Full` is redundant. **The same pattern still stands unedited at SONG_J cues 8.1, 10.1 and 15.1** (`QX40 MM ALL` carrying `Dimmer.Full` + `Swell Sine 2`). If it is a rule it belongs in the emitter and those three want the same treatment; if 23.1 was a one-off taste call, leave them. **Not resolved.**

## Shape 3 — same value in two different century PARTS is NOT a duplicate

**"Delete-thinking-it-is-a-duplicate" is a distinct desk failure mode:** parts-per-century puts the same VALUE on two different century parts routinely (a wash line in P2 beside a beam line in P5 can look like one doubled line in a flat sheet view). **Before deleting an apparent duplicate at the desk, check the PART it sits in** — the same value in two different centuries is the architecture working correctly, not a double.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (the sibling redundancy class at the POOL-OBJECT/figure level rather than the recipe-line level). `reconciliation-identity-per-song-verification-method` (corrections found this way are logged to the ledger, deferred to circle-back — not fixed in place mid-run). `tourshow-cue-century-review-sheet-doctrine` (the review artifact these shapes are read off of).

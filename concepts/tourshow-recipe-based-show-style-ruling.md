---
id: tourshow-recipe-based-show-style-ruling
title: "{TOUR} is recipe-based programming all the way through — not Broadway cue-to-cue"
role: programmer
tags: [ma3, doctrine, tourshow, recipes, v2.4]
when_to_load: "Before choosing a programming approach for any {TOUR} cue — settles cue-to-cue vs recipe-based at the show level, not per-cue"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's ruling: {TOUR}'s programming style is **recipe-based ALL THE WAY THROUGH** — not the Broadway cue-to-cue model (hand-built, fully-baked cues one at a time). Recipes (Selection/Group reference × preset-values reference × shape × grid/measure — see `recipe-lane-end-to-end-verified` for the mechanics) are the **PRIMARY programming mode** for the whole rebuild, not one tool among several.

**Relation:** this is the show-level "what mode do we build in" ruling; `tourshow-programming-ramp-plan` is the separate "in what order do we build" sequencing plan — load both together when planning build sessions.

**DOCTRINE, extended (2026-07-17, Dave, dictated, paraphrased):** building a phaser recipe directly into a cue part is mechanically possible, but it is NOT our working style. {TOUR} references **PRESETS** — phasers live in the preset pool, and recipe lines reference them (a Selection reference × a Values-preset reference), rather than a phaser being baked directly into the part. This is the concrete mechanism behind "recipe-based all the way through": the fully-referenced workflow (see `recipe-lane-end-to-end-verified`), not a build-it-into-the-part shortcut.

**Nuance, 2026-07-19 (Dave, same live session as the group-contract work):** the store-a-Group-before-it-enters-a-recipe discipline (see `tourshow-gesture-groups-on-demand-doctrine`) is a **consequence of choosing this recipe-based mode, not an MA3 technical law.** It remains possible to program groupless/old-style — hard, baked preset-based values written straight into cues, the way shows have been built for decades — and MA3 itself imposes no requirement against it. What that alternative forfeits is recipes and tourability: the whole show would live in the hard-value/cookover layer, with nothing left that recomputes per rig. The store-groups-for-recipes discipline follows from this ruling plus the inheritable-file mission (see `tourshow-mission-and-handoff`), not from any console necessity — the doctrine should be stated that way rather than as a claimed technical requirement.

**Extended 2026-07-21:** paid for again the hard way — a first-pass SONG_G build skipped this ruling entirely (9 baked SET→OUT cues, no recipes, cell/grid spine unused) despite the ruling being on record; see `review-plan-gate-precedes-programming-doctrine` for the named failure mode and the new REVIEW→PLAN gate proposed to prevent recurrence.

## The ruling is now a CLOSED, EXECUTABLE CONTRACT (2026-07-28)

"Recipe-based all the way through" was the mode ruling; it now has a concrete object-by-object
contract — **phaser preset = the temporal figure (stock Shape + Universal Dimmer preset) ·
group = who · MAtricks bound at the SEQUENCE = spatial · one phaser preset per use-site ·
`cLD ` prefix · ours numbered at `21.<century>20`.** Full specification, including what is
copied versus referenced and why the per-use-site duplication is deliberate:
`tourshow-authoring-contract-v01`.
History: none — ruling stated 2026-07-16. Extended 2026-07-17: Dave's follow-on doctrine ruling out building phasers directly into cue parts, reinforcing the preset-reference model. Extended 2026-07-19: added Dave's mode-vs-law nuance — the store-for-recipes discipline is a consequence of this ruling, not an MA3 requirement. Extended 2026-07-21: cross-referenced `review-plan-gate-precedes-programming-doctrine`, the process gate proposed after this ruling was skipped in practice despite being on record. Updated 2026-07-28 [0727-2cLD]: the mode ruling now has a closed executable contract in tourshow-authoring-contract-v01.

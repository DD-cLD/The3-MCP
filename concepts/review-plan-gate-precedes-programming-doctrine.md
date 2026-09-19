---
id: review-plan-gate-precedes-programming-doctrine
title: "A REVIEW→PLAN step must precede programming any song — never bake cue-to-cue; skipping the gate is what let this session tunnel into baked cues despite recipe-based doctrine already being loaded"
role: operational-live
tags: [doctrine, process, tourshow, recipes, v2.4]
when_to_load: "Before starting ANY programming session on a new song — run the review→plan gate first (doctrine + spine inventory + cue-sheet-as-instructions read → phaser/recipe story + per-cue plan → one build-macro) rather than going straight to console/XML authoring"
status: active
source: "findings/INBOX.md [0721-2cLD] block, 2026-07-21, Dave (dictated + ratified in review); wraps/2026-07-21-days-first-pass-recipe-miss.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The lesson, paid for hard:** {TOUR} is recipe-based (see `tourshow-recipe-based-show-style-ruling`) — cues hold recipes that cook live (Group=WHO / preset+phaser=WHAT / grid=WHEN), never baked cue-to-cue values. This session built the whole SONG_G chain end-to-end via the proven macro-import lane, but programmed it WRONG: 9 cues of hard SET→OUT values, nothing recipe-referenced, the cell/grid spine unused, and the cue sheet's gesture tags (Bloom/Propagation/Color pump/Sustain drift/Isolate/Phrase turn) flattened to one static color + one global dim sine instead of being read as phaser/recipe instructions. `recipe-lane-end-to-end-verified` and `v24-phaser-model` were both LOADED this session and still didn't get applied — the tell that doctrine being *known* is not sufficient; it has to be turned into a plan BEFORE console/XML time.

**Failure mode, named:** a single hard blocker (the `ColorAdd`→silent-empty-preset color-syntax trap, see `baked-phaser-preset-xml-schema`) tunneled the session into "just make it import" mode, and the recovery back to doctrine never happened. One blocker early in a build session can hijack the whole session's mode if nothing forces a checkpoint back to the plan.

**The fix — a mandatory REVIEW→PLAN gate before any programming session touches console or XML:**
1. **Load doctrine:** the recipe-based-mode ruling (`tourshow-recipe-based-show-style-ruling`), `phaser-story-doctrine` ("write the phaser story before console time"), `tourshow-gesture-groups-on-demand-doctrine`, `tourshow-functional-vs-flavor-fixture-taxonomy`, `grid-is-a-time-map-doctrine`.
2. **Inventory the spine:** what the rig/group/recipe spine can actually DO for this song, concretely — not just that it exists.
3. **Read the cue sheet's device/gesture tags AS PHASER/RECIPE INSTRUCTIONS**, not flavor text — each tag (Bloom, Propagation, Color pump, Sustain drift, Isolate, Phrase turn, etc.) implies a specific phaser/recipe shape.
4. **Write the phaser/recipe STORY + a per-cue plan** (WHO/WHAT/HOW/level, expressed as recipes, not hard values) — the deliverable of the planning pass.
5. **Only then** does one build-macro author it all onto console. Console time = translation, never invention — extends `phaser-story-doctrine`'s console-is-translation framing from the per-song phaser story up to the whole-session process level.

**Planning heuristic (Dave, dictated, paraphrased):** plan for the **hardest** moment in the song first — the best/easiest moments "shine like diamonds" on their own and don't need the planning budget spent on them.

**Status note:** candidate doctrine — proposed as a standing gate on the strength of this one paid-for failure; not yet tested on a second song's build. Cross-reference `tourshow-programming-ramp-plan` for the separate "what order to build songs in" sequencing plan this gate slots into per-song.

History: none — doctrine named and the failure mode diagnosed 2026-07-21, digesting the SONG_G first-pass build flagged for a recipe-based redo; see `wraps/2026-07-21-days-first-pass-recipe-miss.md`.

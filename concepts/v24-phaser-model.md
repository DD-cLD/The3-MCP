---
id: v24-phaser-model
title: "v2.4 phaser model — phasers ARE recipes with 2+ steps; CLI ranges are spatial not temporal; Shapes pool"
role: programmer
tags: [ma3, v2.4, recipes]
when_to_load: "Before generating any Lua, CLI, or recipe-editor UI steps intended to build a phaser (temporal, multi-step effect) or configure its controls (nShot/Direction/Adaptive) — corrects the MA2-era mental model of phasers as a separate object type and covers the v2.4 STANDARD-vs-PHASER recipe split"
status: active
source: "MEMORY §v2.4 console-UI first contact — v2.4 phaser model, 2026-07-04, onPC 2.4.2.2 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Corrects the MA2-era mental model. Source: `WORKING/cLD_CONSOLE_NOTES_v0.1.md`; corrections approved by Dave 2026-07-04.

- **Phasers = recipes with 2+ steps.** A single-step recipe is a "Standard Recipe." Both are built in the Recipe Editor / Phaser Editor — there is no separate "Phaser" object class distinct from Recipe.
- **`EditRecipe Programmer` is standard-recipe ONLY** — it **cannot build phaser recipes**. See `store-recall-recipe-toggle-rules` for the scoping of the EditRecipe bookend pattern to standard recipes.
- **PSR (Partial Show Read) over a phaser recipe breaks its shape links.**
- **CLI value ranges are SPATIAL, not temporal.** `At 0 Thru 100` (even `Thru 0`) produces a fan across the current selection as a **single step** — you cannot type a temporal phaser into being via CLI ranges. Temporal steps must be added **graphically**: Phaser Editor → A⁺/R⁺ arms add-mode → click the value grid to place the step.
- **`At Shape <n>` is valid syntax; `Shapes` is a new v2.4 pool** (22 predefined) — reusable transition/width/accel/decel blocks. **Storing a shape deactivates programmer values.** See `shapes-pool-facts` for shape-link (angular-bracket) semantics, stock-shape locking, and the speed-override pattern.
- **Phaser workflow:** base value → add step 2 in the editor → MAtricks phase object distributes → adjust Speed/Phase/Width on encoder layers → Store to Preset (the **violet cooking-pot icon** marks a phaser recipe in the pool).

**STANDARD vs PHASER recipe split (official MA webinar, YouTube `W0fSSxlog-A`, notes banked to `PHASER_RECIPE_WEBINAR_v0.1.md`):** v2.4 draws a second, complementary axis alongside the step-count criterion above — **STANDARD recipes reference existing data**; **PHASER recipes build the phaser from scratch inside the recipe** (logic-based). Both framings are banked as-given; not reconciled into one rule.

**Phaser recipe controls (webinar; nShot popup mechanics live-verified 2026-07-16):**
- **nShot** = cycle count, then auto-stop. Calculator popup: range **0..128**, an **NShot Stay** toggle, and **Remove/Unlimited** buttons; a committed value shows in the encoder bar (e.g. `NShot 3.00`).
- **Direction**: fwd / back / **ALTERNATE** (bounce).
- **Adaptive Measure** + **Adaptive Width**: auto-calculate timing/width from the *current selection grid*, as opposed to this project's manual literal phase math — reconcile/test before assuming parity.

**Recipe selection (webinar doctrine):** a recipe can reference a **Group** OR **capture the current programmer selection** directly — no per-variation group objects needed. See `recipe-lane-end-to-end-verified` for the live-verified UI mechanics of this same choice (Selection-cell picker: None / From Value / Take Selection + Group tiles).

**Fully-referenced workflow (MA best practice, webinar):** phaser recipe → store in a **Preset** → embed that preset inside a **STANDARD recipe** used in cues; the cue stack then auto-updates on any upstream change. See `recipe-lane-end-to-end-verified` for a live-verified instance of this exact chain (Group reference + phaser-recipe-preset Values, stored into a cue, cooked by the executor).

**Recipe limits (webinar):** recipes never play back directly — they must **cook to the programmer** (realtime update while editing, confirmed live). **Generators and bitmaps are NOT allowed** in phaser recipe lines yet. Legacy phaser→recipe conversion **mistranslates some phase values** — don't trust an auto-converted legacy phaser's phase without checking it.

History: first-contact correction of the MA2-era model, recorded and Dave-approved 2026-07-04. **2026-07-16:** extended with webinar-sourced (`PHASER_RECIPE_WEBINAR_v0.1.md`) STANDARD-vs-PHASER split, recipe controls (nShot/Direction/Adaptive), selection-reference doctrine, fully-referenced workflow, and recipe limits; shape-link mechanics split out to the new `shapes-pool-facts` concept for atomicity.

---
id: store-recall-recipe-toggle-rules
title: "EditRecipe toggle, /MAtricks store flag, and Store-time label inference"
role: programmer
tags: [ma3]
when_to_load: "Before scripting a Store sequence for a preset/cue, or before toggling EditRecipe Programmer — also see v24-phaser-model for the v2.4-specific phaser exception"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules / Patterns We Use, 2026-04-01 (v2.4 scope added 2026-07-04)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Three related Store/recall rules from the original v2.3 rule set:

- **`EditRecipe Programmer` is a toggle** (on/off) — it must be explicitly turned on before storing and off after. Pattern: "Recipe mode bookend" — `EditRecipe Programmer` ON before store, OFF after.
- **`Store` with the `/MAtricks` flag embeds spatial settings** in the preset/cue.
- **Label is inferred on Store** — no `Label` keyword needed; just wrap the name in quotes and the console infers it's the label.

**v2.4 scope added (2026-07-04):** the EditRecipe bookend pattern above applies to **STANDARD recipes only**. In v2.4, `EditRecipe Programmer` **cannot build phaser recipes** (2+ step recipes) — see `v24-phaser-model` for the full phaser-vs-standard-recipe distinction and why PSR additionally breaks phaser recipe shape links.

**Live-verified 2026-07-15 (first full recipe build, 2.4.2.2):** the EditRecipe bookend pattern was exercised end-to-end for real — `EditRecipe Programmer` ON, `Store Sequence 101 Cue 1 Part 1`/`Part 2` with Group + universal-preset references, `EditRecipe Programmer` OFF — and it cooked correctly to DMX on `Go+`. Notably, firing **`ClearAll` INSIDE the recipe-edit mode did NOT break the bookend** — the toggle-off afterward stayed clean and the stored recipe was unaffected. See `recipe-lane-end-to-end-verified` for the full worked build (Show Creator menu, universal preset creation, DMX-cook verification).

History: the "Recipe mode bookend" pattern was scoped 2026-07-04 to standard recipes only, after discovering in the v2.4 UI first-contact session that EditRecipe cannot construct multi-step phaser recipes at all. Live-verified end-to-end 2026-07-15 on a real Sequence/Cue/Part build, including confirming ClearAll-inside-mode survives without breaking the bookend.

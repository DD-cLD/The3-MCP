---
id: recipe-step-level-cli-write-path
title: "Step-level recipe writes: Set ... Part 0.1.\"PhaserRecipeSteps\".<step>.<valuesource> Property \"PropName\" value — after \"PhaserRecipeSteps\" the path is always .Step.ValueSource"
role: programmer
tags: [ma3, cli, recipes, v2.4, xml-schema]
when_to_load: "Before writing a CLI Set command that targets an individual step/value-source inside a recipe (below the whole-recipe-line level) — the address path segment order below PhaserRecipeSteps"
status: active
source: "findings/INBOX.md, 2026-07-17, forum 69919 (robinhood) [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Worked example:** `Set Sequence <x> Cue <y> Part 0.1."PhaserRecipeSteps".1.1 Property "ValueAbsolute" 100` writes step 1, value-source 1 of the recipe on that part.

**Path rule:** once the address descends past the literal segment `"PhaserRecipeSteps"`, the remaining path is **always `.Step.ValueSource`** — a step index followed by a value-source index, both dot-separated integers (robinhood, forum 69919).

**Structural mirror:** this CLI path shape mirrors the XML nesting decoded in `recipe-xml-schema` — `PhaserRecipe → PhaserRecipeSteps → PhaserRecipeStep → PhaserRecipeValueSource`. The CLI address is effectively walking the same tree: recipe-line → `PhaserRecipeSteps` → step → value-source.

Cross-reference: `recipe-line-cli-addressing-and-list-readback` for the whole-recipe-line address this nests under (`Part <p>.<r>`); `recipe-line-pool-binding-via-assign` for the `Assign Preset` form that targets this same step/value-source address for pool-object binds instead of a literal `Set ... Property` value.

History: none — first captured, 2026-07-17, forum sourcing not yet independently live-verified against the console.

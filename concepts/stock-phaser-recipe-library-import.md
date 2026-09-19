---
id: stock-phaser-recipe-library-import
title: "Importing MA's stock phaser-recipe template library — Show Creator route + forum-flagged pool-in-sequence caveat"
role: programmer
tags: [ma3, recipes, v2.4, import]
when_to_load: "Before importing MA's stock phaser-recipe presets into a show, or before referencing an imported recipe preset directly from inside a pooled sequence"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave + community-confirmed forum thread 69977)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Import route (Dave):** Setup → Show Creator → Import presets → the **"All 2"** pool imports MA's phaser-recipe preset library. These land as templates/base recipes — inspect via the recipe editor or via preset XML export.

**Source file (community-confirmed):** Show Creator → presets → **`predefined_phaser_recipes`** is MA's stock phaser-recipe preset library file.

**Known caveat [forum 69977]:** pool phaser-recipe presets referenced directly from inside sequences have been reported to misbehave. MA's own best-practice workaround is preset → standard recipe in the cue (the fully-referenced workflow — see `v24-phaser-model`). Test before relying on a direct pool reference inside a sequence.

**Possible connection (unconfirmed, flagged not asserted):** this forum-reported misbehavior may be the same underlying phenomenon later diagnosed live as `stock-recipe-presets-empty-as-templates` — bare pool/preset calls on a fresh stock recipe template are silent no-ops, and the fix (a recipe line with Selection+Values) matches MA's preset→standard-recipe workaround exactly. Not confirmed as the same root cause; noted as a likely match.

History: created 2026-07-16, merging Dave's practical import-route description with the community/forum-sourced exact filename and caveat — two facets of one import fact.

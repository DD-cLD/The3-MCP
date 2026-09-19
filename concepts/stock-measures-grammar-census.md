---
id: stock-measures-grammar-census
title: "MA's stock phaser-recipe library measures grammar — per-category Measure/Direction/Adaptive census"
role: programmer
tags: [ma3, recipes, measures, v2.4]
when_to_load: "Before designing a new recipe in a given effect category (wipe, flyout, oneshot, alternate, chase, movement) — MA's own stock library's Measure/Direction/Adaptive choices per category, as a design-pattern reference"
status: active
source: "findings/INBOX.md, 2026-07-16, read of predefined_phaser_recipes.xml against Dave's measure framing"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Design-language census read from MA's own stock recipe library (matches Dave's measure framing captured elsewhere as measure doctrine):

| Category | Grammar |
|---|---|
| Wipes | `Measure=1` — live in one beat |
| Flyout specials | `Measure=4` + `Speed` |
| OneShots | `NShot=1` + `Measure=1` |
| Alternates | `Measure=1` + `Direction=Alternate` + `Phase 0→180` (HALF spread — bounce doubles the traversal) |
| Chase / Snap | `AdaptiveMeasure` (chases add `AdaptiveWidth` too) — grid-synced |
| Movement | `Has=Speed` + **RELATIVE** pan/tilt (rides the base position — portable across positions) |

**Attribute census across the library:** Dim 62, Tilt 34, Pan 34, Zoom 2; 70 relative-value cells total.

Cross-reference: `measure-layer-math` for the Measure definition/formula this table applies; `wipe-in-thru-range-anatomy` for the worked wipe example behind the "Wipes: Measure=1" row; `v24-phaser-model` for the nShot/Direction/Adaptive control definitions this table's columns use.

History: created 2026-07-16 from the same XML read that produced `recipe-xml-schema`.

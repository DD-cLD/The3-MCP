---
id: wipe-in-thru-range-anatomy
title: "Wipe-in anatomy worked example — Thru ranges on a layer value distribute width spatially across the grid inside one recipe cell"
role: programmer
tags: [ma3, recipes, measures, worked-example, v2.4]
when_to_load: "Before building or debugging a wipe-style phaser recipe, or when a step's width uses a Thru range and you need to know what that range actually does"
status: active
source: "findings/INBOX.md, 2026-07-16, read of predefined_phaser_recipes.xml WipeIn preset"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Worked example from MA's stock `WipeIn` recipe preset: **4 steps, `Measure=1`**. Widths per step:

1. `25%`
2. `"0% Thru 100%"`
3. `25%`
4. `"100% Thru 0%"`

**The mechanism:** a `Thru` range on a layer value distributes that width **spatially across the grid** — this is a spatial Thru operating *inside a single recipe cell/step*, not a temporal range. Steps 2 and 4 are **complementary** Thru ranges (`0→100%` and `100→0%`), so every fixture's total width across the 4 steps sums to **150%** — a uniform loop length per fixture — but the position of the *lit window* travels across the grid as the steps play. That traveling lit edge, composed purely from step widths, is the wipe. The whole figure is pinned inside **one beat** (`Measure=1`).

Cross-reference: `stock-measures-grammar-census` (the "Wipes: Measure=1" row this example demonstrates); `measure-layer-math` (the width/Measure math this figure is built from — Σwidths here is 150, not 100, precisely because of the complementary Thru pair).

History: created 2026-07-16 as a standalone worked example, since it demonstrates a distinct mechanism (spatial Thru inside a recipe step) not covered by the Measure formula alone.

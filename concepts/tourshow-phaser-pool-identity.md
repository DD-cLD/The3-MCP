---
id: tourshow-phaser-pool-identity
title: "Pool 21 'Phaser' = predefined_phaser.xml (107 baked phasers); Pool 22 'All 2' = predefined_phaser_recipes.xml (46 recipe templates) — two parallel stock libraries"
role: programmer
tags: [ma3, inventory, pools, v2.4, tourshow, stock-library]
when_to_load: "Before referencing a stock phaser/recipe preset by pool number, or reasoning about which stock library a preset came from, in the {TOUR} build file"
status: active
source: "findings/INBOX.md, 2026-07-16 (console census + Dave-confirmed at console; 3 near-identical/escalating-confidence captures merged into one concept per librarian duplicate-merge instruction)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Two parallel stock libraries, confirmed live in this show file (cLD_SANDBOX):

- **Pool 21 "Phaser"** = `predefined_phaser.xml` — the stock BAKED-phaser library, 107 presets, imported the prior session (2026-07-15). Includes the Release color family (see `release-family-ships-stock`) and 61 "mixcolor" 2-step color phasers (multi-step badge; echo confirms "has multiple steps").
- **Pool 22 "All 2"** = `predefined_phaser_recipes.xml` — this session's (2026-07-16) import, the stock RECIPE-template library, 46 content presets across 7 sections (see `tourshow-stock-recipe-library-inventory` for the full census).

**Pool numbering confirmed two ways:** (1) Dave confirmed directly at the console — "pool 21=phaser pool / pool 22=All 2" (windows at the time: D2=Recipe Editor, D1=pools 21+22); (2) corroborated independently by the Values-cell preset-picker tabs in the Recipe Editor, which enumerate pool numbers directly (Phaser=21, All 2=22, All 3=23…) — this closes the [VERIFY] the first capture of this finding carried on numbering.

Note these are THIS show file's current pool-number assignments (Show Creator imports land in the next available slot) — the underlying stock XML content (`predefined_phaser.xml` / `predefined_phaser_recipes.xml`) is universal MA3 stock, but the pool numbers 21/22 specifically describe cLD_SANDBOX, not a console-wide constant.

Naming provenance: pool 21's generic default label ("All 1") was renamed to "Phaser" in v2.4 — explaining why pool 21 reads "Phaser" while pool 22 still carries its generic default label ("All 2"), rather than a matching "Recipe"-style name. (Renaming pool 22 to something like "Recipe Phasers" is a live candidate — see `pool-labeling-doctrine-inherited-risk`.)

**Relation:** FX White/Red/Green presets appear in BOTH pools at slots 110-112 despite `predefined_phaser.xml` itself carrying no FX presets — see `tourshow-fx-preset-dependency-anomaly`.

History: none — pool identity established and confirmed same session, 2026-07-16.

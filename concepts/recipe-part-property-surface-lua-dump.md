---
id: recipe-part-property-surface-lua-dump
title: "Recipe-part (StandardRecipe) full property surface — ~149 props via handle:PropertyName(), six bind slots, part carries its own full MAtricks prop set"
role: programmer
tags: [ma3, lua, recipes, matricks, v2.4]
when_to_load: "Before writing Lua/MCP calls that read or Set properties directly on a recipe cue-part object — the full live-dumped property inventory and bind-slot map"
status: active
source: "findings/INBOX.md line 38, 2026-07-17 [0717-2cLD], console live 2.4.2.2, handle:PropertyName() dump"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Live property dump via `handle:PropertyName()` on a StandardRecipe cue-part surfaced **~149 properties**. Six bind slots identified: **SELECTION / VALUES / PRESET / MATRICKS / FILTER / GENERATOR**.

The part carries its **own full MAtricks property set** as first-class part properties (**XWINGS, PHASEFROMX/TOX, XBLOCK**, etc.) — meaning the store-time `/MAtricks` embed (see `live-selection-matricks-cli-set-syntax`'s "two carriers" finding) likely lives as directly Set-addressable part properties, not just an embed baked at Store time. **Untested** — not yet confirmed by an actual `Set` call against one of these MAtricks part-properties.

**Relation:** this is the raw Lua-object-model property inventory underlying `assign-cli-recipe-line-grammar`'s routing table (Group→Selection, Preset→Values, MAtricks→MAtricks slot). It surfaces a potential fourth recipe-MAtricks carrier alongside the CLI Selection-object form, the store-time `/MAtricks` embed, and the recipe-line MAtricks editor already mapped in `live-selection-matricks-cli-set-syntax`.

History: none — first dumped live 2026-07-17.

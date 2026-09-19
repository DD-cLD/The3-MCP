---
id: measure-not-a-safe-lua-property-part-or-preset
title: "Measure lives at neither the recipe-part NOR the Preset object surface — not a safe-Lua-readable property anywhere; step data (where it actually lives) stays GPDF-gated"
role: programmer
tags: [ma3, lua, measures, phasers, presets, v2.4, danger]
when_to_load: "Before assuming Measure can be read or set as a plain object property via Lua on either a recipe cue-part or a Preset — it can't at either level; also before reaching for GetPresetDataFast as a workaround to get at step data"
status: active
source: "findings/INBOX.md lines 43, 45 — 2026-07-17 [0717-2cLD] (line 43 Dave, dictated, paraphrased); console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Not a recipe-part property (Dave, dictated, paraphrased):** Measure is a PHASER/PRESET property, not a sequence-recipe-line property. The full ~149-prop recipe-part dump (`recipe-part-property-surface-lua-dump`) confirms it — no MEASURE among them. Measure edits happen in the preset-edit lane, not on the cue part. **Consequence:** the bridge battery item "Measure 2 on the part" was mis-scoped and is retired.

**Not a Preset object property either:** preset-lane probes (Copy Preset 21.1→21.121, Label, both via MCP, verified — see `preset-copy-label-mcp-and-century-scratch-slots`) also found Measure is **NOT** a property on the Preset object surface — only transform props (Speed, Phase From/To, etc.) are exposed there. The Preset object shows **0 children**, so step data (where Measure actually lives — see `baked-phaser-preset-xml-schema` for its file-side location and encoding) is **unreachable via safe Lua**. The `GetPresetDataFast()` ban (`gpdf-console-killer`) stands as the only door to that data, and it remains closed.

**Relation:** `phaser-layer-cli-grammar-measure-keyword` is the one lane that DOES reach Measure — the bare `Measure 2` CLI keyword — but only once a phaser is loaded into the programmer via `Edit Preset`, a different mechanism entirely from object-property access.

History: none — both findings landed live 2026-07-17, same session, folded into one concept since together they establish "Measure is unreachable via safe-Lua object properties at any level."

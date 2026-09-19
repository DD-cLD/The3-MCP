---
id: phaser-layer-cli-grammar-measure-keyword
title: "Bare `Measure 2` at the CLI sets the Measure layer once a phaser is loaded into the programmer via Edit Preset — a first-class layer keyword like the encoder layers"
role: programmer
tags: [ma3, cli, measures, phasers, v2.4]
when_to_load: "Before typing or generating a bare layer-keyword CLI command (Measure, or other phaser layer keywords) — only works once a phaser is loaded into the programmer via Edit Preset; also before assuming a baked phaser pulled via Edit Preset carries recipe parts (it doesn't)"
status: active
source: "findings/INBOX.md line 47, 2026-07-17 [0717-2cLD], console live 2.4.2.2, visually confirmed on encoders (Dave)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

With a phaser loaded into the programmer (via `Edit Preset x` — see `edit-session-mechanics-and-contamination-risk` for what that pull does and its contamination risk), the bare CLI line **`Measure 2`** sets the Measure layer directly — Dave visually confirmed the change reflected on the encoders. **Measure is a first-class layer keyword**, the same class as the encoder layers.

**Baked phasers pulled via `Edit Preset` show as HARD VALUES** — no recipe parts appear, and `EditRecipe` stays OFF. Recipe mode is **recipe-preset-only**; it does not apply when editing a baked/hard-value phaser preset.

**Relation:** this is the CLI-keyword access path to Measure, distinct from — and currently the only working live path around — the object-property inaccessibility described in `measure-not-a-safe-lua-property-part-or-preset`. See `measure-layer-math` for what the Measure value means once set, and `phasers-via-measures-curriculum` for the broader learning context this was captured in.

History: none — confirmed live 2026-07-17.

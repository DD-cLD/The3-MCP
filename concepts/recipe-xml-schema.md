---
id: recipe-xml-schema
title: "Phaser-recipe preset XML schema — PhaserRecipe/PhaserRecipeSteps/PhaserRecipeValueSource, Has= layer knock-in, embedded dependencies"
role: programmer
tags: [ma3, recipes, xml-schema, v2.4]
when_to_load: "Before reading, generating, or hand-authoring phaser-recipe preset XML (e.g. for a file-side authoring/import lane) — the decoded element/attribute shape"
status: active
source: "findings/INBOX.md, 2026-07-16, read of gma3_2.4.2/shared/resource/lib_presets/predefined_phaser_recipes.xml (1135 lines) against the live console"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Element nesting:** a recipe preset is `<Preset><PhaserRecipe attrs><PhaserRecipeSteps><PhaserRecipeStep><PhaserRecipeValueSource .../>` — i.e. `Preset` wraps one `PhaserRecipe`, which wraps `PhaserRecipeSteps`, each containing one or more `PhaserRecipeValueSource` elements.

**`Has="Measure;AdaptiveMeasure;Speed;..."`** — this attribute serializes **which phaser layers are knocked in** (layer activation), as a semicolon-separated list.

**`Individual="Measure;"`** also observed on at least one element — semantics **[VERIFY]**, not yet confirmed against live behavior.

**Embedded dependencies:** shapes and referenced presets travel with the recipe preset via `<DependencyExport><Dependency RelAddrNum="14.14.1.16.x" ...>` — the `RelAddrNum` branch `14.14.1.16.x` addresses the **Shapes pool** (see `shapes-pool-facts`).

**Section headers:** the XML's section-divider entries are bare `<Preset>` elements with **no `PhaserRecipe` child** — a structural tell for skipping non-recipe entries when parsing the file.

Cross-reference: `shapes-pool-facts` for what a `Shape` element itself holds (`Trans`/`Width`/`Accel`/`Decel` + `Attributes`/`Speed`/`Measure`/`Adaptives`, `Lock="UL"` on stock shapes); `measure-layer-math` for what the Measure layer this schema knocks in actually means at runtime; `stock-recipe-presets-empty-as-templates` for the behavioral consequence of a recipe preset with no stored Selection.

**Recipe-line props are ATTRS directly on `<PhaserRecipe>`** (live-confirmed 2026-07-17, file-side authoring session): `Shape=` carries the **full pool path** (e.g. `"ShowData.DataPools.Default.Shapes.Sine"`); `PhaseFromX`/`PhaseToX` are stored as **DISPLAY STRINGS with a degree sign** (e.g. `"180°"`), not raw numbers; `Enabled`/`PlaybackDirection`/`SelectionFromValue` are also plain attrs on the same element.

**Steps reference the shape internally** via a path string, e.g. `"PhaserRecipeSteps.Step 1.Value Source 1"`; the shape itself travels along via `DependencyExport` (see the `RelAddrNum` branch above).

**Two dialects, one `<Preset>` schema — important distinction:** a **baked** phaser preset (values hard-committed, no live recipe parts) encodes `Speed`/`Measure`/`Phase` as **fixed-point integers** (see `phaser-preset-xml-measure-speed-fixed-point-encoding`), while a **recipe** preset (this schema) encodes its phase endpoints as **display strings with degree signs**. Same outer `<Preset>` container, divergent inner value encoding depending on whether the preset is baked or recipe-based — don't assume one encoding scheme reading the other dialect's file.

Cross-reference: `export-sequence-xml-schema` for how a recipe cue-part (a different element, `<StandardRecipe>`, not this concept's `<PhaserRecipe>` preset-template) serializes its own bind-slot refs inside a live Sequence export — same dotted full-path ref convention, confirmed live 2026-07-17.

History: created 2026-07-16 from the file-side XML read that decoded the recipe schema in one pass. Extended 2026-07-17: added the attribute-vs-element clarification (recipe-line props are `<PhaserRecipe>` attrs), the display-string phase-value format, the step-to-shape reference path format, and the baked-vs-recipe two-dialect distinction — all from a live file-side authoring proof (`xml-file-side-authoring-import-lane-proven`). Same day: cross-referenced `export-sequence-xml-schema` (the sibling StandardRecipe cue-part dialect cracked via a live Sequence export).

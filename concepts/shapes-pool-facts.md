---
id: shapes-pool-facts
title: "Shapes pool (v2.4) — angular-bracket link semantics, locked stock shapes, and the shape-speed-override pattern"
role: programmer
tags: [ma3, recipes, shapes, v2.4]
when_to_load: "Before editing any phaser-recipe value shown in angle brackets (shape-derived), before assuming a stock Shape is editable, or before overriding a shape-linked property (e.g. Speed) on a recipe line"
status: active
source: "findings/INBOX.md, 2026-07-16 (official MA webinar notes + Dave, console live 2.4.2.2, + predefined_phaser_recipes.xml read)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Angular brackets = external-object link (webinar):** a recipe-line value shown in angle brackets (e.g. `<600 BPM>`) is derived from an external **Shape** object, not typed locally. Overwriting it breaks the link and the brackets disappear — the value becomes a local literal.

**Shapes carry Speed, and other layers (Dave; corroborated by the XML schema):** a Shape can bake **Speed** — and Measure/Adaptives — into the phaser it feeds. A shape is functionally the most basic base phaser; the old-school pattern of building basic-shape presets up into full phaser presets is what v2.4 formalized as the Shapes pool. Shapes are the programming shortcut inside phaser recipes. Corroborated by the recipe XML schema (see `recipe-xml-schema`): a `Shape` element holds `Trans` / `Width` / `Accel` / `Decel` plus `Attributes` / `Speed` / `Measure` / `Adaptives`.

**Stock shapes are locked:** the 22 preinstalled shapes are **NOT editable** — copy first, edit the copy. Matches the `Lock="UL"` attribute observed on `Shape` elements in the stock XML.

**Shape speed-override pattern (live-verified):** a shape link brings Speed into the recipe line bracketed (e.g. `<600 BPM>` from a Strobe shape). Typing directly into the Speed encoder's calculator breaks **only that property's** link — other shape-linked properties (curve, width, etc.) stay linked. This is the core move for putting a shape-driven effect at song tempo without losing the rest of the shape's profile. Calculator popups for shape-linked properties carry **Take from Shape / None / Invert** side buttons — a relink lane exists to restore the link later.

Cross-reference: `v24-phaser-model` for the Shapes-pool intro (22 predefined, `At Shape <n>` syntax); `recipe-xml-schema` for the full Shape XML element; `speed-distribution-bpm-hz-decimal-trap` for the separate BPM/Hz decimal-conversion gotcha when typing Speed values directly (a different mechanism from this link-breaking behavior).

History: created 2026-07-16, merging four related findings (angular-bracket semantics, shapes-carry-speed, stock-shapes-locked, shape-speed-override pattern) into one atomic Shapes-pool concept.

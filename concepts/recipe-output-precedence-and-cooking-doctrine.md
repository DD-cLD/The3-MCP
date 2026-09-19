---
id: recipe-output-precedence-and-cooking-doctrine
title: "Recipe output precedence (official manual flowchart): a hard stored value always beats a recipe; COOKING = materializing a recipe into that hard cookover layer"
role: programmer
tags: [ma3, doctrine, recipes, v2.4]
when_to_load: "Before reasoning about which value a sequence actually outputs when both a recipe and a hard/cooked value exist for the same attribute — or before deciding whether a generated Sequence export should carry cooked values"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD] — official grandMA3 2.4 manual 'Output decision flowchart' (Recipes page, Dave-directed) + Export Sequence 102 capture"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Output decision flowchart (official 2.4 manual, Recipes page):**

1. No stored value for the attribute → the sequence sends NOTHING to it.
2. A stored value exists — is it a link to a preset?
   - **YES (preset-link):** is the value stored directly in the preset? Yes → **PRESET value** wins. No → the **RECIPE in the preset** wins.
   - **NO (local, not a preset-link):** is the value stored in the cue part? Yes → **CUE PART value** wins. No → the **RECIPE in the cue part** wins.

**Governing rule: a hard stored value ALWAYS beats a recipe**, resolved at whichever level holds it (preset-link level or cue-part level). The recipe is the fallback — it only outputs where no harder value overrides it. The manual's Recipes page has deeper per-layer detail beyond this flowchart, not yet dug into further.

**COOKING** = materializing a recipe into hard per-fixture values that ride a "cookover" layer and then WIN over the recipe per the flowchart above (Dave's framing). Confirmed directly by the Seq 102 export: a `Cooked="AbsPreset,RelPreset,...,Phase,GridPos,Measure,NShot"` attribute plus a full `<PresetData>` cooked block rode alongside the live `<StandardRecipe>` in the same Part — see `export-sequence-xml-schema`. The export carried the recipe AND the cooked snapshot together.

**Open item — which carrier actually cooks:** Seq 102 Part 0.1 has its own part-level `PhaseFromX="0°"`/`PhaseToX="270°"` override coexisting with a bound MAtricks `"Phase X 0-180"` (`PhaseToX="180°"`). Both attrs are present in the export without overwriting each other. The export's cooked per-fixture phase spanned to 270° (the part-level value) — SUGGESTIVE that the part-level phase drove the cook over the pool's 180°, but this is NOT pinned. Needs the manual's deeper recipe-layer detail plus a clean visual test to confirm. Raw values: see `export-sequence-xml-schema`'s worked-example notes.

**Relation:** `clean-authoring-and-persistence-doctrine` reframes this flowchart as a design-time GUARDRAIL (deliberate authoring prevents ambiguous overlapping layers from ever existing) rather than a runtime resolution problem. `export-sequence-xml-schema`'s design implication — that cLD MAker's Sequence export must default to recipe-only — is grounded directly in this precedence rule: a cooked value would freeze/pin a stale look on import.

History: created 2026-07-17 from the official manual flowchart (Dave-directed) plus the same-session Export Sequence 102 capture that supplied live confirmation of the cooked-vs-recipe carrier behavior.

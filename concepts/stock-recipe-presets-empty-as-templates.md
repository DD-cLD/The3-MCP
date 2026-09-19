---
id: stock-recipe-presets-empty-as-templates
title: "⛔ Stock phaser-recipe presets are EMPTY as presets — bare call or pool tap is a silent no-op; they only cook through a recipe line"
role: programmer
tags: [ma3, recipes, v2.4, gotcha, cli]
when_to_load: "Before calling a stock (or any freshly-imported) phaser-recipe preset directly via CLI or a pool tap — it will silently do nothing. Also load when diagnosing why a preset call produced no output with no error on the docked command line."
status: active
source: "findings/INBOX.md, 2026-07-16, console live 2.4.2.2, diagnosed against the imported All 2 pool"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔-class lesson.** Stock phaser-recipe presets are **empty as presets**. A bare call — CLI `Preset "All 2"."Chase"` with a selection, or a pool tap — produces a **silent no-op**, or an echoed **"Preset 'Chase' is empty"**. These presets are **selection-less recipe TEMPLATES**: they cook only through the recipe lane — a recipe line with `Selection` = a Group/capture and `Values` = the preset, placed in a cue part or the programmer's Part Zero — per MA's fully-referenced workflow (see `v24-phaser-model`). A bare preset call tries to apply stored VALUES that simply don't exist on a fresh-imported recipe preset.

**Diagnostic lane that found it:** the target selection was verified visually first (Group 121's yellow outlines showing correctly on the SPOT PLOT layout, Display 2) — so selection wasn't the problem. A **pool TAP** then produced the definitive echo (**"Preset is empty"**) where the equivalent **CLI call had stayed silent**. Lesson: a pool tap echoes errors that a CLI call swallows — when a CLI preset call produces no visible effect and no error, cross-check it with a pool tap before assuming the selection or preset itself is at fault.

**The fix:** see `recipe-lane-end-to-end-verified` for the live-verified recipe-line lane that cooks these templates correctly.

History: created 2026-07-16 — first documented as a live diagnostic during the second recipe build session.

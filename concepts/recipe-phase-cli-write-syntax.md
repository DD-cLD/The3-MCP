---
id: recipe-phase-cli-write-syntax
title: "Recipe-line Phase properties via CLI: target PhaseFromX/PhaseToX individually; \"Swap Phase\" is a working per-property special value; a \"*-1\" multiplier value syntax works; a \"0 t 360\" range value landed as 0..180, unexplained"
role: programmer
tags: [ma3, cli, recipes, v2.4, phase-math, verify]
when_to_load: "Before generating a CLI Set command that writes a recipe line's Phase properties — PhaseFromX/PhaseToX are set individually, Swap Phase and *-1 multiplier syntax both work; do not trust a Thru-style range value on a single Phase property until the 0 t 360 → 0..180 anomaly is explained"
status: verify
source: "findings/INBOX.md, 2026-07-17 — Kanarek and Stevegiovanazzi via forum [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Individual targeting:** `PhaseFromX` and `PhaseToX` are set as separate properties, not a combined pair — target each individually via the standard `Set ... Property "PhaseFromX"/"PhaseToX" <value>` form (see `recipe-line-set-property-syntax-and-value-casing` for the Property-keyword requirement).

**Special value confirmed working:** `"Swap Phase"` works as a per-property special value (Kanarek) — swaps the phase on whichever property it's applied to.

**Multiplier syntax confirmed working:** a `"*-1"` value (multiply-by-negative-one) works as a value expression on a Phase property (Stevegiovanazzi).

**[VERIFY] unexplained range behavior:** setting `"PhaseX" "0 t 360"` (a `Thru`-style range value) landed as **0..180**, not the literal 0-360 requested — cause unexplained. Do not assume a `Thru`-range value on a Phase property behaves as a literal pass-through; it may be getting halved, normalized, or otherwise reinterpreted. Needs a live retest with a known fixture count to characterize.

**Related open question:** `recipe-phase-endpoint-convention` separately flags that stock recipes ship a literal `PhaseFromX=0`/`PhaseToX=360` full-circle pair, in tension with this project's `360 − 360/N` MAtricks formula (`phase-math-formulas`) — that concept's collision question and this concept's `0 t 360 → 0..180` anomaly may or may not share a root cause; both are unresolved and should be tested together if a live phase-recipe session is available.

Clears with: a live test setting `PhaseToX` via a `"0 t 360"`-style range expression against a recipe with a known fixture count, checking the resulting per-fixture phase values.

History: none — first captured, 2026-07-17, forum-sourced with one live-observed anomaly; kept at `verify` for the unexplained range-value behavior.

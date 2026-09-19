---
id: recipe-line-pool-binding-via-assign
title: "Pool objects bind to a recipe line via ASSIGN, not Set — Set with a pool number silently doesn't bind; per-object-type Assign forms for MAtricks, Preset, Shape, and Group"
role: programmer
tags: [ma3, cli, recipes, v2.4, matricks]
when_to_load: "Before generating a CLI command that binds a pool object (MAtricks/Preset/Shape/Group) to a recipe line — Set silently fails to bind pool numbers; Assign is the correct verb, with a different address grammar per object type"
status: superseded
source: "findings/INBOX.md, 2026-07-17 — forum 69993 (Kanarek), forum 69919 (robinhood, chrislose) [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: assign-cli-recipe-line-grammar
---

**Core rule:** binding a pool object to a recipe line uses **`Assign`**, not `Set`. `Set` with a pool number **silently doesn't bind** — no error, no effect (Kanarek, forum 69993) — consistent with the general silent-failure doctrine in `set-command-unknown-property-fails-silently`.

**Per-object-type Assign forms observed:**
- **MAtricks:** `Assign MAtricks 6 At Sequence c Cue 1 Thru Part *.*` — a `Thru`-ranged wildcard part address binds across every recipe line in the cue.
- **Preset:** `Assign Preset a.b At Sequence c Cue d Part 0.1."PhaserRecipeSteps".<step>.<valuesource>` — targets a specific step/value-source inside the recipe (see `recipe-step-level-cli-write-path` for the step-address grammar this nests into).
- **Shape:** `Assign Shape n At ... Part 0.1` — a trailing `Property "Shape"` suffix is **optional** on this form (chrislose).
- **Group:** `Assign Group X At Programmer <part>.<recipe>` — binds via the Programmer address rather than a stored Sequence/Cue address (Kanarek).

**Relationship to the recipe MAtricks editor:** this Assign lane is a distinct CLI write path from the recipe-line MAtricks editor UI documented in `live-selection-matricks-cli-set-syntax` — that concept established that `Set Selection MAtricks` does not reach a recipe's own MAtricks and that the UI editor was the only known write surface at the time. `Assign MAtricks n At Sequence ... Part *.*` is a CLI alternative reaching the same target; the two have not been cross-verified against each other for identical results.

History: none — first captured, 2026-07-17, from forum sourcing (not yet independently live-verified against these specific fixture/console pairings — see the companion INBOX line 34 outside this shard's partition for the live end-to-end confirmation of the Group/Assign form).

History: superseded 2026-07-17 (run 14 merge) — content folded into `assign-cli-recipe-line-grammar` (live-verified twin; parallel-shard duplicate, lines 24 vs 34/35/39).

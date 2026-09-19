---
id: phaser-preset-update-after-edit-rewrite-behavior
title: "Update after Edit rewrites a baked-phaser preset's XML: explicit Speed/SpeedMaster attrs dropped, GridPos/GridPosMatr added per fixture; universal template row doesn't take the edit"
role: programmer
tags: [ma3, recipes, xml-schema, v2.4, verify]
when_to_load: "Before diffing or hand-authoring a baked-phaser preset that has been through an Edit→Update round-trip on console — the re-export is not a minimal diff, several structural changes ride along"
status: verify
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD], export-diff (Edit→Measure 2→Update→re-export)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Observed on an Edit→Update round-trip (Edit Preset → set Measure 2 → Update → re-export, diffed against pre-edit export):**

- **Explicit `Speed`/`SpeedMaster` attributes get DROPPED** from entries where they were previously present — consistent with the project's zero-attribute-omission convention (defaults aren't written explicitly).
- **`GridPos`/`GridPosMatr` attributes get ADDED** per fixture entry that didn't have them before.
- **The universal template row (`IDType 2 ID 1`) did NOT take the Measure edit** — only the per-fixture **selective** entries picked up the new Measure value. The template/universal row is a separate write target from the per-fixture rows.

**Open corner [VERIFY]:** the full "layer-carry" semantics of Edit/Update — i.e., which layers/attributes an Edit→Update round-trip is guaranteed to preserve vs. silently rewrite/drop — is not yet mapped. Flagged to verify if it ever bites (e.g. if a future Edit→Update round-trip is expected to be a clean single-attribute diff and isn't).

Cross-reference: `phaser-preset-xml-measure-speed-fixed-point-encoding` for the encoding math this round-trip was used to ground-truth; `recipe-preset-edit-requires-update` for the related silent-revert-without-Update behavior on recipe presets specifically (this concept is about baked presets).

History: created 2026-07-17 from the same export-diff session that pinned the Measure/Speed encoding; status `verify` — the layer-carry question is explicitly open.

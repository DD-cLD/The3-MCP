---
name: ma3-phaser-gate
description: Authoring gate for grandMA3 phaser and preset XML plus any pool-stored phase math. Use BEFORE authoring or verifying baked phaser presets, color presets, recipe presets, or storing MAtricks phase values. Triggers on PhaserRecipe, phaser steps, Measure, Speed encoding, ColorRGB, phase spread, MAtricks phase.
---

> **Historical workflow reference.** This file records the original show's
> session or authoring procedure. Start with
> [the portable agent quickstart](../docs/AGENT_QUICKSTART.md) and
> `skills/ma3-assistant/SKILL.md` for a new agent or show. Keep your own identity;
> `cLD`/Claude and Dave describe historical roles, not required products or users.
> The quickstart translates the old `WORKING/`, `agents/`, and `generated/`
> paths. Private memory/state files, show packets, bindings, and golden exports
> named below are not supplied: use the operator's actual inputs and report
> missing prerequisites. Show-specific slot numbers and fixture populations are
> examples, not addresses to copy. The console clearance, checkpoint, and
> read-back gates still apply; this reference does not authorize console contact.

# MA3 Phaser / Preset Authoring Gate

Structural gate (repo law: `WORKING/AGENT_LANES_SPEC_v0.1.md`): no phaser/preset XML and no pool-stored phase values until the dialect and the math are armed. Paths relative to the MA_PROGRAMMING repo's `WORKING/` folder.

## Preferred lane — dispatch the smith

Dispatch PHASER SMITH per `agents/PHASER_SMITH_v0.1.md` (stage manifest + goldens + design spec; smith shows its math in the report).

## Inline lane — small edits only

Read FIRST, in order:

0. **`agents/cards/CARD_AUTHORING.md`** — the whole silent-failure kit for song content, one page; its PHASE MATH block carries the literal formulas verbatim. This is the foreground; the concepts below are the depth. In a main session the spine (`concepts/SPINE.md`) is already loaded, so the card alone re-arms you. In a smith dispatch, stage the card AND the manifest.
1. `concepts/baked-phaser-preset-xml-schema.md`
2. `concepts/phaser-preset-xml-measure-speed-fixed-point-encoding.md`
3. `concepts/recipe-xml-schema.md`
4. `concepts/v24-phaser-model.md`
5. `concepts/measure-layer-math.md`
6. `concepts/phase-math-formulas.md` + `concepts/mtricks-phase-vs-encoder-phase.md`
7. `concepts/universal-presets-emitter-aware.md`
8. `concepts/xml-file-side-authoring-import-lane-proven.md`

## Hard rules (violation = stop and fix)

- **Phase math is LITERAL** (⛔ MEMORY #4): full spread = `360 − 360/N`; apply the pinned formulas manually; NEVER encoder-bar values in pool-stored objects.
- Fixed-point encoding: XML Measure/Speed = value × 16777216 (2^24). `16777216` is a literal 1.0, not a none-sentinel. Verify arithmetic both directions.
- Color presets author `ColorRGB_R/G/B` — `ColorAdd` silently fails. Store Universal, not Global.
- Slot discipline: per-song phaser banking (SONG_E = 1400 block); cLD scratch slots start x.121 (stock occupies through .113).
- `[VERIFY]`-tagged concepts are hypotheses — never build a conclusion on one; route to QUESTIONS.
- Authored files carry no GUIDs.

## Known silent traps

Stock recipe-preset templates are EMPTY on bare call (cook only through a recipe line). Edited recipe presets revert on clear unless committed via Update. Both are ⛔/⚠-class — see the concepts.

---
name: ma3-sequence-tc-gate
description: Authoring gate for grandMA3 Sequence XML and Timecode XML. Use BEFORE writing, editing, or verifying any sequence deliverable, recipe-only sequence, cue-list XML, or TC event XML. Triggers on Import Sequence, StandardRecipe, PresetData, UseExecutorTime, cue parts, CmdSubTrack, timecode events.
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

# MA3 Sequence / Timecode Authoring Gate

Structural gate (repo law: `WORKING/AGENT_LANES_SPEC_v0.1.md`): no sequence or TC XML gets authored or certified until the dialect is armed. Paths relative to the MA_PROGRAMMING repo's `WORKING/` folder.

## Preferred lane — dispatch the smith

Dispatch SEQUENCE SMITH per `agents/SEQUENCE_SMITH_v0.1.md` (stage manifest + golden + target + cue/binding tables; smith returns VERDICT/CHECKS/FINDINGS report).

## Inline lane — small edits only

Read FIRST, in order:

0. **`agents/cards/CARD_AUTHORING.md`** for the sequence/cue work — and **`agents/cards/CARD_TIMECODE.md`** the moment the task is timecode (TC is a separate session by ruling; its card is separate for the same reason). Cards are the foreground; the concepts below are the depth. In a main session the spine is already loaded and the card alone re-arms you; in a smith dispatch, stage the card AND the manifest.
1. `concepts/export-sequence-xml-schema.md`
2. `concepts/recipe-xml-schema.md`
3. `concepts/recipe-output-precedence-and-cooking-doctrine.md`
4. `concepts/clean-authoring-and-persistence-doctrine.md`
5. `concepts/cuefade-not-a-real-property-gotcha.md`
6. `concepts/xml-file-side-authoring-import-lane-proven.md`

Golden: `beatgrid/Meta/cld_maker_handoff/fixtures/cld_seq102_inspect.xml` (sequences) / `Tc1_Inspect.xml` (timecode; + `concepts/export-timecode-tc-event-xml-schema.md`).

## Hard rules (violation = stop and fix)

- Recipe-only doctrine: every cue part carries a `StandardRecipe`; ZERO cooked `PresetData` blocks in a recipe-only deliverable.
- `UseExecutorTime="No"` on this show, always.
- Timing lives in recipes + cue-stack follow times. `CueFade` is not a real property — setting it silently no-ops.
- Bind refs use the golden's dotted full-path form; cross-check every Group/Preset/MAtricks ref against the binding table.
- Same quote/attr hygiene as macros: no raw `"` inside quoted attr values.
- DependencyExport: embedded (console-export style) vs omitted (authored style) is a per-file decision — state it, verify consistency.
- Authored files carry no GUIDs.

## After any import (before any Go+)

Readback census vs the cue table (cue count, numbers, labels, parts), then the desk-clear callout before anything fires.

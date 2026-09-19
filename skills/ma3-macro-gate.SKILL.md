---
name: ma3-macro-gate
description: Authoring gate for grandMA3 macro XML. Use BEFORE writing, editing, regenerating, or verifying ANY MA3 macro XML file or builder macro — including quick label fixes. Triggers on macro XML, MacroLine, builder macro, Import Macro, quote dialect, &quot; escaping, cld builder files.
---

# MA3 Macro Authoring Gate

This gate exists because on 2026-07-23 a session authored macro XML twice with the exact quote-dialect fix sitting filed and unopened in the corpus — the import shredded silently and cost a desk session. The gate is structural: no macro XML gets touched until the dialect is armed. (Repo law: `WORKING/AGENT_LANES_SPEC_v0.1.md`; paths below are relative to the MA_PROGRAMMING repo's `WORKING/` folder.)

## Preferred lane — dispatch the smith

Whole-artifact authoring or any pre-desk certification: dispatch MACRO SMITH per `agents/MACRO_SMITH_v0.1.md` (stage its arming manifest + golden fixtures + target; packet carries expected slots/members; smith returns VERDICT/CHECKS/FINDINGS report). The smith's manifest is its boot — the gate cannot be skipped.

## Inline lane — small edits only

Read FIRST, in order, before touching the file:

0. **`agents/cards/CARD_AUTHORING.md`** — the whole silent-failure kit for song content, one page. This is the foreground; the concepts below are the depth behind it. In a main session the spine (`concepts/SPINE.md`) is already loaded, so the card alone re-arms you. In a smith dispatch, stage the card AND the manifest.
1. `concepts/macro-xml-schema-cracked.md`
2. `concepts/macro-line-syntax-and-batching-rule.md`
3. `concepts/xml-file-side-authoring-import-lane-proven.md`
4. `concepts/universal-presets-emitter-aware.md`

Then diff your result against a golden (`generated/cLD_GROUP_BUILDER.xml` or a factory sample) before it goes anywhere.

## Hard rules (violation = stop and fix)

- Command attributes double-quoted; embedded quotes as `&quot;` entities. Raw `"` inside single-quoted attrs = silent line-shredding on Import (import echoes OK — you will not be told).
- One command per MacroLine. No `;` batching in macro lines (interactive CLI batches; macros never).
- Labels ride Store-with-name-inline (`Store Group 60 "name"`); separate Label lines are legacy.
- `/Universal` on every `Store Preset`.
- Authored files carry no GUIDs.

## After any import (before any Go+)

LINE-READBACK DIFF: read every macro line back off the console and diff against the authored file. Check the CLI history tail (`(Macro N 'x')OK:` / `Illegal object:` per line). Never fire without the desk-clear callout.

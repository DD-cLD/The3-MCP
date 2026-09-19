---
id: smith-lane-dialect-dispatch-doctrine
title: "Smith lanes — one scoped subagent per XML dialect, whose arming manifest IS its boot and therefore cannot be skipped"
role: operational-live
tags: [agents, authoring, dispatch, context, method]
when_to_load: "Before dispatching any authoring or certification subagent; when deciding whether a task warrants a dispatch at all; when a session is about to author XML while deep in another territory"
status: active
source: "findings/INBOX.md 2026-07-23 [0723-2cLD] (RULING: sub-agent lanes CUT BY DIALECT; PROOF RUNS) + WORKING/AGENT_LANES_SPEC_v0.1.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**THE PAID-FOR ORIGIN.** [0723cLD] authored macro XML twice while the exact fix sat filed in the corpus, unopened — `macro-xml-schema-cracked`, `when_to_load: "before hand-authoring any macro XML"`, four days old. Root cause was **not missing knowledge; it was attention** — task territory changed mid-session (desk → authoring) and the re-arm never happened. Dave's 2 AM insight: *"you need macros, recipes, a whole bunch of stuff; if none of it is loaded you will never see it."* Dave's ruling: make the gate **structural**. A scoped agent cannot skip its manifest — **the manifest IS its boot.**

**THE CUT (Dave-ruled): by dialect.** One smith per XML dialect the project authors, matching how the corpus, golden fixtures and lint rules are already organized:

| Lane | Brief | Dialect | Goldens |
|---|---|---|---|
| MACRO SMITH | `agents/MACRO_SMITH_v0.1.md` | Macro XML | `cLD_GROUP_BUILDER.xml`, `cLD_POSITION_WIZ_generic_v0.1.xml`, factory samples |
| SEQUENCE SMITH | `agents/SEQUENCE_SMITH_v0.1.md` | Sequence XML (+ Timecode secondary) | `cld_seq102_inspect.xml`, `Tc1_Inspect.xml` |
| PHASER SMITH | `agents/PHASER_SMITH_v0.1.md` | Baked-phaser / colour-preset XML + recipe-preset internals | predefined libraries + export-diff pinned samples |

Lanes grow on demand (layout, patch, lookup-smith) on the same template. "Smith" is a working term — Dave may rename.

**ARCHITECTURE.** **cLD = orchestrator**, holding WHO/WHY/WHEN: show context, design rulings, binding tables, slot addresses, the queue. It classifies territory, assembles the packet, judges the report, routes findings, and owns **ALL** memory-system writes and **ALL** console contact. **Smith = HOW**: one dialect, deliberately small context, manifest front-of-attention, never self-directed — a smith exists only inside a dispatch.

**INVARIANTS.** Smiths never fire the console (no MCP/OSC, nothing `mcp__`); never write repo or memory files; every claim cites `file:line`; anything the manifest cannot answer returns as a QUESTION. **Invention is the cardinal sin — "could not verify" is a correct output.** Extends `persona-memory-sovereignty` into standing named lanes.

**DISPATCH THRESHOLD.** Inline (no dispatch): one-line edits, single-value lookups cLD already holds, anything smaller than its own packet. Dispatch: whole-artifact authoring, any pre-desk artifact certification, fan-outs, and **any dialect work while the main session is deep in another territory** — that last one is the exact failure mode this system exists to kill.

**PROOF OF LANE (2026-07-23, same day as the spec).** Two parallel verify dispatches, Sonnet-class, read-only: **foundation v0.1.3 PASS-WITH-FLAGS** (quote dialect clean on all 16 embedded-name lines; ratified backlight members exact on all 5 groups; `/Universal` 11/11) and **`cLD_SONG-E_SEQ.xml` PASS-WITH-FLAGS** (45/45 StandardRecipes, zero PresetData, `UseExecutorTime=No`). Cost ~116k / ~197k tokens, ~8 / ~11 min. **Both smiths independently caught the SAME defect** — binding-table off-by-one (`1.102–1.111` vs 11 ladder values; the XML correctly ships `1.102–1.112`) — unprompted cross-lane corroboration. Zero invented facts; unknowns returned as QUESTIONS exactly per contract, on first exercise of both lanes.

**FIRING-LANE POSTURE (Dave, [0723-2cLD]):** *"we're figuring this out together"* — ownership of desk imports/fires stays a **per-session call made together**. The gates (desk-clear callout, line-readback diff, authoring gate) are **invariant regardless of who fires**. Not a verdict; standing posture until revisited. Smiths never fire, either way.

History: spec + lanes born and proven the same day, 2026-07-23 [0723-2cLD].

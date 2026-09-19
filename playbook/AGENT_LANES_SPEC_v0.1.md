---
metadata_version: "1.0"
doc_id: ma3-agent-lanes-spec
title: "AGENT LANES -- smith dispatch spec"
owner: DaveDibb
version: "0.1"
status: active
created_at: 2026-07-23
session: "[0723-2cLD]"
tags: [tier-2, method, agents, context, authoring]
notes: |
  Born from the [0723cLD] retrieval-miss postmortem + Dave's sub-agent instinct
  ([0723-2cLD]). Ratifies AUTHORING GATE + ARMING MANIFESTS as structure rather
  than discipline. First two lanes (macro, sequence) proven live the same day
  the spec was written -- verify dispatches on both SONG_E deliverables.
---

# AGENT LANES -- spec v0.1

## Why this exists (the paid-for origin)

[0723cLD] authored macro XML twice while the exact fix sat filed in the corpus, unopened -- `macro-xml-schema-cracked`, `when_to_load: "before hand-authoring any macro XML"`, four days old. Root cause was not missing knowledge; it was attention: task territory changed mid-session (desk → authoring) and the re-arm never happened. Dave's insight (2 AM): "you need macros, recipes, a whole bunch of stuff; if none of it is loaded you will never see it." Dave's ruling ([0723-2cLD]): make the gate structural. A scoped agent cannot skip its manifest -- **the manifest IS its boot.**

## The cut: by dialect (Dave-ruled)

One smith per XML dialect the project authors, matching how the corpus, golden fixtures, and lint rules are already organized:

| Lane | Brief | Dialect | Goldens |
|---|---|---|---|
| MACRO SMITH | `agents/MACRO_SMITH_v0.1.md` | Macro XML | `cLD_GROUP_BUILDER.xml`, `cLD_POSITION_WIZ_generic_v0.1.xml`, factory samples |
| SEQUENCE SMITH | `agents/SEQUENCE_SMITH_v0.1.md` | Sequence XML (+ Timecode XML secondary) | `cld_seq102_inspect.xml`, `Tc1_Inspect.xml` |
| PHASER SMITH | `agents/PHASER_SMITH_v0.1.md` | Baked-phaser / color-preset XML + recipe-preset internals | predefined libraries + export-diff pinned samples |

Lanes grow on demand (layout XML, patch XML, lookup-smith for manual/concept retrieval) -- same template. "Smith" is a working term; Dave may rename.

## Architecture

**cLD = orchestrator.** Holds WHO / WHY / WHEN: show context, design rulings, binding tables, slot addresses, the queue. Classifies task territory, assembles the dispatch packet, judges the returned report, routes findings, owns ALL memory-system writes and ALL console contact.

**Smith = HOW.** One dialect, deliberately small context, manifest always front-of-attention. Never self-directed -- a smith exists only inside a dispatch.

**Model routing** per `model-routing-doctrine-bakeoff-evidence` *(concept not included in this release — ops-meta family)*: Opus-class for first-authoring dispatches; Sonnet-class for verification, regeneration, and mechanical fan-outs; the lead session orchestrates and judges. (Proof runs 2026-07-23 ran the verify lane on Sonnet-class, both PASS-WITH-FLAGS, zero invented facts.)

## Dispatch protocol

1. **Stage.** cLD stages the lane's manifest concepts + golden fixtures + target + context docs into the session workspace (`device_stage_files`).
2. **Packet.** Prompt = brief core (inline) + staged paths + ONE bounded task + expected values (ratified bindings, slot addresses, censuses -- superseding stale doc prose where applicable) + output contract.
3. **Work.** Smith reads the manifest FIRST, in order, then works. Verify dispatches are read-only. Authoring dispatches write only to the packet-designated workspace path and self-verify before returning.
4. **Return.** Final message = raw report: VERDICT · CHECKS (evidence file:line) · FINDINGS (severity + quoted line) · QUESTIONS · FINDINGS_LOCAL.
5. **Judge + route.** cLD spot-checks citations, routes FINDINGS_LOCAL → `findings/INBOX.md`, QUESTIONS → Dave or the queue, artifacts → `generated/` only after cLD-side verification. The librarian digests INBOX as usual -- smiths never touch the memory system.

**Invariants:** smiths never fire the console (no MCP/OSC, nothing `mcp__`); never write repo or memory files; every claim cites file:line; anything the manifest can't answer returns as a QUESTION -- invention is the cardinal sin; "could not verify" is a correct output.

## Dispatch threshold

Inline (no dispatch): one-line edits, single-value lookups cLD already holds, anything smaller than its own packet. Dispatch: whole-artifact authoring, any pre-desk artifact certification, fan-outs, and ANY dialect work while the main session is deep in another territory -- that last one is the exact failure mode this system exists to kill. Measured overhead (2026-07-23 proof runs, Sonnet-class, parallel): macro verify ~116k tokens / ~8 min; sequence verify ~197k tokens / ~11 min. A verify dispatch pays for itself the first time it blocks one bad import.

## Proof of lane (2026-07-23, same day as this spec)

First two dispatches: **foundation v0.1.3 PASS-WITH-FLAGS** (quote dialect clean on all 16 embedded-name lines; RATIFIED backlight members exact on all 5 groups -- re-fire hazard cleared; `/Universal` 11/11; envelope + line discipline clean) and **cLD_SONG-E_SEQ.xml PASS-WITH-FLAGS** (45/45 StandardRecipes, zero PresetData, `UseExecutorTime=No`, refs cross-checked by name against binding table + group builder). Both smiths **independently caught the same binding-table off-by-one** (`1.102-1.111` vs 11 ladder values) -- unprompted cross-lane corroboration -- and surfaced the stale superseded backlight ranges still in the build note / binding table prose. Flags routed to INBOX + the queue the same session.

## Relationship to existing doctrine

- Extends `persona-memory-sovereignty` *(not included in this release)* (clean-room workers, FINDINGS_LOCAL carry-out) into standing named lanes.
- Implements the AUTHORING GATE + ARMING MANIFESTS (INBOX 07-23) as structure. `SONG_BUILD_SPEC` Step 3 is the primary dispatch surface; its v0.2 should point here.
- The librarian remains the knowledge-side agent; smiths are delivery-side. The `crosscheck-subagent-pattern` stays in force for Tier-2 MCP/code work.
- Manifests still bind cLD itself: kickoff loads the applicable territory manifest, and every mid-session task-type transition re-arms. The full-corpus arming experiment (INBOX rider) is a separate main-session question -- smiths stay focused-manifest by design either way.

## Open items

- **Firing lane:** per-session call, decided together at the desk (Dave, [0723-2cLD]). Gates invariant. Smiths never fire regardless.
- Brief v0.2 ratification pass after the first AUTHORING dispatch (verify lane proven; author lane next -- candidate: SONG_E v0.2 life-layer phasers via PHASER SMITH).
- Candidate lanes on demand: lookup-smith, layout, patch.

---
id: external-cross-vendor-review-lane-pattern
title: "External cross-vendor review lane: independent Grok Heavy 4.5 + clean-room Opus review corroborated on the #1 blocking item — first cross-vendor data point"
role: tools
tags: [tourshow, cld-maker, process]
when_to_load: "Before routing a spec pack or deliverable to an external (non-Claude) model for independent review, or when weighing how much to trust a single reviewer's findings vs. corroboration across vendors"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD] (Dave)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Trial:** cLD MAker spec-pack verification was routed to an EXTERNAL reviewer — Grok Heavy 4.5 (abundant credits there), possibly Opus 4.8 in parallel. `REVIEW_PROMPT.md` was written into `cld_maker_handoff/` as a drag-and-drop clean-room brief.

**Ground rule hard-coded into the prompt:** external models must NOT "correct" MA3 console facts from training priors — the live-verified project corpus outranks them. Suspicious facts get routed to a QUESTIONS section for cLD adjudication rather than silently overwritten.

**Intake model:** findings come back as proposals; cLD judges intake. This extends `crosscheck-subagent-pattern` to external, non-Claude models — the first data point for cross-vendor review economics.

**Result:** two independent reviews (Grok Heavy 4.5 + a clean-room Opus) corroborated on every BLOCKING item — a strong cross-vendor signal. The #1 blocking item for BOTH reviewers was the recipe→XML mapping, which was then over-resolved by the live Export Sequence capture (see `export-sequence-xml-schema`) before the pack was melded to v0.2.

**Relation:** `crosscheck-subagent-pattern` — the pattern being extended to external vendors. `bakeoff-sandbox-pattern` — the clean-room-brief precedent this reuses. `persona-memory-sovereignty` — the adjudicate-don't-auto-append intake model this follows. `cld-maker-identity-rename-and-scope` — where the reviewed pack landed (v0.2, Codex-ready).

**Elevated to standing resources, 2026-07-21 (Dave, dictated, post SONG_G first-pass build):** Grok(max) + GPT/Codex(max) are now STANDING resources for this project, not one-off trial reviewers — cLD stays in the driver's seat, pulling them in as needed rather than working solo. Reaffirmed the hard way: this session's recipe-vs-baked doctrine miss (see `review-plan-gate-precedes-programming-doctrine`) went uncaught by cLD itself and surfaced only on Dave's own review — direct evidence for the standing value of a **fresh-eyes external clean-room pass** (model diversity + relief from long-exposure/model-shape blindness a single agent can't self-diagnose). A dedicated external clean-room review pass is now P0-queued before SONG_G gets re-programmed.

History: none — trial run and result both recorded 2026-07-17, same session as the pack meld. Extended 2026-07-21: Grok(max) + GPT/Codex(max) ruled standing resources (not one-off); fresh-eyes external review value reaffirmed by a same-session miss that cLD didn't self-catch.

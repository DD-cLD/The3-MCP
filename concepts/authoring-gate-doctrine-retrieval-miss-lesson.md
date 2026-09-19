---
id: authoring-gate-doctrine-retrieval-miss-lesson
title: "Retrieval-miss postmortem: the quote-dialect fix was already in the corpus before a same-session authoring failure, because task territory changed (desk→authoring) mid-session and the re-arm never happened — AUTHORING GATE candidate doctrine"
role: operational-live
tags: [doctrine, retrieval, authoring]
when_to_load: "Before hand-authoring or regenerating any console XML artifact — and at every mid-session task-type transition"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (RETRIEVAL-MISS POSTMORTEM; NEW STANDING RULE — AUTHORING GATE)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**RETRIEVAL-MISS POSTMORTEM (exposed by Dave's audit question):** the quote-dialect fix that would have prevented a same-session macro-authoring failure ALREADY existed in the corpus before the failure — `macro-xml-schema-cracked` (filed 07-19) states "Inner quotes are XML-escaped: `&quot;`" with `when_to_load` literally `"Before hand-authoring or generating any macro XML file"`. The failing session loaded 7 desk-territory concept bodies and ZERO macro-authoring bodies, then went on to author macro XML twice. **Root cause:** the task's territory changed mid-session (desk work → authoring work) and the re-arm — reloading authoring-relevant concepts — never happened. Compounding factor: the index one-liner for `macro-xml-schema-cracked` didn't mention "quotes," so even a skim of the index couldn't have caught the gap (this is the retrieval-miss root cause the mandated index-line fix addresses — see the fixed line proposed for `macro-xml-schema-cracked` in this run's STAGING_REPORT).

**NEW STANDING RULE (candidate doctrine) — AUTHORING GATE:** before hand-authoring or regenerating ANY console XML artifact:
1. Open that dialect's schema concept — honor its `when_to_load` literally, don't skip it because "desk" concepts are already loaded.
2. Diff the authored file against a proven same-dialect exemplar (factory file or a live-verified cLD file).
3. Doctrine lint includes DIALECT checks (envelope shape, attribute quoting, `&quot;` escaping) — not just a structure census.

**Corollary:** re-run territory classification at every mid-session task-type transition — don't assume the concepts loaded at session start still cover what the session is doing an hour later.

Relation: `macro-xml-schema-cracked` (the concept this postmortem is about); `arming-manifests-proposal` (the proposed deterministic mechanism to make this gate automatic rather than judgment-dependent).

History: none — captured 2026-07-23 [0723cLD] digest run.

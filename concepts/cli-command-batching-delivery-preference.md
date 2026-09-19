---
id: cli-command-batching-delivery-preference
title: "When handing Dave command lines to type at the interactive CLI, batch them into one line with semicolons — one-command-per-line stays a macro-only rule"
role: operational-live
tags: [delivery-format, cli]
when_to_load: "Before writing out a block of console commands for Dave to type at the interactive CLI"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (DELIVERY PREFERENCE)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**DELIVERY PREFERENCE (Dave):** when handing Dave command lines to type at the interactive CLI, batch them into ONE line with semicolons — the interactive CLI batches `;` (verified rule). This is a delivery-format preference, distinct from macro authoring: one-command-per-line stays a MACRO-only rule (see `macro-line-syntax-and-batching-rule` — macro lines never batch `;`; the interactive CLI does). Do not confuse the two lanes when generating either a macro XML file or a block of desk-typed commands.

History: none — captured 2026-07-23 [0723cLD] digest run.

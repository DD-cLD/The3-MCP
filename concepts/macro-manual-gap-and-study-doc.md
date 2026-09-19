---
id: macro-manual-gap-and-study-doc
title: "06_Macros.md manual gap inventory + MACROS_STUDY_v0.1 closes it; corrects MA2-carryover 'Trigger type' drift"
role: programmer
tags: [ma3, manual, macro, process, v2.4]
when_to_load: "Before hunting the repo manual for macro documentation, or before trusting a repo-manual macro-CLI claim (e.g. a 'Trigger' line type) as current — cross-check MACROS_STUDY_v0.1 first"
status: active
source: "findings/INBOX.md, 2026-07-17 (macro deep-dive session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Repo manual gap inventory:** `06_Macros.md` is stubbed for Overview / Editor / CommandDelay / Echo / Conditional-If — only the Variables section and the v2.4-updates section are real content.

**Specific drift caught:** the manual's §2 stub outline lists macro-line cell types as "Command/Wait/Trigger" — **there is no "Trigger" macro-line type in MA3.** Macro rows are uniform command rows with exactly five cells: `Command` / `Wait` / `Enabled` / `AddToCmdline` / `Execute` (official `macros.html`, "Elements in a Macro"). The "Trigger" listing is MA2 carryover — flagged as repo manual drift, fix on backfill.

**Resolution:** all five stub topics (Overview, Editor/line-cells, CommandDelay, Echo, Conditionals) are now fully answered from the official manual in `MACROS_STUDY_v0.1`. No console-only verification remains for the stubbed content. **Update 2026-07-19: the one item this concept originally left open — exporting a real macro to crack the macro XML schema — is now closed too, and without needing a console export at all.** The schema fell out file-side from 13 factory `lib_macros` samples; see `macro-xml-schema-cracked`.

This joins the running manual-gap list alongside `measure-layer-math` (Measure) and `at-filters-worlds-manual-gap-and-study-doc` (If/At/Filters/Worlds).

History: created 2026-07-17 from the macro deep-dive session. Extended 2026-07-19: noted the schema-cracked resolution (see `macro-xml-schema-cracked`), closing this concept's own last open item.

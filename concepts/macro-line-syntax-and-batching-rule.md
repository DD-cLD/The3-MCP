---
id: macro-line-syntax-and-batching-rule
title: "Macro Store/Set syntax, and where semicolon batching does (and does not) work"
role: programmer
tags: [ma3, v2.4]
when_to_load: "Before generating grandMA3 macro lines, or before writing multi-command CLI sequences — the batching rule differs between macro lines and interactive CLI"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules / Patterns We Use, 2026-04-01 (scoped/refined 2026-07-04)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Macro line syntax:** `Store Macro X.Y` then `Set Macro X.Y "command" "text"`.

**One command per macro line — this rule still holds, unchanged:** semicolons between `Set MAtricks` (and other) property commands do **NOT** batch inside a macro line; each command must be its own macro line. This was the original 2026-04-01 rule and remains true.

**Refinement (verified live, onPC 2.4.2.2, 2026-07-04):** the no-batching behavior is specific to **macro-line authoring**. **Interactive CLI entry DOES support `;` to batch distinct commands** — verified live on 2.4.2.2. The two contexts are genuinely different:
- Macro line: one command per line, no semicolon batching, ever.
- Interactive/live CLI: `;` batches distinct commands.
- In **both** contexts, `Set <obj>` property chains stay semicolon-free internally (i.e. don't put semicolons inside a single `Set` command's property list).

Also unchanged: **MAtricks recall MUST be a separate macro line from Group/Preset** — do not combine them on one line.

**Gotcha when a batched command pops a dialog:** if one of the `;`-batched commands in interactive CLI triggers a blocking dialog (e.g. an `Assign Layout` Merge/Overwrite prompt), the remainder of the line is not dropped — it suspends and resumes once the dialog is resolved, even on Cancel. See `dialog-suspend-resume-batched-lines`.

**Factory short-form option keywords (noted, NOT adopted) — 2026-07-19:** shipped factory macros use `/NoConfirm` (short form) and `cd` (shorthand for `ChangeDestination`), plus quoted symbol tokens for Align modes (e.g. `Align "><"` for butterfly). These are valid MA-shipped short forms, recorded here verbatim for reference — but our own SaveShow standing rule keeps the long `/NoConfirmation` form (see `saveshow-discipline-and-mcp-tier`), and that rule is unchanged by seeing the short form in factory content.

History: originally stated (2026-04-01) as a blanket "no semicolon batching" rule for MA3 generally. Scoped 2026-07-04 after live verification on 2.4.2.2: the rule is macro-line-specific; interactive CLI entry does batch with `;`. The macro-line rule itself did not change. Flagged-not-resolved 2026-07-17: a 2021 forum report describes semicolon-separated commands working as one synchronous unit within a SINGLE macro line, on an older pre-2.2 build. This does **NOT** supersede the rule above — Dave's live verification on 2.4.2.2 (2026-07-04) stands as current truth. The 2021 thread is recorded here as historical context only, not as a correction (behavior may genuinely have changed across builds, or the old report may describe a different mechanism — unconfirmed either way). Extended 2026-07-19: factory short-form option-keyword usage (`/NoConfirm`, `cd`, quoted Align tokens) noted verbatim, explicitly not adopted.

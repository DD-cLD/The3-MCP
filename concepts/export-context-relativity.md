---
id: export-context-relativity
title: "Export may depend on which CLI prompt you're at (LivePatch vs root) — one data point, now uncertain after the dialog-suspend-resume finding"
role: programmer
tags: [ma3, cli, v2.4, export, verify]
when_to_load: "Before running Export from inside a pool-object context (e.g. LivePatch) rather than the root prompt — check the prompt path first, and don't treat this as fully confirmed yet"
status: verify
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2 — single data point, confidence undercut same session"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Observed once:** from the **LivePatch** CLI prompt, `Export Layout 2` failed silently — no file was produced. The same command worked from the **root** prompt (recorded as `Admin[Fixture]>`). Standing practical guidance from this observation: **run `Export` from the root prompt**, or more generally, check which prompt/context is current before targeting a pool object with `Export`.

**[VERIFY] — this needs re-testing in isolation.** The same session later found that a blocking dialog suspends and resumes a `;`-batched line rather than killing it (see `dialog-suspend-resume-batched-lines`). The one clean data point behind this context-relativity claim (the file missing when run from the LivePatch prompt, present when run from root) may be explained by that dialog-timing behavior instead of true prompt-context sensitivity — a dialog could have been in play around that test without being attributed correctly at the time.

**Clears with:** re-run `Export Layout <n>` (or `Export Patch`) from a LivePatch prompt as a standalone line — no batching, no dialogs in flight — and confirm whether it still fails silently. If it succeeds in isolation, the original finding was a dialog-timing artifact, not context-relativity.

History: none — single observation 2026-07-14, flagged [VERIFY] the same session once the dialog-suspend-resume mechanism came to light.

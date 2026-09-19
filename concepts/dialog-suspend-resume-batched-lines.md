---
id: dialog-suspend-resume-batched-lines
title: "A blocking dialog SUSPENDS the rest of a `;`-batched CLI line and RESUMES it on resolution — even Cancel resumes the queue"
role: programmer
tags: [ma3, cli, v2.4, dialog]
when_to_load: "Before batching multiple `;`-separated commands where one might pop a blocking dialog (Assign Layout Merge/Overwrite, etc.) — determines whether queued commands after the dialog will still run"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2 — revised same-session finding; wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Settled behavior (revised mid-session, 2026-07-14): a blocking dialog SUSPENDS the remainder of a `;`-batched CLI line and RESUMES executing the queued remainder once the dialog is resolved — even clicking Cancel resumes the queue; it does not abort it.** Evidence: a batched line queued a command past an Assign-Layout Merge prompt; after clicking **Cancel** on that dialog, a later command in the same batch still executed — `cld_l2_probe.xml` materialized on disk *after* the Cancel click, proving the queued remainder ran rather than being dropped.

**This supersedes an earlier same-session reading.** The first pass at this finding concluded the opposite: that a blocking dialog (e.g. Assign's Merge prompt) **kills** the rest of a `;`-batched line, with commands after it never running, and recommended keeping any dialog-popping command at the end of a paste or standalone. Better evidence collected later the same session overturned that reading. **Practical effect:** the old workaround (isolate dialog-popping commands at the end of a batch) is no longer necessary.

**This reopens the "Export is context-relative" question — see `export-context-relativity` [VERIFY].** The one data point behind that separate finding (an `Export` failing from a LivePatch prompt) was captured around the same test where a dialog was in play. Now that suspend/resume is understood, that data point may have another explanation and needs re-testing in isolation before the context-relativity claim stands on its own.

History: first pass (same session, 2026-07-14) concluded dialogs kill the rest of a batched line; corrected the same day after the Cancel/`cld_l2_probe.xml` evidence showed suspend-then-resume instead — the corrected reading is what's stated above.

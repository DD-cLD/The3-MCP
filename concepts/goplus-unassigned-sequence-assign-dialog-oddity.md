---
id: goplus-unassigned-sequence-assign-dialog-oddity
title: "[VERIFY] An empty 'Assign Page 1 Executor 401' dialog appeared unprompted after Go+ on a then-unassigned sequence"
role: programmer
tags: [ma3, cli, v2.4, verify, oddity]
when_to_load: "If an unprompted Assign dialog pops up after firing Go+ on a sequence — this may be expected MA3 behavior (Go+ on an unassigned sequence auto-prompting assignment), not a bug; check here before treating it as an anomaly"
status: verify
source: "findings/INBOX.md, 2026-07-16, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

An empty **"Assign Page 1 Executor 401"** dialog appeared unprompted after a `Go+` on then-unassigned Sequence 102. (The source note also allows it may have come from a fall-through paste round instead, in flight the same moment — cause is not pinned down either way.)

It turned out useful in the moment — it became the lane actually used to assign the sequence to the executor — but *why* it appeared is unconfirmed.

**[VERIFY]:** does `Go+` on an unassigned sequence deliberately pop an Assign dialog as designed MA3 behavior? Or was this specific popup a side effect of something else in flight that session (e.g. the fall-through paste candidate mentioned in the source)?

History: none — first observed live 2026-07-16, cause not yet isolated.

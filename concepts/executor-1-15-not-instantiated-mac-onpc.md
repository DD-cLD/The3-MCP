---
id: executor-1-15-not-instantiated-mac-onpc
title: "Executors 1-15 are NOT instantiated by default on this Mac onPC — Assign fails silently, Executor 15/Page 1.15 resolve nil; the 101+ bank works, Assign instantiates an executor on first use"
role: programmer
tags: [ma3, cli, executors, v2.4, onpc]
when_to_load: "Before assigning a sequence to an executor in the 1-15 range on this Mac onPC — check the executor actually exists first, or expect a silent no-op; also relevant when remapping a build off the 101+ scratch bank onto the tour desk's real 1-15 fader envelope"
status: active
source: "findings/INBOX.md [0721-2cLD] block, 2026-07-21, console live 2.4.2.2, cLD SONG_G + cLD SLIDE POP build"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The gotcha:** on this Mac onPC, executors **1-15 are not instantiated** by default. `Assign Sequence 15 At Executor 15` **fails silently** — no error, no effect. Downstream, `Executor 15` and `Page 1.15` both **resolve nil** (object-list lookups against them come back empty), even though the CLI accepted the Assign command without complaint.

**The 101+ bank works:** the scratch executor range instantiates cleanly, and `Assign` appears to **instantiate the executor on first use** in that range — e.g. `Assign Sequence 101 At Executor 102` resolved to a live object address (`14.14.1.12.2.102`) immediately.

**This session's workaround:** built on the working bank instead of the intended 1-15 tour-desk range — **cLD SONG_G** (Seq 15) → **Exec 102**, **cLD SLIDE POP** (Seq 101) → **Exec 101**. **Re-mapping to the real 1-15 fader envelope is still owed** before this show runs on the actual tour desk.

**Open question:** whether this is a Mac-onPC-specific quirk (parallel to `mac-vs-windows-onpc-network-output`'s Mac-vs-Windows onPC split) or a more general "executors must be paged/instantiated before Assign can bind" console behavior isn't yet determined — not tested against Windows onPC or a real console. Possibly related to the older `goplus-unassigned-sequence-assign-dialog-oddity` [VERIFY] (an unprompted Assign dialog on an unassigned sequence/executor) — unconfirmed, not established as the same root cause.

History: none — paid for live 2026-07-21, [0721-2cLD] session, building the cLD SONG_G + cLD SLIDE POP sequences.

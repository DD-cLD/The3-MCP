---
id: store-default-values-keyword
title: "`Store Default` (two words) values a fixture type's DEFAULT — Merge mode is the master-default staging pattern for multi-instance cell recipes"
role: programmer
tags: [ma3, cli, patch, multi-instance, v2.4, doc-gap]
when_to_load: "Before building cell-level recipes/cues on a multi-instance fixture (plate+beam, pix+tube, etc.) — stage the type's Default values first so per-cell recipes can carry the look alone"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Syntax settled live:** `Store Default` — **two words**. `StoreDefault` (one word) is **Illegal object**. The repo manual has **no entry at all** for this command (a doc gap, not a doc error).

Firing it opens a popup, verbatim: **"Store Default values — choose mode"** with options **Overwrite / Merge / Remove / Cancel**. **Merge is the standard call** (Dave's default choice).

**Master-default staging pattern (Dave's doctrine):** before programming cell-level cues on a multi-instance fixture, stage the programmer first — **MASTER** element at **full**, **ALL instances** (e.g. plate + beam cells) at **zero** — then `Store Default` → Merge. This makes the fixture's masters ride at full **by default**, so per-cell recipes only need to carry the look itself rather than also fighting the master level. Applied and Dave-approved on the JDC1 type (Layout 3 + the session's sequence recipes checked and approved against it).

History: an initial pass same session flagged the exact syntax `[VERIFY exact syntax via popup]` after only the doctrine (not the keyword) was confirmed; settled minutes later live — `Store Default`, two words, Merge mode — folded here as the single settled statement rather than carrying the transient VERIFY forward.

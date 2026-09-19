---
id: beatgrid-undo-side-cache-pattern
title: "Undo systems must keep heavy binary payloads OUT of JSON snapshots — id-keyed side caches, reattached on restore by id + reference match"
role: tools
tags: [process, beatgrid]
when_to_load: "Before designing or debugging any undo/redo system whose state includes heavy binary payloads (decoded audio, image dataURLs, frame captures) — especially before trusting a 'harvest from current state before restore' recovery strategy"
status: active
source: "findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Paid-for via cross-check M2 (see `crosscheck-subagent-pattern`'s 3rd data point) plus a real bug the fix exposed. **Rule: heavy binary payloads (decoded audio, image dataURLs) must live OUTSIDE JSON undo snapshots**, in **id-keyed, session-lifetime side caches** (`S.framePix`, `stemAudioCache` in beatgrid.html), and get **reattached on restore by id + reference-field match** — not carried inside the snapshot itself.

**Naive alternative fails:** "harvest the payload from current state right before restoring" **loses payloads** when the mutation being undone is the one that removed the holder — e.g. delete-section → undo dropped the lane's stem audio, because by the time the harvest ran, the current state no longer had a lane to harvest from.

History: none — found and fixed same session, 2026-07-06.

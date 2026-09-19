---
id: speedmaster-name-token-exact-match-gotcha
title: "Sequence SpeedMaster value token is the master's exact object NAME — 'Speed1' (no space) works, 'Speed 1' (with a space) is a silent no-op with a clean OK echo"
role: programmer
tags: [ma3, sequences, speed-master, cli, v2.4]
when_to_load: "Before setting a Sequence's SpeedMaster property via CLI or MCP — the value must exactly match the speed master's object NAME string, and a plausible-looking variant with a space silently does nothing"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_B SpeedMaster fix x17, live 2.4.2.2)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Finding (card-candidates):** a Sequence's `SpeedMaster` value token IS **the master's exact OBJECT NAME** — `'Speed1'`, **NO SPACE** (this is literally Master 3.1's name). `'Speed 1'` **with a space is a SILENT NO-OP** — clean `OK` echo, no error, and the property does not actually change. Readback caught it, **twice**.

**Speed masters census:** Master 3.1-3.16 are named `Speed1`..`Speed16`. Master pool layout: 1=Selected · 2=Grand · 3=Speed · 4=Playback · 5=Timing.

**Proven working command:** `Set Sequence <n> Property 'SpeedMaster' 'Speed1'` — single-quoted, over MCP, works.

**Transport trick banked:** `string.char(34)` builds real double-quotes inside a `send_lua` payload when a value needs them — legal, produces no raw quote in transport (the raw-quote transport ban stays intact).

**Relation:** `saveshow-discipline-and-mcp-tier` (existing concept, not staged this run — the sibling single-quote-inside-long-bracket transport trick for `SaveShow`, same transport-safety family). `tourshow-seq1110-song-b-build-record` (the x17-sequence fleet fix this gotcha was caught during).

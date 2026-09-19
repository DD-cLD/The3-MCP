---
id: osc-only-remote-protocol
title: "OSC is the only remote command protocol for MA3 — no telnet; /cmd address, string type s"
role: programmer
tags: [ma3, osc]
when_to_load: "Before choosing a remote-control transport for MA3, or when tempted to reach for telnet-style console access"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**OSC is the ONLY remote command protocol** for grandMA3 — there is no telnet interface. The command address is `/cmd` with string-type argument `s`, i.e. an OSC message shaped `/cmd ,s <command-text>`.

Lua version running under MA3 v2.3: **5.4.6** (later confirmed **5.4.8** as of the v2.3→v2.4 migration — see `v24-migration-facts`).

History: none — stable since 2026-04-01. The Lua version number was later refined per-version (5.4.6 under v2.3, 5.4.8 under v2.4); both values are accurate for their respective console versions.

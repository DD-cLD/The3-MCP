---
id: osc-line-property-surface
title: "OSC line property surface (live-verified via :Dump()) — one PORT controls both inbound and outbound"
role: programmer
tags: [osc, lua, mcp]
when_to_load: "Before scripting Set OSC N property commands, or when looking for a 'destination port'/'echo port'/'reply port' field that does not exist"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — OSC line property surface, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`Lua "ObjectList('OSC 1')[1]:Dump()"` returns these properties: `NAME, NOTE, TAGS, DESTINATIONIP, MODE, PORT, PREFIX, DATAPOOL, PAGE, FADER, EXECUTORKNOB, KEY, FADERRANGE, RECEIVE, SEND, RECEIVECOMMAND, SENDCOMMAND, ECHOINPUT, ECHOOUTPUT`.

**There is no hidden "destination port" or "echo port" or "reply port" field.** One `PORT` property controls both inbound listen and outbound send destination for that line.

**Capitalization gotcha:** in `Set OSC N "Property" "value"`, the property name string must match the **visible UI label**, not the dumped uppercase form — use `"Receive"`, not `"RECEIVE"`.

History: none — standalone live-verification result, 2026-05-27 evening.

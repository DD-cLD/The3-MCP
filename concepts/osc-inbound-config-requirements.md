---
id: osc-inbound-config-requirements
title: "Required minimum inbound OSC config — 8-layer checklist for /cmd packets to reach execution"
role: programmer
tags: [osc, mcp]
when_to_load: "When configuring OSC on a fresh onPC install, or debugging why /cmd packets aren't executing on the console — walk this full checklist top to bottom"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — Required minimum inbound config, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

For Python `/cmd` packets to reach MA3 command execution, **ALL** of the following must be true:

| Layer | Requirement |
|---|---|
| Network window | Active Session (loopback session for single-machine dev) |
| SONG_S OSC page | Master `Enable Input = Yes` |
| SONG_S OSC page | Master `Enable Output = Yes` (for any outbound to function) |
| SONG_S OSC page | `Interface` set to a real NIC (`lo0 (127.0.0.1)` for loopback) — NOT `<None>` |
| OSC line | `Receive = Yes` |
| OSC line | `ReceiveCommand = Yes` |
| OSC line | `Port` matches what Python sends to |
| OSC line | `DestinationIP` = the source we want any outbound to go to (irrelevant for pure inbound) |

**When wire is working**, `OSCReceiver : OSCInput: /cmd ,s <text>` appears in System Monitor.

This table **supersedes/corrects** an earlier, weaker claim that `Receive Command = Yes` was sufficient "independent of" the general `Receive` toggle. The corrected understanding: the OSC line requires **BOTH** `Receive = Yes` **AND** `ReceiveCommand = Yes` for inbound `/cmd` traffic — `Receive = No` prevents the line from binding the port at all, regardless of `ReceiveCommand`.

See also `osc-session-required-for-traffic` for the Network-window prerequisite that sits above this whole table, and `osc-line-property-surface` for the property-name capitalization gotcha when scripting these `Set` commands.

History: corrected 2026-05-27 evening. The original (same-day, earlier) MEMORY entry read: "the OSC line MUST have `Receive Command = Yes` (independent of the general `Receive` toggle)." That "independent of" framing was wrong — both flags are required together. This concept file states the corrected, current requirement.

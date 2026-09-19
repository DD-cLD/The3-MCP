---
id: osc-session-required-for-traffic
title: "MA3 requires an active Session before OSC will carry any traffic — the single most-blocking gotcha"
role: programmer
tags: [osc, mcp]
when_to_load: "When OSC packets appear correctly configured but nothing arrives — check Session status before anything else in the OSC config"
status: active
source: "MEMORY §Session activation + corrected OSC architecture, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Without an active Session, OSC lines exist in config but the network subsystem stays dormant — `OSCReceiver` never logs inbound packets even with `EchoInput=Yes`.

**Visible tell:** `ManetSend : Sending multicast (Admin) data without address. Reports skipped: N` repeating in System Monitor.

**Fix:** open the Network window, create or join a session (a loopback session on the local IP works for single-machine dev). After session activation, `OSCReceiver` immediately logs inbound packets.

This was **the** thing that unblocked the OSC inbound wire on 2026-05-27 evening — described in the corpus as "THE thing that unblocked the wire tonight." Check this before any other OSC diagnostic step.

History: none — this is a standalone discovery, not a correction of an earlier claim.

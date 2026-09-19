---
id: osc-two-machine-vs-loopback-topology
title: "Why the Coachella two-line OSC topology worked there but fails on single-machine loopback"
role: programmer
tags: [osc, mcp, coachella]
when_to_load: "Before assuming a two-OSC-line inbound/outbound split will work on a single-machine onPC dev setup — it only works across two real hosts"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — Why the Coachella OSC echo recipe worked there but not here / Once a Session is active binds every Port, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Once a Session is active, MA3 binds every configured OSC line's `Port` regardless of that line's `Receive` setting.** A second OSC line on port 8001 with `Receive=No` will still take port 8001 and block other processes from binding it. On single-machine loopback this is fatal: Python's listener can't share the port with MA3.

**Coachella deployment topology:** MA3 console at `192.168.0.91`, MCP/laptop at a different LAN IP. With different IPs on different hosts:
- MA3 binds port 8000 on `.91`.
- MCP listens on port 8001 on the laptop's IP.
- MA3's outbound destination `<laptop>:8001` reaches the laptop's listener — no port collision, because it's a different machine.

**On single-machine loopback** (`127.0.0.1` everywhere), the same two-line recipe self-conflicts: MA3 wants to send to `127.0.0.1:<port>`, which is its own listen port; whichever port is picked collides with one of the two processes.

**Documented "two-line topology"** (one inbound on 8000, one outbound on 8001) therefore **only makes sense on multi-machine setups**. On single-machine onPC: use **one line**, and accept that command-result round-trip needs the Lua-file pattern (see `osc-outbound-is-event-driven`) rather than a second OSC line.

The original MEMORY note that the Coachella echo recipe (`Send=Yes` + `EchoOutput=Yes` → round-trip echo) worked wasn't wrong in its original two-machine context — it just generalizes badly to loopback, and it also conflated the `EchoOutput` diagnostic with actual transport behavior.

History: this concept explains and reconciles the topology difference behind the correction recorded in `osc-outbound-is-event-driven`; both corrections were made together 2026-05-27 evening.

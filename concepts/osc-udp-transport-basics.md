---
id: osc-udp-transport-basics
title: "OSC transport basics: UDP port 8000, single messages only, Bundles unsupported, addresses shift by version"
role: programmer
tags: [osc, mcp]
when_to_load: "Before wiring any OSC send/receive code against MA3 — baseline transport constraints that apply regardless of topology"
status: active
source: "MEMORY §MCP v2.1 Build — OSC contract, 2026-05-27, onPC 2.3.2.0"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- UDP, default port **8000**; **single messages only** — **OSC Bundles are still unsupported**.
- Enumerated addresses like `/13.13.1.6.X` **shift between MA3 versions** — always resolve at runtime rather than hardcoding: `Lua "Printf(ObjectList(<ref>)[1]:Addr())"`.
- **2.3.1.1** fixed inconsistent spacing in outbound OSC between sequence-name and cue-number — downstream parsers that depended on the old form break across this version boundary.

For the inbound-config requirements (Receive/ReceiveCommand/Session/etc.) and why round-trip echo doesn't work the way you'd expect, see `osc-inbound-config-requirements` and `osc-outbound-is-event-driven` — those sections **correct** two claims originally made alongside these basics (see History).

History: this concept originally also asserted (1) that `Receive Command` was independent of the general `Receive` toggle, and (2) that `Send=Yes` + `EchoOutput=Yes` produces OSC round-trip echo for command results. Both were corrected 2026-05-27 evening after live wire-proving; the corrected facts now live in `osc-inbound-config-requirements` and `osc-outbound-is-event-driven` respectively. This file retains only the claims that were never contradicted.

---
id: osc-outbound-is-event-driven
title: "MA3 outbound OSC is event-driven on mapped state changes, NOT an echo of received commands — no built-in round-trip"
role: programmer
tags: [osc, mcp]
when_to_load: "Before designing any MCP round-trip that expects MA3 to echo command results back over OSC — it will not, by design"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — MA3 outbound OSC is event-driven, not echo-driven, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`EchoInput` and `EchoOutput` are **System Monitor diagnostic toggles only** — they do nothing to actual network traffic.

MA3 emits outbound OSC **only** for mapped state changes on the OSC line: changes to the line's configured **Data Pool / Page / Fader / Executor Knob / Key**. An `Echo "..."` command or any other arbitrary command produces **no** OSC output. (The third-party `ArtGateOne/MA3_OSC_FEEDBACK` plugin exists precisely because users have to write Lua to make MA3 emit arbitrary OSC.)

**Implication for the MCP server:** there is **no "OSC round-trip"** for command results via built-in MA3 OSC. Round-trip queries must use one of:

- **Lua-file pattern** (preferred for read-only queries): send `Lua "..."` that writes JSON to a known path; Python polls and reads it. Proven by the `alchemease_snapshot` plugin.
- **Custom Lua plugin** (for live observers / push channel): the plugin calls MA3's OSC send API explicitly when a watched object changes.

`echo_received` in the `gma3-mcp probe` (as of this writing) will always be `false` on this topology and was flagged for rework.

This concept **corrects** an earlier same-day claim that `Send=Yes` + `EchoOutput=Yes` on the OSC line produces round-trip echo of command results. See `osc-two-machine-vs-loopback-topology` for why that earlier claim wasn't fabricated — it worked on a different (two-machine) topology, which is what generalized badly.

History: corrected 2026-05-27 evening. Original MEMORY entry (same day, earlier): "For round-trip echo, set `Send = Yes` AND `EchoOutput = Yes` on the OSC line." This is wrong — no such built-in mechanism exists. The Coachella experience that suggested this recipe worked did so because of two-machine LAN topology (port collisions/outbound-emission concerns vanish across separate hosts), not because of an actual echo feature; see `osc-two-machine-vs-loopback-topology`.

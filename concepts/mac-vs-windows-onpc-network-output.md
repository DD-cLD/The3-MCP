---
id: mac-vs-windows-onpc-network-output
title: "Mac onPC has no show-network output (Art-Net/sACN/DMX) — fine for pure OSC, use Windows onPC for show-network testing"
role: programmer
tags: [osc, onpc]
when_to_load: "Before testing anything that exercises MA3's outbound show-network stack, or fader/executor-to-OSC mappings, on a Mac onPC install"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — Mac onPC vs. Windows onPC, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

MA3 onPC on **macOS** does **NOT** output a "show network" (no Art-Net / sACN / external DMX node output). **Windows onPC does.**

For pure OSC inbound `/cmd` work, the Mac is fine (proven live 2026-05-27 evening). But any test that exercises MA3's outbound show-network stack — or that needs to verify fader/executor → OSC-out mappings — will probably be cleaner on **Windows onPC**.

The recurring `ManetSend : multicast without address` warnings in System Monitor may be tied to the Mac's missing show-network subsystem; treat as **cosmetic, not blocking**.

History: none — standalone observation, 2026-05-27 evening.

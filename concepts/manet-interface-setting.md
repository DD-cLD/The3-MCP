---
id: manet-interface-setting
title: "MA-Net Interface setting is separate from the OSC line's Interface — both lo0 for loopback dev"
role: programmer
tags: [osc, onpc]
when_to_load: "When configuring network interfaces for a loopback dev session — don't confuse the Network window's MA-Net Interface with the OSC-page Interface setting"
status: active
source: "MEMORY §Session activation + corrected OSC architecture — MA-Net interface, 2026-05-27 evening, onPC 2.3.2.0 Mac"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The Network window's **`MA-Net Interface`** setting governs which NIC MA3 uses for MA-Net **session** traffic — this is separate from the OSC line's own `Interface` setting (on the SONG_S OSC page).

For loopback dev, **both** should be set to **`lo0 (127.0.0.1)`**.

Reference session from the night this was verified: active session `onPCRack-100380`, Local, IdleMaster status. Session ID: `536dbc23a529e584`.

History: none — standalone note, 2026-05-27 evening.

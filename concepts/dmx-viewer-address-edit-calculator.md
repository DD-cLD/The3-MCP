---
id: dmx-viewer-address-edit-calculator
title: "DMX viewer's Address field opens an Edit Address calculator popup (keypad + Please) to jump straight to a universe.channel"
role: programmer
tags: [ma3, cli, dmx, ui, v2.4]
when_to_load: "Before manually scrolling a DMX viewer to find a specific universe/channel — use the Address field's calculator popup to jump straight there"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Verified live:** clicking the DMX viewer's **Address** field opens an **Edit Address** calculator popup — keypad clicks to enter the target address, confirmed with **Please**. Worked example: entering **202.320** jumped the viewer straight to the JDC block at that universe/channel, confirming the fixture's channel-map position (see `jdc1-anatomy-ground-truth` for the JDC1 SPix channel ranges this lines up against).

History: none — confirmed live in one session, 2026-07-15, while verifying the recipe build's cooked DMX output.

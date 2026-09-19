---
id: release-family-ships-stock
title: "Stock Release color family (predefined_phaser.xml, pool 21) already ships 13+ named color+release presets"
role: programmer
tags: [ma3, inventory, release, v2.4, stock-library]
when_to_load: "Before building release presets from scratch — check whether MA's stock library already covers the needed color"
status: active
source: "findings/INBOX.md, 2026-07-16, console live 2.4.2.2 (predefined_phaser.xml census)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`predefined_phaser.xml` (landed in pool 21 "Phaser" in this show file — see `tourshow-phaser-pool-identity`) contains a full Release color family, shipped stock: **Release White, Red, Orange, Yellow, FernGreen, Green, SeaGreen, Cyan, Lavender, Blue, Violet, Magenta, Pink** (13 named).

⚑ The source finding's list ends with an ellipsis after Pink — treat this as **at least 13, not confirmed exhaustive**; the census wasn't closed out to a hard count.

Dave confirmed live, in the phaser editor, that these are 2-step hard-value pairs (color value + release value baked together) — see `release-preset-design-doctrine` for the exact construction and why our design departs from it.

Practical read: Dave's release-preset "homework" was therefore partly already solved by the prior session's stock import (2026-07-15), before this session's design work even started.

History: none — inventoried 2026-07-16 from a same-session census of `predefined_phaser.xml`.

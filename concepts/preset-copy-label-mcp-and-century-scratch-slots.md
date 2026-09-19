---
id: preset-copy-label-mcp-and-century-scratch-slots
title: "Copy Preset + Label work via MCP; cLD preset scratch slots start at .121 to dodge pool 21's stock occupancy through .113"
role: programmer
tags: [ma3, mcp, presets, pools, v2.4, tourshow]
when_to_load: "Before creating a new custom preset in pool 21 (or copying a stock preset as a starting point) — the verified MCP copy/label lane and the scratch-slot numbering convention that avoids stock collisions"
status: active
source: "findings/INBOX.md line 45, 2026-07-17 [0717-2cLD], console live 2.4.2.2, MCP-driven"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Copy Preset 21.1 → 21.121, then Label**, both executed via MCP — both **OK, verified**.

**Pool 21 stock occupies through slot 113** (see `tourshow-stock-recipe-library-inventory` / `tourshow-phaser-pool-identity` for what's in there). The cLD century convention collides with that range, so **cLD preset scratch slots start at 21.121+**.

**Relation:** this is a pool-21-specific instance of the century-numbering convention referenced in `tourshow-festival-group-theory` (Groups/FID domain) — same shorthand pattern, different pool.

History: none — established live 2026-07-17.

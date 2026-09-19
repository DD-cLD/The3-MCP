---
id: subfixture-cell-architecture-doctrine
title: "Subfixture doctrine (Dave): the bar/master is a SEPARATE handle from the cells; cells live in X/Y physical space (never a bar-stack, never Z unless architectural); linear selections are uniform-only, spatial effects need baked 2D coords"
role: programmer
tags: [ma3, doctrine, subfixture, grid, tourshow, v2.4]
when_to_load: "Before building or programming any multi-cell fixture (ACME pixel lines, JDC1) — how to split the bar-master from the cells, why cells must carry baked X/Y grid coordinates for effects, the no-Z ruling, and which rig types actually carry a cell split"
status: active
source: "findings/INBOX.md, 2026-07-21 [0721cLD], Dave dictated live (paraphrased per dave-dictation-paraphrase-rule)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's settled architecture for multi-cell fixtures, dictated across the 2026-07-21 subfixture session.

**Two layers, NEVER mixed in one group:**

1. **BAR / MASTER** = the whole-strip parent handle (top-level fixture: master dim/strobe/control). The ACME parent geometry "Body" is the bar master; the JDC1 parent splits into a plate master (`.1`) and a beam master (`.2`). The parent **scope** groups (e.g. PIX 301–308) already ARE the bar handles. The bar goes "somewhere else" — it is NOT part of the cell grid.
2. **CELLS** = the individual zones (ACME 48, JDC1 24), where color and effects live. Cells must be laid out in **X/Y PHYSICAL space**. A logical bar-stack tiling is meaningless because a bar's strips sit on multiple different rig parts.

**Linear = uniform-only; spatial effects need baked 2D coords** (Dave course-correction, cLD had missed it): a subfixture group built as a LINEAR/compact dot-range selection (no Grid cursor) is **UNIFORM-VALUE-ONLY** — good for a single color change or a whole-group pop, useless for effects, because a phaser/MAtricks across a linear selection walks selection order, not space. For ANY spatial effect (chase/wave/figure) the cells must carry **2D grid coordinates baked into the Group at Store**. A laid-out group also serves uniform recalls, so it is strictly more capable than the linear one. The six whole-rig linear subfixture groups (320/321 PIX, 420/421 JDC, 1320/1321 PLINE) are kept as the **uniform layer** beneath the per-truss laid-out cell groups.

Two build lanes for the 2D coords: (1) **GridStore (GS)** per fixture type — elegant, but multi-fixture recall is nondeterministic AND the bake does not survive a repatch (see `gridstore-keyword-and-fixture-type-write`, `gs-multifixture-recall-unreliable`); (2) **manual Grid X/Y cursor baked into the Group at Store** — the RELIABLE carrier (Dave: Groups hold, GS does not). See `grid-cursor-cli-recipe-for-2d-group-layouts`.

**Z ruling (Dave, 2026-07-21):** cells are laid out X/Y, layers go in SEPARATE groups, **NO Z stacking**. Z is not worth it for pixel/cell layouts — a separate group programmed right beats Z, and effects on a Z-stacked layout go "willy-nilly." Reach for Z only for genuine architectural / fancy dimensional lighting. This deprioritizes the standing Z-occupancy verify (`subfixture-down-up-cli-navigation-and-grid-stacking`) as a practical matter — Z is not needed, not disproven.

**Which rig types actually carry a cell split** (live handle census, 2026-07-21): ONLY **JDC1** (plate/beam) and the **ACME / STROBE-3-IP pixel lines** (color/beam) carry a functional subfixture split. **Mac Ultra Wash** (2xx, `MacUlWsh`) has 2 subs (main + Instance2, likely an aura ring) — not single-cell, note for wash pixel work. **Robe Pointe** beams (5xx) and **Proteus Lucius** (11xx) are flat, 0 subs.

The physical X/Y cell mapping is a **chosen convention pending warehouse verification** (FID→X direction, top/bottom color rows) — see `acme-pixel-line-ip-anatomy` for why the GDTF cannot supply it. The per-truss laid-out cell groups built this way live in the subfixture layer of `tourshow-group-contract-v01`.

History: none — doctrine dictated live across the 2026-07-21 subfixture session; the linear-vs-laid-out course-correction and the Z ruling both landed the same session.

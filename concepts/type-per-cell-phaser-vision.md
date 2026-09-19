---
id: type-per-cell-phaser-vision
title: "One whole fixture type per grid cell — phasers popping between type-blocks instead of between individual fixtures"
role: design
tags: [ma3, doctrine, grid, phasers, vision, v2.4]
when_to_load: "When designing a phaser or chase across multiple fixture types — consider putting each entire type in one grid cell so the phaser pops type-block to type-block"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's vision for a further variant of cross-type grid grouping: instead of one fixture per grid cell, put an entire fixture TYPE into a single cell — e.g. all spots in cell 1, all JDCs in cell 2, all washes in cell 3 — so a phaser sweeping across the grid pops from one type-block to the next rather than fixture-by-fixture.

This explicitly extends `cross-type-groups-vision` (Dave's signature move of mixing fixture types within one grid group for rhythm figures) one step further: where that doctrine mixes types inside a group, this vision makes each type-block itself the unit of grid time — a whole type becomes one time-column, the same role a single fixture normally plays.

Dave's own framing: "can do it all sorts of ways" — presented as one option among several for building type-based phaser figures, not a single mandated layout.

See `grid-is-a-time-map-doctrine` for the foundational doctrine this vision builds on, and `grid-drill-exemplar-groups-121-124` for the existing worked exemplars of grid group construction this vision would extend into type-block form.

History: none — dictated live 2026-07-15, extending the 2026-07-14 cross-type-groups-vision.

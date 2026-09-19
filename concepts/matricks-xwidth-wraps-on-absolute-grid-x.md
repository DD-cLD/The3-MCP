---
id: matricks-xwidth-wraps-on-absolute-grid-x
title: "MAtricks XWidth re-wrap uses ABSOLUTE grid X position (mod width), not selection order — a non-zero grid origin produces uneven wrapped rows"
role: programmer
tags: [ma3, matricks, v2.4]
when_to_load: "Before applying an XWidth re-wrap to a stored Group — check the group's actual grid X origin first, or a non-zero-origin grid will wrap unevenly; also relevant when deliberately using an XWidth wrap to collapse a sparse aligned multi-row selection into one block"
status: active
source: "findings/INBOX.md, 2026-07-10, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**XWidth re-wrap operates on each fixture's ABSOLUTE grid X coordinate (mod the width value), not on selection/storage order.**

**Observed case:** Group 101 turned out to be stored with fixtures at grid **X = 1..10** (not the expected 0..9 — an off-by-one grid origin baked in at storage time). Applying a **width-5 wrap** against this group produced uneven rows — **(1-4) / (5-9) / (10)** — with an **empty origin cell**, instead of the clean split you'd get from a zero-based 0..9 origin.

**Grid warts persist through group store and survive into transforms.** A grid-coordinate irregularity (like a non-zero origin) baked in when a Group was stored doesn't get normalized away — it silently propagates into any later MAtricks transform (XWidth, and presumably other absolute-grid-coordinate operations) applied to that group.

**Practical rule:** before applying an XWidth re-wrap (or any width/coordinate-based MAtricks transform) to a stored Group, check the group's actual grid X origin — don't assume it starts at 0.

**Open question this raises:** does MAtricks **Phase** distribution behave the same way (absolute grid coordinates) or does it compress to only the occupied cells on a gappy/offset grid? See `matricks-phase-distribution-on-gappy-grids-open-question` (unverified).

**Deliberate use, reframed 2026-07-14 (grid drill session):** the same mod-width wrap behavior, once understood, doubles as a controlled collapse tool rather than just a trap. `Set Selection MAtricks "XWidth" 12` applied to a sparse aligned pair of rows (e.g. two rows built at different step intervals over one shared window) folds both rows into a single 12-wide multi-layer block — Dave's framing: "bring them together." `Reset Selection MAtricks` unwinds the transform cleanly back to the original sparse layout. Same underlying mechanism as the trap above; the difference is knowing the group's grid-X origin going in and choosing the width deliberately.

History: discovered live 2026-07-10 while re-wrapping Group 101 (uneven-wrap trap). Reframed 2026-07-14 as a deliberate collapse tool when the grid origin is known and the width is chosen on purpose — see `grid-drill-exemplar-groups-121-124`.

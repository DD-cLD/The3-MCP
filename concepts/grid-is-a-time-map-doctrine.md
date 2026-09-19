---
id: grid-is-a-time-map-doctrine
title: "The selection grid is a time map — shared column position sets WHEN fixtures react, not just where they sit"
role: programmer
tags: [ma3, doctrine, grid, matricks, v2.4]
when_to_load: "Before designing any selection-grid layout — decide what a shared column should mean in time before choosing grid-cursor moves or a MAtricks re-wrap"
status: active
source: "findings/INBOX.md, 2026-07-14, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The selection grid isn't just a spatial arrangement tool — Dave's core framing is that it's a **time map**: fixtures that share a grid column will react at the same moment when a chase or effect sweeps across X. Column position sets *when*, not just *where*; row (Y) is a separate plane/layer.

There are two ways to arrive at a given shape, and which one you use is itself a decision:
- **Cursor-mode at selection time** — the grid cursor's move mode, chosen live as you select, IS the layout decision. The three modes: **no-move** (stay in the current cell), **new-line** (advance to a new row), and **Append X** (advance along the row) — you compose the time map fixture-group by fixture-group as you go.
- **MAtricks reshape after the fact** — the alternate lane: select fixtures flat with no manual cursor placement, then use a MAtricks width re-wrap/collapse to fold the flat selection into the desired grid shape afterward. Same end state, decided in a different order.

Design purpose: use the grid to make spatially different rig parts (DS/MS/US planes, wings) share ONE clean chase — a single shared timeline — instead of each part running its own siloed effect. Dave's standing preference: **tight beats everywhere-at-once** — a small number of purposeful shared moments reads better than maximal simultaneous spread.

Dave's own framing at the close of the drill arc: "temporal, spatial concept locked in — everything compounds on top of this." This doctrine is the foundation the rest of the 2026-07-14 grid work builds on — see `alignment-pairing-vs-proportional-doctrine`, `grid-mirror-symmetry-doctrine`, and `grid-bounce-pattern`.

History: none — dictated live 2026-07-14, foundational doctrine for the grid drill arc.

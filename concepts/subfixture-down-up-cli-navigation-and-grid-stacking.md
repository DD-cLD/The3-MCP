---
id: subfixture-down-up-cli-navigation-and-grid-stacking
title: "Down/Up navigate into sub-fixtures via CLI; multipart bars stack inside the parent's single grid cell by default — GS changes Down's propagation, dot-range Thru selection is a third lane; Z-occupancy still unverified"
role: programmer
tags: [ma3, cli, v2.4, verify, gs]
when_to_load: "Before programming multipart/sub-fixture bars (e.g. pixel bars) via CLI Down/Up navigation, before trusting that a Z-axis MAtricks set actually separates stacked subs, or before assuming which of the three sub-layout lanes (Down-stack / GS-propagated / dot-range-selected) is in play"
status: verify
source: "findings/INBOX.md, 2026-07-10, console live 2.4.2.2; corroborated by wrap 2026-07-14-console-cli-era-layouts-audit-grouptheory"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Down` works as a pasted CLI keyword** (confirmed OK in command history).

**Verified behavior:** Group 105 (6× Pixel Line ACME) + `Down` → **288 Fixtures Selected = 48 leaf subs per bar** (6 bars × 48 = 288). A second `Down` is a **no-op** (already at the deepest level — there's an implicit `Up` counterpart for navigating back out).

**Sub-stacking rule:** subs do **NOT** spread across the selection grid's X axis — they **stack inside the parent fixture's single grid cell** (the cell display shows a truncated list like `201.1–201.4 + "…"`). Y rows stay empty. This means the one-fixture-one-cell rule from `selection-grid-and-fixture-cell-model` holds at the PARENT level, but multiple leaf subs collapse into that same one cell rather than each claiming their own.

**[VERIFY] Z-occupancy — open question, unresolved as of the 2026-07-14 wrap:** a probe was fired to test whether subs can be separated on the Z axis — `Set Selection MAtricks "Z" 2 ; At Full` (both commands returned OK in command history) — but **visual confirmation never happened**; programmer state was cleared at session handoff before the result could be checked. **Verifies with:** re-fire the same probe on a multipart fixture and visually confirm (screenshot or 3D view) whether the subs actually separate on Z, or whether Z is subject to the same stacking behavior as X.

**Deprioritized 2026-07-21 (Dave's X/Y-only ruling):** Dave has ruled Z out of practical use for pixel/cell layouts — cells are laid out X/Y and any additional layer goes in a SEPARATE group, never Z (Z only for genuine architectural/dimensional work; see `subfixture-cell-architecture-doctrine`). So this Z-occupancy question is now **parked, not blocking** — Z is not needed, not disproven; re-probe only if an architectural Z effect is ever actually wanted.

**Stale cross-reference — 2026-07-14 repatch:** this drill was run against **Group 105 = 6× Pixel Line ACME at FID 201–206** (and Group 104, presumably the JDC1 equivalent at FID 101–104) in the pre-repatch sandbox. The 2026-07-14 template-rig repatch **reassigned FID 101–148 to spots**, overwriting that numbering — **Groups 104/105 are stale** and must be re-pointed at the fixtures they now actually reference before reusing this drill's group numbers. See `tourshow-template-rig-patch-and-layout-state`.

**Three distinct sub-layout lanes clarified 2026-07-15 (multi-instance session):** the `status: verify` on this file is specifically about the Z-occupancy question below — the X-axis behavior is now well characterized across three separate, non-contradictory lanes:
1. **`Down`-expansion, no GS stored** — stacks in the parent's one cell, as described above (the original 2026-07-10 finding).
2. **`Down`-expansion AFTER a `GS` (GridStore) bake** — instead PROPAGATES the stored layout, tiled per fixture, across the grid (see `gridstore-keyword-and-fixture-type-write`). But this propagation is **not always reliable on multi-fixture recall** — see `gs-multifixture-recall-unreliable` for the failure signature and the doctrine that Groups (baked at Store time) are the trustworthy carrier, not GS (2026-07-21: a GS type-bake also does not survive a repatch — a second, independent reason Groups are the durable carrier).
3. **Explicit dot-range `Thru` selection** (e.g. `Fixture 301.1 Thru 16`, no `Down` involved at all) — see `subfixture-thru-range-syntax`. Without `Grid X/Y` cursor guidance this compact-packs onto one row in selection order; paired with Grid-cursor moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`) it lands each sub-range block at its own specified cell. A GS-stored type layout does **not** apply to this lane — GS only engages on `Down`-expansion.

History: none — first run live 2026-07-10; Z-occupancy remains open as of the 2026-07-14 wrap (programmer state cleared at handoff before visual confirm). 2026-07-15: clarified that the stacking rule is the default/pre-GS case specifically, and cross-referenced the two other sub-layout lanes (GS-propagated, dot-range-selected) discovered the same session — Z-occupancy itself still not re-probed. 2026-07-21: Z-occupancy verify deprioritized by Dave's X/Y-only ruling (parked, not blocking); the GS lane also confirmed not durable across a repatch.

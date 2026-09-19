---
id: multi-instance-grid-frontier
title: "Multi-instance/subfixture grid layouts are the next and last selection-grid frontier before recipes"
role: historical
tags: [ma3, grid, roadmap, v2.4]
when_to_load: "Historical/context load: explains why multi-instance (pix/wash subfixture) grid layout was considered the hard remaining piece before recipes, and how it maps onto the concepts that resolved it — `gridstore-keyword-and-fixture-type-write`, `subfixture-thru-range-syntax`, `gs-multifixture-recall-unreliable`. The frontier itself was CROSSED 2026-07-15; load this for the roadmap history, not as an active blocker."
status: active
source: "findings/INBOX.md, 2026-07-14, Dave dictated; wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's framing of what's left on the selection-grid side of the workflow: whole-fixture grid layouts are now solid (see `grid-drill-exemplar-groups-121-124`), but **multi-instance fixtures — pixel and wash subfixtures — laying out on the grid is the harder remaining part**, and the last grid frontier before moving on to recipes (chases/effects built on top of baked Groups).

Dave's reassurance about scope: "once you Grid+Store the fixtures laid out the way you want, everything is fine" — the added intricacy is front-loaded into the layout step itself; once a multi-instance layout is built and stored as a Group, everything downstream (recall, MAtricks, chases) behaves the same as it does for whole fixtures.

Groundwork already banked for this: the `Down`/`Up` CLI navigation into multipart subfixtures and the rule that subs stack inside their parent's single grid cell rather than spreading across X (see `subfixture-down-up-cli-navigation-and-grid-stacking`) — though Z-occupancy for subfixtures is still an open/unverified question there.

**Frontier crossed 2026-07-15:** Dave's live GS drill (Grid-cursor + sub-range dot-syntax, `GridStore`/`GS` baking a layout into the fixture type, `Down`-propagation) took this from open question to "pretty much nailed" (Dave's verdict) in one session — worked on the ACME (48-sub sandwich layout) and the JDC1 (24-sub mirrored-gap layout, GS'd into the type). See `gridstore-keyword-and-fixture-type-write` for the keyword mechanics, `subfixture-thru-range-syntax` for the settled dot-range Thru syntax that made direct per-instance builds possible, and `gs-multifixture-recall-unreliable` for the important caveat banked the same session — GS's multi-fixture Down-recall is not always reliable, so Groups baked at Store time remain the trustworthy layout carrier.

History: none — flagged as the next open frontier, dictated live 2026-07-14 at the close of the grid-drill session. **Frontier crossed 2026-07-15** (see body) — concept kept active as the historical record of what this frontier was and how it resolved, per the 2026-07-15 multi-instance session wrap.

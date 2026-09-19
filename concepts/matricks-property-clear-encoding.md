---
id: matricks-property-clear-encoding
title: "Clearing a MAtricks block/group: assign 0 — m.XBlock=0 / m.XGroup=0 reads back 'None', which IS the clean clear; wings survive, and Copy carries the SOURCE's Name so re-Label after"
role: programmer
tags: [ma3, matricks, lua, v2.4, tourshow]
when_to_load: "Before minting a 'flat' MAtricks twin from a block/group-carrying source — how to clear a property, what the readback should say, and the Copy-carries-the-name gotcha that follows every twin mint"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-2cLD] and [0826-5cLD]/[0828-1cLD] 2026-08-26→28 — twins 210/211/212 at {FESTIVAL}, 216-219 at {FESTIVAL} / {FESTIVAL} / {FESTIVAL}"
supersedes: []
superseded_by: null
---

**The clear:** assign **`0`**.

```lua
m.XBlock = 0
m.XGroup = 0
```

**The readback says `None`** — that is the *correct* cleared state, not a failed write and not a stored zero. Verified on every flat twin minted across four venues.

**Wings and phase survive a block/group clear.** `XWings`, `PhaseFromX/ToX`, `PhaseFromY/ToY` and shuffle are untouched — which is precisely what makes the 1-cell adaptation possible (`mx-cell-geometry-law`: strip the cell geometry, keep the population geometry).

**⚠ Copy carries the SOURCE's Name — always re-Label after.** Minting a twin by `Copy … At <slot>` brings the source's name with it, so the new object silently masquerades as the old one until relabelled. This is the same behaviour proven in the colour pool (`Copy Preset /o /nc` carried the source name into the crowned base — see `color-consolidation-crowning`). **Mint → Label → verify the label reads back** before anything else references it; a stale label is what a later name-lookup will match.

**And verify sources by NAME before copying.** The venue kit's mint step looks its sources up by name rather than slot, because pool labels lie (`pool-labeling-doctrine-inherited-risk`) and slot contents drift between file lineages — at {FESTIVAL} the plain `SHUFFLE 5` source was simply absent from that lineage and had to be minted from a different parent.

**Relation:** `mx-cell-geometry-law` · `matricks-pool-reusability-and-block-structure` · `pool-labeling-doctrine-inherited-risk` · `macro-lua-label-race-needs-wait` (what happens when a later line reads a label the console has not finished writing) · `copy-at-occupied-slot-dialog-trap`.

History: none — clear encoding banked 2026-08-26, re-attested at three further venues through 2026-08-28.

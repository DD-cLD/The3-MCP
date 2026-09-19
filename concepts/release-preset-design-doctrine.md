---
id: release-preset-design-doctrine
title: "Our release-preset pattern: a recipe referencing TWO presets (standing color preset + release preset), not stock's baked hard-value pairs"
role: programmer
tags: [ma3, doctrine, release, presets, v2.4, tourshow]
when_to_load: "Before building a release-color preset — this is the design decision on HOW to build them, distinct from what Release itself does"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session; 3 near-identical captures merged into one concept per librarian duplicate-merge instruction)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Stock behavior (reference point, not our pattern):** pool-21's Release family ships as HARD-VALUE pairs — each preset bakes a color value + a release value together in one 2-step preset. Dave confirmed this live in the phaser editor. See `release-family-ships-stock` for the exact stock inventory.

**Our design:** build release-color presets as RECIPE-style presets that REFERENCE two other presets, instead of baking values —
1. the standing/always-used color preset (the single editable color — one edit point, color authority stays single-sourced), and
2. a release preset.

Editing the standing color preset then propagates everywhere it's referenced, instead of hand-rebaking N hard-coded release presets whenever a color changes.

**Purpose:** this pattern directly serves `tc-bump-button-architecture` — bumps exit via Release, and a recipe-referenced release-color preset keeps that exit color centrally editable rather than duplicated per bump.

**Status:** designed, not yet built — tracked as a console-queue item in `NEXT_ACTIONS_A0716.1.md` ("Build release-as-recipe presets").

History: none — design decided 2026-07-16, captured three times near-identically in the inbox as the session progressed; merged here as one concept.

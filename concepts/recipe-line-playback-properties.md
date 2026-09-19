---
id: recipe-line-playback-properties
title: "Recipe-line playback properties per forum doctrine (PlaybackNShot/PlaybackDirection/PlaybackAdaptiveMeasure/PlaybackAdaptiveWidth/PlaybackAdaptiveXYRotation) — but live 2.4.2.2 doc-correction: PlaybackDirection does NOT exist on a sequence cue-part recipe line, it's a PRESET-phaser-only function"
role: programmer
tags: [ma3, cli, recipes, v2.4, doc-correction, verify]
when_to_load: "Before writing or reading a recipe line's playback properties (nShot, direction, adaptive measure/width/rotation) via CLI — PlaybackDirection specifically does not apply to a sequence cue-part recipe line on 2.4.2.2, despite forum documentation listing it there"
status: verify
source: "findings/INBOX.md, 2026-07-17 — forum 69919; live 2.4.2.2 doc-correction (Dave) [0717-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Forum-documented playback property set (forum 69919):** `PlaybackNShot`, `PlaybackDirection` (`Forward`|`Backward`|`Alternate`), `PlaybackAdaptiveMeasure`, `PlaybackAdaptiveWidth`, `PlaybackAdaptiveXYRotation` — all listed as recipe-line playback properties, presumably via the same `Set ... Property "PropName" <value>` form as other recipe-line properties.

**Live doc-correction, 2.4.2.2 (Dave):** `PlaybackDirection` does **NOT** exist on a **sequence cue-part recipe line**. Playback direction is a **PRESET-phaser** function instead — it rides the phaser **preset** (e.g. `Preset 21.x`), not the recipe line stored in a cue's part. Forum 69919's "Sequence Cue Playback Area" `Set` block, which implies `PlaybackDirection` is settable at the cue-part recipe-line address, **does not hold** on 2.4.2.2.

**[VERIFY]** which version or context the forum's cue-part `PlaybackDirection` form actually worked on (if ever) — unconfirmed whether this is a version regression, a documentation error, or a context the forum thread never actually tested at the cue-part level.

**Practical implication:** the other four playback properties (`PlaybackNShot`, `PlaybackAdaptiveMeasure`, `PlaybackAdaptiveWidth`, `PlaybackAdaptiveXYRotation`) are NOT independently live-verified by this correction — only `PlaybackDirection` has been specifically disproven at the cue-part recipe-line address. Treat the other four as forum-sourced and unconfirmed until independently tested.

History: created 2026-07-17 from the forum-sourced property list, immediately doc-corrected same session by a live finding that one of the five (`PlaybackDirection`) doesn't apply at the address the forum describes — kept together as one concept since both describe the same "what playback properties can I write on a recipe line" surface, and the correction directly narrows the forum's claim rather than standing apart from it.

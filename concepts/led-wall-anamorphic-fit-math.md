---
id: led-wall-anamorphic-fit-math
title: "Fitting 16:9 content to an ultra-wide house LED wall: never let the wall rescale (map 1:1), spend the crop budget top-anchored first, then stretch — and cap the stretch by CONTENT TYPE, not by fill percentage"
role: design
tags: [video, festival, tourshow]
when_to_load: "Before mapping the show's video content onto a house LED wall of unfamiliar aspect — the order of operations, the anamorphic formula, and the ruling that decides how much stretch is allowed"
status: active
verified: EU tour leg 2026-08
source: "findings/INBOX.md [0820-2cLD] 2026-08-20 — house wall 3432×768 against 1920×1080 content; Dave's 20%-max ruling"
supersedes: []
superseded_by: null
---

## Order of operations

1. **Map the output screen 1:1 to the wall's real pixel dimensions.** Never let the wall rescale — the video machine does all scaling, so it is inspectable and repeatable.
2. **Keep the composition at the content's native size** — the deck that was tested under timecode is the deck that plays. Do not re-render for the venue.
3. **Spend the crop budget first, top-anchored.** Crop takes height off the bottom (the top of frame is protected), which raises the effective aspect ratio before any stretch is needed.
4. **Then stretch, within the ruled cap**, and centre the result.

## The math

With the crop budget spent, the anamorphic ratio required for a **full-width** fill is:

```
(wallW / contentW) / (wallH / croppedH)
```

On the attested wall (3432×768 wall, 1920×1080 content, 400 px bottom crop → 680 px of usable content height) that came to **1.583** — rejected outright. The stretch menu computed from it: **0% → 2168 px wide · 20% → 2602 px · 30% → 2820 px**.

**Deployed:** 20% stretch, output rect x=415 y=0 w=2602 h=768 — **75.8% of the wall filled**, with a documented retreat to 10% (w=2385, x=523) if faces read wide in the room.

## ⛔ The ruling that governs the cap

**Dave: 20% stretch maximum — because the artist appears in the content.** The cap is set by **content type, not by fill percentage**. Figurative content (a person on screen) tolerates far less distortion than abstract content; an unfilled wall is a smaller sin than a stretched face. **Ask what is in the clips before computing a fit.**

**Pro option, offered and available:** two layers — a full-width blurred fill underneath, a true-scale hero image on top. Fills the wall without distorting anything.

**Relation:** `resolume-dmx-one-hot-clip-select` · `tourshow-resolume-video-kit-list` · `tourshow-resolume-scope-and-tc-chain`.

History: none — computed, ruled and deployed 2026-08-20.

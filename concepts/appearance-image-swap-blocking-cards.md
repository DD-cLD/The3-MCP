---
id: appearance-image-swap-blocking-cards
title: "Swapping an image on a layout card: the layout element WEARS an appearance, the appearance's Image property holds a handle, and `a.Image = <image handle>` assigns clean — so one appearance + one image pool = a per-song picture that changes itself"
role: programmer
tags: [ma3, layout, appearance, images, lua, showrun, v2.4, tourshow]
when_to_load: "Before building any layout view whose picture must change per song/cue — the indirection (element → appearance → image) is the whole mechanism, and the assign form is proven"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-2cLD] (design + package recon) · [0808-4cLD] (property truth by name census) · [0808-9cLD] (a.Image assign scratch-proven, restored) · [0808-10cLD] (Dave: layout view works) 2026-08-08"
supersedes: []
superseded_by: null
---

## The mechanism

```
layout element  →  wears an Appearance  →  Appearance.Image = <image handle>  →  the picture
```

The layout element is never touched at runtime. **Swapping the appearance's `Image` swaps the card.**

- The image reference property is literally **`Image`**, and renders as `Image <pool>.<slot>` — proven by a property-schema dump, not guessed.
- **`a.Image = <image handle>` assigns clean.** Scratch-proven by cycling an appearance through two images and back, readback exact each time.
- User images live in the **MediaPools image pool**; `ImageMode` (Bar vs Stretch), tint and transparent-back are appearance properties set once at design time.

**⚠ Read the appearance's number from a NAME CENSUS, not from memory.** The build initially targeted the wrong slot; the live name census gave the right one. Pool labels and remembered numbers both lie (`pool-labeling-doctrine-inherited-risk`).

## The per-song lane

A toolbox function takes the song token (defaulting to the `selectedsong` global), **hunts the image pool for a name matching `upper(token)`**, and points the appearance at the hit; **no match = no-op**. Called from the shared song macro, it costs zero per-song code (`automator-tc-architecture`).

**Exact-match law:** the images had to be **renamed to the macro tokens** for the match to run clean — one card's name differed from its token and was renamed, taking the match to 18/18 (`name-token-single-holder-cutover-law`).

## Package notes worth carrying

- The card set was delivered as small PNG8 images in **show order**, with a manifest carrying per-file sha256 and an authority reference. **Show order ≠ track numbering** — two songs were swapped relative to the session's own numbering, which is exactly the kind of mismatch a slot-math error is built on. **Derive slot from the manifest's order, and write the mapping down** (card NN → image slot NN+offset).
- A deliberately blank card is a legitimate entry (blocking not yet authorised); when its content lands, **rebuild that one card and re-import that one image** — the machine is unchanged.
- The manifest's route summaries doubled as the per-song zone progressions used elsewhere in the design work — a package can carry more than its stated payload.

**Relation:** `automator-tc-architecture` · `layout-element-property-names-vs-sheet-headers` · `layout-cli-assign-and-posxy-syntax` · `pool-labeling-doctrine-inherited-risk` · `plugin-code-runs-at-showfile-load`.

History: none — designed, corrected by census, built and verified in show conditions, 2026-08-08.

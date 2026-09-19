---
id: tc-slot-enum-internal-default
title: "TCSlot enum: 255 = Internal (frame readout flips to 'UP'), 256 = Default (readout follows slot 1), 1-8 = explicit slots — the rehearsal/show toggle is two one-line macros over the song TC range"
role: programmer
tags: [ma3, timecode, macro, v2.4, tourshow]
when_to_load: "Before reading or writing a Timecode object's TCSlot, or when building a rehearsal-vs-show clock toggle — the enum is not documented and the automator's own slot must be left out of the sweep"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0812-3cLD] 2026-08-12 — teach-by-diff: Dave set one show to Internal, cLD diffed the full property set against a Default sibling; round-trip scratch-verified both directions before baking"
supersedes: []
superseded_by: null
---

| Value | Meaning | Frame readout |
|---|---|---|
| **255** | **Internal** — the show runs on its own clock | flips to **`UP`** |
| **256** | **Default** — follows the console's timecode slot 1 | reads **`S1`** |
| **1-8** | an explicit slot | that slot |

**How it was found:** Dave set one show to Internal, left the rest default, and said "figure out the parameter." A full property diff of the two objects isolated `TCSLOT`. **Teach-by-diff is a cheap and reliable way to name an undocumented property** — set one object differently, diff it against a sibling.

**Historical read this unlocks:** an inherited fleet sitting at 255 means it was set **Internal**, not "parked at some default." The enum makes an old census legible.

## The toggle

Two macros, **one Lua line each**, looping **only the song timecode range**:

- **`TC Internal`** → 255 on every song show (rehearsal: internal clock, no playback rig)
- **`TC Default`** → 256 on every song show (show: follows Art-Net/LTC on slot 1)

**⚠ Deliberately excluded: the automator TC show and the utility shows.** The automator's slot is its own animal — the same reasoning as its Assert exception (`timecode-assertprevevents-and-goto-seam-controls`).

**Test cycle used:** fire Internal → census 20/20 at 255 → fire Default → census 20/20 at 256 → **restore the one show Dave had set by hand to as-found** (leave-as-found law). Exported to `gma3_library/datapools/macros/` as XML pairs so they travel to any file.

**Relation:** `timecode-assertprevevents-and-goto-seam-controls` · `automator-tc-architecture` · `macro-cli-creation-and-edit-lane` · `many-lines-ride-macros-not-lua` · `tourshow-artist-tc-sheet`.

History: none — decoded, built, tested and exported 2026-08-12.

---
id: beatgrid-session-json-schema-conventions
title: "Beatgrid session JSON conventions: version hardcodes 0.4, suggestedDevice is a single enum value, level/ldnote populate only on moments"
role: tools
tags: [beatgrid]
when_to_load: "Before hand-authoring or generating a beatgrid session JSON file, or before trusting a suggestedDevice/level/ldnote field's shape"
status: active
source: "findings/INBOX.md 2026-07-07 + fleet worker FINDINGS_LOCAL, 2026-07-07 (7 builds, convergent)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Conventions confirmed convergently across the bake-off builders and all six fleet-batch builds (7 builds total, all independently arrived at the same shape):

- **`beatgrid` version string hardcodes `"0.4"`** (source ~line 1768). The loader is tolerant: it only requires `grid` + `events` to be present; `palette`/`stemsets` are optional. (Note: the SONG_G exemplar file predates this and says `"0.3"` — match the *current* `beatgrid.html` source, not an older exemplar file, when the two disagree.)
- **Top-level keys:** `{beatgrid, file, grid, events}`. **`grid` sub-keys:** `{bpm, offset, meter, fps}`.
- **Per-event key set is fixed at 20 keys**, identical whether the event is a region or a moment — verify by programmatic key-diff (`json.load` + set-compare) against a known-good exemplar (e.g. the SONG_G session), not by eyeballing.
- **`suggestedDevice` is a single enum value.** Compound device chains (e.g. "+ Color pump (slow)", "+ Sustain drift") are **presentation-layer only** — they live in cuelist/CSV notes text, never in the JSON field itself.
- **`level` and `ldnote` populate ONLY on `kind:moment` events.** Region events carry `level:""` and `ldnote:""` (empty strings) and `qcue:false`; moment events carry real values and `qcue:true`. Checked with zero exceptions across all 7 builds' full event sets.
- **`category` values must be a subset of `beatgrid.html`'s own `CATS` array**, and **`suggestedDevice` values a subset of its `DEVICES` array** — read both directly from the tool's source (not assumed from memory or from an older doc) before validating a build against them.
- **Moment `startSec` always equals its parent region's `startSec`** — one moment per region is the standard 1:1 pairing in every build examined so far.
- **Outro region convention:** extend the final region to the file's true end, even if the ground-truth kit's stated `music_region` closes earlier, so no unaccounted tail remains — flag this as a boundary-only edit, not a content claim, and confirm the tail is true measured silence (or near-silence) before extending. Mirrors the SONG_G exemplar's own practice.

See `fleet-build-self-verification-checklist` for the full verification method these conventions get checked against, and `beatgrid-tc-carried-cuts-and-seam-gap` / TC math conventions for the timecode side of the schema.

History: none — conventions convergently confirmed across 7 independent builds (2 bake-off + 6 fleet batch), 2026-07-07.

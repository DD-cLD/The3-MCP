---
id: ma3-show-container-format-facts
title: "MA3 .show file container facts (bytes-verified): GMA3 binary object DB, not zip/gzip/XML — cue data unreachable file-side"
role: programmer
tags: [ma3]
when_to_load: "Before attempting to parse, mine, or extract data from an MA3 .show file directly (without onPC) — know what's readable file-side (names/labels via strings) versus what isn't (cue-level values, live in binary tables)"
status: active
source: "findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Verified byte-level against the {FESTIVAL} showfile (`ARTIST_festival_AR_as-received_2026-07-06.show` — see `tourshow-showfile-intake-ritual`):

- **Magic `"GMA3"` at offset 0.** The container is a **binary object DB** — **NOT** gzip, zip, or an XML surface.
- **Names/labels are readable via a strings sweep** — 615k strings recovered from this file.
- **251 embedded PNGs** found in this file (counts are per-file, not a fixed constant — expect variation by show).
- **Sporadic zlib buffers are binary tables, not XML** — don't assume a zlib hit means readable structured text.
- **Cue-level data is unreachable file-side.** The real extraction path is **onPC + XML pool exports.**
- **Extension was `.show`, not `.show3`** — content is MA3 regardless of the extension actually used.

History: none — recorded 2026-07-06, from strings-sweep + byte-offset inspection of the {FESTIVAL} file (see `festival-showfile-save-lineage` for what the names layer revealed, and `festival-rig-fixture-inventory-strings` for the rig-string mining that used this same method).

---
id: jdc1-anatomy-ground-truth
title: "JDC1 anatomy ground-truth: 24 subs = 12 plate pixels (2×6 RGB) + 12 tube segments (white); SPix ch21-56 plates, ch57-68 tube — full map in JDC1_SPIX_MAP_v0.1.md"
role: programmer
tags: [ma3, jdc1, gdtf, patch, v2.4]
when_to_load: "Before addressing individual JDC1 subs/channels by hand — read the full channel map in WORKING/JDC1_SPIX_MAP_v0.1.md first; this concept is the pointer + headline facts, not the full table"
status: active
source: "findings/INBOX.md, 2026-07-15 — GDTF (extracted from MVR export) cross-checked against the official GLP manual, both agree; console 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Cross-verified from two independent sources that agree:** the GDTF pulled out of the MVR export (see `patch-mvr-export-import-lane-and-schema` for how every patched fixture type's `.gdtf` is embedded there) and the official GLP manual.

**Headline anatomy:** 24 subs total = **12 plate pixels** (2 rows × 6, RGB — "1st Plate" = subs 1–6, "2nd Plate" = subs 7–12) + **12 tube segments** (white, no color mixing).

**SPix channel ranges:** channels 21–56 = the plate RGB pixels; channels 57–68 = the tube segments.

**Open point carried with the anatomy, not yet resolved:** channel 7 carries **pixel-orientation inversion flags** (an "all" inversion and a "2nd-plate-only" inversion) — mirroring for a symmetric layout can be done either in the FIXTURE's own channel/orientation setup or in the GRID layout itself; the anatomy data doesn't dictate which lane to use, that's a pending pick.

**Full map:** the complete sub-by-sub / channel-by-channel table lives in `WORKING/JDC1_SPIX_MAP_v0.1.md` — load that file directly for the full detail; this concept is intentionally just the pointer plus the headline facts, not a duplicate of its tables.

**Related but distinct (2026-07-16):** this concept is the fixture's channel/sub *anatomy*. A separate question — how those channels *gate* each other — turned out to have a gap: the same GDTF declares no relation for plate/beam master gating over cells, only per-cell virtual dimmers. That's a different fact about the same profile; see `jdc1-gdtf-no-gating-relations-root-cause` (and `jdc1-output-gated-chain` for the real, non-viz gating levels: fixture master × plate master × cell).

History: none — anatomy dug out and cross-verified live in one session, 2026-07-15, immediately put to use for the JDC1 GS grid layout that session. 2026-07-16: cross-referenced the separately-discovered GDTF gating-relations gap (see body) — anatomy facts here unchanged.

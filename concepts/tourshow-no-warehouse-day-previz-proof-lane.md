---
id: tourshow-no-warehouse-day-previz-proof-lane
title: "RULED: there is NO warehouse day — MA3 3D previz run against timecode audio is the proof lane before first load-in, and JDC1 viz stays untrustworthy so the DMX viewer is readback truth"
role: operational-live
tags: [tourshow, schedule, previz, process, ruling, proof-lane]
when_to_load: "Before scheduling, deferring, or gating ANY verification item to 'warehouse day' — that day does not exist on this tour's plan; also before trusting onPC visualization during a previz proof pass"
status: active
source: "findings/INBOX.md [0730cLD] 2026-07-30 (Dave, dictated ruling)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's ruling, 2026-07-30: no warehouse day.** The tour goes straight to **first load-in**. The proof lane before that is **MA3 3D previz run against the timecode audio** — which is exactly how SONG_T and SONG_A were both confirmed, so the method is already exercised, not aspirational.

**This supersedes the show packet's "warehouse proof day, before 2026-07-31" milestone** and every verify item parked against it.

## What that re-homes

Items previously gated on warehouse day go to **previz where the answer is visible there, else load-in day**:

- ACME pixel-line **cell-convention verify** (FID->X direction, top/bottom colour rows) — `acme-pixel-line-ip-anatomy`
- JDC1 **ch8-vs-ch20 hardware gate** question — `jdc1-standing-order-plate-master-full`
- **Palette-lock** session and **fixture-colour pre-match** — `tourshow-warehouse-day-fixture-color-prematch`

## ⚠ The caveat that rides with the lane

**JDC1-class visualization is structurally untrustworthy** — its GDTF declares no relation for plate/beam master gating, so onPC cannot render the real gate chain in either direction (`jdc1-gdtf-no-gating-relations-root-cause`). During a previz proof, the **DMX viewer** — or the real unit at load-in — is the readback truth for any multi-instance output judgement. Previz proves timing, structure and the shape of a look; it does not prove JDC1 output.

**Consequence for every remaining build:** each song has to arrive *previz-provable* — TC track re-targeted and audio offset clean — because there is no physical rig between now and the first look.

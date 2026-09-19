---
id: patch-mode-census
title: "Patch DMX-mode census (cld_patch_v2.xml): JDC1=SPix ×118, MacUlWsh Mode 0 ×64, MACEncPerCLD Basic ×64, Lucius Extended Pan630 ×10, BMFL Mode 1 ×6 — fixture-TYPE index ≠ FID century"
role: programmer
tags: [ma3, patch, v2.4]
when_to_load: "Before assuming a fixture type's DMX mode/personality from its FID range, or before reasoning about total instance counts per fixture type across the whole show (overhead + House/floor combined)"
status: active
source: "findings/INBOX.md, 2026-07-15, from cld_patch_v2.xml, console 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Census, from `cld_patch_v2.xml`:**
- **JDC1 = SPix (68CH) × 118** — explicitly **NOT** Mode 13 (that mode number belongs to the ACME PIXEL LINE × 100, a different fixture type).
- **MacUlWsh (MAC Ultra Wash) Mode 0 × 64** — has `[Instance2]` subs.
- **MACEncPerCLD (MAC Encore Performance CLD) Basic × 64.**
- **Lucius Extended Pan630 × 10.**
- **BMFL Mode 1 × 6.**

**Cross-check:** the 64-count entries match the template rig's overhead spot (MACEncPerCLD, FID 101–164) and wash (MacUlWsh, FID 201–264) categories one-for-one; the Lucius (10) and BMFL (6) counts match the House/floor folder's unpositioned fixtures exactly (see `tourshow-template-rig-patch-and-layout-state`). JDC1's 118 = the overhead JDC (64, FID 401–464) plus the House/floor JDC1 (54) — the two JDC populations summed.

**The rule to hold onto:** **fixture-TYPE index (the mode/personality slot a type is patched under) is NOT the same number space as FID century** (the hundreds-digit convention used for FID ranges/century-numbering schemes — see `tourshow-festival-group-theory` for a related but distinct century-numbering cross-check, that one about Group numbers vs. FIDs). Don't conflate the two when reasoning about the patch.

History: none — census pulled live from the patch XML in one session, 2026-07-15.

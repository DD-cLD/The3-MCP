---
id: tourshow-group-contract-v01
title: "Group Contract (v0.3): Group# = FID century + scope slot, 28×4 frame/category; her-key carveout = Group 51 (FID 51-54, re-FID'd for rig-position identity); backlight Groups 60-64 (FID 55-60, MVR-ratified membership); + the subfixture cell layer — built + census-verified"
role: programmer
tags: [tourshow, v2.4]
when_to_load: "Before creating, numbering, or recalling any template-rig or subfixture-cell Group, before touching the her-key or backlight FID/group blocks (51-60), or before assuming Groups 101-110 still include FID 55-60 after the 2026-07-23 carve"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], Dave-delegated design (\"you're the one that's gonna be using them\"); ARTIST_TOURSHOW_GROUP_CONTRACT_v0.1.md; her-key rationale + backlight arc extended findings/INBOX.md 2026-07-20 (07-20 bridge), 2026-07-22/23 [0722-2cLD], 2026-07-23 [0723cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Numbering — one arithmetic rule, no lookup needed:** Group number = **FID century + scope slot**. Same ten ones-digits in every category century:

| ones | scope | members |
|---|---|---|
| x01 | ALL (full 2D frame) | 64 |
| x02 | DS row | 12 |
| x03 | MS1 row | 12 |
| x04 | MS2 row | 12 |
| x05 | US row | 12 |
| x06 | WINGS both | 16 |
| x07 | WING SR | 8 |
| x08 | WING SL | 8 |
| x09 | HALF SR (movers only) | 32 |
| x10 | HALF SL (movers only) | 32 |

Centuries mirror the FID patch exactly (Dave's ruling, see `tourshow-festival-group-theory`): **1xx SPOTS · 2xx WASHES · 3xx PIX · 4xx JDC · 5xx BEAMS**. Halves (x09/x10) exist only for the pan/tilt-capable categories (spots/washes/beams — 1/2/5). Labels follow `cLD <CAT> <SCOPE>`.

**6xx composites (members-only, compact grid — MAtricks does the shaping, not the grid):** `601 cLD AIR ALL` (v0.2: **252** with her-key 51–54 excluded, **316** with beams folded in — was 256/320) · `602 cLD MOVERS` (v0.2: **124**, key-excluded, rebuilt with beams like 601 — was 128/192) · `603 cLD FX` (pix+JDC, 128) · `604 cLD POP` (JDC+beams, 128 — beams-macro only). **601/602 were explicitly NOT extended the backlight carveout on 2026-07-23** (see the CARVE ruling below) — Dave's call, key-precedent symmetry not extended this round; treat 601/602's FID 55-60 membership status as current/unchanged unless a future ruling says otherwise.

**The frame — identical shape stamped per category:** X spans **0–27** (SR wing outboard→in 0–7, main truss 8–19, SL wing in→outboard 20–27, mirror seam between columns 13/14); Y spans **0–3** mapping DS→US. **Wings ride Y0** — same plane as DS (Dave's ruling, 2026-07-18: wing Y = 0). All coordinates stay **≥ 0** by design; negative grid coordinates are unverified on the CLI, so the frame is shifted rather than centered on zero. This 2D frame is exactly what makes whole-category POSITION WIZ runs able to depth-grade Blind — see `tourshow-position-wiz-blind-depth-grade-root-cause`.

**Stale groups resolved:** Groups 104/105 (stale since the 2026-07-10 multipart drill — see `tourshow-template-rig-patch-and-layout-state`) are deleted and re-pointed as SPOTS MS2/US by the builder macro, closing that flag. Grid-drill exemplars 121–124 and the JDC set 128–130 (125–127 empty) are left untouched by the contract.

**v0.2 her-key carveout (Dave ratified 2026-07-21):** her key group is **Group 51 `cLD {ARTIST} KEY`** (group number from FID-block arithmetic, deliberately below 100 on Dave's side of the pool; her four key spots are FID 51–54). **FIDs 51–54 are EXCLUDED from `601 AIR ALL` and `602 MOVERS`** — the key is carved out of the programmable field at the GROUP level, so any look that includes her references Group 51 deliberately. The contract builder was regenerated to carve out 51–54, leaving DS-row rests at grid X10/12/15/17 (the positions the four key spots used to occupy — authored rests, see `gap-is-a-rest-doctrine`); sim census PASS; the regenerated builder XML supersedes the pre-swap one.

**Re-FID rationale (07-20 bridge, Dave, dictated) — why 51–54 and not new units:** the four original candidates (FID 103/105/108/110) were chosen for their **RIG POSITIONS**, not their serials — the hang points those FIDs sat at make the pictures on her that Dave wants her key coming from in the show. So the key block's identity is **four positions in the rig**, not four fixture serials; re-FID'ing preserves that identity (on a house rig, spread-fill would pick the units nearest those same hang points). This is what decided Option A (re-FID 103/105/108/110 → 51–54) over Option B (add four new units at 51–54): keys are carved from the real rig, not added to it. Patch executed 2026-07-21; 103/105/108/110 vacated.

**Per-song fluid key layer (Dave, 07-21, dictated — supplements the fixed 51-54, does not replace it):** beyond the fixed her-key block, some fixtures per song may stay SOLID on her (not chase) depending on where she is on stage, or a couple as additional {ARTIST} specials — a per-song adjustable layer, not fixed doctrine. Lives alongside the manual-reserve handle (see below).

**Spares / manual reserve — CLOSED, no group slots reserved.** No manual-reserve layer exists in the show file, so the contract allocates nothing for it. Full ruling and the superseded 07-20 proposal: `tourshow-spares-no-manual-reserve-ruling`.

**v0.3 backlight Groups 60–64 (FID 55–60) — proposed 2026-07-22, RATIFIED from MVR geometry 2026-07-23:**

- **Origin:** backlight fixtures = **FID 55–60**, six units spread across the upstage catwalk/riser, siblings to Group 51 on Dave's side of the pool (below 100, outside the cLD 101+ namespace). Design rule these groups serve: whenever her key runs saturated/semi-saturated color, the white backlight must be ON so she still reads — see the design-side doctrine and position-based fixture picks in `tourshow-her-key-and-backlight-doctrine`.
- **Physical map (MVR `cld_patch_v4`, verified 2026-07-23):** FID 55 = unit30, MS2, Y+6 X−0.6, SR-inner · 56 = unit31, MS2, X+0.6, SL-inner · 57 = unit39, US, Y+9 X−4.2, SR-outer · 58 = unit41, US, X−1.8, SR-mid · 59 = unit44, US, X+1.8, SL-mid · 60 = unit46, US, X+4.2, SL-outer. All **MAC Encore Perf CLD**, Z+8.
- **Penciled-then-corrected:** the first dictated proposal (contiguous ranges: 61 BL SR=55-57 / 62 BL SL=58-60 / 63 CTR DS=57+58 / 64 CTR US=56-59) was **geometrically WRONG against the MVR** — a contiguous-range guess, not a geometry read. Superseded in-body, not deleted.
- **RATIFIED membership (Dave, from MVR geometry, 2026-07-23) — current truth:** **G60 `cLD BACKLIGHT ALL`** = 55-60 (the widener) · **G61 `cLD BL SR`** = {55, 57, 58} · **G62 `cLD BL SL`** = {56, 59, 60} · **G63 `cLD BL CTR DS`** = {55, 56} (the MS2 pair) · **G64 `cLD BL CTR US`** = {58, 59} (tight US inner pair). This supersedes the dictation-era contiguous ranges everywhere they appear, including in `SONG-E_BUILD_NOTE` / `SONG-E_BINDING_TABLE` prose — those docs still carry the old ranges as of 2026-07-23 and are owed a docs round-trip (cLD's, not the librarian's).
- **Proven idiom used to build these:** `Store Group 60 "cLD BACKLIGHT ALL"` (inline name, no separate Label line — see `macro-xml-schema-cracked`'s quote-dialect fix, since Label lines are exactly where the quote-truncation bug bites).

**CARVE ruling (Dave, 2026-07-23) — purge FID 55-60 from the spot contract:** because these six units were **re-FID'd FROM 130/131/139/141/144/146** (originally MS2/US-row spots inside the 1xx contract), and **group membership follows the fixture OBJECT through a re-FID, not the FID number** (see `group-membership-follows-refid-not-number`), they silently remained members of `G101` (ALL spots, showed 60 incl. 55-60), `G105` (US row, showed 57-60 present), and `G601` (AIR ALL, showed 316 incl. all six) after the re-FID. Dave ruled: **purge FID 55-60 from the FULL spot contract block, Groups 101-110 (ALL/rows/wings/halves)** via `Store Group <n> /Remove` on each, export-census-verifying each group afterward. **601/602 were explicitly LEFT AS-IS this round** — the her-key (51-54) precedent of excluding from 601/602 was **NOT extended** to the backlight block; that's Dave's call, not an oversight, and it means 601/602's current census (252/124 etc., above) may still include 55-60 pending a future ruling.

**v0.2 subfixture cell layer (built + census-verified, v0.23→v0.24):** on top of the contract categories, the multi-cell fixtures (ACME pixel lines 3xx/13xx, JDC1 4xx) got a full cell-group layer. Numbering, by scope:
- **Uniform layer** (whole-rig, membership only — the uniform tier of `subfixture-cell-architecture-doctrine`): `x20` = color/plate, `x21` = beam/tube → **320 PIX COLOR / 321 PIX BEAM · 420 JDC PLATES / 421 JDC TUBES · 1320 PLINE COLOR / 1321 PLINE BEAM**.
- **Laid-out per-truss cells** (2D grid coords baked, effect-capable): color **32x**, beam **34x**, plate **42x**, tube **44x**, by scope DS/MS1/MS2/US → **322–325 PIX COLOR · 342–345 PIX BEAM · 422–425 JDC PLATE · 442–445 JDC TUBE** (JDC groups 144 members each; 322 DS COLOR verified 384 members, X0–191, 192@Y0 + 192@Y1). Floor: **1322/1323 (BAND/UPPER COLOR) · 1342/1343 (BAND/UPPER BEAM)**.
- **JDC masters** (must be ON for any cell output — see `jdc1-standing-order-plate-master-full`): **426 cLD JDC PLATE MASTER** (`401 Thru 464.1`) · **446 cLD JDC BEAM MASTER** (`401 Thru 464.2`).
- **Dave's hand-built full-rig combined GRID pictures** (whole-rig versions of the per-truss cells; Dave-authored — verify existence, do NOT rebuild): **334 cLD PIX COLOR GRID · 335 cLD PIX BEAM GRID · 434 cLD PLATES GRID · 435 cLD(C) TUBES GRID** (note the BEAM-vs-TUBE label split, see `beam-not-strobe-terminology`).
- **Floor scope/composite groups** also built: **1101 Lucius · 1301–1303 P-Lines** (Fourline v11 numbering; see `tourshow-floor-package` for the full floor FID scheme, extended to 1304-1309 upper-deck).
The uniform layer is kept beneath the laid-out cells; a laid-out group also serves uniform recalls (strictly more capable). The physical X/Y cell mapping is a chosen convention pending warehouse verification — see `acme-pixel-line-ip-anatomy`, `subfixture-cell-architecture-doctrine`.

**Implementation — two builder macros generated, self-verified; contract + subfixture layers BUILT + census-verified (v0.23→v0.24):**
- `cLD_GROUP_BUILDER.xml` — 39 main groups, deployed to `gma3_library/datapools/macros/`.
- `cLD_GROUP_BUILDER_BEAMS.xml` — 13 more groups (including a 601/602 rebuild to fold beams in, plus 604 POP), gated behind the beam patch (FID 501–564, see `tourshow-template-rig-patch-and-layout-state`) landing first.

Generation self-verified: member census matches this contract exactly, XML valid, no batching, all coordinates ≥ 0. **Desk process (was v0.1-pending; RUN in v0.23→v0.24):** empty-slot census on Groups 101-110/2xx/3xx/4xx/6xx first (an occupied slot stalls the macro on a popup — only 104/105 are pre-deleted), import via `ChangeDestination Macro` → `Import Library "cLD_GROUP_BUILDER.xml"` → `ChangeDestination Root`, fire it (~4 min of stores), then `Export Group` census-verify 101/109/601 against the member table above. The contract layer (40 scope+composite groups + 13 beam groups + 4 floor groups) plus the full subfixture cell layer above are now built and census-verified in v0.24 — Dave also built the full-rig GRID pictures from the cells himself. Wings (pixel 349–364, JDC 449–464) deferred — Dave said add wings later.

**Status:** the subfixture cell layer queued in v0.1 is now BUILT (see the v0.2 section above) — done via the reliable Grid-cursor-baked-into-Groups lane, NOT GS (GS bakes didn't survive the v11 repatch; see `grid-cursor-cli-recipe-for-2d-group-layouts`, `gs-multifixture-recall-unreliable`). Still deferred: pixel/JDC **wing** cell groups (349–364 / 449–464), Dave said add later. Gesture-layer groups (Bank D — see `tourshow-gesture-groups-on-demand-doctrine`) get a suggested home at century **7xx**, labeled `cLD GESTURE <name>`, once actually built. The old v2 idea of baking the 6xx composites with grid **Z** as a category layer is **dropped** — Dave ruled cells are X/Y only, layers go in separate groups, no Z (see `subfixture-cell-architecture-doctrine`). **NEW v0.3 status note (2026-07-23):** the backlight block (Groups 60-64) is RATIFIED and the spot-contract CARVE (101-110) is ruled — both owed a desk re-fire/verify pass; a smith proof-run already confirmed the ratified backlight membership is EXACT in the authored foundation XML (`cLD_ST_FOUNDATION.xml` v0.1.3) ahead of that desk pass.



## ⛔ CORRECTED 2026-07-31 [0731cLD] — the JDC chain-opener group numbers above are STALE

**Live desk-clear read, 2026-07-31:** the JDC master groups are **415 `cLD JDC PLATE MASTER`** and **422 `cLD JDC BEAM MASTER`**. **426 and 446 are EMPTY.** The "426 PLATE / 446 BEAM" numbers in the v0.2 subfixture-cell-layer section above are wrong and must not be used — `CROSSWALK_CHEAT_SHEET_v0.1.md` and `generated/crosswalk_prep/SUBMAP.md` already carried the correct pair. SONG_A's Mark cue ships `cLD JDC PLATE MASTER` + `cLD JDC BEAM MASTER` as its gate-openers on this basis (see `tourshow-seq1010-build-record`).

**⚑ FLAGGED, NOT FIXED — the 4xx block looks renumbered wider than this one pair.** This file's own arithmetic defines **422 as `cLD JDC PLATE DS`** (the `42x`-by-truss cell scheme), which collides with the live read; and the cheat sheet reads **416/417 = PLATES/TUBES GRID** where this file's arithmetic says 434/435. A full live 4xx census is owed before any other number in this file is trusted. Do not auto-resolve — surface it.

**⚑ SEPARATE, SAME SESSION — the arithmetic describes the SANDBOX, not the inherited file.** In `EXAMPLE_SHOW gov bal_cLD`, cLD's contract groups sit **relocated**: `cLD SPOTS ALL` is **Group 181**, not the predicted 101 — slot 101 there is {LD}'s `PL FL [RGBMM] (Grid)`. Every bind cLD authors into that file is **name-form** for exactly this reason. Treat the century arithmetic as the design of the clean sandbox; in an inherited file, read the live name. See `inherited-file-membership-is-ground-truth`.

History: v0.1 designed 2026-07-19; **v0.2 landed 2026-07-21** — added the her-key carveout (Group 51; 51–54 excluded from 601/602) and the full subfixture cell layer (uniform x20/x21; laid-out color 32x/beam 34x/plate 42x/tube 44x; masters 426/446; Dave's full-rig grids 334/335/434/435), all built + census-verified in cLD_SANDBOX v0.23→v0.24. Original v0.1 note: contract designed and both builder macros generated in the 2026-07-19 session, Dave-delegated ("lay it out the way that makes sense for you... you're the one that's gonna be using them"). **Extended 2026-07-20 (07-20 bridge):** added the re-FID rig-position rationale for Group 51 (why 103/105/108/110 → 51-54) and the per-song fluid key layer note; recorded (then 07-22-superseded) the original manual-reserve proposal. **Extended 2026-07-22/23 ([0722-2cLD]):** spares/manual-reserve question CLOSED (no such layer exists — physical spares, unpatched); backlight Groups 60-64 (FID 55-60) proposed with contiguous ranges. **v0.3 landed 2026-07-23 ([0723cLD]):** backlight physical map MVR-verified, penciled contiguous ranges found geometrically wrong and corrected, final membership RATIFIED from geometry; CARVE ruling purges FID 55-60 from the 101-110 spot contract block (601/602 explicitly not extended the same treatment). 2026-07-31 [0731cLD] — chain-openers corrected 426/446 -> 415/422 from a live console read; wider 4xx renumber flagged for census; relocated-groups caveat added from the SONG_A build.

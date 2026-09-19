---
id: tourshow-festival-group-theory
title: "ARTIST_FESTIVAL_GROUP_THEORY_v0.1 (all PROPOSED): template rig as a mold, SPREAD-FILL of FID role slots replaces fixture cloning, Groups=WHO/MAtricks=HOW, century numbering, Bank D gesture vocabulary"
role: design
tags: [tourshow, verify]
when_to_load: "Before adapting the template festival rig to a new festival's actual fixture count, before building any Group/MAtricks numbering scheme for the template show, or before drafting Bank D composite gestures — this whole doctrine is Dave-authored but still PROPOSED, not ratified"
status: verify
source: "findings/INBOX.md, 2026-07-10 (architecture seed + ARTIST_FESTIVAL_GROUP_THEORY_v0.1.md summary + rig spec); wrap 2026-07-14-console-cli-era-layouts-audit-grouptheory"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Status: all PROPOSED** (Dave's own doc status on `ARTIST_FESTIVAL_GROUP_THEORY_v0.1.md`). A ratify pass is still pending — the wrap tracks it as "group-theory ratify list (§7 — numbering, composites, understudies)."

**The architecture (seed, 2026-07-10):** a generic festival rig template — truss positions **DS / MS1 / MS2 / US / wings / (audience)** + floor package; each truss carries **category slots** (spots, washes, strips, strobes). Per-festival adaptation = **Clone fixture info into house fixtures + re-grid the groups** — sequences bind to **group numbers only** (groups are the API, not raw fixture IDs). Workflow order: Dave builds the **layout/plot first** (his own custom visual style, not Vectorworks; can carry GDTF + real locations) → **THEN** the group contract skeleton + numbering conventions get drafted together → **THEN** gesture programming (1-2-3 chases, bump-bump-pop). The **contract doc is deferred** until his layout lands. This is explicitly meant to **evolve, not be fixed from song one**.

**The theory (v0.1 written same day, more developed):** the template rig = a **mold**; festivals "pour in" via **SPREAD-FILL of FID role slots** (allocated by **stage position**, never sequential) — this **replaces fixture-to-fixture cloning** and survives selective-group programming.

- **Groups=WHO, MAtricks=HOW** — odd/even/buddies groupings are **MAtricks**, never stored Groups.
- **Century numbering, FID↔Group — CORRECTED 2026-07-18 by Dave's ruling (see below):** **century = CATEGORY**, and the **truss position blocks repeat inside every century**. `1xx`=spots, `2xx`=washes, `3xx`=pix/linear, `4xx`=JDC1/strobe, `5xx`=beams (Pointe class, added 2026-07-18); within each century, `01-12`=DS, `13-24`=MS1, `25-36`=MS2, `37-48`=US, `49-64`=wings (49-56 SR, 57-64 SL). The v0.1 doc's original line — `1xx`=DS, `2xx`=MS1, `3xx`=MS2, `4xx`=US, `5xx`=SR, `6xx`=SL, tens=category — is **superseded**; `ARTIST_FESTIVAL_GROUP_THEORY_v0.1.md` itself still carries the old wording and needs a Dave edit pass.
- **Bank D composites = gesture vocabulary:** SPINE / FRAME / WALL / CANOPY / CORRIDOR / HALO / JAB / CURTAIN.
- **Density loads:** FEATURE / FIELD / TOTAL + WASH-LOW — **one TOTAL per song, max.**
- **Truss collapse order:** MS2→MS1 first; DS and US keep their identity longest.
- **Understudy chains** cover missing categories (a smaller festival rig without some category borrows/chains to a neighbor).
- **Enabling mechanic:** "recipes-not-values" — the v2.4 rebuild thesis (build recipes that recompute per-rig, rather than hardcoded per-rig values).

**Concrete rig spec (large end of expected festivals):** 4×50' trusses (DS/MS1/MS2/US) × 12 each of spot/wash/JDC1/ACME pixel line + wings 8+8 per category = **256 house + floor package**. Adaptation must scale **DOWN** gracefully from this ceiling.

**[VERIFY] Clone syntax:** `Clone Fixture X At Y` semantics on 2.4.2.2 have **not been live-verified** — this is the literal mechanism behind "per-festival adaptation = Clone fixture info into house fixtures," so it needs a live-verify drill before the template show actually relies on it (queued 2026-07-10, not yet run as of the 2026-07-14 wrap).

**✅ RESOLVED 2026-07-18 (Dave, direct ruling) — was a librarian ⚑ open cross-check.** The flag asked whether the century scheme (read as one-century-per-truss) could be reconciled with the as-patched FIDs, where spots for all four trusses sit consecutively in **101–148**. Dave's answer: there was never a conflict — **"the way that they're patched is the way that I was expressing the grouping."** Century = category; the position blocks repeat inside each century (101–112 DS spots, 113–124 MS1 spots, 125–136 MS2 spots, and so on, then the same shape again for washes at 2xx, pix at 3xx, JDC1 at 4xx). The misread was in the transcription of the v0.1 doc, not in the patch. This also closes the "likely-but-unconfirmed" wash/pix/JDC sub-range mapping noted in `tourshow-template-rig-patch-and-layout-state` — it repeats identically for every category.

**Category vocabulary (Dave, 2026-07-18):** a rig is programmed in the order **SPOTS → WASHES → BEAMS → STROBE → LINEAR**. The template rig was built without a **BEAM** category (Robe Pointe / Sharpy class — "pointies"); it gets the same position-block treatment at the next free century, **FID 501+**. Note the conceptual build order and the numeric century order diverge here: beams are third conceptually but land at 5xx because 3xx/4xx were already assigned to pix and JDC1.

History: none — architecture seeded and the v0.1 doc written same session, 2026-07-10; rig-spec and Clone-syntax gap recorded same day. Century-vs-FID cross-check flagged by the librarian, 2026-07-14 run, not yet resolved.

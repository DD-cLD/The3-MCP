---
id: tourshow-global-preset-portability-verify-items
title: "⚠ VERIFY (data-loss class): GLOBAL preset data reportedly anchors to a real fixture, not the fixture type — can be silently lost on a rig move; countermeasure = Save-Presets-To-FT (untested); posture scoped to careless fixture deletes"
role: programmer
tags: [tourshow, verify, ma3]
when_to_load: "Before trusting a GLOBAL/universal preset (including any POSITION_WIZ-produced preset) to survive a rig clone or fixture swap — also the home of the (untested) Save-Presets-To-FT portability countermeasure and Dave's 2026-07-21 scoped posture (don't over-gate routine work)"
status: verify
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], practitioner reports via world-practices research intake (ARTIST_TOURSHOW_WORLD_PRACTICES_v0.1.md, 27-source pass)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Three practitioner-reported MA3 portability gotchas surfaced by the world-practices research pass (see `tourshow-world-practices-research-intake` for the pass's overall status), all **unverified against our own console** as of this session:

1. **⚠ GLOBAL preset data anchor risk (the one that matters most here):** practitioners report GLOBAL preset data anchors to a REAL, specific fixture rather than to the fixture TYPE — meaning it can be **silently lost** when a rig is cloned or a fixture is swapped/moved. This touches our own universal position presets directly — everything `factory-position-wiz-anatomy-and-porting` and `cld-position-wiz-generic-v01-authored-and-deployed` produce is exactly this kind of GLOBAL/universal preset. **Verify this before trusting the WIZ universals to survive a clone onto a different physical rig** — desk-test a clone/swap and confirm the preset data actually follows the fixture type, not just the original fixture.
2. Converted MA2 profiles reportedly can't travel via MVR.
3. "Stomp" is reportedly no longer an attribute-level technique in MA3 the way it was busked in MA2.

None of these three are adjudicated or desk-verified yet. Citations for all three live in `ARTIST_TOURSHOW_WORLD_PRACTICES_v0.1.md`. Adjudicate and desk-verify before promoting any of them to a hard rule or an active concept.

**Posture update (Dave, 2026-07-21) — scoped, drops out of routine gating:** do NOT let this flag over-gate normal work. It only bites when fixtures are deleted from the patch carelessly; we run backups/checkpoints, and Dave will explicitly call it out when we are actually in could-lose-data territory. Stays `status: verify`, but no longer gates routine programming.

**Designed countermeasure (Dave, UNTESTED in MA3 — verify before leaning on it):** preset data does not persist into the fixture type unless deliberately saved there. Portability lane: **Save Presets To Fixture Type → Export the fixture type** (carry it anywhere) **→ reimport on the target rig → Show Creator setting "Create Presets from FT"** regenerates the presets. Per Dave this mechanism has existed since grandMA v1. This is the designed answer to the anchoring concern above and a candidate lane for the inheritable {ARTIST} file. Sandbox-test queued for AFTER SONG_G programming; patch stays intact until then.

**Messy field alternative (Dave, context):** many show files carry a "DO NOT DELETE" folder holding one unpatched fixture type — keeping the anchor FT resident in the show so global preset data survives, and grabbing a fixture from it when needed. This is the sloppier workaround for the same anchoring problem, vs. the cleaner Save-Presets-To-FT lane above (which requires remembering where your FTs live).

History: none — captured 2026-07-19 from the world-practices research pass; kept as its own concept (rather than folded into the research-intake concept) because of its direct, immediate relevance to the WIZ universal presets already in active use. Extended 2026-07-21: added Dave's deprioritized posture (scoped to careless fixture deletes; stays verify but no longer gates routine work) and the Save-Presets-To-FT → export → reimport → "Create Presets from FT" countermeasure (untested) plus the "DO NOT DELETE" resident-FT field alternative.

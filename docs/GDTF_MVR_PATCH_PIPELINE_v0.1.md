---
doc_id: GDTF_MVR_Patch_Pipeline
version: v0.1
status: draft
owner: Alchemease LLC
last_reviewed: 2026-07-04
related:
  - server/README.md                   # the shipped MCP server — consumer of this pipeline (spec deltas in §6)
  - MA3_MCP_Server_Spec_v1.md          # (not included in this release)
  - 13_GridCompositionApproach.md      # (not included) — see concepts/ GROUPS, SELECTION & LAYOUT for the role-based portability doctrine
tags: [gdtf, mvr, mvr-xchange, patch, grandma3, mcp, festival, alchemease]
notes: |
  v0.1: Resource paper drafted 2026-07-04 from live research (MA help 2.0–2.3,
  gdtf.eu, GDTF Hub blog). Written mobile-side during the 2026 EU festival
  run. Companion to the design-token festival architecture. Verify-on-console
  checklist (§8) is executable now that the MA3 MCP server is live.
---

# GDTF / MVR Patch Automation — Resource Paper v0.1 (DRAFT)

> ⚠ **STATUS: draft resource paper, NOT a verified concept.** §8 is the list of what has *not* yet
> been proven on a console. Everything in `concepts/` is attested and version-stamped; this document
> is the map of the next build. Read it as intent, not as console truth.

## 0. Why This Exists

The design-token festival architecture absorbed every daily task except one. Palette, texture, motion, and dynamics compile to role-based MA3 objects; Beat Grid places them in time; the showfile skeleton never changes. What remains manual is the front door: getting each festival's house rig *into* the showfile and bound to the role groups. That is a patch problem, and patch is exactly what GDTF and MVR were built to standardize. With the MA3 MCP server now writing groups and presets from the desktop, the patch step is the last human-copy-paste territory on a festival day. This paper maps the standards, what MA3 v2.4.2.2 actually supports, and a five-stage pipeline that turns "here's our rig" into "your show is bound" with an agent driving.

---

## 1. The Standards Stack — Three Layers

| Layer | What it describes | Standard | Transport |
|---|---|---|---|
| **GDTF** | One fixture *type*: DMX modes, channels, attributes, geometry, physical data | DIN SPEC 15800:2022 | `.gdtf` file (zip: `description.xml` + resources) |
| **MVR** | One *rig instance*: fixture placements, patch addresses, fixture IDs, positions, layers/classes — with the GDTF files embedded | DIN SPEC 15801:2023-12 | `.mvr` file (zip archive) |
| **MVR-xchange** | Live *network exchange* of MVR data between applications — no file handoff | Part of MVR spec | TCP/mDNS on the production network |

The mental model: **GDTF is the fixture-type contract, MVR is the rig manifest, MVR-xchange is the wire.** A festival's Vectorworks/Capture/Depence world speaks all three natively. The console does too.

Ecosystem note: this is no longer a niche. Vectorworks, Capture, WYSIWYG, Depence, Lightwright (now exports MVR direct to grandMA3), Unreal, ETC Eos, ChamSys, Avolites, and BlenderDMX all read/write these formats. A European festival advance in 2026 is more likely than not to have an MVR available — someone drew the rig in CAD.

---

## 2. What grandMA3 v2.4.2.2 Gives You Today

**GDTF import.** Patch menu → Fixture Types → Import. Default library path for file-based import: `/grandMA3/gma3_library/fixturetypes` (USB or internal). With an active World Server connection, the Import dialog exposes a **share button** that lists fixture types directly from the GDTF Share library — search and import without leaving the console.

**MVR import.** Imports the *entire* rig in one operation: fixtures, their fixture-type files, stage elements, Layers, and Classes. MA's own documentation warns to **store the showfile before importing** — a bad MVR can add unwanted elements or, worst case, corrupt the show. Treat MVR import as a Tier-2 operation with a mandatory pre-snapshot.

**MVR export.** Patch menu → Export MVR → lands in `shared/resource/lib_mvr`. The export carries the full patch including fixture files. This is the reverse flow: send *your* skeleton rig to the festival's previz world.

**MVR-xchange.** Native in MA3 with improvements shipped in v2.3.0.4 and further MVR work in v2.4.2.2. The console can join an MVR-xchange group on the network and exchange rig data live with CAD/previz applications. This is the zero-file path: the festival's Vectorworks operator shares the rig, the console receives it.

**Version caveat (known, but load-bearing):** 2.4 showfiles do not open in 2.3.x. The pipeline must record which MA3 version each festival's house console runs before deciding where patch assembly happens (onPC-side vs console-side).

---

## 3. GDTF Share as a Programmatic Source

GDTF Share (gdtf-share.com) passed 7,000 files in 2024 and keeps growing; it hosts both manufacturer-official and community-built fixture types with revisions and ratings. Critically for the MCP server: **GDTF Share operates a public API with a dedicated developer section** (launched 2025). Third-party tools (BlenderDMX among others) already consume it programmatically — authenticated REST, list/query/download.

This turns fixture-type resolution into a tool call: rider says "12× Robe MegaPointe," the agent queries the Share, retrieves candidates, matches the DMX mode, and stages the `.gdtf` for install. Exact endpoints, auth flow, and redistribution terms go on the verify list (§8) — the redistribution question matters doubly because a cached GDTF library on the Pi bridge is a natural extension of the knowledge-corpus moat.

---

## 4. The Five-Stage Festival Patch Pipeline

Each stage is agent-executable through the MCP server; human confirmation gates sit where judgment or blast radius demands it.

### Stage 1 — Acquire
Normalize whatever the festival provides into a **rig manifest** (JSON): fixture type names, counts, modes, universe/address, positions where known. Input quality tiers, best to worst:

1. **MVR file** from their CAD/previz → manifest is nearly free (parse the MVR)
2. **House MA3 showfile** → import patch, read back via MCP Tier-0 tools
3. **Spreadsheet / PDF rider** → agent parses to manifest; lowest trust, most confirmation

### Stage 2 — Resolve
Map manifest names → concrete GDTF fixture types + modes. Sources in order: fixture types already on console → GDTF Share API → manufacturer download. Mode matching by channel count first, mode-name heuristics second. **Any ambiguity is a confirm-gate stop** — a wrong mode patches clean and fails live, which is the worst failure class.

### Stage 3 — Patch
- MVR available → `import_mvr` (Tier 2, showfile snapshot first, per MA's own warning)
- No MVR → install resolved GDTFs to the library path, then patch via command line / Lua (exact scriptable surface: verify list)

### Stage 4 — Bind
Assign patched fixtures into the token system's role groups (KEY / WASH / AERIAL / BACK / AUDIENCE / FX). The agent proposes a binding sheet from evidence:
- **GDTF physical data**: zoom range, beam angle, gobo wheels → spot vs. wash vs. beam classification
- **MVR position data**: trim height and stage position → AERIAL vs. FLOOR vs. FOH, left/right symmetry pairing
- **Counts**: balance wings, reserve center specials

Human approves the sheet (one look, on a phone, over coffee). Groups populate; every sequence, phaser, and Beat Grid cue downstream is now live on the house rig without modification. This stage is where doc 13's thesis cashes out: the composition never knew what fixtures existed, so binding *is* the port.

### Stage 5 — Pre-Focus
MVR position data populates the MA3 3D stage → build position presets against stage targets in onPC **the night before, from the hotel**. On-site focus becomes trim, not creation. Working LDs already report MVR as essential to pre-programming workflows; the agent just removes the clicking. CAD positions are trusted for pre-focus only — never as final focus.

**The compounding effect:** Stages 1–3 shrink toward zero as festivals send MVRs. Stage 4 is minutes with a good binding sheet. Stage 5 moves focus time off the clock entirely. The festival day converges on: verify patch, trim positions, soundcheck.

---

## 5. Why GDTF Underwrites the Token System

This is worth stating explicitly because it is the theoretical foundation of the whole portable-show argument: **GDTF's standardized attribute dictionary is what makes role-based presets clone across brands.** A Color preset means the same thing on a MegaPointe and a Mac Ultra because both fixture types map their wheels and emitters into the same attribute grammar. Dimmer, Pan/Tilt, ColorRGB, Zoom, Gobo — the token system compiles to attributes, attributes resolve per-fixture through GDTF. Without that layer, "role-based" would be a naming convention; with it, it's an executable contract. The patch pipeline isn't adjacent to the design-token architecture — it's the bottom half of it.

---

## 6. Proposed MCP Spec Deltas (v1 → v1.1)

New tools, tiered per the existing safety model:

| Tool | Tier | Notes |
|---|---|---|
| `gdtf_share_search(query)` | 0 | Share API query; returns candidates + revisions/ratings |
| `resolve_fixture_types(manifest)` | 0 | Name→GDTF+mode matching; flags ambiguities |
| `export_mvr(name)` | 1 | Skeleton out to festival previz |
| `install_gdtf(file)` | 2 | Library-path drop + import |
| `import_mvr(path, dry_run)` | 2 | Mandatory pre-snapshot; diff report after |
| `bind_roles(binding_plan)` | 2 | Executes approved binding sheet into groups |
| `patch_from_manifest(manifest)` | 2 | Fallback path when no MVR exists |

New resources: `ma3://rig_manifest` (current normalized rig), `ma3://mvr/last_import_report` (what the last import added/changed).

**Pi bridge tie-in (Phase 2/3):** the box becomes a standing **MVR-xchange node** on the production network — it can receive the festival's rig broadcast before anyone sits at FOH, pre-run Stages 1–2, and have a binding sheet waiting. The Pi also hosts the cached GDTF library (licensing permitting), extending the curated-corpus moat from syntax to fixture data.

---

## 7. Gotchas

- **GDTF quality variance.** Official and community files coexist on the Share with different revisions; bad default values and missing modes happen. Prefer manufacturer-official + latest revision; sanity-check footprint against the house patch.
- **Mode mismatch is the #1 failure.** Channel-count match is necessary, not sufficient. Confirm against the house patch's actual mode, not the rider's claim.
- **MVR import can pollute or corrupt.** MA says it plainly: store first. Automate the snapshot, always.
- **Subfixture assembly.** MA3 assembles GDTF geometries into its own subfixture structure (overview screen added in 2.1.1.2); complex multi-instance fixtures may not land the way the grid math expects. Spot-check one fixture per new type.
- **House patch ≠ rider.** Festivals swap fixtures the week of. The manifest that matters is the one on their console Thursday, not the PDF from April.
- **Version churn.** 2.4 showfiles are one-way. Record house console versions in the advance sheet.
- **CAD trust.** MVR positions are as good as whoever drew them. Pre-focus, then trim with eyes.

---

## 8. Verify-On-Console Checklist (MCP-Executable Now)

1. Command-line syntax for MVR import/export (`Import`/`Export` keywords) — is the full flow scriptable via `/cmd`, or menu-bound?
2. GDTF import from library path via command line — scriptable end-to-end?
3. Lua Patch API surface — can fixtures be created/addressed programmatically, and does it survive `ReloadAllPlugins`?
4. GDTF Share API: auth flow, endpoints, rate limits, **redistribution/caching terms** (Pi library question)
5. Share button availability when console has no World Server / no internet — offline behavior
6. MVR-xchange: enable/config location in station settings; can an onPC node on the LAN act as the receiving station headless?
7. FixtureType exchange behavior: when swapping a placeholder type for the house type, which preset data survives?
8. MVR import diff: what does the console report, and can the MCP capture it for `ma3://mvr/last_import_report`?

---

## 9. References

- MA Lighting help — Import GDTF: https://help.malighting.com/grandMA3/2.0/HTML/ft_import_gdtf.html
- MA Lighting help — My Virtual Rig (MVR): https://help.malighting.com/grandMA3/2.3/HTML/patch_mvr.html
- MA Lighting help — Import Fixture Types: https://help.malighting.com/grandMA3/2.0/HTML/ft_import.html
- GDTF Hub — MVR Improvements in grandMA3 2.4.2.2: https://www.gdtf.eu/blog/mvr-improvements-in-grandma3-2.4.2.2/
- GDTF Hub — MVR-xchange Improvements in grandMA3 2.3.0.4: https://www.gdtf.eu/blog/mvr-xchange-improvements-in-grandma3-version-2.3.0.4/
- GDTF Hub — GDTF Share Developer Section / Public API coverage: https://www.gdtf.eu/blog/gdtf-share-launches-developer-section-to-enhance-access-to-gdtf-and-mvr/
- GDTF Share: https://gdtf-share.com
- DIN SPEC 15800:2022 (GDTF), DIN SPEC 15801:2023-12 (MVR)

---

*End of resource paper v0.1. Redline freely — §4 stage gates and §6 tier assignments are the parts most worth arguing about.*

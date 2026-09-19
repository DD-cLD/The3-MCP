---
metadata_version: "1.0"
doc_id: ma3-librarian
title: "The Librarian — capture/curate knowledge protocol"
owner: DaveDibb
version: "0.3"
status: active
created_at: 2026-07-04
updated_at: 2026-07-24
tags: [tier-1, process, knowledge-architecture, librarian]
notes: |
  Born in [0704cLD]Live-Cook-Crash-Librarian. Solves the "two hats" problem:
  doer and librarian in one context degrade both, and MEMORY.md was becoming
  a long flat scroll paid for in full by every session.
  v0.2 (2026-07-23, [0723-2cLD], Dave-ratified): ROLE PARTITION law added —
  the corpus re-shelves around the programmer role (split index files, show
  packets, trigger-worded lines, front-matter diet). Origin: the retrieval-miss
  postmortem + Dave's ruling that the remaining mission is being a good MA3
  programmer from the Claude interface; everything else is done or parked.
---

# The Librarian

## The problem this solves

Two hats: a session doing console/build work is also expected to curate knowledge as it goes. Curation loses — findings land as unstructured appends to `MEMORY.md`, which grows into a flat scroll that every future session must load whole, whether it's cooking phasers or answering tour email.

## The split

**Capture** is in-flow and near-zero cost: when a finding lands mid-session, append one line to `findings/INBOX.md` and keep working. No structuring, no filing, no hat-switch.

**Curate** is delegated: an event-triggered subagent (cheap model — Sonnet-class) digests the inbox and any new wrap into **atomic concept files** under `concepts/`, updates the lean index files, merges duplicates, and marks superseded entries stale. Not a daemon — dispatched at defined moments by whatever session is running.

**Load** stays lean: sessions auto-load the **programmer spine index only** (`concepts/INDEX.md`, post-partition) plus the active show packet. Bodies load on demand, by id, when an index line, arming manifest, or smith dispatch says the concept is relevant.

The model split is deliberate: cheap model restructures, thinking model designs and verifies. This generalizes the wrap's stage-1/stage-2 rhythm (digest → pause → rehydrate) into a continuous discipline.

## Role partition — the shelves (ratified 2026-07-23, [0723-2cLD])

The corpus is shelved **by role**, with the programmer as the spine. The mission ruling behind it (Dave): the remaining job is being a good MA3 programmer from the Claude interface — design is largely done, the tools are built; the programmer must be portable enough to receive a design package from any show, any time, and program it.

| Role | What belongs | Index file | Boot? |
|---|---|---|---|
| `programmer` | The mechanical toolkit: CLI/syntax, macros, phasers & recipes, phase math, patch & 3D, layouts, release/TC, XML dialects & goldens, Lua/plugins, MCP, OSC, input lanes, show-file format | **`concepts/SPINE.md`** | **YES — whole** |
| `operational-live` | Operational facts that can bite *during a build*: Drive/stage false-negatives, crosscheck pattern, dispatch sovereignty, the authoring/review gates, desk hygiene | **`concepts/SPINE.md`** | **YES — whole** |
| `operational-meta` | How cLD organizes *itself* rather than how it programs: librarian protocol, model-routing economics, bake-off records, project file locations, kickoff/wrap machinery | `concepts/INDEX.md` § Operational | no — summoned |
| `design` | WHAT/WHY: grid doctrine, palettes, treatments, daylight, design theory, effect taste | `concepts/INDEX_DESIGN.md` | no — summoned |
| `tools` | Built engineering: beatgrid/cLD MAker internals, audio/DSP/LTC pipeline, bakeoff records | `concepts/INDEX_TOOLS.md` | no — summoned |
| `historical` | Past-rig facts (Coachella etc.) | `concepts/INDEX_TOOLS.md` § Historical | no |

**Show packets** are a separate document class, not a corpus role: `WORKING/<SHOW>_SHOW_PACKET_v*.md` distills the operative facts of one show (slot mirror, group contract, pool identities, team/routing, ruling digest) with pointers to its concept ids for depth. The active show's packet boots alongside the spine; it is also the seed of that show's `LD.md` handoff. Show-scoped concepts keep their era tags and stay in the corpus; the packet is the curated operative view. The packet is a working doc — **cLD writes it, the librarian only flags packet-relevant findings in its run report.**

Partition rules:

- Every concept file carries a `role:` field (`programmer` | `operational-live` | `operational-meta` | `design` | `tools` | `historical`). Era tags stay orthogonal (`coachella` / `tourshow` / evergreen-untagged).
- **The operational split (v0.3 law) is where "nothing that isn't necessary" is won.** An operational concept rides the spine ONLY if it can bite *while a build is happening*. If it describes how the knowledge system, model routing, or session machinery works, it is `operational-meta` and gets summoned. When genuinely unsure, ask: *would not knowing this silently break an artifact I am authoring right now?*
- A finding files to exactly one role index. Dual-nature concepts (e.g. grid doctrine with mechanical consequences) shelve where they are *retrieved for use*; a one-line cross-pointer in the other index is allowed — bodies are never duplicated.
- Bodies never move, never delete (gardener rule 4 unchanged). The partition is re-shelving, not pruning.
- Boot chain (README owns it): README → MEMORY core → **`concepts/SPINE.md` (whole)** → active show packet → cards → latest state pair → wrap-pending check → DIARY tail.

## The spine loads whole (v0.3 law, ratified 2026-07-24)

**The programmer spine is no longer indexed for retrieval — it is carried.** Measured on the day of the ruling: `INDEX.md` cost 63,496 bytes (~16K tokens) *every session* to describe knowledge that costs roughly six times that to simply hold, inside a confirmed 1M-token window where the spine is ~10%. The retrieval-miss postmortem had already shown that filing was never the problem — a correctly filed concept with a correct `when_to_load` still went unopened, because nothing *fired* the load. Carrying the spine removes the firing step entirely.

- **`concepts/SPINE.md` is a BUILD ARTIFACT.** Generated by `generated/build_spine.sh` from every `programmer` + `operational-live` file whose `status` is not `superseded`, in **build order** (patch → 3D → layout → groups → presets → recipes/phasers → sequence/cues → timecode, then macros · CLI/input · transport & safety · show-file · operational). Filing metadata and `History:` sections are stripped in the generated view and remain in the sources.
- **Never hand-edit `SPINE.md`.** The individual files in `concepts/` are the source of truth. **Regenerate after every librarian run and after any concept edit** — a stale spine is the one real failure mode of this design.
- `INDEX.md`, `INDEX_DESIGN.md` and `INDEX_TOOLS.md` are likewise generated (`generated/build_indexes.sh`). Index lines are built from each concept's own `title` + `when_to_load`, so the trigger-worded-line law is satisfied by construction and cannot drift.
- **Trigger-worded lines still matter — for the summoned shelves.** Design and tools are still retrieved by skim, so their lines still have to carry the words someone would be staring at. For the spine the law is demoted: it aids orientation, it no longer prevents disaster.
- **Corpus = reference, card = foreground.** Carrying the spine guarantees a fact is *available*; it does not guarantee it gets *applied* (proven by the SONG_G recipe miss, where doctrine was loaded and still ignored). The dialect/step cards in `agents/cards/` are the separate foreground layer. Do not let the spine's existence argue the cards away.

## Concept file schema

One file = one retrievable concept, in `concepts/<id>.md`:

```markdown
---
id: gpdf-console-killer
title: "GetPresetDataFast() segfaults onPC 2.4.2.2 — banned from generated Lua"
role: programmer
tags: [lua, mcp, crash, v2.4, onpc]
when_to_load: "Before generating Lua that reads preset internals; when an MCP round-trip times out unexpectedly"
status: active
source: "MEMORY §Console-crash paid-for lessons, 2026-07-04"
supersedes: []
superseded_by: null
---

Two hard crashes (2026-07-04, 11:34 + 11:42), each the instant
`GetPresetDataFast(handle,...)` ran on a freshly built preset/phaser. ...
```

Field rules:

- **id** — short, stable, kebab-case. Never reused, never renamed once the index ships. Domain-prefixed where it reads naturally (`osc-inbound-config`, `phase-math-formulas`).
- **title** — the fact as a headline. A reader should get the gist without opening the body.
- **role** — the shelf (see partition table). Required on every new/updated concept from v0.2 on; the heavy partition run backfills the rest.
- **tags** — domain + era. Era tags matter: `coachella` / `tourshow` / evergreen (no era tag). Rig-specific facts are *scoped*, not superseded — the Spectra Tower grid is still true, it's just not this tour.
- **when_to_load** — the retrieval trigger, written for a future session scanning the index. This is the most important field; write it as "you need this when…".
- **status** — `active` | `superseded` | `verify`. `verify` = fact is banked but flagged unverified (the corpus marks these [VERIFY]).
- **source** — provenance. Section + date of origin. Evidence chains are house style.
- **supersedes / superseded_by** — links between concept files only. Corrections that already happened inside the corpus (strikethrough + "Corrected" notes) collapse into the active file's body as a one-line `History:` note.

**Atomicity rule:** one retrievable decision per file. If you'd ever want to load half of it, split it. If two files would always load together, merge them. A table of eight OSC config requirements is *one* concept; "phase math" is one concept even though it holds six formulas.

## Index format (all three files)

The index files are the only corpus parts that ever auto-load or get skimmed. They must stay scannable:

- Grouped by domain, `##` headers. `INDEX.md` orders programmer domains first, then the operational section.
- One line per concept: `` - `id` — hook (when to load) ``.
- **Trigger-worded lines (v0.2 law):** the hook MUST carry the concept's retrieval triggers — the `when_to_load` essence plus the failure keywords someone would actually be staring at. A line that names its topic but omits its triggers is a **filing defect** (the quote-miss lesson: `macro-xml-schema-cracked`'s line never said "quotes," so the skim couldn't save the session that needed it).
- Superseded concepts drop to a single `## Graveyard` section at the bottom of the index that held them, one line each: `` - `id` — superseded by `other-id` ``.
- No bodies, no multi-line entries, ever.
- **Front-matter diet (v0.2 law):** index front-matter stays under ~15 lines. Librarian run history lives in `LIBRARIAN_LOG.md` (one block per run), never in index front-matter — boot cost is paid by every future session; history is not knowledge.

## Gardener rules (the librarian's law)

1. **Never invent.** Copy exact values verbatim — IPs, ports, formulas, syntax strings, version numbers are the payload. If the source is ambiguous, flag it in the run report; don't guess. (House rule: don't invent MA3 facts.)
2. **Provenance always.** Every concept carries `source`.
3. **Merge duplicates.** One active concept per fact. Fold variants into the strongest statement and note the fold in the run report.
4. **Supersede, don't delete.** A stale concept gets `status: superseded` + `superseded_by`, and its index line moves to the Graveyard. Bodies are never deleted. Memory files are the crown jewels; the librarian is a gardener, not a shredder.
5. **Scope ≠ stale.** Era- or rig-specific facts stay `active` with era tags and a scoped `when_to_load`.
6. **Respect [VERIFY].** Unverified facts keep `status: verify` and say what would verify them.
7. **The index is sacred-lean.** If an index stops fitting on roughly one screen per domain, tighten hooks — don't wrap lines.
8. **Read-only on the corpus.** The librarian writes only inside `concepts/` (+ `LIBRARIAN_LOG.md`) and clears digested lines from `findings/INBOX.md`. It never edits MEMORY.md, wraps, state files, show packets, or README.
9. **Role on everything (v0.2).** Every concept written or touched gets its `role:` field and files its index line to the matching index file. Show-packet-relevant findings get flagged `→packet` in the run report for cLD to fold.
10. **Trigger-worded lines (v0.2).** Enforce the index line law above on every line written or rewritten. Run reports call out any line whose triggers wouldn't have caught its own source finding.

## Dispatch triggers (event-driven, no daemon)

- **Wrap time (primary):** Stage 2 rehydration gains a step — after state files are rewritten, dispatch the librarian on the new wrap + INBOX.
- **Inbox pressure:** if `findings/INBOX.md` exceeds ~15 undigested lines mid-session, dispatch opportunistically.
- **On demand:** Dave or the session says "run the librarian."

## Dispatch prompt template

Launch as a subagent (general-purpose, **model: sonnet**) with:

> You are the Librarian for the MA3_PROGRAMMING project. Read `WORKING/LIBRARIAN.md` and follow its schema, partition table, and gardener rules exactly.
>
> Corpus for this run: [list files — e.g. `findings/INBOX.md`, `wraps/<newest>.md`].
> Existing knowledge base: the three index files + the concept files they list. Read the indexes first; read full bodies only where a new finding might duplicate or supersede one.
>
> Do: (1) extract atomic concepts from the corpus per the schema, assigning `role:` per the partition table; (2) write/update files in `concepts/`; (3) merge dupes, mark superseded; (4) rewrite the affected index files with trigger-worded lines; (5) append this run's block to `LIBRARIAN_LOG.md` (never index front-matter); (6) clear digested lines from the inbox, leaving flagged `⚑` any line you couldn't confidently digest, and flag `→packet` any show-operative finding.
>
> Report back: counts (created / updated / merged / superseded) per index file, every supersede decision with one-line rationale, every ⚑ and →packet flag. Do not editorialize facts; verbatim values only.

## Verification checklist (dispatching session, after every run)

- Mechanical: ids unique; frontmatter parses (incl. `role:`); every index line has a file and every active file an index line in exactly one index; Graveyard consistent with `superseded_by`.
- Semantic: spot-check ~3 concepts against their sources — exact values survived; correction chains resolved to current truth.
- Retrieval: spot-check ~3 new/rewritten index lines — would their trigger words have caught the original finding's moment of need?
- Anything flagged `⚑` gets a human (or Fable) decision, not a silent drop.

## Relationship to MEMORY.md

**Cutover executed 2026-07-04 (Dave ratified).** `MEMORY.md` is the lean always-load core — identity, division of labor, current infrastructure, ⛔ hard rules (each pointing to its concept id), retrieval pointers. The lesson corpus lives here in `concepts/`. Auto-load chain (post-partition): README + MEMORY-core + `concepts/INDEX.md` (programmer spine + operational) + active show packet + latest STATE/ACTIONS + newest wrap. New lessons route INBOX → librarian → concepts; only new ⛔-class rules also earn a core line. The pre-cutover 509-line MEMORY is preserved at `Archive/MEMORY_pre-cutover_2026-07-04.md` — the librarian never deletes.

## Relationship to the smith lanes (2026-07-23)

The librarian is the knowledge-side agent; the smiths (`AGENT_LANES_SPEC_v0.1.md`) are delivery-side. The librarian files what sessions learn; the smiths consume it through arming manifests at dispatch time. The partition serves both: manifests draw from the programmer spine, and a well-triggered index line is what routes a task to the right manifest in the first place. Doorway skills (harness-level triggers pointing at briefs + manifests) are the third ring; they point at repo files and carry no content of their own.

## Later

- ~~MCP `concept_lookup(keyword)` tool~~ — **SHIPPED 2026-07-05 (server 0.2.1):** searches id + summary + domain from INDEX.md, returns the body on an exact-id or single match. (Searching body tags/when_to_load hooks: possible v2 refinement. Post-partition: point it at all three index files — verify at next server touch.)
- `wraps/processed/` convention: wraps move there once the librarian has digested them. (Still undecided; wraps continue to accumulate, none migrated.)

---
doc_id: MA3_Agent_Knowledge_System
version: v0.1
status: draft
owner: Alchemease LLC
last_reviewed: 2026-09-02
inherits_from:
  - Forgejo_Deployment_Spec_v2.1.md#section-8   # (not included) — frontmatter schema
related:
  - server/README.md                            # the shipped MCP server — transport + safety tiers (this spec sits in front of it)
  - docs/GDTF_MVR_PATCH_PIPELINE_v0.1.md        # PATCH DAY load case source
  - concepts/INDEX.md                           # the verified corpus this system serves
  - playbook/LIBRARIAN.md                       # graduation path as practised (DIARY → MEMORY → concept)
  - 13_GridCompositionApproach.md               # (not included) — doctrine reference
  - File_Organization_Patterns_v0.6.md          # (not included) — tier doctrine
tags: [ma3, skill, intent-compiler, schema, emitter, load-cases, brigade, agents, alchemease]
notes: |
  v0.1: Architecture brief for the agent-builder team. Consolidates the
  post-tour design sessions (Aug–Sep 2026) into a buildable spec with a
  build order and definition of done per phase. Schema and verb vocabulary
  are DRAFT — builders finalize. Client-specific material (tour, artist,
  venues) is explicitly out of scope for skill content.
---

# MA3 Agent Knowledge System — Architecture Brief v0.1 (DRAFT)

> ⚠ **STATUS: draft architecture brief.** It describes a system to be built (§12 phases), not one that
> ships in this release. What ships is the material it consumes — `concepts/` (the verified corpus),
> `playbook/`, `skills/`, `server/` (the transport), `kit/` (the manual-era build tools). Read this
> first if you want to know why the corpus is shaped the way it is.

> **One-line summary.** Package everything cLD learned this tour into a system any agent can load on demand: a skill that routes context by session goal, serves verified MA3 knowledge as both prose and queryable data, and compiles structured intent into console-correct syntax through a deterministic emitter. The MCP server remains the transport; this is the knowledge and compilation layer in front of it.

---

## 0. Purpose and Scope

**In scope:** the MA3 skill package, the load-case routing model, the serving layer (read vs. query), the intent schema + emitter (the "intent compiler"), the validator, the intent-compiler subagent definition, brigade integration rules, the eval loop, build order, and definition of done.

**Out of scope:** the MCP server itself (see `MA3_MCP_Server_Spec_v1.md`), the Pi bridge hardware, Beat Grid internals (only its output contract touches this spec), and any client-specific show content.

**Audience:** agent builders. Assume fluency in Claude skills, subagents, MCP, JSON Schema, and Python. Assume *no* MA3 fluency — everything MA3-specific the system needs is supposed to live *inside* the package, which is the point.

---

## 1. Where We Are (Inputs to This Spec)

Validated in production during the 2026 EU festival run:

- **MA3 MCP server is live.** Groups and presets written from Claude Desktop directly to the console. Phase 1 success criterion from the MCP spec (Spectra Tower workflow, no human copy-paste) is met.
- **Show data is file-shaped.** cLD authors presets and sequences as MA3 XML outside the console; the Lua + MCP bridge imports them. The console is a render target.
- **A crosswalk exists.** Translation contract from an inherited, rig-specific, mislabeled showfile into the role-based festival schema. Reusable artifact; every inherited festival file has the same disease.
- **Song one is complete** with recipes and timecode and is the golden template for the cutover assembly line.
- **A verified syntax corpus exists** (one-sheet + anti-patterns), earned by correction over many sessions. Today it lives in chat history, project knowledge, and one account's memory — fragile and unversioned. This spec makes it durable.

---

## 2. Design Principles

1. **Load what you need, index the rest.** Context is the scarce resource. Nothing loads by default except routing.
2. **Prose to read, data to query, code to run.** Three consumption modes, three storage forms. Never make a model re-read a table to find one row.
3. **Language is the model's job; syntax is code's job.** The agent translates intent into a schema. A deterministic emitter renders the schema. Nothing freehand reaches the console.
4. **The schema is the stationary joint.** MA versions, models, rigs, and agents all churn. The schema does not. The emitter is where change gets absorbed.
5. **Nothing reaches the console without crossing the pass.** Validation before emission, reference checks before import, readback after import. Imports stay behind the MCP tier gates.
6. **Role-based, never fixture-based.** Skill content references role groups (KEY, WASH, AERIAL, BACK, AUDIENCE, FX) and pool structures, never a specific rig or client.
7. **Offline-clean.** Every layer must function with no network. Festival life guarantees air gaps.

---

## 3. The Three Layers

```
        ┌────────────────────────────────────────────────┐
        │  LAYER 1 — LOAD CASES (routing)                │
        │  SKILL.md declares named session goals, each   │
        │  with an explicit manifest of what to load.    │
        └───────────────────────┬────────────────────────┘
                                │
        ┌───────────────────────▼────────────────────────┐
        │  LAYER 2 — SERVING (read vs. query)            │
        │  references/*.md   → doctrine, anti-patterns   │
        │  references/*.json → keyword/attribute data    │
        │  scripts/ma3ref.py → lookup without loading    │
        │  (mirrored as MCP resource when networked)     │
        └───────────────────────┬────────────────────────┘
                                │
        ┌───────────────────────▼────────────────────────┐
        │  LAYER 3 — INTENT COMPILER (schema + emitter)  │
        │  agent: intent → intent.json (schema v0.1)     │
        │  scripts/validate_intent.py → pass/fail        │
        │  scripts/emit.py → CLI | Lua | XML             │
        │  version-targeted templates in assets/          │
        └───────────────────────┬────────────────────────┘
                                │
                     MCP server (transport + tier gates)
                                │
                             console
```

Build order is top-down: Layer 1 is an evening, Layer 2 is a few days, Layer 3 is the real engineering. Each layer is useful without the ones below it.

---

## 4. Layer 1 — Load Cases

A load case is a named session goal bound to an explicit manifest. SKILL.md carries the routing table; the agent reads *only* the manifest for the declared case. This is the skill-creator "organize by variant" pattern applied to session goals instead of frameworks.

| Load case | Trigger phrases (for SKILL.md description) | Manifest |
|---|---|---|
| **PATCH DAY** | patch, fixture types, GDTF, MVR, house rig, role binding | `references/patch_pipeline.md`, `references/crosswalk_schema.md`, `assets/binding_sheet_template.md`, keyword subset: patch |
| **TIMECODE** | timecode, TC, cue timing, song programming, Beat Grid | `references/beat_grid_contract.md`, `references/song_template.md` (song one, de-identified), keyword subset: timecode, sequence |
| **BUSKING PREP** | busking, live, executors, MAtricks, phasers, effects | `references/grid_composition.md`, `references/matricks_phaser_recipes.md`, `references/macro_onesheet.md` |
| **LUA DEV** | plugin, Lua, Object API, ReloadAllPlugins | `references/lua_sandbox.md`, `references/lua_api_allowlist.md`, `assets/plugin_skeleton.lua` |
| **CUTOVER** | crosswalk, inherited showfile, migration, XML import | `references/crosswalk_schema.md`, `references/allocation_ledger_spec.md`, `assets/xml_templates/` |
| **SESSION WRAP** | wrap, hand off, end session | `references/wrap_template.md` (from File Organization Patterns) |

**Rules**
- Five or six cases. A case that loads everything is a slow way of loading nothing.
- Every manifest entry states *when* to read it, not just *that* it exists.
- SKILL.md stays under 500 lines. If a case grows, it gets its own reference file with a table of contents.
- The `description` field in SKILL.md frontmatter must be deliberately "pushy" — it is the trigger mechanism, and skills under-trigger by default. Enumerate the MA3 vocabulary (grandMA3, MA3, showfile, executor, sequence, preset, MAtricks, phaser, timecode, GDTF, MVR, Lua plugin, macro) so the skill fires even when the user doesn't say "skill."

---

## 5. Layer 2 — Serving Layer

Split the corpus by how it's consumed.

### 5.1 Prose (read)
Doctrine and reasoning the agent should actually think with:
- `references/anti_patterns.md` — each entry as a contrastive pair: the wrong form, *why it fails*, the verified form, the edge cases.
- `references/grid_composition.md` — the relationship-not-position doctrine (from doc 13).
- `references/lua_sandbox.md` — what MA3 Lua does not have and what to use instead.
- `references/crosswalk_schema.md` — the translation contract, generalized.

### 5.2 Data (query)
Precise lookups that should never cost a full read:
- `references/keywords.json` (or SQLite if the record count justifies it). Fields:
  ```
  keyword, verified_syntax, example, ma3_version_min, ma3_version_notes,
  anti_patterns[], related_keywords[], source, verified_date, verified_by
  ```
- `scripts/ma3ref.py` — CLI lookup. `ma3ref lookup "Set MAtricks"` returns the verified form and notes. Executes without loading the data into context. Fuzzy match on keyword; exact match on verified form.

**Two doors, one corpus.** Locally, the script. When networked, the same data is served as `ma3://keyword-reference` per MCP spec §6. The file in the skill is the source of truth; the MCP resource is a mirror with TTL.

### 5.3 Seed content (already verified — migrate first)
- `Set Macro N.M "command" "text"` — lowercase `"command"`, no `Property` keyword; each `Set Macro` auto-creates the line.
- Semicolons are legal at the command line between separate commands; **illegal inside a macro line's command string** (parser breaks). One command per macro line.
- Label quoting: single quotes inside double quotes — `"Store Sequence 101 Cue 1 'GRP 1 STRB'"`.
- MAtricks pool objects must exist (`Store MAtricks n`) before `Set MAtricks` can edit them; `Set MAtricks` takes all properties in one command, property names unquoted, values quoted.
- MA3 Lua sandbox: no `io.open`, no `os.execute`, no `gma.*` namespace (MA2 idiom — a common failure when priming generic sessions). Long loops must `coroutine.yield`.
- Selection Grid: one cell per fixture per selection; "multi-grid participation" is multiple sequences running under LTP/HTP, never multi-cell membership.
- Showfile version: 2.4 files do not open in 2.3.x. Record the target console version before emitting.

---

## 6. Layer 3 — Intent Compiler

### 6.1 Split of responsibilities
```
messy human/agent intent
        │  (the model's job — language)
        ▼
intent.json  ── validate_intent.py ──►  pass / fail with reasons
        │  (code's job — syntax)
        ▼
emit.py --target cli|lua|xml --ma3 2.4.2.2
        │
        ▼
console-correct text  ──►  MCP tier gate  ──►  console
```
A pure program that parses unbounded natural language into command line is a compiler for English. Don't build that. Constrain the *input* (schema), not the intelligence.

### 6.2 Intent schema v0.1 (DRAFT — builders finalize verb vocabulary)

```json
{
  "schema_version": "0.1",
  "intent_id": "8c1f…",
  "verb": "store_sequence",
  "target": { "type": "sequence", "number": 101, "name": "GRP 1 STRB" },
  "selection": { "group": 2 },
  "ingredients": [
    { "pool": "preset", "ref": "1.11", "role": "intensity" },
    { "pool": "preset", "ref": "5.5",  "role": "effect" }
  ],
  "timing": { "fade": 0, "delay": 0 },
  "render": {
    "format": "cli",
    "ma3_version": "2.4.2.2",
    "delivery": "cli_blocks_of_10"
  },
  "provenance": {
    "source": "beat_grid | token_system | operator | subagent:<name>",
    "song": "<song-id>",
    "notes": ""
  }
}
```

**Initial verb vocabulary** (grounded in what cLD already does): `create_group`, `store_preset`, `store_sequence` (recipe ingredients), `build_macro` (list of discrete lines), `store_matricks`, `set_matricks`, `assign_executor`, `import_xml`, `set_variable`. Anything else is rejected by the validator with a schema-level error, not guessed.

**Invariants**
- `schema_version` is mandatory on every object. Breaking changes bump it; the emitter supports N and N-1.
- Pool numbers must fall inside the caller's range in the allocation ledger (§8) or validation fails.
- `render.ma3_version` is mandatory. No default — the wrong default patches clean and fails live.

### 6.3 Emitter contract (`scripts/emit.py`)
- Pure function: `intent.json` in, text out. No network, no console, no side effects. Deterministic — same input, byte-identical output.
- Template-driven. Templates live in `assets/emit_templates/<ma3_version>/<verb>.<format>.j2` (or equivalent). Adding an MA3 version = adding a template directory, not touching logic.
- Enforces the delivery contract:
  - **CLI delivery:** semicolon-separated commands, ten per block, one paste per block.
  - **Macro delivery:** one command per `Set Macro N.M` line; no semicolons inside the command string; label quoting single-in-double; explicit `Wait` lines where programmer state must commit between operations.
  - **Lua delivery:** MCP spec §5.2 skeleton; header comment with purpose/safety/generated_at; yield in any loop above the threshold.
  - **XML delivery:** MA3 pool-object XML; pool numbers from the ledger; `DataVersion` matching `render.ma3_version`.
- Refuses unknown verbs, unknown versions, and any intent that failed validation.

### 6.4 Validator (`scripts/validate_intent.py`, `scripts/validate_xml.py`)
Five checks, in order; first failure stops with a reason the agent can act on:
1. **Schema** — JSON Schema validation of the intent object.
2. **Ledger** — pool numbers inside the caller's allocated range; no collisions.
3. **References** — every Group/Preset/MAtricks the intent cites exists on the console (MCP Tier-0 `list_*` calls) or in the same batch being imported.
4. **Delivery lint** — semicolons in macro strings, quote nesting, MAtricks store-before-set ordering, version compatibility.
5. **Target-specific** — Lua: `luac -p` + Object API allowlist + yield check. XML: well-formedness + `DataVersion` check.

### 6.5 Golden tests (`tests/golden/`)
Pinned from the verified one-sheet. Every emitter change diffs against known-good output instead of against anyone's memory. Minimum seed set:
- Macro 50 (15 sequences across 5 groups, skip-10 numbering) reproduced byte-identical from intent objects.
- The semicolon-in-macro-string case: validator must **reject**.
- `Set MAtricks` without prior `Store MAtricks`: validator must **reject**.
- Same intent rendered for `2.4.2.2` and `2.3.x` where syntax differs: both outputs pinned.
- A `gma.*` call in Lua: allowlist must **reject**.

### 6.6 Version targets
`render.ma3_version` selects the template directory. This turns console-version churn (the "which version is the festival running" question) into a flag: same intent, different render. The operator records the house console version during advance; the emitter does the rest.

---

## 7. The Skill Package

Follows the standard skill anatomy so it loads correctly everywhere (Claude.ai, Desktop, Claude Code, and on the Pi bridge unchanged).

```
ma3-programming/
├── SKILL.md                      # frontmatter (name, pushy description) + load-case routing table
├── references/
│   ├── anti_patterns.md          # contrastive pairs
│   ├── macro_onesheet.md
│   ├── grid_composition.md
│   ├── lua_sandbox.md
│   ├── lua_api_allowlist.md
│   ├── crosswalk_schema.md
│   ├── allocation_ledger_spec.md
│   ├── patch_pipeline.md         # from GDTF/MVR resource paper
│   ├── beat_grid_contract.md     # Beat Grid OUTPUT format only
│   ├── song_template.md          # song one, de-identified, role-based
│   ├── wrap_template.md
│   └── keywords.json             # queried, not read
├── scripts/
│   ├── ma3ref.py                 # keyword lookup
│   ├── validate_intent.py
│   ├── validate_xml.py
│   └── emit.py
├── assets/
│   ├── emit_templates/
│   │   ├── 2.4.2.2/
│   │   └── 2.3.x/
│   ├── xml_templates/
│   ├── plugin_skeleton.lua
│   └── binding_sheet_template.md
└── tests/
    └── golden/
```

**Loading behavior to design for:** metadata (name + description) is always in context; SKILL.md body loads on trigger; everything under `references/`, `scripts/`, `assets/` loads only when the manifest says so — and scripts execute without ever loading their source into context. That last property is why the query layer and the emitter cost nothing until used.

**Packaging:** `package_skill.py` produces a `.skill` file. The same folder is what ships on the Pi bridge and what backs the Field Manual appendix — one artifact, three products.

---

## 8. Brigade Integration (Assembly Line Rules)

The cutover runs as a brigade de cuisine: station chefs per song, everything crosses the pass. Four rules, enforced by the tooling above rather than by discipline alone:

1. **Allocation ledger before parallelism.** A machine-readable file (`working/allocation_ledger.json`) assigns pool number ranges per song and per pool type. Every subagent loads it; the validator refuses anything outside the caller's range. Two agents improvising sequence numbers recreate the mislabeled showfile at machine speed.
2. **Song one is the golden template.** Subagents fill structure; they never invent it. A subagent that "improves" the schema mid-line has broken the crosswalk.
3. **One agent works the pass.** A validator role that only reads. Nothing reaches `emit.py` without passing `validate_intent.py`; nothing reaches the bridge without passing `validate_xml.py` and the reference check. Imports stay at MCP Tier 2, gated at batch boundaries — the line speeds up production, not the trigger.
4. **Readback after import.** Tier-0 `list_*` calls diffed against the song manifest. The file says what was meant; the console says what happened; the diff is the taste test. Diff output is written to the wrap.

---

## 9. The Intent-Compiler Subagent

A Claude Code subagent (or equivalent) whose entire education is the `ma3-programming` skill.

```yaml
name: ma3-compiler
role: >
  Translate structured or lightly-structured MA3 programming intent into
  validated intent.json objects and render them through emit.py. Single
  responsibility. No design opinions.
inputs:
  - intent (natural language or partial JSON) from operator, Beat Grid, token system, or brigade subagent
  - allocation ledger range for the calling song/workstream
  - target ma3_version and delivery format
outputs:
  - intent.json (validated) + emitted text (CLI/Lua/XML)
  - on ambiguity: a schema-level question, never a guess
tools:
  - scripts/ma3ref.py, scripts/validate_intent.py, scripts/emit.py
  - MCP Tier-0 list_* (read-only) for reference checks
never:
  - choose colors, looks, timing, or structure (upstream owns design)
  - emit freehand syntax that bypassed the validator
  - write to the console (the bridge and its tier gates own that)
```

In the brigade, this is the station cook: hears the call, plates the dish, never editorializes.

---

## 10. Knowledge Graduation and Eval Loop

**Graduation.** The File Organization Patterns path — DIARY → MEMORY → Canon — is the curation pipeline for skill content. An observation that repeats across sessions, survives contradiction, and changes how work gets done graduates into a reference file or a keyword record. The MCP spec §8.2 learning log is the raw material. Every graduated item carries `verified_date` and `verified_by`.

**Eval.** The validator's pass/fail is the metric. Benchmark: identical task prompts run skill-on vs. skill-off; measure first-try validation pass rate and first-try import success. Use the skill-creator eval tooling (`benchmark.json`, `generate_review.py`) so results are reviewable, not anecdotal. Re-run the benchmark on every MA3 version bump and every schema version bump.

**Rhythm.** Wrap → process-wrap → graduation check → skill update → golden test re-run → package. Skill releases are versioned and tagged alongside the schema version they support.

---

## 11. Boundaries

- **Donate the craft, keep the compiler.** Verified MA3 truths, doctrine, and anti-patterns may be published or donated (the Family Meal channel). The intent schema, emitter templates, validator, and crosswalk tooling stay proprietary — that's what the Pi bridge and the training products sell.
  *Release note (v0.1, 2026-09):* this boundary applies to the **compiler described here**, which does not yet exist. The manual-era kit that preceded it (`kit/cld_songbuild.py` — the mechanical half of a per-song crosswalk build, taste left to the human) ships in this release under Apache-2.0; the compiler that replaces it will not.
- **No client material in the skill.** Song templates are de-identified and role-based. No artist, tour, venue, contact, or network specifics anywhere in the package.
- **The MCP tier model is not bypassed by this spec.** Emission produces text; only the bridge writes; only the gates release writes.

---

## 12. Build Order and Definition of Done

| Phase | Deliverable | Definition of done |
|---|---|---|
| **1. Load cases** | `SKILL.md` with routing table + pushy description | A fresh session declaring any load case receives exactly its manifest and nothing else. Trigger test set passes. |
| **2. Serving layer** | `keywords.json` + `ma3ref.py` + migrated reference files | 100% of one-sheet entries retrievable by lookup; lookup runs offline; contrastive pairs written for every known anti-pattern. |
| **3. Schema + emitter** | `schema v0.1`, `validate_intent.py`, `emit.py`, templates for 2.4.2.2 | All golden tests pass; all reject-cases reject; Macro 50 reproduced byte-identical from intent. |
| **4. Compiler subagent** | `ma3-compiler` definition | Song-one artifacts regenerated from intent objects produce XML identical to the shipped version. |
| **5. Brigade integration** | ledger, pass role, readback diff in wraps | One full song runs through the line: validated → emitted → imported → readback diff clean, with no manual syntax. |
| **6. Benchmark + package** | `benchmark.json`, results, `.skill` file | Skill-on vs. skill-off comparison documented; package installs and triggers on Desktop and Claude Code. |

Phase 1 is one evening. Phase 2 is days. Phase 3 is the engineering center of gravity — budget accordingly.

---

## 13. Open Questions

1. **Verb vocabulary scope** — start with the nine verbs above, or derive the full set from the crosswalk and song-one artifacts first?
2. **JSON vs. SQLite** for `keywords.json` — decide by record count and whether the Pi serves it over MCP with query load.
3. **Ledger location** — `working/` file (per-project) vs. MCP resource (per-console). Probably both, with the file as source of truth.
4. **Beat Grid → schema** — does Beat Grid emit intent objects directly, or a song manifest the compiler expands? Affects where timing lives.
5. **Template engine** — Jinja2 vs. plain string templates. Jinja2 wins on version directories; confirm it's available in every execution environment (it is not guaranteed in Claude.ai sandboxes without install).
6. **2.3.x support depth** — full parallel templates, or only the verbs whose syntax actually differs?
7. **Public release shape** — skill-only, skill + Field Manual appendix, or skill + Pi image?

---

## 14. References

- `MA3_MCP_Server_Spec_v1.md` — §4 tool tiers, §5 code-gen validation (Lua skeleton, `luac -p`, allowlist, yield check), §6 resources (`ma3://keyword-reference`), §8 learning log
- `GDTF_MVR_Patch_Pipeline_v0.1.md` — PATCH DAY pipeline and verify checklist
- `13_GridCompositionApproach.md` — relationship-not-position doctrine
- `File_Organization_Patterns_v0.6.md` — tier model, session lifecycle, graduation path, frontmatter profile
- Anthropic skill-creator conventions — skill anatomy (`SKILL.md` + `scripts/` + `references/` + `assets/`), progressive disclosure, organize-by-variant, description as trigger mechanism, `package_skill.py`

---

*End of brief v0.1. The parts most worth arguing about: §6.2 verb vocabulary, §8 rule 3 (where the gate sits), and §12 phase boundaries.*

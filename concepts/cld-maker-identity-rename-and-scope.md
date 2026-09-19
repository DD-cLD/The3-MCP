---
id: cld-maker-identity-rename-and-scope
title: "cLD MAker (was beatgrid): renamed tool, scope widens beatgrid→cue list→cues→cue specifics→desk; spec pack at v0.2, Codex-ready; cue-PARTS gap re-ranked P2 behind the manual contract"
role: tools
tags: [tourshow, cld-maker, process]
when_to_load: "Before touching CLD_MAKER_SPEC, planning a cLD MAker feature, or referring to the tool by name — current identity, ratified scope (v1 vs v1.1), spec-pack version status, and the current build-priority ranking"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD] (Dave); wrap 2026-07-17-cld-maker-spec-review-handoff; assessment + re-ranking extended 2026-07-21 [0721-3cLD] per wraps/2026-07-21-external-review-and-method-direction.md and WORKING/CLD_MAKER_PRIMARY_TOOL_ASSESSMENT_v0.1.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Rename:** beatgrid RENAMED → **cLD MAker** — a name collision with an existing product was found in the wild; the tool is not being released under the old plan, but the new name stands regardless.

**Scope widens:** beatgrid → cue list → cues → cue specifics → desk, built as a polished web app. Framed in the session wrap as the missing middle of the pipeline: audio→grid→treatments already exist, the MCP write lane already exists — cLD MAker is the cue-authoring-and-export layer in between.

**Scope ratified in talk-through (Dave):**
- **Cue strip** — video-editor-style cells.
- **Cue inspector** — its fields ARE the console recipe model (six bind slots; see `recipe-part-property-surface-lua-dump` for the live-dumped bind-slot inventory this maps onto).
- **Groupings section** — festival group theory made operational: plot in → role-slot remap → Group XML out (see `tourshow-festival-group-theory`).
- **Dashboard** — indexes tour docs + boards + CHOREOGRAPHY as a timeline lane; locale events (e.g. "{ARTIST} to DSC") feed QCaller prompts + specials/position-preset planning (see `choreography-lane-generalizes-stemsets` for the underlying architecture pattern).
- **Two-layer sandbox** — a repo copy for Codex to build against, plus `cLD_SANDBOX` for imports (see `cld-maker-build-lane-economics`).

**Spec pack authored (Sonnet/Opus lane):** `beatgrid/Meta/CLD_MAKER_SPEC_v0.1.md` (product/architecture spec — supersedes nothing, extends `BEATGRID_SPEC_v0.3`) + `beatgrid/Meta/cld_maker_handoff/` (`schema/cld_maker_session.schema.json`, `fixtures/` + `FIXTURES_README.md`, `CODEX_BRIEF.md` — clean-room per `persona-memory-sovereignty` — and `ACCEPTANCE_CHECKLIST.md`). Design source: `CLD_MAKER_DESIGN_NOTES_v0.1.md` (WORKING root).

**v1 / v1.1 scope locked (Dave)** — decided after the dual external review (see `external-cross-vendor-review-lane-pattern`) and the live Export Sequence capture that over-resolved its #1 blocking item:
- **v1:** schema + cue inspector/Approve gate + Sequence-XML export (recipe-only — see `export-sequence-xml-schema`'s design implication) + choreography→QCaller heads-up + QCaller append (appends to existing QCaller output rather than regenerating it).
- **v1.1** (all seams reserved): groupings panel; palette-ma3 lock (closes the empty-`ma3`-field gap — see `cld-maker-corpus-and-schema-validation`); TC-event export (schema already fully captured — see `export-timecode-tc-event-xml-schema` — so this seam is unblocked whenever it's picked up).

**Status: MELDED and applied → v0.2, Codex-ready.** Schema revalidated 11/11 real sessions clean under the new constraints (see `cld-maker-corpus-and-schema-validation`). Golden fixture: real `cld_seq102_inspect.xml` (see `export-sequence-xml-schema`). Also applied at the meld: the persistence/clean-authoring doctrine (`clean-authoring-and-persistence-doctrine`), plus verbatim meld items not further decoded here — "five-section fix," "literal-phase restatement." Pack: `beatgrid/Meta/CLD_MAKER_SPEC_v0.2.md` + `beatgrid/Meta/cld_maker_handoff/` (CODEX_BRIEF, ACCEPTANCE_CHECKLIST, schema, fixtures, MELD_v1, review docs); the v0.1 spec file is now stubbed to redirect to v0.2.

**Relation:** `cld-maker-build-lane-economics` for who builds this (Codex as contractor, cLD as lead). `external-cross-vendor-review-lane-pattern` for how the pack was verified before the meld.

**Gap identified 2026-07-21 (Dave), post SONG_G first-pass build:** the cue inspector (see `cld-maker-v1-build-landed-and-verified`) currently models **ONE recipe LINE per cue** — Selection/Values-Preset/MAtricks/Filter/Output Filter/Generator, Phase, Measure, Enabled — which can hold everything a single recipe has, but a cue **cannot stack multiple lines**. Real looks need **cue-PARTS / multi-line support** — e.g. a key-solid line + a field line + a breathe-phaser line + a flavor-phaser line simultaneously in one cue, matching how the console's own Cue→Part→(multiple recipe lines) structure works. Without this, MAker can plan a look's *first* layer but not the layered look itself — directly relevant to why the SONG_G first-pass build ended up single-layer/flattened rather than the intended layered recipe build (see `review-plan-gate-precedes-programming-doctrine`).

**Tool assessed + cue-PARTS RE-RANKED P2, 2026-07-21 [0721-3cLD] (Codex external review + Dave):** cLD MAker earns a **conditional yes** as the off-console recipe-authoring surface — the blocker remains cue-PARTS (still one recipe line per cue as of this pass). Codex's sharpened recommendation, which Dave adopted: **build the MANUAL executable per-song contract FIRST** (the closed, zero-pick-at-desk deliverable — see `executable-per-song-contract-doctrine`), and treat cue-PARTS tool support as **P2**, second in line behind that. Full assessment: `WORKING/CLD_MAKER_PRIMARY_TOOL_ASSESSMENT_v0.1.md`. This re-ranks, but does not retract, the cue-PARTS gap above — it is still the needed feature for Codex to eventually spec and build, just not the immediate next move.

History: created 2026-07-17 — rename, scope ratification, and v0.1 pack authored earlier in the session; updated same day within this same concept to record the v1/v1.1 scope lock and the v0.2 meld (Codex-ready) that closed the session. Same day, later: v1 BUILD LANDED and confirmed workable live on Dave's screen — see `cld-maker-v1-build-landed-and-verified`. Extended 2026-07-21: cue-PARTS/multi-line gap identified post SONG_G first-pass build — v1's cue inspector holds one recipe line per cue, needs multi-line stacking to express layered looks; queued for Codex. Extended 2026-07-21 [0721-3cLD]: external review (Codex) issued a conditional-yes tool assessment and re-ranked cue-PARTS to P2, behind building the manual per-song contract first — see `WORKING/CLD_MAKER_PRIMARY_TOOL_ASSESSMENT_v0.1.md`.

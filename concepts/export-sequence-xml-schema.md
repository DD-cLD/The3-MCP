---
id: export-sequence-xml-schema
title: "Export Sequence <n> XML schema — fully self-contained: Sequence>Cue>Part>{cooked PresetData + StandardRecipe}, dependencies embedded recursively"
role: programmer
tags: [ma3, xml-schema, recipes, sequences, v2.4]
when_to_load: "Before reading, generating, or hand-authoring a Sequence-export XML file (e.g. cLD MAker's Sequence-XML export feature, or any parts-per-century multi-part emitter) — the full element/attribute shape, bind-slot ref format, dependency-embedding behavior, and the multi-part census/import gotchas paid for on the SONG_C build"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD], console live 2.4.2.2 — Export Sequence 102, Dave exported live at desk, cLD read via Desktop Commander; UPDATED findings/INBOX.md [0731-2cLD] 2026-07-31 (multi-part census/import facts, SONG_C seq 1210 build) + wraps/2026-07-31-song-b-heard-song-c-built.md; UPDATED findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: bind-census exact location, recipe-line direct-children-only census rule, binds-vs-content location)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Ground truth confirmed:** Dave's claim proven live — "the recipe goes along with the sequence." `Export Sequence <n>` produces a **FULLY SELF-CONTAINED artifact**.

**Schema tree:**

```
GMA3
 > Sequence (playback attrs)
    > Cue (OffCue/CueZero: No="0" | named cue: No="1")
       > Part
          > <PresetData Size=N>            — cooked snapshot, per fixture
             > <Phaser IDType ID Attribute Phase Measure GridPos GridPosMatr Selective Cooked>
                > <Step Function Absolute Accel AccelSplineType Decel DecelSplineType Width>
          > <StandardRecipe [inv/align attrs] PhaseFromX PhaseToX Selection Preset MAtricks Values Enabled SelectionFromValue>
```

A Part carries BOTH blocks side by side: the cooked `<PresetData>` snapshot AND the live `<StandardRecipe>` — see `recipe-output-precedence-and-cooking-doctrine` for what "cooked" means and which one wins at runtime.

**Bind-slot refs are DOTTED FULL-PATH strings** on the `<StandardRecipe>` element, e.g.:
- `Selection="Default.Groups.cLD DS WING PAIRED16"`
- `Preset="ShowData.DataPools.Default.PresetPools.All 2.Wipe In"` and `Values="ShowData.DataPools.Default.PresetPools.All 2.Wipe In"` (same ref, both attrs — see the dual-fill note below)
- `MAtricks="Default.MAtricks.Phase X 0-180"`

**Dependencies embed recursively:** a `<DependencyExport Size=3>` on the Part EMBEDS the full definition of every referenced object:
- Group — with its full `SelectionData` grid coords.
- Preset — with its own nested `PhaserRecipe` + an embedded Shape dependency.
- MAtrick — with its own `PhaseFromX`/`PhaseToX`.

**One sequence export = a portable, dependency-complete show fragment** — nothing external needs to be resolved to reconstruct the recipe's bindings.

**Worked-example notes (Seq 102, 2026-07-17):**
- **Dual-fill confirmed:** `<StandardRecipe>` carries BOTH `Preset=` AND `Values=` attrs, both populated with the SAME reference (`"All 2.Wipe In"`) — a genuine dual-fill (two attrs actually written), not a single aliased slot exposed under two names. This resolves `assign-cli-recipe-line-grammar`'s open `[VERIFY]` on exactly this question.
- **Both phase carriers coexist:** Seq 102 Part 0.1's `<StandardRecipe>` has its own `PhaseFromX="0°"`/`PhaseToX="270°"` (a part-level override) sitting in the same file alongside a bound MAtricks `"Phase X 0-180"` whose own `PhaseToX="180°"`. Both carriers are present in the export and neither overwrites the other — but which one actually cooks at runtime is still an open item (see `recipe-output-precedence-and-cooking-doctrine`'s "open item" for the evidence and what would pin it).
- **Measure serializes as a display string with a leading space:** `Measure=" 1.00"`.
- **Recipe widths serialize as display strings:** e.g. `"25.0%"`, `"0.0% Thru 100.0%"`.
- **Golden fixture saved:** the real capture is archived as `cld_seq102_inspect.xml` in the cLD MAker handoff pack (`beatgrid/Meta/cld_maker_handoff/`) — see `cld-maker-identity-rename-and-scope`.

**Multi-part cue-part census + import facts (added 2026-07-31 [0731-2cLD], SONG_C seq 1210 build — parts-per-century is now the standing multi-part shape, see `parts-per-century-emit-pattern-and-et-gate`):**
- **Part attribute ORDER is load-bearing on import for multi-part cues.** `SpeedScale` must sit between `MAgic` and `Mode` in the attribute sequence, on EVERY part including part 0/OffCue/CueZero — an emitter that instead places it after `CueInFade` causes the importer to silently absorb the cue's first content part into part 0. Full mechanism and the paid-for incident: `part-attr-order-import-absorption-gotcha`.
- **`SpeedScale="One"` is DEFAULT-ELIDED on export** — a clean export-back of parts that are all at the default Speed Scale shows ZERO `SpeedScale` attributes at all. This is a genuine exception to the general rule that MA3's export writes exhaustive attribute sets (so absence is normally usable negative evidence): **absence of `SpeedScale` in an export-back is NOT itself evidence that an import dropped it** — it may simply mean the value is `One`. Non-default Div values (e.g. `Div2`/`Div4`) DO serialize and were confirmed to survive import/export round-trips.
- **Export-back bind-slot refs resolve to NAME-FORM, even when the object was deployed/authored in slot-form.** E.g. `Phaser.cLD SONG_C MARK SINE`, `Dimmer.50` — the console always exports references by name. **Any census parser reading an export-back must count by NAME, not by slot** — a slot-form counter silently reads zero and reports a false miss.

**Design implication (cLD MAker):** per `recipe-output-precedence-and-cooking-doctrine`, a hard/cooked value always beats a recipe — so a Sequence export that includes the cooked `<PresetData>` block would PIN an imported recipe to stale frozen values instead of letting it recompute per rig. Consequence: **cLD MAker's Sequence-XML export must be RECIPE-ONLY by default** — strip or make optional the cooked `<PresetData>` block. A separate deliberate "freeze this look" mode can export cooked values on request. This landed as CLD_MAKER_SPEC §6 export scope at the v0.2 meld — see `cld-maker-identity-rename-and-scope`.

**Relation:** `recipe-xml-schema` is the different PhaserRecipe-*template* dialect (a recipe **preset**, not a cue-part's StandardRecipe) — same dotted-path convention for Shape refs, different element shape. `baked-phaser-preset-xml-schema` is the baked/Export-Preset dialect — its `<PresetData>` block is the same cooked-snapshot shape that rides alongside `<StandardRecipe>` here. `shapes-pool-facts` for what a Shape dependency itself holds. `export-timecode-tc-event-xml-schema` for the companion Export Timecode schema cracked the same session, which targets a Sequence by the same dotted-path convention. `part-attr-order-import-absorption-gotcha` for the full multi-part attribute-order incident. `parts-per-century-emit-pattern-and-et-gate` for the standing multi-part architecture this schema now has to serve. `smith-packet-must-stage-multi-part-golden` for the certification consequence of these multi-part facts.

## Extended 2026-08-01 [0801-2cLD] — a cue Part can carry NO Name attribute at all, proven and kit-patched

**Sequence-XML: a cue may carry NO `Name` attribute on its Part at all** — observed on {LD}'s own SONG_J cue 28 (nameless, zero StandardRecipes, a trailing cue). This is broader than the existing OffCue/CueZero no-Name convention already known for this dialect (see `authored-sequence-dialect-vs-desk-golden-fixed-diffs`) — this is a regular, non-OffCue/CueZero cue with no Name at all. The build kit was patched to emit such a cue correctly: no `Name=` on the cue header, and a Part carrying the standard PART attributes plus `Sync`/`Morph` but no `Name`. **Round-trip verified:** export-back reports `nameless=1`, and all 43 other cues in the same file kept their Name. The SONG_A regression stayed BYTE-EXACT 5/5 across both patches to the kit.

## Default-elision family, 2026-08-01 [0801-2cLD]

**Desk exports default-elide `SpeedMaster` on a `Sequence` element entirely** (SONG_I's `gb_s1900.xml` export has none) — the same elision family as `SpeedScale="One"`'s default-elision already noted in this concept. Absence of `SpeedMaster` in a desk export is not itself evidence of anything wrong; it means the value sits at its default.

## Bind census + recipe-line census laws, weighted 2026-08-04 [0803-3cLD]

**GOVERNING (G=0.9) — bind census: count binds by NAME from the export-back `Dependency`
element's `RelAddr` attribute; a slot-form counter reads zero.** This sharpens the existing
NAME-form census law above (2026-07-31) with the exact XML location: the countable bind
reference lives on `Dependency/@RelAddr` inside a Part's `DependencyExport`, not on the
`StandardRecipe`'s own `Selection=`/`Preset=`/`Values=`/`MAtricks=` attributes directly. (A
distinct, numeric `RelAddrNum` attribute also exists — see `recipe-xml-schema` — treat the two
as separate attributes until proven otherwise; don't conflate them.)

**CONSTRAINING (G=0.7), scoped to parsing a {LD} export — recipe-line census: read a Part's
`StandardRecipe` DIRECT CHILDREN only.** Recursive iteration also walks into each Part's
`DependencyExport` and counts the wrapper `StandardRecipe` copies embedded inside a bound
Preset's own dependency tree (see `source-matricks-wrapper-recipe-encoding`) as if they were
additional cue lines — silently inflating the total. This generalizes the parser-census
correction already on file in `recipe-layer-is-fixture-agnostic-doctrine` (105 direct-child
StandardRecipes vs. 10 more nested inside DependencyExport, wrongly countable) into a standing
rule for any new source-export parser.

**CONSTRAINING (G=0.7), scoped to reading an export-back — where binds vs. content live:
binds are in `Dependency`; content is in `Cue/Part/PresetData/Phaser`.** The `<Preset>` stub
that appears nested under a `<Dependency>` is EMPTY by design — it exists to let the resolver
identify which preset is referenced, not to carry that preset's own data a second time. Don't
read an empty embedded `<Preset>` stub as a corruption signal.

## Three more schema/census facts, SONG_L build, 2026-08-05 [0805cLD]

1. **Grep-counting a slot/name string double-counts.** A `<StandardRecipe>` carries the SAME
   reference on BOTH `Preset=` and `Values=` (the dual-fill already noted above), so a raw
   string count like `xml.count('Phaser.NNNN')` reads **2x** the true line count — SONG_L
   read `21.2222 x30` for 15 actual lines. Divide by two, or count `<StandardRecipe` elements
   instead. **MAtricks does NOT double-count** (single `MAtricks=` attribute) — 23 MX binds
   against 23 phaser lines landed exact.
2. **An export-back legitimately carries `PresetData`, and that is normal.** SONG_L's
   export-back holds 75 `PresetData` blocks against an authored file with 0 — the console
   cooks on export and embeds the snapshot alongside the live `StandardRecipe`. **The
   recipe-only authoring doctrine (`universal-presets-emitter-aware`'s doctrine-lint) applies
   to the AUTHORED deliverable, not the export-back read after import** — do not read a
   non-zero `PresetData` count on an export-back as a doctrine failure. Also: never re-import
   an export-back as a restore, since its cooked layer carries `&apos;`-quoted refs that kill
   resolution silently (see `import-resolver-laws`).
3. **A bind authored in SLOT form survives a rename of the bound object; one authored in NAME
   form would not.** MAtricks 183 was renamed (`cLD W2 G14 X-45to-90` → `cLD W2 G5
   X-45to-90`) AFTER a sequence was emitted against it, and the export-back resolved the bind
   correctly with no re-emit needed — because the emitter had written
   `MAtricks="Default.MAtricks.183"` (slot form), a rename of the target object is invisible
   to an already-authored bind. This is the authoring-side complement to the NAME-form
   export-back census law above (export-backs always resolve refs by name on the way OUT;
   this is about what the emitter writes on the way IN).

History: created 2026-07-17 from the live Export Sequence 102 capture — first ground truth on the Sequence-export schema, and the finding that over-resolved the #1 blocking item from both external spec-pack reviews (see `external-cross-vendor-review-lane-pattern`).

History: extended 2026-07-31 [0731-2cLD] — added the multi-part Part attribute-order import hazard, the `SpeedScale="One"` default-elision caveat, and the export-back NAME-form census law, all paid for or discovered during the SONG_C (Seq 1210) parts-per-century build.

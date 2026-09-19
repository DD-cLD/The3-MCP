---
card: AUTHORING
version: "0.1"
created_at: 2026-07-24
scope: "Building song content OFF-console — XML dialects, macros, groups, presets, recipes, phasers, sequences"
not_scope: "Live console contact (CARD_DESK) · timecode (CARD_TIMECODE)"
---

# CARD — AUTHORING

**What this is:** the error messages grandMA3 refuses to print. Every line below is a
place the console accepts your work, echoes OK, and silently does the wrong thing.
Nothing here is derivable — it was all paid for. Each line ends in its concept id;
open that body only if you need the full story.

---

## ⛔ THE FIVE THAT HAVE ACTUALLY COST US A SESSION

1. **Raw `"` inside a single-quoted macro `Command` attr → MA3 TRUNCATES at the first quote.** XML-legal, parses fine in Python, import echoes OK. `Command='Label Group 60 "cLD BACKLIGHT ALL"'` landed as the fragment `['Label]`. Escape as `&quot;`: `Command="Set Selection 1 MAtricks &quot;XShift&quot; &quot;-1&quot;"`. `macro-xml-schema-cracked`
2. **`Attribute="ColorAdd"` is WRONG and fails SILENTLY** → empty preset, no error. Correct: `ColorRGB_R` / `ColorRGB_G` / `ColorRGB_B`, values 0–100. `baked-phaser-preset-xml-schema`
3. **Every `Store Preset` carries `/Universal` — dimmer included, not just colour.** Plain `Store` takes console-default scope, looks perfect, resolves wrong per fixture type. `universal-presets-emitter-aware`
4. **A hard stored value ALWAYS beats a recipe.** Recipe output is only the fallback, resolved at whichever level holds the hard value. Bake nothing you want a recipe to drive. `recipe-output-precedence-and-cooking-doctrine`
5. **Multi-part cue-part attribute ORDER is not free-form on import.** `SpeedScale` must sit between `MAgic` and `Mode`, on every part incl. part 0/OffCue/CueZero. Out-of-order (e.g. after `CueInFade`) silently absorbs the cue's first content part into part 0 — 33 SRs moved this way in one SONG_C build. Clone the golden's part-attr order byte-for-byte. `part-attr-order-import-absorption-gotcha`

---

## PHASE MATH — literal, never inferred

- Full spread: **`PhaseTo = 360 − (360 / N)`** — stops short of 360° so first and last don't collide. `phase-math-formulas`
- Line-by-line (X and Y are NOT symmetric): **`PhaseToX = (360 / Y) × ((X − 1) / X)`** · **`PhaseToY = 360 − (360 / Y)`**. `phase-math-formulas`
- Effective N: Wings = `ceil(total / wings)` · Group = `group_count` · Block = `ceil(total / block_size)`. Wrong sub-formula skews the whole spread silently. `phase-math-formulas`
- **N = the FULL grid extent INCLUDING gaps**, not the occupied-cell count. A gap consumes a full beat. `matricks-phase-distribution-on-gappy-grids-open-question`
- **MAtricks pool Phase is a LITERAL manual value. Never trust the encoder bar** — Encoder Bar Phase auto-calculates and is not what gets stored. `mtricks-phase-vs-encoder-phase`
- `XWidth` re-wrap uses each fixture's **ABSOLUTE grid X mod width**, not selection order — a non-zero grid origin gives uneven rows. `matricks-xwidth-wraps-on-absolute-grid-x`
- Measure: runtime scale = `Measure ÷ (Σwidths / 100)`; per step = `Measure × width ÷ Σwidths`. Widths are not rewritten — only the rate scales. `measure-layer-math`
- Measure is **not** a Lua-readable/settable property on a recipe part or a Preset object. `measure-not-a-safe-lua-property-part-or-preset`
- **`Copy Preset` does NOT carry `Measure`** — a copied template figure needs `Edit Preset <n>` → `Measure <n>` → `Update` → `ClearAll` reapplied by hand, every time. `phaser-copy-does-not-carry-measure`

## SELECTION & GROUPS

- **`Thru` right-hand side must NOT be fully qualified.** `Preset 4.101 Thru 105` = OK · `Preset 4.101 Thru 4.105` = **Illegal object**. `preset-pool-thru-range-syntax`
- `Fixture 301 Thru 301.16` (bare left, dotted right) silently selects **only the `.16` sub**, not a range. `subfixture-thru-range-syntax`
- **Group membership follows a re-FID** — groups bind the OBJECT, not the number. After any re-FID, carve moved fixtures out of stale groups by hand. (GS type-bakes behave the OPPOSITE way — they do not survive a repatch.) `group-membership-follows-refid-not-number`
- `handle:Children()` returns **0** for Group objects. The only reliable census is `Export Group <n>` → read `SelectionData Size`. `handle.Count` is a METHOD — call `handle:Count()`. `group-xml-export-selectiondata-census`
- `ObjectList('Preset 22.1 Thru 22.46')` returns an **empty list, no error**. Use the wildcard: `ObjectList('Preset 22.*')`. `objectlist-thru-vs-wildcard-gotcha`
- `Store <Object> <n> "Name"` labels inline at store time — a separate `Label` line is unnecessary and is exactly the line type the quote bug destroys. `store-with-inline-name-labels-object-idiom`
- **In an inherited file, cLD's own contract groups sit RELOCATED from their sandbox numbers** — `cLD SPOTS ALL` is Group **181** in the gov file, not the predicted 101 ({LD} holds 1xx). Bind by exact NAME, never by contract arithmetic. `tourshow-group-contract-v01`

## RECIPES & PHASERS

- **Pool objects bind with `Assign`, never `Set`.** `Set` with a pool number silently does nothing. `assign-cli-recipe-line-grammar`
- Recipe-line writes need the `Property` keyword: `Set Sequence <x> Cue <y> Part 0.1 Property "Name" "Value"`. Required syntax, not style. `recipe-line-set-property-syntax-and-value-casing`
- `Enabled` accepts **only** `Y/N`, `YES/NO`, `0/1`. Mixed-case `Yes`/`No` does **not** take. `recipe-line-set-property-syntax-and-value-casing`
- Recipe line address is a dot sub-index on the Part: `Part <p>.<r>` (e.g. `Part 0.1`). `recipe-line-cli-addressing-and-list-readback`
- **Stock phaser-recipe presets are EMPTY.** A bare CLI call or pool tap silently no-ops — only a recipe line cooks them. `stock-recipe-presets-empty-as-templates`
- `PlaybackDirection` does **not** exist on a cue-part recipe line (preset-phaser only) — `Set` on it fails silently. `recipe-line-playback-properties`
- Recipe XML: a layer only takes effect if named in the semicolon list `Has="Measure;AdaptiveMeasure;Speed;…"` — set-but-unlisted values are silently inactive. `recipe-xml-schema`
- Recipe XML phase values are **display strings with a degree sign** (`"180°"`), unlike the baked dialect. `recipe-xml-schema`
- Baked-phaser XML `Measure`/`Speed` are **2^24 fixed-point ints**: stored = value × `16777216` (Measure 2 → `33554432`). `16777216` is literal 1, not a "none" sentinel. `phaser-preset-xml-measure-speed-fixed-point-encoding`
- One universal template row — `IDType="2" ID="1"` — imports and works across every patched ID. No per-fixture entries needed. `baked-phaser-preset-xml-schema`
- v2.4 renamed the UI mode "Universal" → "Generic"; the store flag is still `/ForceUniversal`. `baked-phaser-preset-xml-schema`
- **MA3 auto-suffixes a DUPLICATE preset name with `#2`, silently.** Labelling a preset with a name already used in that pool returns `ok`, no error, no warning — the readback is the only tell. **Every cLD-authored preset carries the `cLD ` prefix**, which dodges it and makes provenance readable. `cld-sandbox-and-namespace`
- **`PresetMode` is NOT evidence of portability, and swapping the group does NOT fix it.** A preset can read `PresetMode="Global"` while its `PresetData` holds per-fixture `Selective` rows with baked phase AND its `DependencyExport` embeds the actual GROUP objects it was built against. **Read the rows AND the dependencies — re-author, don't re-point.** `recipe-layer-is-fixture-agnostic-doctrine`
- CLI value ranges are **SPATIAL, not temporal** — `At 0 Thru 100` fans the selection as ONE step. Temporal steps need the Phaser Editor. `v24-phaser-model`
- **When spec-reading an inherited phaser preset, grep the export for `XWings`/`XGroup`/`XBlock`/`XShuffle`/`YShift`/`Width` literals FIRST** — the store-time `/MAtricks` embed travels with the preset export as literal attrs. Phase-distribution inference is the fallback, not the method. `matricks-store-time-embed-travels-with-preset-export`

## SEQUENCE & CUES

- **`CueFade` is not a real property.** `Set … Property "CueFade"` compiles, echoes clean, no-ops. Real Cue props are only `TRIGTYPE`, `TRIGTIME`, `TRIGSOUND`, `FADERENABLED`. `cuefade-not-a-real-property-gotcha`
- Set `UseExecutorTime=No` — with `Yes`, the executor's time silently overrides sequence fades. `cuefade-not-a-real-property-gotcha`
- Cue 5's internal `.no` is **5000** (display ×1000). `Cue 5000` resolves nil; wildcard `Cue *` enumerates by `.no`. `cue-display-number-vs-no-addressing-gotcha`
- The property is **`CommandEnabled`**, not `CommandEnable` — the short name fails silently. `command-enabled-property-name-gotcha`
- A Sequence export's cooked `<PresetData>` block **pins the imported recipe to frozen stale values**. Omit it from recipe-only exports. `export-sequence-xml-schema`
- `Measure` serializes with a **leading space**: `Measure=" 1.00"` — an easy silent string-match miss. `export-sequence-xml-schema`

## MACROS

- **Macro lines never batch with `;`** — one command per line. The interactive CLI *does* batch; don't confuse the lanes. `macro-line-syntax-and-batching-rule`
- Absent `MacroLine` attribute defaults: `Execute=Yes`, `AddToCmdline=No`, `Wait=follow`. `Command` is the only always-present attribute. `macro-xml-schema-cracked`
- Macro-line cells are exactly five: Command / Wait / Enabled / AddToCmdline / Execute. There is **no "Trigger" cell** (MA2 carryover myth). `macro-manual-gap-and-study-doc`
- No true if/then/else exists. `If`/`EndIf` is **scope restriction** — a WHERE clause on the next command, not branching. `macro-conditional-branching-not-implemented`
- `Macro X.Y` calls **that ONE line**, not "start macro X at line Y". Nested calls do **not block** — the parent's next line fires immediately. Bare-called sub-macros die with the parent. `macro-call-and-nesting-lifetime-semantics`
- File-side `Handles` serialize as raw hex and **dangle or resolve to the WRONG object** in a different show. `macro-handle-persistent-object-reference`

## ⚑ SELF-VERIFY BEFORE THE ARTIFACT LEAVES YOUR HANDS

A structure census (right count, right names) is **not sufficient** — it never catches a scope or dialect mistake. Lint explicitly, every time:

1. Zero raw `"` characters inside any single-quoted attribute.
2. Every `Store Preset` line carries `/Universal`.
3. No `PresetData` blocks in a recipe-only sequence export.
4. `UseExecutorTime=No`.
5. Every cue part is a `StandardRecipe`.
6. One command per line in macro XML.
7. Every cLD-authored preset name carries the **`cLD ` prefix** (and readback confirms no `#2` suffix landed).
8. **Diff against a proven same-dialect golden exemplar** before shipping.
9. **Every generated XML file passes an `ET.fromstring` parse (well-formedness), not just lint.** Lint alone missed a regex swallowing a self-closing part tag and eating the next cue whole. `parts-per-century-emit-pattern-and-et-gate`

`authoring-gate-doctrine-retrieval-miss-lesson` · `executable-per-song-contract-doctrine`

---

## ⛔ ONE SCOPED EXCEPTION TO THE `/Universal` RULE — QX40 STB, ruled 2026-08-03

Item 3 above says **every** `Store Preset` carries `/Universal`. That stands
everywhere except **three named objects**, and this note exists so no future
session "corrects" them back:

| object | pool | store mode |
|---|---|---|
| `cLD LED WHITE` | Colour 4.x | **GLOBAL** |
| `cLD LED (R)` | Colour 4.x | **GLOBAL** |
| `cLD RATE (R)` | Beam | **GLOBAL** |

**Dave's reason: GLOBAL so ONLY OUR QX40 look at it.** These address the QX40's LED
engine specifically. Universal resolves through every fixture profile's emitter
engine — which is the whole point of the rule, and the whole problem here. The
rule's PURPOSE is served by the exception.

**If you are authoring a preset and it is not one of those three, `/Universal`, no
exceptions.** `universal-presets-emitter-aware`

**Also ruled the same day — the STB (R) is a PAIR, not one preset.** The QX40-STB
expansion drives both the MM/colour engine and the beam rate, so a release takes
one preset in EACH pool the expansion touches. `tourshow-stb-white-release-ruling`

> **[0805-2cLD] name correction:** live console names for the trio: 4.83 **"QX40 Only W"** · 4.84 **"QX40 Only W (R)"** · Beam 5.8 **"QX40 STB (R)"** — none carry the cLD prefix. Census by NAME uses these. The ruling stands unchanged.

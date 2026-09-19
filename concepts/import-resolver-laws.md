---
id: import-resolver-laws
title: "⛔ Sequence-XML import has THREE separate resolver families — Preset=/Values= is a name/slot minefield: numeric preset names parse as SLOT INDEX, &apos;-quoting kills resolution everywhere, and golden exports lie about pool names; a fourth family (SR-level spread attrs) imports clean with no hazard found so far"
role: programmer
tags: [ma3, xml, import, recipe, sequence, v2.4, resolver]
when_to_load: "Before hand-authoring or generating ANY sequence/recipe XML for import — Selection=/MAtricks= and Preset=/Values= are resolved by DIFFERENT rules, and a numeric-named preset will silently bind to the wrong (or no) object if referenced by name instead of slot; spread attrs (XShuffle/XBlock/PhaseFromX/ToX) are a separate, so-far-clean fourth family"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, 6-variant + 3-variant scratch-import dialect tests on throwaway Seq 1990, onPC 2.4.2.2; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md; extended findings/INBOX.md [0729cLD] 2026-07-29; extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: import-order precondition)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The paid-for cost: one full silent half-import.** A 100-recipe-line sequence imported clean (`ok` echo, correct cue/part/StandardRecipe counts) with 50 of 100 preset bindings silently empty. Only a per-line Lua `:Get('Values')` binding census against a known-good line caught it. **Structure census ≠ content census ≠ binding census** — the first two both pass on a damaged import.

## Three resolver families, not one

Recipe-line bind attributes on a `<StandardRecipe>` are resolved by **at least three different rules**, depending on which attribute is being parsed:

1. **`Selection=` (groups)** — tolerant. Both the short form (`Default.Groups.<name>`) and the long `ShowData…` full-path form resolve correctly.
2. **`MAtricks=`** — rides the SAME family as `Selection=` for its SHORT forms: both the name form (`Default.MAtricks.<name>`) and the slot form (`Default.MAtricks.101`) cook. **The long ShowData form silently DROPS** — the recipe imports with no MAtricks bound and no error.
3. **`Preset=` / `Values=`** — strict, and the dangerous one (see below).

## Preset=/Values=: the long form, the live pool name, and the numeric-name trap

Preset/Values bindings require the **long form path using the pool's CURRENT LIVE NAME** — not a cached or historical one. **Pool 21 in this show is currently named `Phaser` (singular)** — even though {LD}'s own exports encode the path with `Phasers` (plural). {LD}'s exports only survive because they resolve by **GUID**, not by the name-path text. **A golden export's name-path is not proof the name is still current — golden name-paths lie**, exactly like group/preset labels do (see `inherited-file-membership-is-ground-truth`).

Within that long path, the trailing preset token resolves two different ways depending on its shape:

- **Non-numeric name** → resolved by NAME. Spaces and trailing spaces are fine.
- **Numeric-looking name** → resolved as a **SLOT INDEX**, not a name lookup — even when a preset is literally NAMED that numeral.

Several of this show's dimmer presets are *named* plain numbers (`"0"`, `"50"`, …). Writing the numeral as if it were the name resolves to the wrong slot (usually nil):

| Want (preset named…) | WRONG (parsed as slot) | RIGHT (its actual slot) |
|---|---|---|
| `"0"` | `Dimmer.0` → slot 0 = **nil** | `Dimmer.15` |
| `"50"` | `Dimmer.50` → wrong/nil | `Dimmer.9` |
| `"Full"` (non-numeric, for contrast) | — | `Dimmer.5` (slot) **or** `Dimmer.Full` (name) — both work |

**Rule: for any preset whose NAME is itself a number, address it by SLOT, never by typing the numeral as a name.** Non-numeric names are safe by either route.

## &apos;-quoting kills resolution — everywhere

Never `&apos;`-quote a bind-path token, on any of the three attribute families. Quoting a name this way **kills resolution silently**, regardless of which resolver is parsing it.

## Resolution is ONE-SHOT at import time

Path/name resolution happens once, at `Import` time. After the import completes and the show is saved, the recipe holds a **resident OBJECT reference**, not a re-evaluated path string. Consequence: **slot-vs-name addressing is only a hazard on a future RE-import of the same XML** — once resident, the live show is safe; renaming the pool or the object afterward does not re-trigger this resolver.

## Fourth family, proven clean — SR-level spread attrs (2026-07-29)

**`XShuffle`/`XBlock`/`PhaseFromX`/`PhaseToX` authored as plain attributes directly on a cue-part `StandardRecipe` import correctly and read back exact via `:Get`** (`XShuffle=5`/`7`, `XBlock=7`, Phase `0→360` all exact) — proven importing the SONG_T Fill 1/Fill 2 sequences (see `tourshow-fill-layer-rebuild-method`). **The flattened lane (spatial attrs written directly on the cue-part line, instead of {LD}'s wrapper-preset pattern) is PROVEN — wrapper presets are unnecessary for spread/shuffle.**

Unlike `Preset=`/`Values=`, **this family has shown no numeric-name/slot trap so far** — it behaves more like the tolerant `Selection=`/`MAtricks=`-short family than the strict `Preset=`/`Values=` family. Not yet stress-tested against the numeric-name hazard specifically (no spread attribute in this corpus is named a bare numeral), so treat as proven-for-the-cases-tested rather than a blanket guarantee.

## Verification method — the only thing that catches it

An `ok` echo, a correct cue/part count, and a correct StandardRecipe count **all pass on a half-bound import.** The only reliable check is a **binding census**: read `:Get('Values')` (or the equivalent bound property) on every recipe line via Lua and compare against what the line is supposed to hold — never trust the import's own report of success.

**Dialect-test method used to establish all of the above:** build a small variant XML file → import it into a disposable scratch sequence (this campaign used **Seq 1990**) → read back via Lua. Six variants isolated the `Preset=`/`Values=` numeric-slot behavior; a further three variants isolated the `MAtricks=` short/long split. Reuse this scratch-sequence method before trusting any new hand-authored bind-path shape.

**Related:** `sequence-xml-ordered-header-law` (a sibling import gotcha on the same XML dialect); `export-sequence-xml-schema` (the general schema these bind attributes live on); `inherited-file-membership-is-ground-truth` (the same "labels/names lie, only live data is truth" pattern, one layer up); `tourshow-seq1510-build-record` (the build these laws were paid for on); `tourshow-fill-layer-rebuild-method` (the build that proved the fourth, spread-attr family).

## Scope pinned 2026-08-01 [0801cLD] — &apos;-quoting is confined to the COOKED export layer; live StandardRecipe binds are clean

**&apos;-quoting scope corroborated, not contradicted:** a console `Export Sequence` writes `&apos;`-quoted name paths ONLY inside the cooked `<Phaser>`/`PresetData` layer (observed 11,540 instances in SONG_G seq 1710) and inside `<Dependency>` blocks (124 instances) — **live `<StandardRecipe>` bind attributes are 0/66 clean**, and 0 of 34 distinct bind values across the sample carried an apostrophe. **Consequence: an export-back file is a READ artifact only — never re-import one as a restore.** Its cooked layer carries `&apos;`-quoted refs that will kill resolution silently on re-import. Always re-import the AUTHORED file, not the export-back. (Three cLD-authored files checked the same session: `&apos;`=0, lint-confirmed clean.)

## Additional dialect facts, 2026-08-01 [0801-2cLD] and 2026-08-03 [0803-1cLD]

**Bind-path pluralization is unstable across exports — another instance of "golden name-paths lie."** `gb_s1900.xml` (SONG_I) writes `PresetPools.Phaser` **SINGULAR**, where earlier {LD} exports wrote `Phasers` **PLURAL**. Slot-form binds are immune to this instability; name-path binds are not — prefer slot-form where the choice exists, and don't hard-code a plural/singular assumption into a parser.

**MAtrick and StandardRecipe do NOT share one attribute order — never port attribute order across element classes.** `XShuffle` sits beside `XBlock` on a `MAtrick` element, but AFTER `ZWidth` on the desk's `StandardRecipe` wrapper element. An attribute-order fact proven true for one XML element type is not transferable to a different element type carrying the same-named attributes.

**Negative-phase serialization asymmetry (verification-method note):** the desk dialect writes negative phase WITHOUT a degree sign (`PhaseToX="-180.00"`) while positive phase keeps it (`"360°"`). Authored-with-degree negatives still import correctly — but an export-back byte-diff comparison must NORMALIZE this asymmetry before comparing, or a genuinely clean import will read as a false failure. (See `matricks-negative-value-lua-uint32-wraparound-gotcha` for the related but distinct live-Lua-read-side wraparound issue this serialization fact is not the same mechanism as.)

## GOVERNING — import order precondition, 2026-08-04 [0803-3cLD]

**Every object a sequence references — groups, presets, MAtricks, shapes — must already
exist in the show BEFORE that sequence is imported.** This is the direct consequence of
"Resolution is ONE-SHOT at import time" above: there is no lazy or retry resolution, so an
import that runs ahead of its own dependencies binds to nothing (or the wrong slot) and does
not self-heal later. Sequence dependency-creation order, not just bind-path correctness, is
load-bearing.

History: none — all three resolver families established in one session, 2026-07-28, via the scratch-import dialect-test method on Seq 1990. Extended 2026-07-29: added a fourth family (SR-level spread attrs), proven clean on the SONG_T fill-sequence import.

---
id: parts-per-century-emit-pattern-and-et-gate
title: "Parts-per-century sequence architecture (Dave's standing shape) + mandatory ET.fromstring well-formedness gate on every emitter — song-c_emit.py is the template record"
role: programmer
tags: [ma3, sequences, xml-schema, tourshow, tooling]
when_to_load: "Before building a new song's main sequence, or before writing/modifying any Python XML emitter that generates multi-part cues for import — the standing part-layout law and the mandatory well-formedness check every emitter must run before its output is trusted"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (Dave's parts-per-century ruling off the Seq 1510 golden decode; song-c_emit.py ET-gate fix); wraps/2026-07-31-song-b-heard-song-c-built.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Architecture ruling (Dave):** main sequences use **PARTS PER CENTURY** — "clean cue parts for each century reads way better." Standing shape per cue: **part 0** (cue-named, carries fade, usually `SR=0`) + **century parts AS NEEDED** — P1 SPOTS / P2 WASHES / P3 PIX / P4 JDC / P5 BEAMS / P6 RIVALE / P7 PLINE / P8 QX40.

Confirmed live on the Seq 1510 (SONG_T) golden: census 20/19/17/17/7/6/6 parts across 42 cues, 140 parts total, 100 StandardRecipes.

**No-inheritance-of-fade law:** part-0's fade is COPIED explicitly onto every part — parts do not inherit part-0 fade automatically; it must be reapplied to every part on regen.

**SONG_A's mono-part kit emission is NOT the standing shape going forward.** SONG_B (seq 1110) and every remaining song build parts-per-century; the per-part Speed Scale natively solves composite-figure mixed gears (each part carries its own Speed Scale divide). Kit consequence: a parts-aware emitter is added ALONGSIDE the original mono-part `build_sequence` — the SONG_A regression must stay byte-exact.

**`song-c_emit.py` is the template record** for this pattern — the parts-per-century explosion in golden attribute order (see `part-attr-order-import-absorption-gotcha` for why attribute order matters) plus the ET gate below, banked as the reference emitter for every remaining song.

**Emitter safety law, paid for (Lint ≠ well-formedness):** the parts-explosion regex in `song-c_emit.py` matched a SELF-CLOSING part as an open tag and swallowed the next cue whole (Bridge cue 8 swallowed 8.1) — and lint stayed CLEAN throughout, because **lint does not check XML well-formedness.** Fix: **`ET.fromstring` gate is now mandatory in every emitter**, run on the emitted XML before it is trusted, not just a regex-based lint pass.

**Related hygiene rule from the same fix:** a swap-a-slot post-pass must replace WHOLE StandardRecipe lines (both `Preset=` AND `Values=`), not a first-reference-only substitution — a partial replace can leave a line internally inconsistent.

**Relation:** `part-attr-order-import-absorption-gotcha` for the sibling paid-for emitter lesson from the same build. `smith-packet-must-stage-multi-part-golden` for why a multi-part emitter's output needs a multi-part golden to certify against. `export-sequence-xml-schema` for the underlying Part/StandardRecipe schema this architecture is built from.


## PAID smith blocker, 2026-08-01 [0801-2cLD] — protective transforms must live in the SHARED emit path, not per-lane

**Caught pre-deploy: the aux emit lane had skipped the main lane's `SpeedScale`-on-Part insert.** Root cause: the protective transform (inserting `SpeedScale`) had been implemented per-lane rather than in a shared path both the main-sequence and aux-sequence emitters call through. **A per-lane assert only proves its own lane** — the main lane's tests passed because the main lane had the insert; they said nothing about the aux lane, which didn't. Fixed and re-certified PASS. **Standing rule: any protective transform that must apply to every emitted sequence belongs in the SHARED emit path**, not duplicated (and potentially forgotten) per lane.

**Absent SpeedScale is a DISTINCT failure shape from the wrong-position absorption gotcha this concept already documents.** Desk exports legitimately ELIDE `SpeedScale` at its default value, so an export-back diff against a desk export reads clean even when an authored file is missing it entirely. **Only a golden BYTE-SHAPE check catches the omission** in an authored file — a diff against a real export cannot, because the real export's own silence at default looks identical to the bug.

**Re-certifying a one-attribute fix: run the masked structural byte-diff against the golden, not just an attribute-index check.** The attribute-index check alone cannot confirm the fix touched nothing else. Example from the SONG_I aux re-certification: the only delta after the fix was 3 inserted `SpeedScale` tokens, +51 bytes — exactly the expected shape, confirmed only by the byte-diff.

## Census-script trap, 2026-08-01 [0801-2cLD] — the absorption counter false-positives on AUX sequences

**A parts-per-century absorption counter false-positives on AUX sequences**, whose single content part is cue-NAMED (e.g. `'[Full]'`), not `'P<n> '` like a main sequence's century parts. **Century-pattern absorption checks apply to MAIN sequences only** — scope the check explicitly, or it will report a perfectly clean aux sequence as absorbed.

## Scope-with-count discipline, 2026-08-01 [0801-2cLD]

**Self-caught miscount:** workup prose described SONG_I's ×2 gear as "16 sites," but the underlying artifact carries **18 LINES across 14 PARTS** — the prose had been counted off memory/summary rather than the artifact itself. Since Speed Scale is a **PER-PART** knob, PARTS is the load-bearing unit for any claim about it — **always state gear counts as PARTS *and* LINES**, never one alone.

**Mixed-gear cues split cleanly at CENTURY BOUNDARIES — but check the boundary, don't assume it.** SONG_I demonstrates why parts-per-century avoids the mixed-gear problem in practice: both of its per-population split figures (Intro Ramp `1922`, Chorus Ramp `1923`) split exactly on a century boundary — QX40/BEAMS at 270 BPM-equivalent vs Strike M/BEAMS at 135 — so each resulting part resolves to one single gear with zero part-splitting needed. A figure that instead split WITHIN one century would still force an awkward split; verify the boundary lines up before assuming parts-per-century has already solved a given figure's mixed gears for free.

## Composites are SEPARATED, not decomposed, plus the join method that executes it — 2026-08-05 [0805cLD]

**Dave's ruling, on SONG_L:** *"they mixed the fixture types in their phasers, we just
assign them on different cue parts."* {LD} puts several shapes in ONE preset because he
binds one object to a mixed population; our parts-per-century explosion already separates by
fixture family, so **a composite is never decomposed as a puzzle — it BECOMES one part per
century, each with its own bind.** This is what keeps the per-figure object count small: on
SONG_L, 5 objects cover 9 hashed figures across 23 bind sites (see
`tourshow-authoring-contract-v01`'s ingredient-reuse ruling, and
`tourshow-seq2210-song-l-build-record` for the worked example).

**The population→shape join is available in-file and cheap, with zero inference — the
standing method for every future composite.** Each figure's own subtree carries
`Preset/StandardRecipe/DependencyExport/Dependency/Group/SelectionData/Item` (the exact
fixture roster per population) alongside `Preset/PresetData/Phaser@ID` (the per-fixture
shape). **Join the roster against the shape and population→shape falls out directly** — never
infer it from ID prefixes or MAtricks shape. (A probe bug that skipped this method and
inferred from truncated ID prefixes instead produced a real inversion on SONG_L's `Verse
1/2` composite — see `probe-called-unreliable-is-not-evidence`.)

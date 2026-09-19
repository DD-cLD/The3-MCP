---
id: baked-phaser-preset-xml-schema
title: "Baked-phaser preset XML schema (Export Preset) — Preset>PresetData>per-fixture Phaser>Step; Speed/Measure are 2^24 fixed-point (16777216 = literal 1)"
role: programmer
tags: [ma3, xml-schema, phasers, presets, v2.4]
when_to_load: "Before reading, generating, or hand-authoring a baked-phaser preset XML file (Export Preset lane) — the decoded element shape, encoding pinned: see phaser-preset-xml-measure-speed-fixed-point-encoding"
status: active
source: "findings/INBOX.md line 46, 2026-07-17 [0717-2cLD], console live 2.4.2.2, Export Preset → gma3_library/datapools/presets/<name>.xml"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Export lane:** `Export Preset` → `gma3_library/datapools/presets/<name>.xml`.

**Element nesting:** `<Preset transform-attrs>` → `<PresetData Size=n>` → per-fixture-ID `<Phaser IDType ID Attribute Speed SpeedMaster Phase Measure Selective>` → `<Step Function Absolute Accel Decel Trans Width>`.

A **universal preset ships one `<Phaser>` entry PER PATCHED ID.**

**[VERIFY] Sentinel value:** both `Speed` and `Measure` were observed carrying the value **16777216 (2^24)**, read at capture time as a default/none sentinel. **The literal beat encoding for Measure is UNKNOWN.** Do not hand-author a Measure value in this XML schema until verified — the prescribed verification method is: set Measure via the editor, re-export, and diff against this baseline to read off the actual encoding.

**Relation:** this is the baked/exported-preset schema, distinct from `recipe-xml-schema` (the PhaserRecipe-template schema for recipe presets — a different XML shape entirely). See `measure-not-a-safe-lua-property-part-or-preset` for why this file-side XML is currently the only ground-truth path to Measure's step data (Lua object access is closed). See `export-sequence-xml-schema` for the same cooked/baked `<PresetData>` shape as it appears embedded inside a live Sequence export's Part (alongside a `<StandardRecipe>`, distinguished there by a `Cooked=` attribute) — same cooked dialect, different export lane (Export Sequence vs. Export Preset).

**Color presets use this SAME schema (2026-07-21):** a color preset is just this schema with `Attribute="ColorRGB_R"`/`"ColorRGB_G"`/`"ColorRGB_B"` (three `<Phaser>` entries per fixture, one per channel) and a single static `<Step Absolute=N>` (no motion) — NOT a separate dialect. **`Attribute="ColorAdd"` is wrong and fails SILENTLY on import — empty preset, no error.** The `<Preset>` element carries a `PresetMode` attribute; the exported cLD Amber preset `4.102` reads `PresetMode="Global"` with three `ColorRGB_R/G/B` `<Phaser>` entries — a mechanical example of where that attribute sits in the XML, **not** a recommendation to store show colors that way.

**Store mode — corrected 2026-07-21:** the 19 SONG_G color presets (`4.121-139`) were first authored `PresetMode="Global"` this session, which is the **wrong** store mode for this show. {ARTIST} show colors are RGB *intent* and must be stored **Universal** so they resolve per fixture type through each profile's emitter engine — author as Universal (the `/ForceUniversal` store flag; v2.4 renamed "Universal"→"Generic" in the UI). The store-mode ruling, the Q-value emitter strategy, and the v2.4 global-vs-universal balancing tools all live in `universal-presets-emitter-aware` — that is the home for the color-storage doctrine; this file documents only the XML *shape*.

**Hand-authoring shortcut, corroborated 2026-07-21:** contrary to "one `<Phaser>` entry per patched ID" above (which describes what a console EXPORT produces), when HAND-AUTHORING a preset from scratch for import, a single **universal template row `IDType="2" ID="1"`** is sufficient — it imports and works across every patched ID without enumerating one entry per fixture. Used for both the 19 color presets and the `cLD SONG_G BREATHE` phaser preset (`21.123`) this session. Worked breathe example: 2 `<Step>`s, `Absolute="100"` then `Absolute="30"`, `Accel="-100" Decel="-100"` on both (sine easing) — cloned from the `cld_dimsinus_m4.xml` exemplar. See `phaser-preset-xml-measure-speed-fixed-point-encoding` for this same build's Measure-4 fixed-point corroboration.

**⛔ CORRECTED/EXTENDED 2026-07-28 [0728cLD] — the hand-authoring shortcut above is INCOMPLETE for color presets, and the failure mode is silent.** Cloning only the `IDType="2" ID="1"` universal template row is not sufficient: the `<Step>` element **must also carry `Function="ColorRGB_R"`/`"_G"`/`"_B"`** (re-stating the same attribute value that already lives on the parent `<Phaser Attribute=...>`, this time on the Step itself). **Omit `Function=` on the Step and Import still echoes OK — but lands a NAME-ONLY EMPTY preset** (`Active="No"`, zero `PresetData`): a new silent-failure shape where the **NAME CENSUS PASSES while the content is completely absent** — only an export readback catches it, not a live property/name read. Decimal `Absolute=` values are legal (a live {LD} exemplar carries `98.0026`).

**Working dialect, round-trip verified (v.30, `cLD OW WHITE` 95.7/94.9/92.5 exact):** clone every attribute a live exemplar carries, not just the ones prose describes — `Active="Yes"`, `PresetMode="Universal"`, the universal row's `IDType="2" ID="1"`, plus `GridPos`/`GridPosMatr="2360738"` and `Selective="Global"` on the row, and both `Function=` and `Absolute=` on the `<Step>`.

**Standing rule this forces: export a live golden exemplar before hand-authoring any new dialect variant of this schema** — schema prose (including this file, before this correction) is not itself an exemplar. This is the second live collection to force that rule. See `import-resolver-laws` for the sibling sequence-XML import gotchas found the same session, and `tourshow-seq1510-build-record` for the build this was caught on.

Cross-reference: `set-command-unknown-property-fails-silently` for the same silent-fail-on-bad-property-name class the `ColorAdd` trap belongs to; `xml-file-side-authoring-import-lane-proven` for the import lane this schema is authored against.

History: none — schema decoded live 2026-07-17 from a fresh Export Preset read.

History: encoding [VERIFY] resolved same-day (run 14 merge) — Measure/Speed are 2^24 fixed-point, pinned by export-diff; see `phaser-preset-xml-measure-speed-fixed-point-encoding`. Schema itself export-verified; status promoted verify->active. Run 15 (2026-07-17): removed a stale dispatching-agent flag left over from the run-14 shard merge (its concern was already resolved by the History line immediately above it); cross-referenced `export-sequence-xml-schema` for the sibling cooked-`<PresetData>` shape found inside a live Sequence export.

History: extended 2026-07-21 [0721-2cLD] — color-preset use of this same schema documented (ColorRGB_R/G/B Attribute, PresetMode=Global, ColorAdd silent-fail trap), plus a hand-authoring shortcut (single IDType=2 universal template row) and a worked breathe-phaser Step example, both export-verified live building the SONG_G color presets and breathe phaser.

History: corrected 2026-07-21 (crown-jewels scrub) — the earlier "PresetMode=Global is the store mode" framing was a baked-paradigm artifact and is WRONG for this show; {ARTIST} colors store Universal (RGB intent, emitter-resolved). The ColorRGB-not-ColorAdd fact, the golden-4.102 schema example, the IDType=2 hand-authoring shortcut, and the breathe Step example are all retained — only the Global store-mode endorsement was scrubbed and redirected to `universal-presets-emitter-aware`.

History: extended 2026-07-28 [0728cLD] — corrected the color-preset hand-authoring shortcut: the earlier IDType=2/ID=1-only description omitted the `Step Function=` attribute and several row attributes (Active, PresetMode, GridPos/GridPosMatr, Selective), and omitting Function= produces a new silent-failure shape (name-only empty preset, passes name census, zero PresetData) caught only by export readback.

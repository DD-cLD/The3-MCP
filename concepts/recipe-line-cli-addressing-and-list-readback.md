---
id: recipe-line-cli-addressing-and-list-readback
title: "A recipe line is addressed as a dot sub-index on the Part — Sequence x Cue y Part <p>.<r> (e.g. Part 0.1) — not a listable named child; List Sequence x Cue y Part 0.1 is the CLI readback lane; on a multi-part cue, address the part by NAME not number"
role: programmer
tags: [ma3, cli, recipes, v2.4, addressing]
when_to_load: "Before writing any CLI command that targets a recipe line inside a cue-part (Set/Assign/List) — the address grammar, the List-based readback lane, and — for a multi-part cue — why the part must be addressed by NAME rather than number"
status: active
source: "findings/INBOX.md, 2026-07-17, live 2.4.2.2 (Dave attended) [0717-1cLD]; extended findings/INBOX.md [0729cLD] 2026-07-29"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Addressing:** a recipe line lives as a **dot sub-index on the Part**, not as a separately-listable named child object — `Sequence <s> Cue <c> Part <p>.<r>`. Worked example from the live session: `Seq 102 Cue 1 Part 0.1` addressed the chase recipe line.

**Not a listable named child:** you cannot enumerate recipe lines as if they were their own object class. The parent Part shows the recipe line inline — `List` inside the cue displays the part as **`"1 P 0"`** with cue-part columns, i.e. the recipe line surfaces as columns on the Part row, not as a separate row of its own.

**Readback lane, live-confirmed:** `List Sequence 102 Cue 1 Part 0.1` **WORKS** — the dotted recipe-line address is directly listable this way. This is the CLI readback lane for confirming any `Set`/`Assign` write made against a recipe line (see `recipe-line-set-property-syntax-and-value-casing` and `recipe-line-pool-binding-via-assign` for the write side).

## Multi-part cue addressing: NAME form is the reliable lane — numeric form misresolved with a dialog open [VERIFY] — 2026-07-29

**Numeric `Part N.1` on a multi-part cue returned `Illegal object` / misresolved** (`Part 0` resolved to the wrong part — the P4 JDC part) **while a sequence-edit dialog was open at the desk** (Dave's read: the open editor context ate it — possibly the same desk-collision family as `desk-clear-callout-before-console-write-rule`, not confirmed as the same mechanism).

**The NAME form works context-independently:** `Part "P3 PIX".1` resolves, Assign-creates lines, and reads back correctly — proven **×14 live** (see `assign-cli-recipe-line-grammar` for the create-on-empty-part behavior this addressing was exercised through). `AddrNative()` confirms the console's own native addressing is name-path (`Sequences.cLD SONG_T.Mark.P3 PIX`), not numeric.

**`[VERIFY]`: retest numeric part addressing with all dialogs closed before trusting it.** Until then, **NAME FORM IS THE LANE for any multi-part cue.**

Cross-reference: `store-recall-recipe-toggle-rules` for the EditRecipe bookend that builds standard recipes; `recipe-lane-end-to-end-verified` for the full worked recipe build this addressing grammar supports; `tourshow-fill-layer-rebuild-method` for the SONG_T air-pixel batch this multi-part finding came from.

History: none — first captured and live-confirmed in one session, 2026-07-17. Extended 2026-07-29: added the multi-part cue addressing finding — numeric form misresolved with a sequence-edit dialog open (name form unaffected, proven the reliable lane); [VERIFY] retest with clean desk.


## Gotcha added 2026-08-01 [0801cLD] — dotted recipe-line reads return NIL when the part NAME contains square brackets

**A dotted `ObjectList` recipe-line read returns NIL when the addressed part's NAME contains square brackets** — e.g. `ObjectList Part '[Full/...]'.N` choked and returned nothing rather than erroring. This is a distinct failure from a genuinely-empty read: the bracket characters in the name break the dotted-addressing/parse path itself. **Export-back is the reliable census lane for any bracket-named part** — don't rely on a live dotted-address read for these (see `cue-names-not-round-trip-stable-content-derived-labels` for why bracket-named parts are common in this corpus — they are {LD}'s content-derived aux-cue naming convention).

**[0805-2cLD] EXTENSION — MX ASSIGN LANE (v2.4.2.2):** CLI `Assign MAtricks <n> At Sequence <s> Cue <c> Part <p>.<r>` returns "Illegal object" — it does not address a recipe line. What works: Lua handle assignment `r.MAtricks = ObjectList('MAtricks <n>')[1]`, where `r` is the StandardRecipe pointer from Sequence→Cue→Part→`Ptr(k)`. Verified 30/30 (SONG_Q) + 48/48 (SONG_O) with per-line readback. NB: this plain property assignment rides Tier 1 through the MCP gate (`delete-command-classifier-tier-gap`); batch in sub-1800-char send_lua chunks (`saveshow-discipline-and-mcp-tier`). **Live property surface (probe):** StandardRecipe exposes Values / Preset / Selection / MAtricks / Enabled / SelectionMode. Values renders in RESOLVED SHORT FORM ("Preset 21.2720"), NOT the XML path form — grepping live objects for 'Phaser' returns zero on a fully-bound sequence; match `"Preset 21%."` instead.

History: extended 2026-08-05 [0805-2cLD] — MAtricks assign lane (CLI Assign…At fails; Lua handle assignment verified 78/78) + live property surface and resolved-short-form Values readback.

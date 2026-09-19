---
id: assign-cli-recipe-line-grammar
title: "Assign CLI grammar rebinds recipe-line bind slots live — Assign <obj> At Sequence x Cue y Part z, bare form, object type routes which slot; on an existing empty part it also CREATES the line"
role: programmer
tags: [ma3, cli, recipes, v2.4]
when_to_load: "Before writing or generating an Assign command to rebind a recipe cue-part's Selection/Values/MAtricks live, or to CREATE a recipe line on an existing empty part — the bare-form grammar, the object-type routing table, the create-on-empty-part behavior, and its Recipe-Editor visual readback"
status: active
source: "findings/INBOX.md lines 34, 35, 39 — 2026-07-17 [0717-2cLD], console live 2.4.2.2; extended findings/INBOX.md [0729cLD] 2026-07-29"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**CLI recipe lane CONFIRMED end-to-end (2026-07-17, live 2.4.2.2).** `Assign <obj> At Sequence x Cue y Part z` rebinds a recipe-line bind slot live, in **bare form — no `Property` suffix required**. Demonstrated on `Assign Group 123/124 At Sequence 102 Cue 1 Part 0.1`, live-swapping Selection across a three-characters demo purely by typed command.

**Object-type routing** (`Assign <obj> At Sequence x Cue y Part 0.1`):
- **Group** → Selection slot
- **Preset** → Values slot
- **MAtricks** → MAtricks slot

**Combined with** List readback (dotted recipe-line address form, e.g. `List Sequence 102 Cue 1 Part 0.1`), `Set` Property writes, and the Enabled toggle, this closes recipe lane 2 (previously UNMAPPED in `low-credit-cli-mcp-first-authoring-doctrine`) — now mapped and MCP-payload-ready.

**Visual readback surface:** the Assign/Set confirmations were observed updating live in the RECIPE EDITOR's cells — the editor is a real-time visual readback surface for CLI writes to recipe lines, pairing with `List` as the text-readback lane.

**RESOLVED 2026-07-17** (live Export Sequence 102 capture — see `export-sequence-xml-schema`): after `Assign Preset 22.9`, BOTH the Values prop AND the Preset prop read back "Preset 22.9" — confirmed as a genuine **dual-fill**. The exported `<StandardRecipe>` carries BOTH `Preset=` and `Values=` attrs, both populated with the SAME reference (`"All 2.Wipe In"` in the Seq 102 export) — two attrs actually written, not a single aliased slot exposed under two names.

**Forum-sourced per-type extended forms** (folded from `recipe-line-pool-binding-via-assign`, forum 69993/69919 — Kanarek, robinhood, chrislose; not all live-verified):
- **Core rule:** `Set` with a pool number **silently doesn't bind** — Assign is the verb (consistent with `set-command-unknown-property-fails-silently`).
- **MAtricks ranged:** `Assign MAtricks 6 At Sequence c Cue 1 Thru Part *.*` — Thru-ranged wildcard binds across every recipe line in the cue.
- **Preset at step level:** `Assign Preset a.b At Sequence c Cue d Part 0.1."PhaserRecipeSteps".<step>.<valuesource>` (nests into `recipe-step-level-cli-write-path`).
- **Shape:** `Assign Shape n At … Part 0.1` — trailing `Property "Shape"` suffix optional (chrislose).
- **Group via Programmer:** `Assign Group X At Programmer <part>.<recipe>` (Kanarek) — alternative to the stored Sequence/Cue address, which IS live-verified above.
- Note: the ranged MAtricks Assign may be an alternate write lane into a recipe's own MAtricks (vs the UI editor per `live-selection-matricks-cli-set-syntax`) — not cross-verified for identical results.

## Assign CREATES recipe lines on existing (empty) parts — 2026-07-29, scratch- and live-proven

**On an EXISTING, EMPTY part:** `Assign Group X At Sequence S Cue C Part P.1` **CREATES line `.1`** and binds Selection (readback-verified). A follow-up `Assign Preset ...` binds Values on that same new line.

**On a NONEXISTENT part:** the identical form **fails LOUD** — `"Illegal object"`. **Parts themselves cannot be Assign-created.** (Part-creation mechanic remains unproven — a `Store Sequence Cue Part N` test is queued but not yet fired.)

**Proven twice:** first on scratch (Seq 1990), then at live scale — the SONG_T air-pixel batch created **7 lines** on existing empty `P3 PIX` parts (Mark `G309`×4.52, `2.1`×1.9, `3.1`×4.51, `22`×1.5, `26.1`×4.53, `27.1`×1.15 + `G310`×1.15 dual kill), census **7/7 exact**, `SaveShow v.41` on disk. See `recipe-line-cli-addressing-and-list-readback` for the companion multi-part addressing finding from the same batch (name-form vs numeric-form part addressing).

**Relation:** this is the CLI grammar that promotes lane 2 in `low-credit-cli-mcp-first-authoring-doctrine` from UNMAPPED to PROVEN — see that concept for the full three-lane strategy. See `recipe-lane-lua-readback-grammar` for the companion Lua-side readback grammar, and `recipe-part-property-surface-lua-dump` for the full bind-slot property inventory this routing table is grounded in. `tourshow-fill-layer-rebuild-method` for the SONG_T fill/air-pixel build this create-on-empty-part behavior was proven on at scale.

History: none — established live 2026-07-17. Same day: the dual-fill `[VERIFY]` resolved by a live Export Sequence 102 capture — see `export-sequence-xml-schema`. Extended 2026-07-29: added the create-on-existing-empty-part behavior (and its loud failure on a nonexistent part), proven first on scratch then at live scale on SONG_T's air-pixel batch.


## EU tour leg attestation, 2026-08 — HANDLE assignment is the proven bulk-repoint form

Live on the tour file, readback-exact, on **existing** recipe lines:

```lua
rl.Values   = <preset handle>
rl.Preset   = <preset handle>
rl.Selection= <group handle>
rl.MAtricks = <matricks handle>
```

**Handles, not pool numbers and not name strings.** This form carried every bulk repoint of the leg: **407** colour-consolidation lines, **65** master-migration lines, **39** pan-shell lines, and the per-venue MX repoints (18 / 19 / 19). Piloted on one line with a readback before each full sweep.

**⛔ Boundary:** this reassigns **existing** lines only. Creating a recipe LINE is not reachable from the wire at all — see `recipe-line-creation-not-wire-reachable`. Dave's note the same week: recipe fields **are** assignable by **macro line** (the Assign lane), which reaches further than raw Lua does.

**Pace the batches.** Reassignment invalidates cooked output and triggers recook storms; a timeout right after a write batch indicts console busy-work before the wire (`wire-timeout-vs-console-busy`).

History: extended 2026-08-28 (librarian, tour leg) — handle-assignment attestation and the creation boundary.

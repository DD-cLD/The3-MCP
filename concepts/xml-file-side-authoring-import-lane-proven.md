---
id: xml-file-side-authoring-import-lane-proven
title: "File-side XML authoring lane proven end-to-end, now three times (presets baked, presets recipe, macros): Export → edit file-side → SaveShow checkpoint → Import .../NoConfirmation → export-back diff"
role: programmer
tags: [ma3, xml-schema, v2.4, mcp, presets, recipes]
when_to_load: "Before hand-authoring any preset (baked or recipe) off-console and importing it, or before surgically editing an existing exported file's span (e.g. a timecode event) rather than composing a whole new object — the proven lane mechanics, GUID handling, and import-filename convention"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD], two live proofs same session; UPDATED findings/INBOX.md [0731-2cLD] 2026-07-31 (sixth proof: TC event surgical-span editing, SONG_B drum-roll repair) + wraps/2026-07-31-song-b-heard-song-c-built.md; UPDATED findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: base64/Desktop-Commander/sha file-bridge mechanism pinned)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The lane:** `Export Preset <slot> "name"` → edit the file file-side (e.g. `sed`) → `SaveShow .../Enumerate` checkpoint (see `saveshow-discipline-and-mcp-tier` standing rule) → `Import Preset <target-slot> "file" /NoConfirmation` → export the target slot back and diff against the authored file to verify. This is the "sleeper lane" for generating console content off-console instead of hand-building it live.

**Proven twice, same session:**
1. **Baked preset:** exported a console-built M4 preset as ground truth, edited it file-side, imported to a scratch slot — landed **byte-identical** except for a fresh console-assigned GUID.
2. **Recipe preset:** exported console-built recipe preset `22.2` (Sine) as ground truth, authored `"cLD Sine 180"` (changed `PhaseToX` 360→180, GUIDs stripped), imported to `22.121` — name and structure verified correct.

**GUID handling — closes a prior [VERIFY]:** stripping GUIDs from the authored file before import works; the console assigns fresh GUIDs on import rather than requiring them to be pre-populated or rejecting the file. This closes the "GUID-on-import" open question **for presets** (the equivalent question for Layout XML imports, tracked in `layout-xml-export-schema-and-import-lane`, is still separately open).

**Import filename convention:** the `Import Preset` filename argument takes **no `.xml` extension** — it resolves from `datapools/presets/` by bare name.

**Proven a third time, 2026-07-19 — macros:** `cLD_POSITION_WIZ_generic_v0.1.xml` was authored entirely file-side (composed from factory-verbatim grammar, see `factory-position-wiz-anatomy-and-porting`), deployed to `gma3_library/datapools/macros/cLD_POSITION_WIZ.xml`, imported, and run live on console successfully — the first cLD-authored macro XML, see `cld-position-wiz-generic-v01-authored-and-deployed`. This is the third dialect this lane has been proven against (baked preset, recipe preset, now macro), and the first where authoring happened without any exported ground-truth file to start from — composed purely from schema knowledge plus factory-verbatim grammar patterns.

**Proven across ALL pool dialects, 2026-07-21 ([0721-2cLD]):** the lane — now named **"Dave's rhythm"** — generalizes cleanly: author XML off-console → Desktop_Commander write to `gma3_library/datapools/<type>/` → `SaveShow` checkpoint → `Import <Object> <slot> 'bare-name' /NoConfirmation` (bare filename, no `.xml`, same convention as presets) → for **builder macros** specifically, `Go+ Macro <n>` fires the import chain → export-census verify. Proven THIS session on: macros (builder macros 6/7/8 in `datapools/macros/`), color presets (`/Global` store mode), phaser presets (the breathe preset), sequences (`cLD SONG_G`, `cLD SLIDE POP`), and timecode (`cLD SONG_G TC`) — five dialects in one session, on top of the three already proven (baked/recipe presets, macros). The **builder-macro pattern** (a macro pool slot whose lines are a sequence of `Import` commands, fired once via `Go+ Macro <n>`) is the concrete mechanism behind "one build-macro authors it all" — see `review-plan-gate-precedes-programming-doctrine`.

**Extended again, 2026-07-31 ([0731-2cLD]) — a SIXTH variant, surgical span-editing rather than whole-object authoring:** for editing individual EVENTS inside an already-exported Timecode file (not composing a whole new object from scratch), the proven move is a byte-surgical edit of one `Track` element's span — verify neighbor tracks stay byte-identical, deploy to `gma3_library/datapools/timecodes/`, `SaveShow` checkpoint, `Delete`+`Import` the object, then export-back census by **per-track EVENT COUNT** (not just Target pointers — a target-only census reads healthy on an event-emptied track). Proven on a live TC repair (SONG_B's drum-roll `Go+`→`Temp` conversion, 4 flips + 5 paired releases, neighbor tracks byte-identical). Named the **"third authoring lane beside CLI and desk."** Full method, file-location, and MCP-tier facts: `tc-xml-event-surgery-lane`. The delete step in this variant carries its own hazard when the object being deleted is a live TC-cutover TARGET rather than the TC object itself — see `tc-cutover-last-and-delete-eats-events-doctrine`.

Cross-reference: `recipe-xml-schema` for the recipe-dialect element/attribute shape this lane authors against; `phaser-preset-xml-measure-speed-fixed-point-encoding` for the baked-dialect's fixed-point value encoding; `saveshow-discipline-and-mcp-tier` for the mandatory pre-import checkpoint bracketing this lane; `macro-xml-schema-cracked` for the macro-dialect schema this third proof authors against; `tc-xml-event-surgery-lane` for the full sixth-proof method (span-surgery rather than whole-object authoring).

## File bridge to gma3_library, pinned 2026-08-04 [0803-3cLD]

~~**CONSTRAINING (G=0.7), scoped to moving files to `gma3_library`: `gma3_library` is not
`device_bash`-reachable.** The proven bridge: base64-encode the file OUT via `device_bash`,
base64-decode it IN via Desktop Commander (which does reach `gma3_library`), and sha-verify
both ends before treating the deployed copy as trustworthy.~~ **SUPERSEDED 2026-08-05 — see
"File bridge simplified" section below: a plain `cp` via Desktop Commander does the whole job,
no base64 round trip.** This was the missing mechanical step behind every "Desktop_Commander
write to `gma3_library/datapools/<type>/`" line already in this concept and its siblings
(`cld-position-wiz-generic-v01-authored-and-deployed`, `plugin-install-loop`) — none of them
previously stated HOW the bytes cross from the authoring side to the Desktop-Commander-
reachable side.

## File bridge simplified — plain `cp` supersedes the base64 round trip, 2026-08-05 [0805cLD]

**Desktop Commander's `start_process` reaches BOTH the Drive-synced repo AND
`~/MALightingTechnology/gma3_library`, so a plain `cp` deploys a file with a `shasum -a 256`
either side.** No base64-out/base64-in round trip, and the bytes never touch the conversation.
Proven on the SONG_L deploy: sha `2f71ee156a0557b1` identical both ends, 50,531 B.
(`device_bash` still cannot reach `gma3_library`, and the **Filesystem MCP is scoped to `My
Drive` + `dev` only** — Desktop Commander is the one tool that reaches it.) This supersedes
the base64 bridge above, which was written when only `device_bash` had been tried as the
outbound leg.

History: created 2026-07-17 — first end-to-end proof of the lane, on both dialects (baked + recipe) in one session. Extended 2026-07-19: proven a third time on the macro dialect (`cld-position-wiz-generic-v01-authored-and-deployed`) — first proof composed without an exported starting file. Extended 2026-07-21: generalized end-to-end across all five pool dialects (macro/color-preset/phaser-preset/sequence/timecode) in one session via the named "builder macro" pattern (Import commands as macro lines, fired by Go+ Macro <n>).

History: extended 2026-07-31 [0731-2cLD] — proven a sixth variant: byte-surgical span-editing of an EXISTING exported file (timecode events) rather than whole-object authoring, on a live TC repair. Full method split out to its own concept, `tc-xml-event-surgery-lane`, since it is TC-specific enough in mechanics (Delete-then-Import of an already-cutover object) to need its own retrieval trigger.

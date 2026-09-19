---
id: tc-xml-event-surgery-lane
title: "TC-XML event surgery lane, proven — byte-surgical span edit of an exported Timecode file (third authoring lane beside CLI and desk)"
role: programmer
tags: [ma3, timecode, xml-schema, import-lane, v2.4]
when_to_load: "Before editing individual TC events (bump/Go+/Temp conversions, timing tweaks) inside an existing timecode file rather than re-recording at the desk or hand-Assigning line by line at the CLI — the proven Export→surgical-edit→reimport chain, plus where TC files live on disk and their MCP tier"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_B drum-roll TC surgery + timecode file-location/tier facts); wraps/2026-07-31-song-b-heard-song-c-built.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The lane:** `Export Timecode <n>` → byte-surgical edit of ONE `Track` element span in the exported file (verify neighbor tracks stay byte-identical; compare pre/post slices around the edited span) → deploy the edited file to `gma3_library/datapools/timecodes/` → `SaveShow` checkpoint → `Delete Timecode <n>` + `Import Timecode <n> 'bare-name'` → export-back census with **per-track EVENT COUNTS**, not just Target pointers (see `tc-cutover-last-and-delete-eats-events-doctrine` for why event counts, not target reads, are the honest census here).

**Proven on SONG_B's drum-roll fix (2026-07-31):** 4 `Go+`→`Temp` flips + 5 paired releases, 0.3s out, neighbor tracks confirmed byte-identical. Checkpoints v.64 (pre-swap) / v.65 (post), both disk-verified.

**"Third authoring lane beside CLI and desk; use for all remaining TC edits."** Joins the proven CLI `Assign`-based cutover (`tc-track-target-cutover`) and hand-typing at the desk as the three ways TC content gets authored or edited.

**Mechanics needed to run the lane:**
- Timecode files live at **`gma3_library/datapools/timecodes/` ONLY** — there is no top-level `timecodes` directory. `Import Timecode <slot> 'bare-name'` resolves from there (same bare-filename, no-`.xml` convention as every other pool dialect — see `xml-file-side-authoring-import-lane-proven`).
- MCP tier: **`Export Timecode` is Tier 2** (gated like `SaveShow`/`Import` — needs the confirm-gate flow). **`Delete`-inside-`Cmd` still rides Tier 1** (ungated) — treat it as unguarded and checkpoint before it fires.

**Hygiene:** the surgical intermediate file (e.g. `cld_tc102_postswap.xml`, resident in both `datapools/timecodes/` and a staging copy) is scratch — delete once the song is confirmed heard.

**Relation:** `xml-file-side-authoring-import-lane-proven` (existing concept — see this run's `updates/`) for the general Export→edit→Import→diff pattern this is a TC-specific instance of. `tc-temp-release-pair-dialect` for the event-XML shape this lane is typically used to edit. `tc-cutover-last-and-delete-eats-events-doctrine` for the standing order governing WHEN this lane may touch an already-cutover TC.

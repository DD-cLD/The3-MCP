---
id: low-credit-cli-mcp-first-authoring-doctrine
title: "Standing lane order for programming actions: MCP first, CLI second, computer-use for exploration/verification only — pixel-driving is the expensive lane to escape"
role: programmer
tags: [ma3, doctrine, process, mcp, cli, v2.4]
when_to_load: "Before choosing HOW to execute a console action (MCP call vs CLI string vs computer-use click) — the standing tool-tier ruling and the current low-credit recipe-assembly strategy"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave + cLD, end-of-session decision, [0716-1cLD] session; 2 complementary captures — authoring decision + correction/hierarchy — merged into one concept)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Standing order for programming actions:** MCP first, CLI second, computer-use reserved for exploration/verification only. Correction folded in same session: the gma3 MCP has already carried real commands (e.g. groups created straight from MCP) — the only prerequisite is starting the console Session, not any config/build task. Next step: prove out CLI recipe assembly, then move cLD's programming onto MCP as the primary lane. Stated purpose of the multi-day CLI/MCP excursion: get to where **cLD does the actual programming**, not Dave via pixels.

**Low-credit recipe-assembly strategy** (pixel-driving = the expensive lane to escape), three lanes:
1. **PROVEN** — the EditRecipe bookend (see `store-recall-recipe-toggle-rules`) builds STANDARD recipes into cues pure-CLI. Limit: standard recipes only — empty phaser-recipe templates don't ride this lane.
2. **PROVEN 2026-07-17 (was UNMAPPED)** — recipe cue-part bind slots (Selection/Values/MAtricks) are live-rebindable via the `Assign <obj> At Sequence x Cue y Part z` CLI grammar, confirmed end-to-end (three-characters demo, no `Property` suffix needed) — see `assign-cli-recipe-line-grammar` for the full grammar, object-type routing table, and its List/Recipe-Editor readback pairing. Combined with `Set` Property writes and the Enabled toggle, this lane is now mapped and MCP-payload-ready.
3. **SLEEPER** — author the recipe preset XML file-side (schema fully decoded, including dependencies/shapes) and drop it into `gma3_library`; one Import would then load a whole per-song recipe set with zero pixels.

Dependency: the MCP OSC session desk task (~10 min, Dave-side) was still pending as of this session's close.

**MCP write lane now FULLY LIVE, not aspirational (2026-07-17, [0717-2cLD]):** the `confirm_gate → send_lua Cmd()` flow ran 5 Tier-2 writes live on `Seq 102 Cue 1 Part 0.1` (Enabled 0/1, Assign Group, Assign Preset, Assign MAtricks) — all OK, RTT 33–68ms, visual **and** Lua readback agreed every time. This is the first session where the MCP-first half of this doctrine (lane 1, above) is proven operational end-to-end rather than a standing intention. First Tier-2 write of the session was `SaveShow /Enumerate` (v0.16→v0.17) — see `saveshow-discipline-and-mcp-tier` for the filesystem verify lane this proved out.

**Relation:** this is the tool/lane-tier doctrine; `model-routing-doctrine-bakeoff-evidence` is the separate model-tier doctrine (which model, not which interface) — the two compose. "Librarian runs = Sonnet-class, standing" was reaffirmed the same session this doctrine was stated.

History: none — doctrine and strategy both stated 2026-07-16, end of session; 2 complementary captures merged into one concept. Updated 2026-07-17: lane 2 promoted UNMAPPED→PROVEN via the live Assign CLI grammar; MCP write lane confirmed fully operational via a 5-write Tier-2 live-fire session.

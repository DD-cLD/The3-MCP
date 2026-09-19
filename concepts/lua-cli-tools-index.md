---
id: lua-cli-tools-index
title: "Project tools index — OSC transport, MCP server, custom plugins, filesystem MCP, librosa pipeline"
role: operational-meta
tags: [process, coachella]
when_to_load: "Orienting to which tool handles which job in this project — remote control, fixture export, phase calc, agenda randomization, or song analysis"
status: active
source: "MEMORY §Tools Index, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

| Tool | Description |
|------|--------------|
| OSC to console | UDP port 8000, `/cmd,s,<command>` (on-site network only) |
| MCP server | Was "Not yet built" as of this entry — see the MCP-build concepts for the now-active Python server |
| PatchExport plugin | CSV fixture export from console |
| PhaseCalc plugin | Phase value calculator popup |
| ShowShuffle plugin | Agenda randomization for nightly variation |
| filesystem MCP | Reading/writing local project files |
| librosa (song analysis) | Master → `beat_track` (BPM/beats), RMS energy bands, beat-sync chroma+MFCC → `segment.agglomerative` (coarse sections), chroma key estimate. Agrees with songbpm/tunebat cross-checks. Full recipe lives in `WORKING/CONCEPTS.md`, "The song-design pipeline" section (not reproduced in MEMORY — load that doc directly for the full pipeline). |

History: the "MCP server: Not yet built" line is stale relative to later corpus sections (the Python MCP server, `gma3-mcp-server-py`, became active — see the MCP-build concepts below); left as-is here since this table is a snapshot of tools known as of 2026-04-01, and the MCP build concepts carry the current state.

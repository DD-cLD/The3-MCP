---
name: ma3-desk-session
description: grandMA3 desk/console session ritual and firing gates (v2, 08-05). Use at the START of any session touching the live console via MCP or OSC, and again before ANY import, macro fire, Go, store, or write chain. Triggers on desk session, console session, Import, Go+, fire the builder, SaveShow, checkpoint, ForceGlobal, ForceUniversal, TC cutover, timecode assign.
---

# MA3 Desk Session Ritual — v2 (08-05)

The console is ONE shared command surface — commands land in whatever context the
desk is in, and its failure mode of choice is silence. Paths relative to
`WORKING/`. Read **`agents/cards/CARD_DESK.md` first** — every way the console
lies while you touch it, one page.

## Bring-up (before ANY console work)

1. `get_console_info` FIRST — fresh PID (changed PID = crash + relaunch; a
   segfault reaches MCP as a timeout), correct `server_version` (stale server
   after any repo change until full app relaunch), roundtrip OK.
2. OSC carries nothing without an active console Session — check before
   debugging anything else.
3. `send_lua` payloads are **expression-only** (wrapped
   `pcall(function() return (…) end)`) — a statement fails silently.
4. Empty-slot census before any builder fires (groups, presets, sequences,
   macro slots — expected vs found, **by NAME**).

## Clearance — PER BATCH, not per session

- **"Desk clear?" callout and Dave's clear-to-fire before EVERY batch.**
  Clearance EXPIRES the moment the operator re-engages. Announce
  **"starting writes" / "writes done"** around every batch.
- Firing-lane ownership is a per-session call made together at the desk; the
  gates apply identically whichever way it goes. Smith agents never fire the
  console.

## Checkpoint + store law

- **`SaveShow '<name>' /NoConfirmation` BEFORE every import chain** — full
  explicit form: name AND flag (single quotes inside a Lua long bracket).
  `/Enumerate` for checkpoint versioning. LoadShow stays denied.
- Scope-forcing stores: `Store /ForceUniversal` for universal presets,
  **`Store /ForceGlobal`** for globals (Dave, 08-03). **CLI is the primary
  lane** — file-side scope-flag surgery is the fallback, not the default.
- `Import <slot> '<bare-name>' /NoConfirmation`; sha-verify every file
  container → `generated/` → `gma3_library` before it.

## Verify — never trust a clean echo

- **LINE-READBACK DIFF** after any macro/sequence import: read the lines back
  off the console and diff against the authored file BEFORE anything fires.
- **CLI history audit**: every macro line logs `(Macro N 'name')OK:` /
  `Illegal object:` — read the tail after every builder run.
- **Export-back census BY NAME, never slot-form** — a slot-form counter reads
  zero silently. Export-backs carry cooked PresetData: serialization authority
  only, never re-import one. A clean import proves nothing below the structure
  layer.

## TC cutover — LAST, on Dave's word, its own step

- ⛔ Never fold the cutover into the import chain. **Deleting a TC-targeted
  sequence eats the track's events; MOVES preserve them.** {LD}'s sequences
  are the rollback state — TC resting on them during a build is a feature.
- `Assign Sequence <seq> At Timecode <tc>.1.<N>` — the dot-index EXCLUDES the
  Marker track, so `.1.1` is the main.
- **Target by track CONTENT, never by assumption** (the SONG_D kick pair
  was reversed against seq numbering).
- Verify on the `ObjectList` dot-address — a cached `:Children()` handle reads
  stale. Census **Target AND per-track EVENT COUNT** — target-only reads
  healthy on an event-emptied track.

## Standing ⛔ (full list: `MEMORY.md`)

Never call `GetPresetDataFast()` (segfaults the console). Oops is irreversible
(no redo). Escape does NOT discard a staged popup line — select-all + delete;
Quickey 20 is the sanctioned abort.

## Depth on demand

`concepts/saveshow-discipline-and-mcp-tier.md` ·
`segfault-manifests-as-mcp-timeout.md` ·
`stale-mcp-process-after-repo-change.md` ·
`osc-session-required-for-traffic.md` · `paste-round-verification-protocol.md`.

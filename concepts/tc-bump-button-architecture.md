---
id: tc-bump-button-architecture
title: "TC bump-button architecture — dedicated bump executors triggered by typed TIMECODE EVENTS, exiting via Release not Off; a manual-ride layer alongside it is a proposed (not yet built) addition"
role: programmer
tags: [ma3, doctrine, timecode, v2.4, tourshow]
when_to_load: "Before designing or building bump executors, TC event lanes, or any cheap one-shot hit that needs to land on a music transient — including a manual-ride executor a human can fire live alongside the TC-fired ones"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session; 2 paired captures — architecture + release-not-off — merged as one design); extended findings/INBOX.md [0729cLD] 2026-07-29"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's architecture for cheap, exact-spot one-shot hits (drum follows etc.) without bloating the main cue stack:

**Structure:** multiple dedicated bump executors, each carrying a one-shot effect. Triggered by TIMECODE EVENTS typed directly into the TC editor — button on/off events sit in their own lanes, with no live recording needed. The main sequence runs its own lane; bump executors ride parallel lanes alongside it.

**Exit rule — release, not off:** bump executors exit via RELEASE (see `release-mechanism-fundamentals`), never Off/zero. Off would fight the main sequence's look; Release lets the channel fall back cleanly to whatever the main sequence is already doing underneath.

**Homework CRACKED 2026-07-17** (incidental capture, Export Timecode read live at the desk): the TC-event XML schema is now fully decoded — see `export-timecode-tc-event-xml-schema` for the full element/attribute shape. Events can now be authored directly file-side, not just recorded.

**cLD synergy, now unblocked:** the TC-event schema confirms a beatgrid moment's `startSec` maps DIRECTLY onto a `CmdEvent`'s `Time` attribute — cLD MAker (the renamed, scope-widened tool — see `cld-maker-identity-rename-and-scope`) can generate a whole TC track file-side straight from the treatment timeline. Reserved as a v1.1 seam (schema fully captured, so unblocked whenever it's picked up).

**Relation:** refines the executor model already on record in `tourshow-showfile-architecture` (one TC-fired master executor per song) — this adds that bump executors ride parallel lanes alongside that master executor, not just the one.

**Design refinement 2026-07-17 — scope bumps with Output Filters:** a recipe-part's full property dump confirmed `FILTER`/`INPUTFILTER`/`OUTPUTFILTER` are first-class recipe-part properties, giving per-layer scoping on a recipe line (e.g. a color-only cook that can't touch dimmer/position). **TC-bump lanes should carry Output Filters** so a bump can only ever emit the attribute(s) it's meant to hit — this keeps a bump from accidentally fighting the main sequence outside its intended layer, reinforcing the release-not-off exit discipline above rather than relying on it alone.

## Manual-ride layer alongside the TC-fired lane — design ask, not yet built (2026-07-29)

Dave wants a few bump executors he can **ride live, by hand**, on anything that needs it — a manual-ride layer that sits alongside the TC-fired bump lane described above, built per-song as needed. This is a forward-looking design ask, not yet a proven or built mechanic; the TC-fired architecture above remains the only implemented lane as of this note. See `tourshow-fill-layer-rebuild-method` for the fill-build context this ask came out of.

History: none — architecture and exit rule both stated 2026-07-16; TC-event schema remains open homework. Extended 2026-07-17: Output Filters design note added from the recipe-part property-surface dump. Same day, later: TC-event schema homework CRACKED via a live Export Timecode capture — see `export-timecode-tc-event-xml-schema`. Extended 2026-07-29: added Dave's manual-ride bump-executor design ask (not yet built) alongside the proven TC-fired lane.

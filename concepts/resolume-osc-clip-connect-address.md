---
id: resolume-osc-clip-connect-address
title: "Resolume clip-connect OSC contract: /composition/layers/<layer>/clips/<N>/connect with int 1 — clip numbers are POSITIONAL, so the song→clip map lives in exactly ONE table, never scattered across per-song code"
role: programmer
tags: [ma3, osc, video, showrun, v2.4, tourshow]
when_to_load: "Before wiring MA3 to trigger video clips over OSC — the address form, the argument, and the positional-numbering consequence that decides where the mapping is allowed to live"
status: active
verified: EU tour leg 2026-08 (address spec from Dave; MA3-side SendOSC arg syntax NOT yet ground-truthed)
source: "findings/INBOX.md [0808-3cLD] 2026-08-08 — Dave's spec"
supersedes: []
superseded_by: null
---

## The contract

```
/composition/layers/<layer>/clips/<N>/connect     arg: int 1
```

- **One layer** carries the show deck; clips are addressed **by position** within it.
- The deck on this tour: 18 song clips + 2 talking clips = 20 positions in a 60-minute show.
- `int 1` is the standard Resolume connect argument.

## The consequence that matters

**Clip numbers are POSITIONAL.** Re-decking in Resolume — inserting a clip, reordering the set — **shifts every number downstream**. Therefore:

**⇒ The song → clip-number mapping lives in exactly ONE place** — a single table in one macro/toolbox function. A re-deck is then a one-table edit, never twenty scattered literals to hunt. The same reasoning applies whichever transport is used, including the DMX-shortcut lane that actually shipped (`resolume-dmx-one-hot-clip-select`).

## Open items (do not assert from memory)

- **MA3's `SendOSC` exact argument syntax** — ground-truth from the manual at the next wire session; never guess it.
- **Which machine runs the video and on which OSC input port** (Resolume's default is 7000) — needed for the one OSC output line in the console's Setup.
- **Deck ordering** — songs at 1-18 with talking clips appended, versus talking clips slotted at their real mid-show positions (which shifts everything after them). The table writes itself off that answer; the shipped DMX deck chose the latter.

**Relation:** `resolume-dmx-one-hot-clip-select` (the lane that shipped) · `osc-outbound-is-event-driven` · `osc-inbound-config-requirements` · `osc-session-required-for-traffic` · `show-run-signals-originate-at-the-desk`.

History: none — spec captured 2026-08-08; superseded in practice (not in fact) by the DMX-shortcut lane the same week.

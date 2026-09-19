---
id: show-run-signals-originate-at-the-desk
title: "⛔ LAW: show-run signals originate from the DESK — never through the MCP bridge. Anything that fires during a show is a native object (TC event, cue CMD, macro line), not a bridge call."
role: operational-live
tags: [ma3, mcp, safety, showrun, doctrine, tourshow]
when_to_load: "Before designing any runtime behaviour for a live show — the bridge is a build-time tool, and a show-run path that depends on it is a single point of failure nobody is watching"
status: active
verified: EU tour leg 2026-08
source: "findings/INBOX.md [0808-2cLD] 2026-08-08 — stated as a design law while scoping the show-run automation"
supersedes: []
superseded_by: null
---

**The law:** everything that fires during a show is a **native console object** — a timecode event, a cue's CMD, a macro line, a plugin function called by one of those. **The MCP bridge is a build-time and audit-time tool. It is never in the show-run path.**

**Why:** the bridge depends on a laptop, a network, an MA-Net session and an OSC line, none of which anyone is watching at 21:00. The desk's own chain depends on the desk. The whole decoded show-run architecture obeys this by construction (`automator-tc-architecture`): timecode in, native cue CMD, native macro, a Lua function that lives inside the show file (`plugin-code-runs-at-showfile-load`) and travels with it.

**Consequences in practice:**

- A per-song action is added as a **line in a macro that already runs**, not as a bridge-side listener.
- Video triggering leaves the desk as **DMX or OSC out of the console**, not as a message from the bridge (`resolume-dmx-one-hot-clip-select`).
- Rehearsal/show clock switching is a **macro press**, not a script run (`tc-slot-enum-internal-default`).
- Venue adaptation ships as a **macro artifact in the show file** so Dave can fire it without cLD present (`many-lines-ride-macros-not-lua`).

**Corollary — the console is one shared surface.** Even at build time, bridge writes land in whatever context the desk currently has open, which is why the desk-clear callout exists (`desk-clear-callout-before-console-write-rule`). During a show that surface belongs to the operator, full stop.

**Relation:** `desk-clear-callout-before-console-write-rule` · `automator-tc-architecture` · `plugin-code-runs-at-showfile-load` · `law-zero-and-failover-architecture` · `many-lines-ride-macros-not-lua`.

History: none — stated 2026-08-08 and held for the remainder of the leg.

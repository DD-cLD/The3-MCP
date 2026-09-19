---
id: lua-pool-walk-allocation-law
title: "Lua #pool returns the pool's ALLOCATION, not its occupied count — holes read nil; always guard a pool walk with 'if o then'"
role: programmer
tags: [lua, ma3, v2.4, pool]
when_to_load: "Before writing any Lua that walks a whole pool (for i=1,#pool do ... end) — #pool is the allocation size (e.g. Dimmer=1000), not how many slots are actually occupied, and empty slots return nil rather than being skipped"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, live 2.4.2.2, confirmed on the Dimmer preset pool 1-16; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`#pool` in Lua returns the pool's ALLOCATION size, not the number of occupied slots.** Observed on the Dimmer preset pool: `#pool` = **1000**, regardless of how many of those 1000 slots actually hold a preset.

**`pool[i]` is SLOT-addressed, and an empty slot returns `nil`** rather than being skipped or omitted from the count. **Every walk over a pool must guard each read** — e.g. `local o = pool[i]; if o then ... end` — or a hole throws on the next line that assumes a real object.

**Confirmed:** `pool[i].no == i` (the object's own slot-number property matches its index) verified across Dimmer slots 1-16.

**Consequence for census/generator scripts:** never use `#pool` as "how many objects exist" — it will wildly overstate occupancy on a sparsely-filled pool (a 1000-slot Dimmer pool with a handful of real presets still reports `#pool == 1000`). Walk the full allocation and count only the non-nil hits for a true census.

**Relation:** distinct from `macro-scratch-slot-idiom-generalizes-to-any-pool` (that concept is about deliberately using a disposable slot to author into — this one is about safely *reading/walking* an existing pool's contents).

History: none — confirmed live, 2026-07-28, while building the SONG_T phaser template set census.

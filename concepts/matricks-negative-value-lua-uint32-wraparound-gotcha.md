---
id: matricks-negative-value-lua-uint32-wraparound-gotcha
title: "Lua :Get() on a negative MAtricks value returns the uint32 wraparound — export readback is the honest lane for signed values"
role: programmer
tags: [ma3, lua, matricks, v2.4]
when_to_load: "Before trusting a Lua :Get() readback of any MAtricks property that might be negative (e.g. YShift) — the live Lua read silently wraps to a huge unsigned int instead of showing the true signed value; the export re-serializes it correctly"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_B MAtricks set build, live 2.4.2.2)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Finding (card-candidate, CARD_DESK):** reading a **negative MAtricks value via Lua `:Get()`** returns the **uint32 wraparound**, not the signed value — `YShift -1` read back as `4294967295`.

**The export lane is honest for signed values:** exporting the same object and reading the XML re-serializes the value correctly as `-1`.

**Same family as the sign-eating patch-`Set` trap** (a bare negative losing its minus sign on write), but a **different mechanism** — this is a read-side DISPLAY problem, not a write-side value-storage problem. The value is stored correctly; only the live Lua read of it lies.

**Practical consequence:** when verifying any MAtricks property that could plausibly be negative, verify via **export readback**, not a live `:Get()` call.

**Relation:** `tourshow-whole-fixture-block-law` (the MAtricks retune session this was caught during, on `144 SHUFFLE 5`'s `YShift`). `patch-set-one-prop-quoted-values` (existing concept, not staged this run — the sibling write-side sign-eating trap in the same family).


## Scope narrowed 2026-08-01 [0801cLD] — the uint32 wraparound is YShift-specific, NOT a blanket negative-value rule

Two corroborating live imports narrow this concept's scope. **`MX 153 cLD S5 X-45`** live-read `PhaseToX=-45.0` exact after import — **PhaseToX is signed-clean on the live Lua read.** A second case landed the same magnitude that originally motivated worrying about wraparound: **negative phase at magnitude 360 also landed EXACT and read exact via live Lua** (`MX 158 PhaseToX=-360.0`) — further corroborating that the uint32 wraparound described in this concept's body is **YShift-specific**, not a phase-wide hazard. Three new MX spatial shapes are proven importable off the back of this: reverse lap (`-360`), double lap (`+720`), and a phase-OFFSET form (`PhaseFromX=180` with no `ToX`).

**Practical narrowing:** treat the wraparound risk as scoped to `YShift` (and other non-Phase* attributes proven to share its mechanism) until a further live case shows a `Phase*` attribute wrapping too. `PhaseToX`/`PhaseFromX` reads via live `:Get()` are trustworthy at least at the magnitudes tested (±45, ±360).

**Serialization asymmetry, separate mechanism, worth keeping alongside this scope note:** the desk dialect writes NEGATIVE phase WITHOUT a degree sign (`PhaseToX="-180.00"`) while positive phase keeps the degree sign (`"360°"`). Authored-with-degree negatives still import correctly (proven on `MX 153`, and again on SONG_J `163`/`164`/`165`/`167`) — but an export-back byte-diff comparison MUST normalize the degree-sign difference before comparing, or a clean import reads as a false failure.

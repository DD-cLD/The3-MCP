---
id: resolume-dmx-one-hot-clip-select
title: "Transport-proof video clip select from the desk: a sequence of per-song cues, each driving its OWN clip shortcut to Full and the PREVIOUS one to 0 (one-hot), fired from the shared song macro — show-proven live"
role: programmer
tags: [ma3, video, dmx, sequence, showrun, v2.4, tourshow]
when_to_load: "When lighting also has to select the video clip per song — this is the shipped pattern, why it beats a per-cue value pile, and how it hangs off the existing show-run chain with zero new wiring"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0808-2cLD] (design) · [0808-9cLD] (built: groups, sequence, plugin, macro line) · [0808-10cLD] (Dave: works, tested under real TC) · [0819-9cLD] (ran live in a show) 2026-08-08→19"
supersedes: []
superseded_by: null
---

## The shape

- **Patch:** one dimmer channel per clip as a DMX shortcut into the video machine, plus a layer-opacity channel. Twenty clips ⇒ twenty single-fixture groups plus an "all" group for the tidy-up.
- **A sequence, one cue per clip**, each cue **named the song token** (talking-break clips sit at their real show positions in the deck order), with an `All_Off` cue at the end.
- **Each cue's recipe is one-hot:** **own clip @ Full** + **previous clip @ 0**. Deterministic, and it avoids the same-fixture cooking conflict a full "all others at zero" pile would create.
- **Fired by name** from the shared song macro's toolbox call: `Go+ Sequence '<sequence>' Cue '<token>'`.

**Out-of-order fires still work.** The video machine's shortcuts are **edge-triggered**, so a cue fired out of sequence still switches the clip correctly — the one-hot pair is about clean DMX state, not about ordering.

**Receipts:** 21 cues + OffCue/CueZero, SR = 40 exact, all cue names true; generator run twice (container and device) byte-identical before deploy; sha-verified on landing.

## Why it hangs off the song macro

The clip-connect rides the **same single touchpoint** as everything else per-song (`automator-tc-architecture`) — the toolbox function reads the `selectedsong` global and fires the matching cue by name. **Zero new wiring**: timecode in → automator → song macro → toolbox → clip. A manually-fired mark cue will not pull video (accepted trade-off, see the automator concept).

## The alternative lane, and why it wasn't needed

Native OSC out to the video machine is a real option and its address contract is banked (`resolume-osc-clip-connect-address`). The DMX-shortcut lane won because the desk was already patched for it, the state is visible in the show file, and it needs no network configuration on show day. **A single-channel Art-Net/DMX fallback is also viable.**

**⇒ Show-proven.** The full chain — Art-Net TC → automator → song macro → toolbox → one-hot clip select — **ran live in a show and worked.** It is production, not a test rig.

**Standing law it obeys:** show-run signals originate at the desk, never through the bridge (`show-run-signals-originate-at-the-desk`).

**Relation:** `automator-tc-architecture` · `resolume-osc-clip-connect-address` · `appearance-image-swap-blocking-cards` (the sibling per-song action on the same touchpoint) · `tourshow-resolume-scope-and-tc-chain` · `led-wall-anamorphic-fit-math`.

History: none — designed, built, TC-tested and show-proven between 2026-08-08 and 2026-08-19.

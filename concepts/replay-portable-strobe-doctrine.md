---
id: replay-portable-strobe-doctrine
title: "Build strobe as a shutter open/closed chase effect for replay-portability — native fixture strobe only when genuinely fast"
role: programmer
tags: [ma3, doctrine, effect, strobe, v2.4]
when_to_load: "Before building a strobe-style look — decide whether a portable two-state chase effect serves better than the fixture's native strobe function"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's standing preference for strobe-style looks: build the effect as a two-state chase — shutter OPEN / shutter CLOSED — rather than reaching for a fixture's native strobe function by default.

Why: an effect built this way is **replay-portable**, both show-to-show and type-to-type. The same chase concept carries from one rig or tour to the next, and from one fixture type to another, because it's built from generic shutter states rather than a specific fixture's strobe implementation.

Known ceiling: the two-state chase is bounded by DMX refresh rate, so it cannot reach the very fast flicker speeds a fixture's native strobe function can hit. When a look genuinely needs that kind of speed, native fixture strobe is still the right tool — this is a default preference, not an absolute ban on native strobe.

The actual win isn't raw speed, it's musical timing control: building strobe as a chase means it inherits the console's chase/phaser timing machinery, so it can be driven to quarter-note taps and other musically precise placements — something a fixture's built-in strobe rate doesn't give you.

This doctrine is general — it isn't tied to {TOUR}'s specific rig, and should apply to any future rig with strobing fixtures.

History: none — dictated live 2026-07-15; the concrete application is `worked-strobe-figure-tap-tap-kill`.

---
id: universal-presets-emitter-aware
title: "Universal presets resolve through each fixture profile's color engine/emitter data — the /Universal store-mode rule applies to ALL preset stores (dimmer included), not just color"
role: programmer
tags: [ma3, presets, color, v2.4]
when_to_load: "Before trusting a universal (device-independent) color/dimmer preset to look right across mixed fixture types — especially ahead of a fixture-color pre-match session, before storing ANY preset (dimmer included), or when a universal preset looks off on one profile"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave, console 2.4.2.2; store-mode ruling extended 2026-07-21; scope BROADENED to all preset types findings/INBOX.md 2026-07-23 [0722-2cLD] (Dave caught it); extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: GDTF named as the specific emitter-data standard)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's operating knowledge:** universal color presets resolve through the fixture profile's **color engine / emitter data** — with correct emitter data, a universal red lands correctly regardless of the underlying engine (multi-LED with warm+cool white, tungsten-based, etc.). The catch: real-world fixture profiles' emitter data is **imperfect**, so results aren't guaranteed automatically.

**Tooling response:** **v2.4.2** adds universal-preset **management tools** to correct emitter behavior per fixture type when needed.

**Why it matters here:** directly relevant to the warehouse-day fixture-color pre-match work (see `tourshow-warehouse-day-fixture-color-prematch`) — universal presets are the mechanism that lets one preset target multiple fixture types at once, but that only works cleanly once any imperfect emitter data has been corrected. Also the preset class used in the first end-to-end recipe build (see `recipe-lane-end-to-end-verified` — Universal Dimmer + Mixcolor presets).

**Store-mode ruling (Dave, 2026-07-21):** ALL {ARTIST} show colors are stored as **Universal** presets — they capture RGB *intent*, not baked per-fixture emitter values, so one preset resolves correctly across every fixture type through that profile's color engine. Do **not** store show colors as Global. When new fixture types are cloned in, or a color lands wrong on one profile, **balance** it with the **v2.4 global-vs-universal color preset management** tools rather than re-storing the preset — that is the emitter-correction path named above. This file is the home for the store-mode ruling; `baked-phaser-preset-xml-schema` documents only the XML *shape* and the `ColorRGB_R/G/B` attribute.

**⚠ SCOPE BROADENED 2026-07-23 [0722-2cLD] (paid-for lesson, Dave caught it) — this is NOT a color-only rule.** House practice applies `/Universal` to **every** preset store, dimmer included — a foundation builder (v0.1) stored dimmer presets with plain `Store` (console-default scope) instead of `/Universal`, a known shortcut that was buried in a parenthetical instead of flagged loudly. **Fix shipped, v0.1.1:** every `Store Preset` line now carries the `/Universal` flag explicitly (manual-verified option keyword; Preset Modes table = Selective / Global / Universal; v2.4 also allows changing mode on an existing preset at any time, so a plain-Store mistake is correctable in place, not a rebuild). **Process fix — DOCTRINE LINT, standing:** any authored preset-store deliverable's self-verify step must now confirm, explicitly: (1) every preset store carries `/Universal`; (2) no `PresetData` blocks appear in a recipe-only sequence export; (3) `UseExecutorTime=No`; (4) every cue part is a `StandardRecipe`. A structure census alone (right number of presets, right names) is **not** sufficient to catch a scope mistake — the lint has to check the store-mode flag explicitly, every time.

**Q value — emitter strategy (Dave, 2026-07-21):** in the color-picker special dialog, the **Q value** chooses how a universal color is realized across a fixture's emitters, continuously variable 0→100. **Q0** favors **broadband** mixing — all available emitters/LEDs contribute (fullest blend). **Q100** drives a **single emitter** — e.g. just the UV LED, or just the white LED — when you want exactly that one source. **Q50** is a **mix** of the two; because it is variable, any point between broadband and single-emitter is reachable.

**Attribute + CLI note:** the color attribute stored underneath is `ColorRGB_R/G/B` (see `baked-phaser-preset-xml-schema` for the XML). **[VERIFY]** whether the Q value is reachable from a CLI/`Attribute` command or is picker-only (special dialog) — not yet tested; treat Q as a picker-side control until confirmed.

## ⛔ SCOPED EXCEPTION RULED — STB (W)/(R) objects store GLOBAL, not /Universal, 2026-08-03 [0803-2cLD]

**RULED (Dave) — a scoped exception to this concept's standing law, not a repeal of it.** The three QX40-STB objects (`cLD LED WHITE`, `cLD LED (R)`, `cLD RATE (R)` — see `tourshow-stb-white-release-ruling`) store **GLOBAL**, not `/Universal`. Dave: *"global so only our QX40 look at it."*

**Why the exception doesn't break the rule's purpose.** The standing law (this concept; CARD_AUTHORING item 3) exists because Universal resolves through each fixture profile's emitter/colour engine and therefore travels across fixture types — exactly what a show colour needs. These three objects are the opposite case: they exist to drive the QX40's own LED/rate engine specifically, and travelling across fixture types is exactly what is NOT wanted here. Global scopes them to the QX40 the way the rule's purpose intends — rule and exception serve the same goal by different mechanisms, depending on whether cross-fixture-type resolution is wanted.

**Written into the foreground already**, so a future session does not "correct" it back to `/Universal`: `generated/songbuild/cld_submap.py` and `agents/cards/CARD_AUTHORING.md` both carry it as of this ruling. This amendment is what makes the corpus agree with the card and the submap.

**Scope of the exception: these three objects only.** Every other preset store still carries `/Universal` per this concept's standing law, dimmer included — nothing else about the rule changes.

**Carried caveat, not a blocker:** the Global-anchor portability verify item still applies in principle, but the QX40 is cLD's own floor fixture and travels with the show, so the caveat is noted rather than acted on.

## Universal colour resolution mechanism, pinned 2026-08-04 [0803-3cLD]

**STRUCTURAL (G=0.5).** Universal resolves through **GDTF emitter data** specifically — this
names the standard behind the "color engine / emitter data" language already in this concept's
body. Where a fixture's GDTF profile is missing or wrong, **balance per fixture type in 2.4.2**
(the global-vs-universal color preset management tools already named above) **rather than
re-storing the preset.**

## Worked example — tune by ENGINE similarity, not fixture type, 2026-08-05 [0805cLD]

**Concrete instance of the balancing mechanism above.** Dave tuned all colours across **FID
1101 thru 1407** in one pass using **Global** presets (Global here per the QX40 scoped
exception ruled elsewhere in this concept — see the STB section above), by matching similar
ENGINES rather than specific fixture types: he fudged the QX40 as an RGBW LED and hacked the
Pixel Line fixture type so its RGBW par mixes RGB values only, so one tuning pass covers every
fixture with a similar engine instead of needing a pass per declared type. **Rivale was the
reference fixture.** Result: colours read correctly across the mismatched engines.

History: none — doctrine stated live by Dave, 2026-07-15. Extended 2026-07-21 (crown-jewels scrub) — added the Universal store-mode ruling for all {ARTIST} show colors, the Q-value emitter strategy (Q0 broadband / Q100 single-emitter / Q50 mix, variable), the v2.4 global-vs-universal balancing path, and the `ColorRGB_R/G/B` attribute link. This file is now the home for the color-storage ruling; `baked-phaser-preset-xml-schema` was scrubbed of its Global store-mode endorsement and redirected here. Ruling stated live by Dave. **Extended 2026-07-23 [0722-2cLD]:** scope broadened from color-only to ALL preset stores after a real miss (dimmer presets stored plain instead of Universal) — v0.1.1 fix (`/Universal` on every Store Preset line) + a standing doctrine-lint process fix (explicit store-mode + PresetData/UseExecutorTime/StandardRecipe checks, not just a structure census) both shipped same finding.

**[0805-2cLD] CORRECTION — exception-table names:** the three GLOBAL-exception objects carry these LIVE console names (read 08-05): **4.83 "QX40 Only W"** (was cLD LED WHITE) · **4.84 "QX40 Only W (R)"** (was cLD LED (R)) · **Beam 5.8 "QX40 STB (R)"** (was cLD RATE (R)). None carry the cLD prefix. The exception ruling itself stands unchanged.

History: corrected 2026-08-05 [0805-2cLD] — exception-table names updated to live console reads; fix the corpus, not the console.

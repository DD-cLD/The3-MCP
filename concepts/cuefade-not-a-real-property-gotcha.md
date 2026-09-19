---
id: cuefade-not-a-real-property-gotcha
title: "Look timing comes from the recipes, not from cue/part fade properties — cue-to-cue follow times live in the cue stack, UseExecutorTime stays OFF, and 'CueFade' is not a real property name (CLI footnote)"
role: programmer
tags: [ma3, recipes, timing, cues, naming-precision, v2.4]
when_to_load: "Before setting or chasing any fade/delay on a cue or part in this recipe-based show — timing is authored in the recipes, not on cue/part fade properties; also before trying to Set a cue's fade via CLI (CueFade is not a property name and no-ops silently)"
status: active
source: "Dave ruling 2026-07-21 (recipe-based timing doctrine); CLI gotcha paid for live 2.4.2.2, cLD SONG_G build [0721-2cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The doctrine (Dave, 2026-07-21): fades and delays come from the RECIPES.** In this recipe-based show, look timing — fade in/out, per-attribute delays, the feel of a move — is authored inside the recipe (its preset + phaser + grid), which cooks live. That is the layer to reach for when a look should breathe faster or a color should crossfade slower. Do not bake fade times cue-by-cue.

**Cue-to-cue FOLLOW times are the one exception.** The timing *between* cues — follow/trigger — lives in the **cue management stack** (the cue's `TRIGTYPE` / `TRIGTIME` / `TRIGSOUND`), not in a recipe. So: within-look timing = the recipe; cue-to-cue advance = the cue stack. Cue/part fade *duration* properties are not the layer you author look timing on for this show.

**UseExecutorTime stays OFF for this show.** `UseExecutorTime` is an **override toggle**: turned ON, it makes the executor's time override the fade times stored in the sequence. It is not the normal path to timing, and leaving it ON during programming can produce strange, hard-to-explain output. Keep it **OFF** and let recipe timing (and cue-stack follow timing) stand. This corrects an earlier reading from this session that treated `UseExecutorTime=Yes` as "where cue fade lives" — that was a baked-paradigm artifact.

**Footnote — the `CueFade` CLI gotcha (still true):** `Set <cue> Property "CueFade" <value>` compiles and echoes clean but **no-ops silently** — `CueFade` is not a property name on either the Cue or its Part. Same silent-fail class as `set-command-unknown-property-fails-silently` and `command-enabled-property-name-gotcha`: never trust a clean `Set` prompt on an unverified property name. Real Cue-level properties actually seen: `TRIGTYPE`, `TRIGTIME`, `TRIGSOUND`, `FADERENABLED` (none is a fade *duration*; `FADERENABLED` only gates whether fading happens at all). Real per-part fade property names do exist on the part surface (`RELATIVEFADE`, `FADEFROMX`/`FADETOX` +`Y`/`Z`, `DELAYFROMX`/`DELAYTOX` +`Y`/`Z`, `OFFFADE`, `RELATIVEDELAY`, `DELAYTOPHASE`) — but for this show you do **not** hand-set them cue-by-cue; timing is authored in the recipe.

Cross-reference: `recipe-line-set-property-syntax-and-value-casing` for the recipe-line `Set ... Property` grammar where real timing is authored; `recipe-part-property-surface-lua-dump` for the fuller part-property surface the CueFade footnote is drawn from.

History: created 2026-07-21 [0721-2cLD] — CueFade-not-a-property CLI gotcha paid for live during the cLD SONG_G sequence build.

History: rewritten 2026-07-21 (crown-jewels scrub) — previously claimed cue fade "lives on the executor (UseExecutorTime=Yes) or on the part." Dave corrected: look timing comes from the recipes, cue-to-cue follow times from the cue stack, and UseExecutorTime is an override that stays OFF for this show. The narrow, still-true CueFade-is-not-a-property CLI gotcha was kept as a footnote; the contaminated "where fade lives" framing was scrubbed.

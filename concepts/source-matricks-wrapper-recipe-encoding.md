---
id: source-matricks-wrapper-recipe-encoding
title: "{LD} binds NO MAtricks pool objects, ever — spread lives on per-population wrapper StandardRecipes inside each phaser's DependencyExport; match wrappers by CROSSWALKED TARGET, never raw name"
role: programmer
tags: [source-dialect, matricks, crosswalk, wrapper, xml-schema, tourshow]
when_to_load: "Before reading {LD}'s spatial/MAtricks spread off any phaser preset, or before crosswalking a wrapper group name to a cLD group for MX purposes — his MX never lives on a bound MAtricks pool object, and matching wrappers by raw name silently drops sites"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**{LD} binds NO MAtricks objects at all — anywhere in his file.** His spatial spread is baked **INLINE on *wrapper* StandardRecipes** that live inside each phaser preset's `DependencyExport` embed, **one wrapper per population**, carrying `XWings`/`XShuffle`/`XBlock`/`YShuffle` + `PhaseFrom`/`To` + `SpeedFrom` per axis. Consequence: his MX must be read **PER FIGURE AND PER POPULATION** — a per-figure read (one spread value per phaser) is wrong by construction, since different populations inside the same figure can carry different wrapper values. This confirms and generalises the 08-01 Swell Dim#3 catch (a fixed-allow-list probe read three populations as two signatures because it missed one population's `YShuffle`).

**Wrapper GROUP spellings differ from SEQUENCE group spellings — match wrappers by CROSSWALKED TARGET, never by raw name.** Observed pairs (sequence name <-> wrapper name):
- `JDC1 US [RGB]` <-> `JDC1 US [RGB] (Lin)`
- `JDC1 DS [RGB]` <-> `JDC1 DS [RGB] (Linear)`
- `Spots + Beam [Sym] (Fest)` <-> `Spots + BEAM (Grid) (Fest)`
- `Strike M [RGB] (Lin) (Fest)` <-> `Strike M [RGB] (Grid) (Fest)`

**Name-matching returned a silent "no MX" on 9 of 47 sites; target-matching (crosswalk both spellings to the same cLD group, then match on that shared target) resolves all 47.** Both spellings already crosswalk to the same cLD group — the target is the reliable key, the wrapper's own group name is not.

**`Strike M US [STB] (Lin)` is the one wrapper spelling with no row of its own in `cld_submap`** — it is the US/QX40 STB population (agrees with the SONG_J `MXMAP` `__QX40__` entries built by hand on 08-01). Currently carried as a file-side wrapper alias inside the sheet generator only; `cld_submap.py` itself was **not** modified. Promote it to a real submap row only if it turns up at the sequence layer on another song.

**Independent corroboration:** re-deriving the MX crosswalk from the raw files, independent of the 08-01 build script, agreed with the hand-built `MXMAP` site-for-site: all 47 phaser sites -> **31 MATCH**, **15 unison-by-design** ({LD} authored `0->0`, no MX needed), **1 ruled variance** (Swell Dim#4, `XBlock` {LD}=14 vs cLD=12, a Dave ruling, not a bug). **Speed is deliberately excluded from this verdict** — ours ships unbaked and rides Speed Scale, except the two Swell 3 objects that carry a real X:Y speed ratio (see `tourshow-speed-architecture-standing-ruling`).

**Relation:** `source-spread-is-one-full-wave` (a different mechanism — {LD}'s phaser's own baked per-fixture spatial figure in the cooked `PresetData` layer, not the wrapper StandardRecipe spread this concept covers). `matricks-store-time-embed-travels-with-preset-export` (reading an INHERITED figure's literal MAtricks-family attributes off its export — the unfiltered-probe method that caught the Swell Dim#3 miss this concept generalises). `tourshow-crosswalk-prework-alias-gap` (the group-name-alias problem this wrapper-target-matching rule is the MAtricks-layer instance of). `tourshow-stb-white-release-ruling` (the STB wrapper alias's downstream consequence).

---
id: release-relative-universal-preset-exemplar-proven
title: "The release dialect is already in the corpus — Position.Release Relative is a Universal preset carrying Relative=\"Specials:Release\", bound by an ordinary StandardRecipe; an (R) is not a new dialect"
role: programmer
tags: [release, xml-dialect, universal-preset, tourshow]
when_to_load: "Before hand-authoring any release-carrying recipe line (an '(R)' on a QC sheet, a bump-exit release, or any other release preset) — a live golden already exists in {LD}'s own file; do not treat release as an unattested dialect"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**No desk golden needed — the release dialect is already in the corpus.** Found as the 4th of 4 preset gaps surfaced by the whole-show crosswalk pass (see `tourshow-crosswalk-prework-alias-gap`): `Position.Release Relative` (SONG_H, 1 line) **is a release exemplar.**

**Its embed:** a **Universal preset** whose `PresetData` rows carry `<Step Function='<Attr>' Relative='Specials:Release'/>` — a universal template row (`IDType 2` / `ID 1`, `Selective='Global'`) plus per-fixture rows.

**The SEQUENCE-LEVEL bind is a completely ORDINARY StandardRecipe** — `Preset=`/`Values=` pointing at the preset, nothing special on the recipe line itself.

**Conclusion: an (R) is not a new recipe dialect at all — it is a normal preset bind whose CONTENT is `Specials:Release`.** The whole release mechanism lives inside the preset's own PresetData, not in any special recipe-line syntax. This unblocks the STB (W)+(R) work (see `tourshow-stb-white-release-ruling`) — the only genuinely open item left for that work is the QX40's own strobe attribute name, not the release mechanism.

**Relation:** `release-mechanism-fundamentals` (what Release does at the channel level — falls back to the next claim rather than forcing zero). `release-preset-design-doctrine` (our existing recipe-referencing release-preset pattern — this exemplar confirms the same "reference, don't bake" shape appears natively in {LD}'s file too). `release-family-ships-stock` (the stock hard-value-pair Release family — a different, coexisting release idiom). `tourshow-stb-white-release-ruling` (the downstream consumer of this dialect fact).

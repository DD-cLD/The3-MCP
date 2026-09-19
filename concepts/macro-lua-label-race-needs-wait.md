---
id: macro-lua-label-race-needs-wait
title: "⛔ A macro Lua line that CONSUMES names minted by earlier Cmd lines in the same macro needs a Wait — the Cmd queue and the Lua object tree are not synchronous (attested 14/19, fixed at Wait 0.50)"
role: programmer
tags: [ma3, macro, lua, v2.4, gotcha, race, tourshow]
when_to_load: "Before writing any macro whose later line looks objects up BY NAME that an earlier line in the same macro created or relabelled — without a Wait the name snapshot is taken too early and the misses are silent and partial"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0828-3cLD] 2026-08-28, {FESTIVAL} — maiden run of macro 'cLD MX 1CELL', 14/19 repointed, 5 skipped; XML patched Wait 0.00 → 0.50 and re-imported"
supersedes: []
superseded_by: null
---

**The race, exactly.** Macro line 1 mints four MAtricks twins and labels them (via `Cmd` lines). Macro line 2 is Lua that repoints recipe lines, looking its targets up **by name**. On the maiden run line 2's **name snapshot caught three of the four fresh labels but not the fourth** — so **14 of 19** repoints landed and the **5 lines targeting that fourth object were silently skipped**. Razor thin: **the `Cmd` queue and the Lua object tree do not settle in lockstep.**

**The failure shape is the dangerous part:** no error, no dialog, a partial success with a plausible count. Only the verification sweep ("still-broken = 0") caught it.

**The fix:** a **`Wait` between the lines** — the macro XML was patched from `Wait 0.00` to **`Wait 0.50`** and re-imported, and the pool artifact is future-proof. (Use the macro-line `Wait` column — the first of the three unrelated "wait" mechanisms, see `macro-wait-and-delay-keyword-disambiguation`.)

**General law:** **name-consuming Lua never immediately follows name-producing `Cmd` in the same macro.** Either interpose a `Wait`, or split the work into two macros, or resolve by handle captured at creation time rather than by name lookup afterwards.

**And always verify by count.** The five stragglers were finished by direct call after the run. A macro that reports a count is worth more than one that reports success — this one Printf's its counts for exactly that reason.

**Relation:** `macro-wait-and-delay-keyword-disambiguation` · `matricks-property-clear-encoding` (the Copy-carries-the-name behaviour that makes the label step necessary at all) · `venue-adapt-macro-pattern` (the artifact this fixed) · `many-lines-ride-macros-not-lua`.

History: none — found on the maiden run, root-caused and patched the same session, 2026-08-28.

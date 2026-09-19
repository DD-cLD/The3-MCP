---
id: macro-control-structure-workaround-idioms
title: "Two factory idioms approximate if/then/else and loop control around macros' missing native conditionals — operator-stepped, not real branching"
role: programmer
tags: [ma3, macro, v2.4]
when_to_load: "Before assuming a macro needs true branching/looping and reaching for Lua — these two factory-verified idioms cover the two most common cases (repeat-until-operator-stops, and a real yes/no gate) without leaving macro-CLI syntax"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD]; MACRO_LIB_CATALOG_v0.1.md §2 (circular copy x plus.xml) and §5 (POSITION_WIZ.xml line 1)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Two idioms found in MA's own shipped macros, together covering the two control structures native macro CLI syntax lacks (see `macro-conditional-branching-not-implemented` — this concept doesn't contradict that ruling, it documents how MA's own factory content works around it).

**1. Self-referential Go-loop (operator-stepped iteration)** — from `circular copy x plus.xml`:
```
Copy Selection 1 At 2
Set Selection 1 MAtricks "XShift" "-1"
Clone Selection 1 At Selection 2 If Programmer /Overwrite     Wait="Go"
Macro "Circular Copy X Plus".3                                 Wait="Go"
```
The last line calls **its own line 3** (`Macro "Name".3` — the thread-7844 rule that `X.Y` addresses one line as a standalone unit, see `macro-call-and-nesting-lifetime-semantics`) with `Wait="Go"`. Every operator Go+ steps the selection grid one notch and re-clones — a manually-paced loop with no native `While`/`For`. Also uses `Selection 1`/`Selection 2` pool objects as disposable scratch slots — a third pool type confirming the RemOff/World scratch-slot idiom generalizes (see `macro-scratch-slot-idiom-generalizes-to-any-pool`).

**2. Self-gating Lua Confirm (real if/then/else)** — from POSITION_WIZ.xml line 1 (see `factory-position-wiz-anatomy-and-porting`):
```
Lua "if Confirm(nil, 'Are you sure you want to overwrite positions?', nil, true)
     then Cmd('Go+ Macro \'Position Wizard\'')
     else Cmd('Off Macro \'Position Wizard\'') end"        Wait="Go"
```
The line halts on `Wait="Go"`. The Lua `Confirm()` popup's Yes branch fires `Go+` on the macro itself (stepping past the halt and continuing); No branch turns the macro `Off`. One embedded Lua line gives a macro that otherwise has no native conditionals a real if/then/else gate.

**Together** these are the factory answer to "MA3 macros can't branch or loop": wrap the one native primitive that DOES exist (`Wait="Go"` + re-firing the macro) around either a manual re-entry point (idiom 1) or a Lua-evaluated yes/no gate (idiom 2). Neither is native branching/looping — both still require an operator Go+ (idiom 1) or a Lua one-liner (idiom 2) to advance, so `macro-conditional-branching-not-implemented`'s "no true if/then/else in native macro CLI syntax" ruling stands unchanged.

History: none — both idioms captured together 2026-07-19, read file-side from factory `lib_macros` content; framed together because POSITION_WIZ line 1 itself describes idiom 2 as completing "the control-structure pair" with idiom 1.

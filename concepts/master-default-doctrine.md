---
id: master-default-doctrine
title: "Masters ride full by default so cell-level recipes carry the look, not the master level"
role: programmer
tags: [ma3, doctrine, recipes, multi-instance, v2.4]
when_to_load: "Before building cell-level recipes on a multi-instance fixture — default the type's master to full first so recipes aren't fighting a dimmed master"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Design rationale for a standing setup step on multi-instance fixtures (fixtures built from sub-cells, like plate+beam): before building any cell-level cues or recipes, the fixture type's master should default to full intensity, with all individual instances/cells defaulted to zero.

Why: this way a per-cell recipe — a cue that lights specific cells in a specific look — carries the entire visual result on its own. The master isn't a second dimmer someone has to remember to also raise; if the master defaulted to zero instead, every cell-level recipe would silently produce nothing on stage until the master was separately brought up.

Practical shape tonight: applied to the JDC1 type — master at full, all instances (plate+beam) at zero — then checked against Layout 3 and the sequence recipes and approved by Dave.

Scope note: the mechanical command that implements this (exact Store Default syntax, its dialog options, Merge vs Overwrite behavior) is tracked as its own concept in this run's console-mechanics shard — this file is the design "why," not the command "how," per the atomicity rule.

See also `multi-instance-grid-frontier` (the broader frontier this sits inside) and `selection-grid-and-fixture-cell-model` (the one-fixture-one-cell model this master/cell relationship extends into sub-cells).

**Refined 2026-07-16 (`jdc1-output-gated-chain`):** live JDC1 work sharpened WHICH intermediate masters this doctrine's "default to full" applies to on a multi-instance fixture — plate masters are included, not just the top-level fixture master. JDC1's real output chain is fixture master × plate master × cell; any one of those three left at zero goes dark regardless of the others. See that concept for the working recipe and for the separate (GDTF-rooted) reason onPC's own visualization can't be trusted to show this correctly.

History: none — dictated live 2026-07-15, applied to JDC1 same session. Refined 2026-07-16 with the JDC1 multi-level-gating detail — see body.


## ⛔ CORRECTED 2026-08-03 [0803-1cLD] — masters are never programmed; the emitter's JDC gate-opener behaviour is retired

**RULED (Dave) — MASTERS ARE NEVER PROGRAMMED. ALL VALUES FLOW FROM THE CHILDREN.** Masters get preset in the default and are never touched inside a cue, so there is never a question of whether a build opened or closed one at the right spot. Dave's words: "one extra and very important gotcha that could cause unwanted issues." **This retires the JDC gate-opener behaviour in the emitter** (`cld_submap.JDC_OPENERS` / `JDC_TARGETS`) — the `+2` lines that had been showing up in every song's reconciliation identity (see `reconciliation-identity-per-song-verification-method`) go away for songs built after this ruling.

**Reframed same day — the asymmetry IS the point, not a defect hunt.** Setting an MM/master to its DEFAULT value (100) in the Mark cue has **no negative side effect**; setting it to 0 anywhere else in the song and forgetting to turn it back on is the actual danger. So "masters flow from the children" is **forward hygiene**, not evidence of an existing bug: the risk is a CLOSE that never re-opens, not an OPEN that was never needed.

**Master exposure censused across every built song — CLEAN, no action owed.** 14 lines, 7 songs, all identical: `cLD JDC PLATE MASTER` + `cLD JDC BEAM MASTER` @ `Dimmer.Full`, at the **Mark cue only**, in SONG_B 1110, SONG_D 1310, SONG_E 1410, SONG_G 1710, SONG_H 1810, SONG_I 1910, SONG_J 2010 (SONG_A / SONG_C / SONG_F had no export-back in the staging set at census time and still need checking). **Every master line in every built song is `Dimmer.Full` at the Mark cue and nowhere else** — `{'Dimmer.Full': 14}` — so **no master is ever driven closed anywhere in the show**, and Dave's gotcha does not exist today. The 14 lines are benign by his own rule; removing them is preference, not repair. The emitter still retires `JDC_OPENERS` so future songs stop adding them at all.


## ⛔ VERSE ONE — masters out of programming (Dave, verbatim, 2026-08-22, tour-proven)

*"leave master MM types out of programming, use the Master and child masters at full all cells in all modules at 0 Store MA+. (store default). We caught it in time and I removed masters from our early tracks but it makes things not go well unless it's very studiously handled. Basicly putting MM on in the mark and not putting cells at 0 goes instant on."*

**Decode.** Multi-module fixtures multiply **master x cell**. The law: **the master and its child (module) masters live at FULL as the stored DEFAULT and are NEVER stored in cues, presets or recipes.** All intensity programming happens at **cell** level; the cell default is **0**, so anything unprogrammed is dark. "Store MA+ (store default)" is Dave's shorthand for storing that masters-full / cells-zero state as the default.

**The violation mechanic:** a mark cue asserts master-up while cells still hold tracked or non-zero values, and the fixture goes **INSTANT ON in the mark** — a visible pop, mid-show. Early tracks did carry stored masters; Dave stripped them after catching a live instant-on. Handled, but the wariness stands.

**cLD enforcement, standing:** (1) nothing cLD generates — sequence XML, recipes, presets, macros — ever writes a master or child-master value; (2) any audit that touches intensity checks for master-instance stores and flags them; (3) a candidate verification sweep scans all sequences for values landing on master instances (a fixture ID with no cell index).

### The tour-leg census, and what it found

The sweep ran at {FESTIVAL}, 2026-08-26, over a **52-unit venue wall**, and found **mixed conventions across the show**: five songs park module masters *and* all cells at Full; five park plate cells Full with no master assert; one zeroes everything; seven assert nothing at all — with values tracking across song jumps. That mix, on a wall that size, **is** the verse's instant-on window, and it is systemic rather than a one-song slip.

**The armor is a shell, not a zero** — Dave ruled the obvious "merge-store master = 0 into every mark" out with *"same issue."* See **`mm-shell-empty-preset-armor`**.

**The migration is a repoint, not a delete.** The master rows turned out to be **recipe-cooked output**, not raw stores, so they were killed by repointing each Dimmer-pool recipe line's Selection from the master group to the cell group — **65 lines** (`0` x36, `50` x14, `Full` x13, `30` x2), look preserved exactly, masters out of the dimmer lane. Fingerprint reproduced identically on a second file. See **`cooked-recipe-rows-immune-to-store-remove`** and **`venue-adapt-macro-pattern`** (the treatment now ships as a one-press macro).

**Residue that is legitimately left alone:** figure-cooked master rows carrying deliberate swell dynamics (phaser-pool values) and a handful of single-fixture raws in utility sequences. Repointing a figure to the cell group changes its spread aesthetics, so each is Dave's call, not a defect.

**Librarian note (Dave):** these are numbered verses. Start a BIBLE/VERSES collection when more land.

History: extended 2026-08-22 with Verse One verbatim + decode, and 2026-08-26 with the tour census, the shell armor and the migrate-by-repoint lane.

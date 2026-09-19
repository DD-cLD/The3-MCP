---
id: mm-shell-empty-preset-armor
title: "⛔ NO HARD ZEROS ON MASTERS (Dave: 'same issue') — point mark-cue master rows at an EMPTY dimmer preset instead; an empty preset asserts nothing, and filling it once makes every mark follow"
role: programmer
tags: [ma3, doctrine, masters, presets, multi-instance, v2.4, tourshow]
when_to_load: "Before arming a mark cue against multi-module fixtures — the instinct is to store master=0 and that is the wrong armor; the shell is the right one"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-2cLD] 2026-08-26 (Dave's ruling, verbatim fragment: 'same issue') + [0826-3cLD] (shell minted, Preset 1.99 'cLD MM SHELL', kids=0); pattern parent = the pan shell, [0822-1cLD] 2026-08-22"
supersedes: []
superseded_by: null
---

## The ruling

The masters census across the show found **mixed conventions on a 52-unit wall**: five songs park module masters *and* all cells at Full, five park plate cells Full with no master assert, one zeroes everything, seven assert nothing at all — with values tracking across song jumps. That is the instant-on window (`master-default-doctrine`) at scale.

The proposed armor was **merge-store top master = 0 into every song's mark**, so each song opens gate-closed. **Dave ruled it out — "same issue":** a hard zero is still a programmed master, and a close that never re-opens is the actual danger. He substituted **the pan-shell play, at dimmer level**.

## The armor

**Point the mark-cue master rows at an EMPTY dimmer preset.**

- Mint the shell: `Preset 1.99 'cLD MM SHELL'`, empty — `Clear` ×3 then a bare `Store` (`empty-preset-mint-clear-then-store`); readback `kids = 0`.
- In each mark cue's part, a recipe line per master group: `Selection = 'cLD JDC PLATE MASTER'` (415), a second line `= 'cLD JDC BEAM MASTER'` (422), optionally `'cLD JDC ALL'` (401); `Preset`/`Values` = the shell.
- **An empty shell asserts nothing** — no value is contributed, no gate is closed, nothing tracks.
- **Fill it once and every mark follows**, because all 18 marks point at the same object.

## Why this generalises

It is the **same move as the pan shell** one pool over (`venue-position-crowning-and-shell`): keep the structure, neutralise the ingredient, retain a single point of later control. The tour used it twice in five days, in two different pools, for two different problems. Treat "point it at an empty shell" as the standing answer whenever an ingredient must stop arguing without being deleted.

## Standing open item

**The shell lines into the 18 mark cues are DAVE'S FINGERS.** Recipe *line creation* is not wire-reachable (`recipe-line-creation-not-wire-reachable`) and raw `AbsPreset` rows are not object-tree reachable, so the shell was minted and the exact per-mark recipe handed over rather than attempted from the bridge.

**Relation:** `master-default-doctrine` (Verse One — the law this armors) · `empty-preset-mint-clear-then-store` · `venue-position-crowning-and-shell` · `cooked-recipe-rows-immune-to-store-remove` (the migration that emptied the dimmer lane first) · `recipe-line-creation-not-wire-reachable`.

History: none — ruled and executed 2026-08-26.

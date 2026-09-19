---
id: paste-round-verification-protocol
title: "Paste-round discipline (paid for repeatedly): re-click ⌨ every round, screenshot-verify before pasting, census-readback after every write batch — never trust a clean echo"
role: programmer
tags: [ma3, computer-use, process, danger]
when_to_load: "Before any computer-use paste round into MA3's Edit Command popup, and before trusting a batched write's clean-looking echo — read this before, not after, a repair cycle"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**This protocol exists because it was paid for repeatedly** — once when a blind repeat-paste fell through a self-closed popup into a patch-sheet cell editor and mangled the paste text into it, again when a 16-command wing-JDC position paste echoed clean but silently hadn't landed at all (caught only by the next census, then repaired and re-verified — see `export-diff-verification-loop`), again on 2026-07-15 when the popup self-closed in the narrow gap between a zoom-verify and the follow-up standalone `Return` during a 6-paste multi-instance build — census caught only 240 of an expected 288 subs, one paste dropped whole (mechanism detail in `computer-use-input-loop`) — and again on 2026-07-16, when a blind-batched paste round fell through mid-`Store` (the zoom looked black; the popup was actually absent) during the phaser/recipe session. A repeat round done *with* the screenshot-verify step passed clean. All four failures looked fine, or would have if the verify step had been skipped; none was safe to assume.

**The rule:**
1. **Re-click the ⌨ icon every round.** Never assume the Edit Command popup is still open from the previous round — it self-closes intermittently and unpredictably, and there's no reliable visual cue that it happened until you try to type into nothing.
2. **Screenshot-verify the popup actually exists before every paste.** Don't blind-repeat a click→paste sequence just because it worked last round. **Reinforced 2026-07-16:** not skippable even under time pressure — the one round that skipped it (mid-`Store`, under time pressure) is the fourth paid-for failure cited above; the repeat done with the verify step passed clean.
3. **Never click the popup's ✗-close button.** Its coordinates land on whatever's behind the popup once it's gone, same as any other fall-through click — skip closing it explicitly rather than risk it.
4. **Readback census after every write batch**, not just when something looks wrong. A clean echo is not proof anything landed — see the phantom-paste case above. **This step is not optional:** the 2026-07-15 zoom-verify/`Return` self-close race (see above) produced zero visible symptoms — no error, no dropped echo, nothing to see — and was caught **only** because a census was run after the build (240/288).
5. **Home-key head-check on long pastes (2026-07-15).** The popup's text field scrolls horizontally at roughly 100+ characters — past that length, the **head of the pasted text can look dropped or missing even though nothing truncated** (it's just scrolled out of view). Press **Home** to scroll back and confirm the head actually landed before treating a long paste as verified.
6. **After any `switch_display` call, take a fresh screenshot before doing step 2's popup-exists check.** Clicks (including the popup-exists check itself) resolve against the **last screenshot taken**, not the newly-active display — verifying against a stale pre-switch screenshot can silently aim the whole round at the wrong display. Full mechanism in `computer-use-input-loop`.

**Where a fall-through paste lands depends on what's behind the popup:** on the patch sheet, it can land inside a `Thru`-capable cell-editor/calculator and get mangled into a spread expression (the repair-cycle case). On a **fullscreen grid canvas**, a fall-through click is usually a benign cursor-move, but a fall-through **drag** could move grid cells — so the same discipline (re-click ⌨, screenshot-verify, no blind repeats) applies there too, not just on the sheet.

**Supporting data point:** paste length isn't the risk — the Edit Command popup accepts pastes of at least 1073 characters (a 28-command batch went through clean) with no ~1KB truncation observed. Failures in this session were consistently popup-**state** problems, not length problems, which is part of why the protocol above focuses on verifying state rather than chunking pastes smaller. (2026-07-15 addendum: the field does **visually scroll** past ~100 characters — a display artifact, not a truncation — which is exactly what rule 5's Home-key check above guards against.)

**Coordinates from this session (Mac onPC 2.4.2.2):** ⌨ icon at approximately `(122, 57x)`; the popup's text field at approximately `(600, 333)`. These corroborate the `~x=122` figure already on file in `computer-use-input-loop`, which documents the underlying click→type/paste→Return loop this protocol wraps a verification discipline around.

History: Updated 2026-07-15 — added a third paid-for failure (the zoom-verify/`Return` self-close race, caught at 240/288), a mandatory-census reinforcement citing that catch, a new Home-key head-check rule for the field-scroll display artifact, and a `switch_display` fresh-screenshot rule; all sourced from the multi-instance GS/recipes live session (`findings/INBOX.md` + same-date wrap). Originally assembled 2026-07-14 from two paid-for failures earlier that evening (the sheet-cell mangle and the phantom wing-JDC paste), both inside the template-rig 3D-position build. Updated 2026-07-16 — added a fourth paid-for failure (a blind-batched round fell through mid-`Store` when the popup was actually absent behind a black-looking zoom), reinforcing rule 2 as not skippable under time pressure; the repeat round done with the verify step passed clean. Source: `findings/INBOX.md`, 2026-07-16, phaser/recipe live session.

# MA3 PROGRAMMER SPINE — generated, do not hand-edit

Source of truth: the individual files in `concepts/`. This is the whole-load view
(`tools/build_public_index.py`): every ACTIVE `programmer` + `operational-live`
concept, frontmatter and History sections stripped. Not a boot load — pull depth
per phase (see `skills/ma3-run-session.SKILL.md`).

> A story in this corpus is a stored value: the miss that drew the rule's edge, the receipt that earned its trust, the why that covers the case nobody wrote down — 🔴 READ IT LIKE PATCH, NOT LINER NOTES.

CONCEPTS: 293 · `⚠ VERIFY` = banked, not live-confirmed.

---

## CLI, INPUT & FEEDBACK

### changedestination-cli-quoting-trap
**ChangeDestination requires a quoted object name — a bare number fails ("Failed:ChangeDestination 1"); an unquoted stray like "cd1" gets parsed as Fixture "cd1" — a dictation-artifact trap**
*when:* Before generating or dictating a ChangeDestination command — bare numbers fail outright, and unquoted shorthand tokens silently get reinterpreted as a Fixture reference instead of erroring


**Bare number fails outright:** `ChangeDestination 1` returns **`Failed:ChangeDestination 1`** — a bare numeric argument is not accepted.

**Quoted object name works:** `ChangeDestination "cld chase gaps"` is the correct form — the destination must be a quoted object name string.

**Dictation-artifact trap:** an unquoted stray token like `cd1` does not error — it gets silently parsed as **`Fixture "cd1"`**, a different command entirely with no relation to `ChangeDestination`. This is a live trap for voice-dictated CLI generation: a garbled/abbreviated destination name doesn't fail loudly, it fails by *executing a different, plausible-looking command*.

**Rule of thumb:** always quote the `ChangeDestination` target as a full object name string, and treat any short/abbreviated token in a dictated command as suspect until verified against the intended object — a clean-looking echo can still mean the wrong command ran (see `set-command-unknown-property-fails-silently` for the sibling "clean prompt ≠ success" doctrine).

History: none — first paid for live, 2026-07-17.


### cli-command-batching-delivery-preference
**When handing Dave command lines to type at the interactive CLI, batch them into one line with semicolons — one-command-per-line stays a macro-only rule**
*when:* Before writing out a block of console commands for Dave to type at the interactive CLI


**DELIVERY PREFERENCE (Dave):** when handing Dave command lines to type at the interactive CLI, batch them into ONE line with semicolons — the interactive CLI batches `;` (verified rule). This is a delivery-format preference, distinct from macro authoring: one-command-per-line stays a MACRO-only rule (see `macro-line-syntax-and-batching-rule` — macro lines never batch `;`; the interactive CLI does). Do not confuse the two lanes when generating either a macro XML file or a block of desk-typed commands.

History: none — captured 2026-07-23 [0723cLD] digest run.


### command-enabled-property-name-gotcha
**Property name is CommandEnabled, not CommandEnable — toggling a cue's CMD line with the shorter name silently fails**
*when:* Before Setting a cue's CMD-line enable property — the correct property name is CommandEnabled; the shorter guess fails silently


The property name for toggling a cue's CMD line on/off is **`CommandEnabled`** — NOT `CommandEnable`. The shorter, more "natural"-sounding name **fails silently**: no error, no effect, clean prompt.

Same family as the pinned `patch-set-one-prop-quoted-values` naming-precision gotcha and `set-command-unknown-property-fails-silently` (unknown/wrong property names on `Set` fail silently with no echo). Different object domain (cue CMD line vs. patch fixtures), same underlying lesson: **never trust a clean `Set` prompt on a property name you haven't verified** — always confirm by readback.

History: none — first captured 2026-07-17, macro deep-dive session, forum thread 8253.


### console-cli-feedback-channels
**Three lanes for reading CLI feedback: the docked line's inline color echo, the Display-2 Command Line History window (click-to-copy), and the History window's per-line macro-execution audit trail**
*when:* When you need to verify whether a just-sent command succeeded or failed, want to reuse/copy a prior command line, or need to audit what a builder macro actually executed line-by-line after a Go+


**Lane 1 — docked command line inline color feedback:** the docked command line shows its **last response inline, colored** — **red = error**, **magenta = echo**. This is usable success/fail feedback for a just-sent command **without needing a Command Line History window open at all**.

**Lane 2 — Command Line History window (Display 2):** Dave swapped Display 2 to a Command Line History window mid-session (2026-07-10) — this fulfills the **cLD Program view spec's non-negotiable History-window element**, now existing live rather than just specified. **Hover hint observed on a history line:** "Click on a line to copy it back into the command line."

Use Lane 1 for a quick glance at the immediately-preceding command; use Lane 2 (when available on Display 2) to scroll back further or to copy an earlier command back into the docked line.

**Lane 3 — per-line macro-execution audit trail (2026-07-23 [0723cLD]):** running a macro (e.g. via `Go+ Macro n`) logs **every line** of that macro to the Command Line History, each prefixed `(Macro N 'name')` followed by either `OK:<cmd>` or `Illegal object:<cmd>` (or similar). This is a genuine **per-line builder-run audit trail** — not just a log of the top-level `Go+` call. **New standing verify (2026-07-23):** after every builder-macro `Go+`, read the History tail (or do a line-readback diff of the authored file against console Command strings) **alongside** the usual object census — this is the only reliable way to catch a macro that ran but silently fragmented or misfired mid-line (see `macro-xml-schema-cracked`'s quote-truncation failure mode for exactly the kind of bug this catches that a clean top-level echo would miss).

**Note:** none of the three lanes substitutes for a readback verification of a `Set` command's actual effect — see `set-command-unknown-property-fails-silently`, since a clean/non-error echo does not prove an unknown property name actually took effect.

History: none — both lanes observed/confirmed live 2026-07-10. Extended 2026-07-23 [0723cLD]: added Lane 3, the Command Line History's per-line macro-execution audit trail (`(Macro N 'name')OK:cmd` / `Illegal object:...`), discovered as the catch lane for the same-day macro quote-truncation bug — now a standing post-Go+ verify step alongside object census.


### dialog-suspend-resume-batched-lines
**A blocking dialog SUSPENDS the rest of a `;`-batched CLI line and RESUMES it on resolution — even Cancel resumes the queue**
*when:* Before batching multiple `;`-separated commands where one might pop a blocking dialog (Assign Layout Merge/Overwrite, etc.) — determines whether queued commands after the dialog will still run


**Settled behavior (revised mid-session, 2026-07-14): a blocking dialog SUSPENDS the remainder of a `;`-batched CLI line and RESUMES executing the queued remainder once the dialog is resolved — even clicking Cancel resumes the queue; it does not abort it.** Evidence: a batched line queued a command past an Assign-Layout Merge prompt; after clicking **Cancel** on that dialog, a later command in the same batch still executed — `cld_l2_probe.xml` materialized on disk *after* the Cancel click, proving the queued remainder ran rather than being dropped.

**This supersedes an earlier same-session reading.** The first pass at this finding concluded the opposite: that a blocking dialog (e.g. Assign's Merge prompt) **kills** the rest of a `;`-batched line, with commands after it never running, and recommended keeping any dialog-popping command at the end of a paste or standalone. Better evidence collected later the same session overturned that reading. **Practical effect:** the old workaround (isolate dialog-popping commands at the end of a batch) is no longer necessary.

**This reopens the "Export is context-relative" question — see `export-context-relativity` [VERIFY].** The one data point behind that separate finding (an `Export` failing from a LivePatch prompt) was captured around the same test where a dialog was in play. Now that suspend/resume is understood, that data point may have another explanation and needs re-testing in isolation before the context-relativity claim stands on its own.

History: first pass (same session, 2026-07-14) concluded dialogs kill the rest of a batched line; corrected the same day after the Cancel/`cld_l2_probe.xml` evidence showed suspend-then-resume instead — the corrected reading is what's stated above.


### edit-command-escape-pending-line-trap
**⛔ Escape on the Edit Command popup does NOT discard the line — it stays pending and can fire later with appended junk**
*when:* Before backing out of / aborting ANY staged Edit Command popup line — this is the correct abort procedure; never reach for Escape


**The trap:** pressing **Escape** on the Edit Command popup does **not** discard the typed line. The popup closes, but the text stays **PENDING in the docked command line underneath** — alive, uncommitted, and waiting for whatever keystroke or click reaches the docked line next.

**Paid-for case (2026-07-15, live):** a staged line was Escaped out of, believed dead. A subsequent **canvas click appended "Grid 12/7"** to the still-pending line, and the whole thing then **committed as `Store Group 128 ... Grid 12/7 /MAtricks`** — a dirty, unintended Store the operator never meant to execute, with no further confirmation prompt in between. This was only caught via a **Display-2 Command Line History** readback (see `console-cli-feedback-channels`); the dirty Group 128 then had to be deleted.

**The rule:** to abort a staged popup line, **select-all (Cmd+A) + delete** the text, or **commit a harmless replacement value** over it. **Never trust Escape to discard content** — treat it as a popup-dismiss action only, with zero guarantee about what happens to the text it was covering.

**Distinct from the self-close race:** this is a different failure direction than the popup self-close hazard documented in `computer-use-input-loop` / `paste-round-verification-protocol`. Self-close silently **drops** a commit (nothing executes). This Escape trap silently **preserves and later contaminates** a commit (something unintended executes). Both are popup-lifecycle dangers; they fail in opposite directions, so a mitigation for one does not cover the other.

**⛔-candidate:** flagged as such in the source INBOX line — a strong candidate for promotion to a `MEMORY.md` hard-rule pointer (paid for live, matches the bar set by existing hard rules like `patch-set-one-prop-quoted-values`). The librarian does not edit `MEMORY.md`; surfaced in the run report for Dave/cLD to ratify.

History: none — first capture 2026-07-15.


### loadshow-cli-when-menu-dead
**LoadShow "name" /nc is the CLI load lane when the Backup/menu UI won't open — quotes for names with spaces, no .show extension, SelectDrive first for USB, and it DISCARDS unsaved work**
*when:* When the console's Backup menu won't open and a show has to be loaded, or before typing any LoadShow — the quoting/extension/drive rules are unforgiving and the command silently discards unsaved changes


**The situation this exists for:** show day, the console's Backup/menu UI refuses to open, and the file has to be loaded anyway. The CLI path works when the menu does not.

## The form

```
LoadShow "Show Name" /nc
```

- **Quote the name** whenever it contains spaces (tour filenames always do).
- **No `.show` extension** — the name only.
- **`/nc`** kills the dialog dependence, exactly as in the SaveShow forensics (`saveshow-enumerate-headless-cancel-class`) — without it the load is at the mercy of a dialog that may be unanswerable.
- **`SelectDrive` first** if the show lives on USB rather than the internal drive.
- **`SaveShow` (bare) first if there is anything unsaved** — LoadShow discards the running show without further ceremony.

**MCP note:** `LoadShow` is **denied** in the MCP classifier and stays denied (`saveshow-discipline-and-mcp-tier`). This is a **desk-typed** lane — Dave's hands on the console command line, not a bridge call.

**Relation:** `saveshow-enumerate-headless-cancel-class` (the `/nc` reasoning) · `save-disk-verify-mtime-delta` (verify before you discard) · `saveshow-discipline-and-mcp-tier` (why this never rides the bridge).

History: none — delivered live on a show day when the UI failed, 2026-08-22, manual-cross-checked at the time.


### quickey-20-popup-abort-lane
**`Quickey 20` — Dave's custom CLI keyword that fires an Esc dismissing any popup/stray window; the sanctioned computer-use popup-abort lane**
*when:* Before scripting any computer-use interaction that might need to abort a stuck popup, dialog, or stray floating window on the MA3 console — this is the tool to reach for, never a synthetic Escape keypress


Dave built a custom console Quickey — **`Quickey 20`** — specifically for cLD's computer-use work. Typing `Quickey 20` on the CLI fires an Esc that dismisses **ANY** popup or stray floating window — live-verified tonight when it killed a stray floating window mid-session.

**Why it exists:** synthetic Escape keypresses are dead at the console layer, the same family of constraint as `synthetic-text-input-rejected-by-command-line` (the console rejects computer-use's synthetic input across multiple channels, not just text). `Quickey 20` is the sanctioned workaround — a real console-side keyword typed through the normal Edit Command popup loop (see `computer-use-input-loop`), which the console itself translates into a genuine Escape that DOES reach the popup layer.

**Scope — what it dismisses vs. what it doesn't:** it dismisses general popups and stray windows. It is a separate, adjacent mechanic from exiting a preset/recipe **Edit session's edit mode** — see `edit-session-mechanics-and-contamination-risk` for that: Escape/`Quickey 20` does turn edit mode off, but the values it pulled into the programmer are NOT cleared by it (that needs a separate `ClearAll`). One source mention phrased this as Quickey "not closing the Edit session banner" — read together with the other two mentions, the resolved understanding is the mode/values split just described, not a claim that Quickey fails on edit-session popups generally.

**Standing tool:** use `Quickey 20` instead of guessing at exits or attempting a synthetic Escape.

History: none — introduced and used live 2026-07-16, first session it existed.


### set-command-unknown-property-fails-silently
**Set with an unknown/wrong property name fails SILENTLY — no error echo, no effect, clean prompt ≠ success**
*when:* Before trusting that any Set <object> "<property>" <value> command worked — especially with a property name you haven't confirmed against the object's actual schema


**`Set` with an unknown or incorrect property name fails silently** on 2.4.2.2: no error echo in the command line, no visible effect, and the prompt returns clean — indistinguishable from success at the command line.

**Paid for twice before the catch:** `Set <layout element> "Border" 1` and `Set <layout element> "Border" "Visible"` both silently no-op'd — "Border" is a sheet **column header**, not the actual property name (the real property is `VisibilityBorder`; see `layout-element-property-names-vs-sheet-headers`).

**Rule: a clean prompt is never sufficient evidence that a `Set` succeeded.** Always verify by readback via one of:
- the object's property sheet (visually confirm the value changed),
- a header/bounds readout (e.g. Layout's `Used X/Y/W/H`),
- or an XML export of the object.

This generalizes beyond Layout — treat it as a standing rule for **any** generated `Set` command against a property name that hasn't been independently confirmed.

**Related failure modes, different trigger:** on **patch fixtures** specifically, `Set` also fails/misbehaves silently in two more ways that have nothing to do with the property name being wrong — chaining multiple properties onto one `Set` silently drops all but the first pair, and unquoted negative values get their sign silently flipped. See `patch-set-one-prop-quoted-values` (⛔ hard rule) for both.

History: none — first paid for live, 2026-07-14, discovered while trying to toggle Layout element borders via CLI.


### synthetic-text-input-rejected-by-command-line
**MA3's docked command line rejects ALL synthetic text input, not just voice dictation**
*when:* Before attempting any automated/synthetic text entry into the MA3 command line — via voice dictation, computer-use type actions, or any non-physical-keystroke input method


Original 2026-04-01 finding: Wispr Flow voice dictation doesn't reliably work in the MA3 command line input field.

**Generalized 2026-07-04:** the docked command line rejects **ALL synthetic text**, not just voice dictation output — this is a broader input-method constraint, not a Wispr-specific quirk. Confirmed during the v2.4 computer-use session: synthetic `type` events do not land in the docked command field at all, while **real key events DO reach the shortcut layer** (see `computer-use-input-loop` for the working workaround via the on-screen keyboard icon and Edit Command popup).

History: generalized 2026-07-04 from a Wispr-Flow-specific note (2026-04-01) to a general synthetic-text-input constraint, after the computer-use session confirmed the same rejection applies to `type` actions, not just dictation.


## GENERAL

### at-filters-worlds-manual-gap-and-study-doc
**If/At/Filters/Worlds study doc created; repo manual confirmed gappy on Worlds/Filters (stub) and At (keyword-list only, no detailed section)**
*when:* Before hunting the repo manual for At/Filters/Worlds documentation, or before trusting a repo-manual 0-hit on these topics as complete coverage


**Study doc created:** `WORKING/IF_AT_FILTERS_WORLDS_STUDY_v0.1.md` — covers the If family / At / Filters / Worlds command surface, our project's use cases for each, and a scoping-stack model tying them together.

**Repo manual gaps confirmed while building the study:**
- **`02_FixtureSelection` §SS12 (Worlds/Filters) is a STUB** — not written out.
- **`01_CommandLine_Reference` has NO detailed `At` section** — `At` only appears in the bare keyword list, with no worked syntax/examples.

This joins the running manual-gap list (see `measure-layer-math`'s "repo-manual gap #4+" note for the prior entry on Measure). Treat any repo-manual lookup on Worlds/Filters/At as **incomplete by default** — cross-check the forum/live console before trusting a manual silence on these topics.

Cross-reference: `at-menu-is-at-filter-menu-reading` for a specific interpretive finding that came out of this same study; `manual-index-vocabulary-is-curated` for the separate (but related) fact that the manual **search index** is hand-curated — this concept is about actual **content** gaps in the manual text itself, not index-vocabulary coverage.

History: created 2026-07-17 from the study-doc build session.


### cld-sandbox-and-namespace
**CLAUDE_SETUP_V0.1.show sandbox and the cLD console namespace reservations (objects 101+, Views 24-26)**
*when:* Before creating any cLD-authored console object — check the namespace reservation to avoid colliding with production pools


- **`CLAUDE_SETUP_V0.1.show`** = the cLD sandbox showfile: 10 generic fixtures, FID 1–10, one 1×10 line. Full-spread phase for N=10 = **324°** (see `phase-math-formulas`).
- **cLD console namespace: objects 101+, labeled `cLD *`.** Example allocations: Groups 101–103 = All/Odd/Even; MAtricks 101–104 = Full/Half/2-Wing/Quarter.
- **Views 24–26 reserved** for cLD Program/Phaser/Verify — not yet built as of this entry.
- **View buttons:** `ViewButton 1.1–1.6` = Fixture / Preset / SeqSheet / Phaser / 3D / DMX.
- `Store View 23 "CLAUDE 1"` exists (already created).

**⭐ EXTENDED TO PRESET NAMES, 2026-07-28 (Dave ruling) — `cLD ` PREFIX ON EVERY cLD-AUTHORED PRESET.**
The namespace rule above governs object NUMBERS; this extends it to NAMES, which is where the
{FESTIVAL} transplant actually needs it — our phasers (`21.<century>20`), colours and positions
all live in pools {LD} already occupies. **Standing form: `cLD <name>`.**

**The console fact that forced it (live-verified 2.4.2.2):** MA3 enforces unique preset names
within a pool and **silently auto-suffixes an exact duplicate with `#2`** — labelling Preset
2.69-75 with names already held at 2.2-2.8 produced `Lowest#2`, `Low#2`, `Down#2`… The command
returned `ok` with **no error and no warning that a rename had occurred**; only a name readback
caught it (same silent-success family as `set-command-unknown-property-fails-silently`).
Re-labelling with the `cLD ` prefix landed clean, confirming the suffix fires **only on an exact
collision** and a prefix avoids it entirely.

**Three reasons this is the right rule, not just a workaround:** it dodges the silent
auto-suffix; it makes **provenance readable at a glance** in a file whose names have already
proved false twice (groups, then position presets — see
`inherited-file-membership-is-ground-truth`); and it is one decision instead of a per-batch one.

**Possible continuity note (unconfirmed, flagged 2026-07-14):** a similarly-named show, `cLD_SANDBOX_v0.1`→`v0.2`, is in active use as of 2026-07-10/2026-07-14 as the festival-template-rig testbed (FID 101–164, MAC Encore Performance CLD spots — see `tourshow-template-rig-patch-and-layout-state`). Whether this is the **same** showfile as `CLAUDE_SETUP_V0.1.show` (renamed/evolved over time) or a **separate** sandbox is **not confirmed** by the corpus — don't assume continuity. Notably, the new patch's fixtures do land inside the **objects 101+ namespace reservation** documented above, which is consistent with either reading (a genuinely separate sandbox would still be expected to respect the same reservation). Confirm file identity (show-file metadata, or ask Dave) before assuming either sandbox's contents describe the other.

## ⛔ COPY CARRIES THE SOURCE NAME AND FIRES THE SILENT `#2` TOO — live 2026-08-05 [0805cLD]

**`Copy Preset 21.73 At 21.2220` echoed `OK` and landed as `cLD PAN SINE#2`**, because the copy
inherits the source object's name and MA3 auto-suffixes an exact in-pool duplicate with **no
error and no warning**. **Confirms the `#2` rule above now applies to the COPY verb
specifically, not just Store/Label.** Same behaviour confirmed on MAtricks copies.

**Standing move: `Copy` then `Label` immediately, then name-census the readback** — the
readback is the only tell, exactly as with the original Store/Label discovery above.

History: none — established 2026-07-04 as the first namespace convention for cLD-authored objects. Flagged 2026-07-14: a same-family-named later sandbox exists; identity/continuity with this one is unconfirmed, noted above rather than assumed.

History: extended 2026-07-28 [0727-2cLD] — Dave ruled the `cLD ` name prefix standing for all cLD-authored presets, after MA3's silent `#2` duplicate-suffix behaviour was discovered live on the first console write of the session.


### computer-use-input-loop
**The reliable computer-use text-entry loop for MA3's command line, plus display-swap click-targeting gotchas (Finder-phantom stale-frame + switch_display stale-screenshot)**
*when:* Before scripting any computer-use interaction with MA3's command line, or any click sequence spanning a switch_display call — use this exact loop, not a direct type into the docked field; check the display gotchas before any multi-display click


- **Docked command line rejects synthetic `type` entirely** (see `synthetic-text-input-rejected-by-command-line` for the generalized rule). ShCuts ON makes single letters fire as keyword shortcuts (`g`→Group, `s`→Store). **Real key events DO reach the shortcut layer**; synthetic text into the docked field does not land.
- **Reliable loop:** click the **⌨ icon** (left end of the command bar, **~x=122**) → **Edit Command** popup opens → click the field → `type` → `Return`. **Prefer `Return`** over clicking the on-screen "Please" key.
- **`;` batches distinct commands in interactive CLI** (verified live, 2.4.2.2) — see `macro-line-syntax-and-batching-rule` for how this differs from macro-line authoring. `Set <obj>` property chains stay semicolon-free internally in both contexts.
- **Cmd+V paste VERIFIED WORKING (2026-07-10, 2.4.2.2 Mac)** into the Edit Command popup field — this is the fast lane for long/batched blocks: **⌨ icon → click field → Cmd+V → Return**, replacing char-by-char `type` for anything long. Use this instead of `type` whenever the text originates on the clipboard.
- **⚠️ Docked-line paste danger (2026-07-10):** the docked command line rejects paste too — **both Cmd+V AND Ctrl+V are dead there**. Worse than a no-op: sending **Cmd+V with focus on the docked line fires the shortcut layer** and pops an unwanted **Edit HIGHLIGHT** popup instead of pasting. **Never send cmd-chords at the docked line** — always route paste through the ⌨ Edit Command popup above, never attempt it directly at the docked field.
- **Display gotcha #1 ("Finder phantom"):** plugging/unplugging a second display mid-session stales the window-frame cache → clicks intermittently hit-test as Finder instead of MA3 (screenshots are unaffected, only click targeting). **Stabilize to ONE display before UI work**; click an inert canvas area to dismiss tangled popups; prefer left-anchored controls (less likely to be affected). **Corroborating data point (2026-07-10):** the phantom-click pattern hit **right-side zones on both displays** that session (MAtricks editor Grid tab, fixture-sheet Prog Only button) while left-anchored controls + the Edit Command popup field stayed clickable throughout — no display topology change occurred that session, so the phantom's actual trigger condition is still unconfirmed, but this is a second data point supporting the left-anchored-controls preference. **Keyboard-commit bypass confirmed (2026-07-15):** when the granted/target app stays frontmost, finishing a staged action with a **keyboard `Return` instead of a click bypasses the phantom entirely** — the phantom appears to intercept mouse hit-testing only, not routed key events (source: wrap `2026-07-15-multiinstance-gs-recipes-storedefault.md`).

- **Display gotcha #2 (`switch_display` stale-screenshot, 2026-07-15) — a DIFFERENT mechanism from gotcha #1 above:** after calling `switch_display`, click coordinates resolve against the **LAST SCREENSHOT taken**, not whatever display is now actually active. A paste round started right after a display switch but before a fresh screenshot lands its clicks on the WRONG display entirely (observed: fell through onto the grid canvas on the non-target display). **Rule: take a fresh screenshot immediately after every `switch_display` call, before any click** — never aim a post-switch click off a pre-switch screenshot.

- **Popup self-closes intermittently (2026-07-14):** the Edit Command popup survives a `Return` with the field cleared, but can **self-close mid-session** on its own. When that happens, a blind repeat-paste lands on whatever is behind the popup instead — this cost a repair cycle once when a stray paste fell through onto the patch sheet and landed in a Pos-cell's Thru-capable calculator, mangling a spread edit into it (see `patch-set-one-prop-quoted-values`). **Rule: don't assume the popup is still there. Screenshot-verify it exists before every paste round, or re-click the ⌨ icon every round regardless.** **Race window narrowed (2026-07-15):** the self-close can land specifically **between the zoom-verify screenshot and the follow-up standalone `Return`** — the paste looked correct at verify-time, the popup then closed before the commit keystroke landed, and the line silently never commits (no error, no echo, nothing visibly wrong). Caught only by post-build census — 240 of an expected 288 subs present after a 6-paste build, one paste dropped whole. Re-paste is a safe repair (placement is idempotent); this exact mechanism is why census is mandatory in `paste-round-verification-protocol`, not optional. (Distinct from `edit-command-escape-pending-line-trap`: that trap silently **preserves and later contaminates** a line via Escape; this race silently **drops** a line via self-close — opposite failure directions, same popup-lifecycle danger class.)
- **Fullscreen-grid variant of the same hazard (2026-07-14):** when the selection-grid window is fullscreen, a fall-through click lands on the grid **canvas** instead — a stray click there just moves the cursor (benign), but a stray **drag** could move cells. Skip clicking the popup's X-close control entirely; its coordinates also land on the canvas.
- **Field-selection behavior confirmed (2026-07-14):** **cmd+A select-all works** in Edit Command popup text fields. **Triple-click does NOT** select an existing `<Default>` token (observed in the Patch Export dialog's name field) — a paste there appends after the token instead of replacing it; use cmd+A first.
- **No length ceiling found (2026-07-14):** a single paste of ≥1073 characters (28 batched commands) executed cleanly — there's no ~1KB truncation. Any past apparent paste "failure" at length was actually popup-state (self-close / fall-through), not a size limit. **Visual scroll caveat (2026-07-15) — not a truncation:** the field **scrolls horizontally at ~100+ characters**, which can make a long paste's **head look dropped even though nothing truncated**. **Home key reveals the head.** See `paste-round-verification-protocol` for the head-check folded into paste verification.
- **Paste-loop coordinates recorded verbatim (2026-07-14, end-of-session handoff note):** `⌨ (122,57x) → field (600,333) → cmd+V → Return → screenshot` — read as roughly icon≈(122,57), field≈(600,333); refines the earlier `~x=122` (no y previously recorded). Quoted as written; the trailing `x` in the source is uninterpreted, not altered.
- **Verification discipline restated (2026-07-14):** a 16-command batch paste on this session's rig build silently failed to land despite a clean echo — the "phantom" paste-failure class isn't closed out. Standing rule: diff/re-export and confirm actual object state after every batch of CLI writes; don't trust a clean echo alone (same theme as `set-command-unknown-property-fails-silently`).

History: none — recorded 2026-07-04, first computer-use session against the v2.4 console UI. Updated 2026-07-10: the Cmd+V clipboard-paste lane (flagged untested/[VERIFY] above) was verified working via the Edit Command popup; a related docked-line paste danger and a Finder-phantom corroboration were recorded the same session. Updated 2026-07-14: documented the popup's intermittent self-close and the resulting fall-through hazard (including a fullscreen-grid-canvas variant), confirmed cmd+A/triple-click field-selection behavior, confirmed no truncation at ≥1073-char pastes, and restated the standing verify-by-diff discipline after a same-session silent-paste-failure recurrence. Updated 2026-07-15: added a second, mechanistically distinct display gotcha (`switch_display` stale-screenshot click-targeting), a keyboard-commit bypass for the Finder-phantom hazard, a narrowed self-close race window (between zoom-verify and standalone `Return`, caught at 240/288), and a field-scroll-vs-truncation caveat — all paid for live during the multi-instance GS/recipes session (see `findings/INBOX.md` 2026-07-15 and the same-date wrap).


### deferred-conclusion-is-not-a-held-conclusion
**A deferred conclusion is not a held conclusion — anything derived file-side that constrains a desk action travels INTO the desk step in writing**
*when:* At every file-side-to-desk handoff — before a desk step executes anything a file-side analysis already constrained, and when writing desk-step instructions.

**LAW: a deferred conclusion is not a held conclusion. Anything derived file-side
that constrains a desk action travels INTO the desk step in writing** — in the
step's own instructions, not in memory of the earlier reasoning.

Incident (08-05, Dave stopped a live batch over it): cLD derived "author clean
per-song objects, don't copy {LD}'s composites" file-side, deferred it to the
desk step, then at the desk let the sheet's "COPY SOURCE KNOWN" label override
the held conclusion and copied {LD} originals. Caught by Dave; rolled back
cleanly (deletes + re-mint from templates). The corrected copy-source law is
filed at `pool21-block-layout-and-copy-source-law`.

History: none — minted 2026-08-05 [0805-2cLD] from the copied-source-originals incident and rollback.


### glob-false-negative-on-drive-synced-dirs
**Glob/list false-negatives, Read-tool stale-cache reads, AND device_stage_files stale-container-copy reads on Drive-synced directories — verify with ls/live grep/byte-size before trusting any of them**
*when:* Before concluding a directory is empty (or that files were lost) from a Glob/list-tool result, before trusting a Read-tool result that looks stale/wrong, OR before editing based on a device_stage_files-staged copy of a file inside a Google-Drive-synced folder (e.g. WORKING/wraps, WORKING/concepts, WORKING/findings) — cross-check with ls/live grep/byte-size comparison first


**Symptom (2026-07-05, session-start rehydration):** a `Glob` on `wraps/*.md` returned **"No files found"** while the directory actually held **14 wraps** — confirmed by running `ls` at rehydration, which listed them all correctly.

**Root cause:** the directory lives inside a **Google-Drive-synced** folder tree (`MA_PROGRAMMING/WORKING/`). Drive-sync directories can cause glob/list-style tools to false-negative — the mechanism isn't confirmed (sync-placeholder files, FS-event timing, virtual filesystem quirks are all plausible), but the observed behavior is reproducible: the tool reports empty when the directory is not.

**Rule: verify with a second method before trusting a Glob/list "empty" result inside a Drive-synced directory.** `ls` (or an equivalent direct filesystem read) is the confirmed-working second method — it correctly saw all 14 wraps when Glob saw none. Don't conclude "directory is empty" or "files were lost" from a single Glob/list call in these directories; cross-check.

**Cost this session:** the false-negative briefly produced a wrong "wraps missing" note written into session state, caught only at the verification step before it propagated further. The near-miss is the reason this is worth banking as a standing check, not a one-off curiosity.

**Scope:** observed specifically for `WORKING/wraps/`; likely applies to any Drive-synced directory in this project (`WORKING/concepts/`, `WORKING/findings/`, etc.) since the sync mechanism is directory-tree-wide, not specific to one folder. Treat the caution as project-wide until/unless a narrower boundary is confirmed.

**Second symptom, same hazard class (2026-07-08, self-observed during a librarian run):** the **Read tool's file-state cache can briefly lag live disk** in this same Drive-synced folder — a file's `History:` date read as stale via Read, while a live `grep` on the same file showed the current content. Different tool (Read vs Glob) and different failure shape (stale content vs false-empty), but the same underlying hazard class: a tool's view of a Drive-synced directory can disagree with the actual filesystem state. **Rule extended:** cross-check with a live `grep`/`ls` (not just a re-Read) whenever a just-edited file reads oddly, not only when a directory looks suspiciously empty.

**Third symptom, same hazard class, the STAGE lane (2026-07-20) — `device_stage_files` can serve a stale container copy of an already-staged path**, even past the tool's own settle delay: a re-stage of `findings/INBOX.md` was read back at **836 bytes** in the container while the stage call's own result reported **2473 bytes** for the same path. **Rule extended again:** before deriving an edit from a staged copy, compare the actual on-disk byte size at the staged path (`ls -la`) against the stage result's own `bytes` field — if they disagree, the staged copy is stale; re-stage (or rebuild from a known-good read) rather than trusting it.

History: none — first-observed, live, 2026-07-05 (restart-gate-021-ship, session-start rehydration). Broadened 2026-07-08 (librarian run 8, self-observed) to cover a second symptom (Read-tool cache lag) in the same hazard class. Extended 2026-07-20 (07-20 bridge): third symptom added — `device_stage_files` can itself serve a stale container copy of an already-staged path; verify by comparing `ls -la` byte size against the stage result's reported `bytes` field.


## Fourth symptom — a stale STAGED SPINE.md fed to a SUBAGENT, first hit on a subagent rather than cLD — 2026-08-03 [0803-2cLD]

**The exit-gate librarian (a dispatched subagent) grepped its staged copy of `concepts/SPINE.md`, found ZERO of the 5 ids the dispatch brief said were already filed, and read the header as `GENERATED 2026-08-01`** — so it flagged the discrepancy and refused to assume, rather than silently trusting the absence. It was reading a snapshot taken at session start, **before** the same-day regen; the live device copy read `GENERATED 2026-08-03 / 255 concepts` with all 5 ids present.

**Standing rule for dispatch: `device_stage_files` serves a POINT-IN-TIME copy, so any subagent packet assembled early and used late is stale by construction.** RE-STAGE the duplicate-check surface immediately before dispatch, or hand the agent a freshly generated extract — do not reuse a packet staged earlier in the session.

Fourth documented instance of this concept's hazard family (first three: Glob/list false-negative, Read-tool stale-cache, `device_stage_files` stale-container-copy on the STAGE lane) — and the first to bite a **subagent** rather than cLD directly.


## Companion rule from the EU tour leg, 2026-08-08 — hunt with ONE full sweep

Dave's teach the same month: when hunting a file on the device, run **one comprehensive sweep from the top of the allowed roots**, never a string of single-path probes off remembered paths — mounts and repo roots drift between sessions, and a serial probe will happily find a **stale snapshot** of the file you wanted and let you write to it. Full rule, with the ground-truth vs stale-copy receipt: **`device-file-hunt-full-sweep-law`**.

The two rules pair: the full sweep finds the candidates, the live `ls`/`grep` cross-check tells you which one is real.

History: extended 2026-08-28 (librarian, tour leg) — pointer to the device hunt law.


### inherited-file-membership-is-ground-truth
**⛔ On an inherited show file, MEMBERSHIP is the only ground truth — names, labels and pool positions are hypotheses; derive composition from SelectionData FIDs, never from what a group is called**
*when:* Before reasoning about, mapping, or building on ANY group/object in a showfile you did not author — and before treating two artifacts as contradictory. Read this before writing a crosswalk, a remap, or an inventory of someone else's file.


**⛔ THE RULE: on an inherited file, derive composition from MEMBERSHIP — never from the
name.** A showfile adapted from a previous production carries the *previous* rig's naming.
Groups get re-pointed at new fixtures; nobody renames them.

## The paid-for case ({FESTIVAL}, 2026-07-26)

The file was adapted from another artist's show. Membership census against a live
FID→FixtureType map proved the names systematically false:

- **`Strike M US / DS / SW` — 20 groups — are GLP JDC1.** Not Strike M.
- **`Veloce (Grid)`** = MAC Viper XIP x20 **+ Proteus Hybrid x14**, and all three `Spots`
  variants are the **same 34 fixtures** — so **no spot-vs-beam separation exists** anywhere
  in the group layer.
- **`Forte`** = Proteus Maximus + BMFL WashBeam; `Forte US` and `Forte SW` are the **same
  six units**. **`PL`** = COLORado PXL Bars. **`Beamwash`** = Maverick.
- **~24 of 80 groups are EMPTY** — including all 12 per-person "band" groups, which were
  vestigial from the previous artist and had no members at all.

cLD made the **same error three times in one document**: read "the file solves the BAND"
(no band existed, groups empty), read "`(Fest)`/`(Tour)` variants already exist — adopt the
pattern" (both `(Tour)` groups empty), and described the naming grammar as decomposing
cleanly (true as grammar, worthless as evidence). **Root cause each time: treating a NAME as
evidence of CONTENT.**

## The method that actually works

`Export Group <n>` → read `<SelectionData>` member FIDs → join against a live
FID→FixtureType map (`ObjectList('Fixture *')` + `:Get('FixtureType')`). Tooling written and
reusable: `showfiles/festival_recon/group_truth.py` + `fidmap.txt` → `GROUP_TRUTH.md`.
Export is the only reliable group census anyway — `handle:Children()` returns **0** for
Group objects (`group-xml-export-selectiondata-census`).

**Payoff, not just caution:** membership analysis also *collapsed* the problem. Behind 56
populated groups sat only ~12 distinct fixture sets — the rest were layout variants
(Grid/Lin/Sym) and cell-depth variants of the same members. The crosswalk was a ~12-row
job, not an 80-row one. **You cannot see that from the names either.**

## ⚠ Companion hazard — FIDs collide across shows in a shared export folder

MA3 exports every show's objects into the **same** `gma3_library/datapools/<type>/`
folders, so two shows' exports coexist and **their FID spaces overlap** (101-164 exist in
both cLD_SANDBOX and {FESTIVAL}). A first analysis run silently misread our JDC 401-412 as
{FESTIVAL}'s "Color Strike M x288." **Always scope a cross-show file-side analysis by
filename provenance; never assume a datapool folder holds one show's objects.**

## Generalisation — provenance determines authority

The same failure shape appeared in a different domain the next day: the corpus held the
SONG_T colour board and the white-void call as two peer authorities needing a ruling,
when the board was **cLD's own early sketch** predating the information that produced the
other. **Before treating two artifacts as contradictory, establish who made each, when, and
on what information.** See `song-t-board-color-contradiction-ratify-pending`.

Relation: `stripped-group-membership-recipe-uncooked-diagnosis` (the sibling failure — an
intact, correctly-labeled group with its fixtures removed makes a good recipe read dead;
**check membership before diagnosing the recipe**) · `group-xml-export-selectiondata-census`
· `source-profile-inheritance-and-reuse-doctrine`.

## ⛔ EXTENDED 2026-07-28 — IT IS NOT JUST GROUPS. PRESET NAMES LIE TOO.

Third instance in the same file, one pool over. {LD}'s **position presets** are, in Dave's
words, **"labeled as a lie"** — `Lowest` points **upstage and high**; `Highest` is **15°
upstage**. The names do not describe the stored values.

**Generalised rule: on an inherited file, an object's STORED DATA is the truth and its NAME is a
hypothesis — for GROUPS (membership), for PRESETS (values), and by extension for any pool
object.** The fix is identical in every case: read the data, never the label. Ladder detail in
`festival-position-preset-stacking-and-tilt-ladder`.

**Corollary that cost real time this session:** four of the seven ladder names were recoverable
file-side from a sequence export's `<Dependency>` blocks, but **2.6-2.8 appear in no exported
song and needed a live console read.** Do not assume a file-side census is complete just because
it returned results — it only covers what the exported material happens to reference.

## Corroboration 2026-07-29 — Strike M "Fest" variants are truthful; the liars are specifically US/DS/SW

A `GROUP_TRUTH` membership cross-check on the {FESTIVAL} file: **`Strike M [RGB] (Grid) (Fest)`** = Color Strike M ×336 subs (24 fixtures, `401-414`/`421-430`, a 49×8 grid); **`[STB] Fest`** = 672 subs. **Both truthful at the group layer.** The JDC1-liar scope established in the paid-for case above is specifically the **US/DS/SW** Strike M groups — not every Strike M-named group. This does not weaken the standing rule (membership is still the only proof); it narrows exactly which names in this file happen to be honest. Confirms Dave's fill-target hypothesis in `tourshow-fill-layer-rebuild-method` (the fills bind `STRIKE M FEST RGB`).

## ⛔ EXTENDED 2026-08-01 [0801-2cLD] — MAtricks pool labels lie the same way group/preset labels do; third pool class to show it

**MAtricks pool slot labels are not evidence of their stored values — extends this doctrine to a third pool class** (after groups and presets/preset names). Live read, same session: slot labeled `'YGroup 6'` actually stores **`YGroup=3`**; slot labeled `'YWing 3'` actually stores **`YWings=2`**; a slot named `'MAtrick 167'` (a DEFAULT, unedited name) turned out to be **fully populated** (`XGroup=6 XWings=4 YGroup=6 YWings=4`, X+Y `0->360`). Dave moved all three objects to pool slots 40-42 once the mismatch was found.

**The rule, restated for this pool: read MAtricks VALUES, never the slot LABEL, before reusing or trusting a pool object** — the same discipline `tourshow-stock-matricks-pool-inventory`'s companion caution already states for stock/imported MAtricks, now confirmed on a cLD-managed pool slot as well, not just inherited ones.


## ⛔ FOURTH OBJECT CLASS 2026-08-03 [0803-2cLD] — PHASER FIGURE NAMES CARRY ALMOST NO IDENTITY INFORMATION

The cross-song phaser figure content-hash (`tourshow-phaser-figure-duplication-across-songs`) confirms the same failure shape one pool over again — the **fourth** object class, after groups (membership), position presets (values), and the MAtricks pool (values), to show inherited/generated labels lying about content.

**A figure's NAME says where in *that song* it was used, not what the figure IS.** Content-hashing 166 figure name-instances across 17 songs resolves them to 57 distinct contents:

- **8** are the SAME NAME reused across songs (`Dim_Sin_Bump` in 17 songs, `Dim Sinus` in 10, `Dim_Ramp Minus` in 5, `Sin` in 4, `20x20 rel PT Circ#4` in 4) — {LD} reusing one object under one name. Not a discovery; already treated as one figure.
- **10** are **DIFFERENT NAMES carrying IDENTICAL content** — this is the actual finding. Widest span: one content hash appears across **12 songs under 8+ different names** (`Intro 1/1 Dim#2` / `Chorus 1/1 Dim#5` / `Bridge 1/1 Dim#8` / …); a second hash spans 12 songs likewise.
- **39** are unique to a single song.

**Standing consequence: hash the content, never dedup figures by name.** A phaser figure's name is exactly as untrustworthy as a group's or a preset's on this inherited file — the object class changes, the rule does not.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (the concept this fact answers; carries the full hash method plus the 47/31/16 result).

## Scope extended — the hazard now confirmed on a cLD-AUTHORED object too, 2026-08-05 [0805cLD]

**First in-house instance of the labels-lie hazard on an object cLD itself authored, rather
than an inherited one.** MX 148 `cLD XY SHUFFLE 5` reads `XShuffle=5` but **`YShuffle=None`**
— its XY phase IS 0-360 on both axes, but the shuffle is X-only despite the object's own name
saying XY. Flagged, NOT fixed (may already be bound in shipped songs); corrected sibling
minted as MX 185 `cLD S5 YS5 XY360` (Copy 148 + `Set YShuffle 5`). Full detail:
`tourshow-seq2210-song-l-build-record`. **The standing rule above — read stored VALUES,
never a label, before reusing or trusting a pool object — evidently is not limited to
inherited/source-authored content; a cLD-authored object's own name is only as trustworthy as
whatever double-check was actually run against it at authoring time.**

History: none — paid for during the {FESTIVAL} recon, 2026-07-26; generalised 2026-07-27. Extended 2026-07-28 [0727-2cLD]: the rule now covers PRESETS as well as groups — {LD}'s position-preset labels proved false the same way the group names did. Extended 2026-07-29: added a corroborating GROUP_TRUTH census result narrowing the JDC1-liar scope to specifically US/DS/SW Strike M groups, and confirming the Strike M Fest fill-target hypothesis. Extended 2026-08-01 [0801-2cLD]: MAtricks pool labels shown to lie the same way (third pool class). Extended 2026-08-03 [0803-2cLD]: phaser figure names shown to carry almost no identity information (fourth object class). Extended 2026-08-05 [0805cLD]: hazard confirmed for the first time on a cLD-authored object (MX 148), not just inherited/{LD} content; relocated to end-of-file same date — `generated/build_spine.sh` truncates a concept's SPINE.md view at the first `History:` line, so the two `##` sections above (MAtricks pool labels, phaser figure names) had been silently absent from SPINE.md since they were written; this relocation recovers them (gardener rule 4 — nothing deleted, only moved).


### ma3-show-container-format-facts
**MA3 .show file container facts (bytes-verified): GMA3 binary object DB, not zip/gzip/XML — cue data unreachable file-side**
*when:* Before attempting to parse, mine, or extract data from an MA3 .show file directly (without onPC) — know what's readable file-side (names/labels via strings) versus what isn't (cue-level values, live in binary tables)


Verified byte-level against the {FESTIVAL} showfile (`ARTIST_festival_AR_as-received_2026-07-06.show` — see `tourshow-showfile-intake-ritual`):

- **Magic `"GMA3"` at offset 0.** The container is a **binary object DB** — **NOT** gzip, zip, or an XML surface.
- **Names/labels are readable via a strings sweep** — 615k strings recovered from this file.
- **251 embedded PNGs** found in this file (counts are per-file, not a fixed constant — expect variation by show).
- **Sporadic zlib buffers are binary tables, not XML** — don't assume a zlib hit means readable structured text.
- **Cue-level data is unreachable file-side.** The real extraction path is **onPC + XML pool exports.**
- **Extension was `.show`, not `.show3`** — content is MA3 regardless of the extension actually used.

History: none — recorded 2026-07-06, from strings-sweep + byte-offset inspection of the {FESTIVAL} file (see `festival-showfile-save-lineage` for what the names layer revealed, and `festival-rig-fixture-inventory-strings` for the rig-string mining that used this same method).


### paste-round-verification-protocol
**Paste-round discipline (paid for repeatedly): re-click ⌨ every round, screenshot-verify before pasting, census-readback after every write batch — never trust a clean echo**
*when:* Before any computer-use paste round into MA3's Edit Command popup, and before trusting a batched write's clean-looking echo — read this before, not after, a repair cycle


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


### pool-discipline-stock-vs-custom
**Use STOCK pools unless there's a fantastic reason — customization breaks cross-show mergeability**
*when:* Before renaming a pool, creating a new pool, or adding encoder banks — and before storing anything into a feature pool, confirm it's the correct one (e.g. Dimmer = Preset 1.x, Color = Preset 4.x)


Pools are **fully customizable** (rename, new pools, new encoder banks) **BUT customization breaks cross-show mergeability** — **use STOCK pools unless there's a fantastic reason** not to.

**Live-confirmed pool assignments:**
- Dimmer presets = **`Preset 1.x`** (pool 1 = "Dimmer")
- Color presets = **`Preset 4.x`**

**Correction noted:** the earlier phaser stores into `Preset 21.x` (see `coachella-rig-identity`'s "Preset 21.1 Sinus phaser (dimmer)") were **into the wrong feature pool** — phasers/dimmer-type content should have gone through the stock Dimmer pool (`Preset 1.x`), not a pool numbered 21.

**Dave's closing framing, worth carrying forward as a standing principle:** "Memory files are the crown jewels — they survive every show file; protect them above any console object."

History: this concept identifies that the Coachella-era `Preset 21.1` phaser assignment (recorded plainly as fact in `coachella-rig-identity`) was, per this 2026-07-04 lesson, a wrong-pool choice — flagging the discrepancy rather than silently editing the Coachella-era record. See FLAGS in the run report. 2026-07-16: `pool-labeling-doctrine-inherited-risk` extends this — renaming stock pools is fine, the risk is inheriting a file where someone else already did it undocumented (the {FESTIVAL} file's custom pools were the trigger).


### pool-naming-song-prefix-collision-rule
**Spell the song prefix out when a short code collides — 'SONG_M' not 'SN', since 'NS' is already SONG_D**
*when:* Before choosing a short song-prefix code for a pool object name (preset/phaser/MAtricks) — check it doesn't collide with another song's existing short code first


**PREFERENCE (G=0.3).** When a song's short abbreviation code would collide with another
song's, spell the prefix out in full rather than inventing a second short form: **`SONG_M`**
for SONG_M, not `SN` — `NS` is already SONG_D, and `SN` reads as its natural but
wrong sibling.

**Relation:** `pool-labeling-doctrine-inherited-risk` (the sibling risk — renaming/labeling
pools without provenance) · `tourshow-songbuild-kit-and-runbook` (the per-song build line
this naming discipline serves).


### probe-called-unreliable-is-not-evidence
**A probe you have just called unreliable is not evidence — fix it or drop it, never keep it in play as a supporting hint**
*when:* Before using a probe or script's output as supporting evidence for a decision after you have already flagged that same output as looking wrong — the moment a probe result reads as suspect, stop treating any part of it as signal until it is fixed or replaced


**Paid-for process rule, worth more than the bug that produced it.** A probe bug manufactured
a false premise, and cLD built on it AFTER already noticing the probe was unreliable.

`dg_pop_shape.py` printed fixture IDs through a `[:6]` string slice, so `13301` silently
truncated to `1301`. Separately, its inner `sub.iter()` grabbed the FIRST `StandardRecipe`
found in a subtree rather than the correct one, so it attributed both shapes of BOTH Dream
Girl composites to `JDC1 US [RGB]`. **cLD saw the output looked wrong** ("only found ONE
population per figure" — a composite has more than one) **and said so — and then still used
the same probe's output as a supporting signal for the population→shape split it was building.**
The resulting split was backwards: the `Verse 1/2` composite's SINE assignment was inverted, 6
of 23 phaser lines wrong, caught only by the phaser smith cross-checking against {LD}'s own
fixture-ID cover. Full incident: `tourshow-seq2210-song-l-build-record`.

**The rule: once a probe's output has been called unreliable, it is not evidence any more —
not weak evidence, not a "consistent with" data point. Fix the probe or drop the result
entirely. Do not keep it in play as a supporting hint for the same decision it already failed
to make correctly.**

## The method that should have been used instead

The population→shape join is available in-file and cheap, with zero inference: each figure's
own subtree carries `Preset/StandardRecipe/DependencyExport/Dependency/Group/SelectionData/Item`
(the exact fixture roster per population) alongside `Preset/PresetData/Phaser@ID` (the
per-fixture shape). Join the roster against the shape and population→shape falls out directly
— the standing method for every future composite; never infer it from ID prefixes or MAtricks
shape. This method, and the composite-handling doctrine it serves, now live in
`parts-per-century-emit-pattern-and-et-gate`.

**Relation:** `tourshow-seq2210-song-l-build-record` (the build this was paid for on),
`empty-census-deserves-selector-suspicion` (sibling discipline — that concept is about
trusting a ZERO; this one is about trusting a probe you have already flagged as buggy, for ANY
value it returns).


## GROUPS, SELECTION & LAYOUT

### assign-layout-merge-dialog-behavior
**Assign Layout onto an existing layout pops an Overwrite/Merge/Remove/Cancel dialog; Merge appends in selection order but one run silently dropped the range-head FID (47/48)**
*when:* Before running Assign Layout against a layout number that already exists — expect a dialog, and verify Merge results by export diff


**Assigning to a layout number that already exists pops a dialog** with four options: **Overwrite / Merge / Remove / Cancel**. This is distinct from the first-time-creation case (`Assign Layout <n>` with no existing Layout `<n>` — see `layout-cli-assign-and-posxy-syntax`), which creates the layout directly with no dialog.

**The dialog only fires when the incoming selection overlaps existing layout content.** Confirmed by contrast: re-`Assign`-ing a single fixture (FID 201) that was already merged in produced **no dialog at all**, because there was no overlap left to resolve.

**Merge appends the new elements in selection order** onto the existing layout.

**⚑ Anomaly, cause unconfirmed:** one Merge of `Fixture 201 Thru 248` (48 fixtures) into an existing layout appended only **47 of 48** — FID 201, the **range head**, was silently skipped, with no error or warning. A follow-up re-`Assign` of FID 201 alone appended it cleanly (and triggered no dialog, since by then it didn't overlap). The mechanism is not understood — **export-verify (XML or MVR diff) after every Merge** until this is root-caused; don't trust the on-screen element count alone.

**Contrast: `Store <object> /Overwrite` does NOT pop a dialog.** Unlike `Assign Layout`'s Merge/Overwrite prompt, storing over an existing object with the explicit `/Overwrite` flag (e.g. `Store Group ... /Overwrite`) ran with no dialog at all — the flag-based CLI form suppresses the interactive prompt that the plain `Assign` form triggers on overlap.

**New elements added by Merge get auto-placed, not left at a fixed default** — they inherit the layout's current arrange-tool state (e.g. a Line arrangement) until explicitly positioned by `Set` — see `layout-xml-export-schema-and-import-lane`.

**Batching note:** this dialog is a blocking dialog — see `dialog-suspend-resume-batched-lines` for what happens to the rest of a `;`-batched line when it pops (suspend, then resume on resolution, even on Cancel).

History: none — first (and so far only) live exercise of the existing-layout Assign path, 2026-07-14; the 47/48 anomaly is flagged, not yet root-caused.


### grid-bounce-pattern
**The bounce pattern — two fixture types on alternating columns fire alternately; drop the surplus in mirrored triplet gaps**
*when:* Before building a two-type alternating-column grid chase, or when a fixture count doesn't evenly divide the available alternating slots


**The bounce**: put two fixture types on alternating columns of the same grid row-set so an X-sweeping effect alternates fire between them, step by step — Dave's term for the feel is "bouncing between each step."

Drill case (Group 124 "cLD DS WING BOUNCE"): wings placed on every even column (0-30, 16 columns), leaving 15 odd-column gaps for 12 stage spots. 15 gaps for 12 fixtures doesn't divide evenly, so 3 columns go unfilled. Per the mirror doctrine (`grid-mirror-symmetry-doctrine`), those 3 dropped columns aren't arbitrary — they're mirrored drops at columns 7/15/23, which preserves a 3-3-3-3 triplet rhythm on both sides and lands the center drop exactly on the physical SR/SL seam.

Verified round-trip; all FIDs readable at the drill's 31-column zoom level (see the render-behavior note in `selection-grid-and-fixture-cell-model`).

History: none — specced by Dave and drill-verified live 2026-07-14. Fourth and final member of the 2026-07-14 canonical two-part alignment set — see `grid-drill-exemplar-groups-121-124`.


### grid-mirror-symmetry-doctrine
**Grid builds should be mirror-symmetric by default — mirror gap positions about center, seam at the SR/SL boundary**
*when:* Before finalizing any grid layout with gaps or dropped columns — check whether the gap pattern is mirrored about center before storing the Group


Standing default: **grid builds should be mirror-symmetric unless there's a deliberate reason to be asymmetric.** When a layout has gaps or dropped/skipped columns, mirror their positions about the grid's center axis, and land the seam (the center drop, or the point of symmetry) at the physical stage-right/stage-left boundary.

Dave demonstrated this live rather than just describing it: the first pass at Group 123 used a flat, unmirrored skip pattern (dropping columns 3/7/11/15 to fit 12 spots against 16 wing columns). Dave rebuilt it by hand into a mirrored triplet pattern and stored his edit directly over Group 123 (`Store /Overwrite` — no confirmation dialog fires on `/Overwrite`).

This generalizes past the single Group 123 fix: any time a grid build has to drop, skip, or otherwise unevenly distribute cells, the default assumption should be a mirrored solution, with asymmetry treated as an exception that needs its own justification.

History: none — dictated + hand-demonstrated live 2026-07-14, applied to Group 123 "cLD DS WING PAIRED16." The same principle governs Group 124's bounce pattern — see `grid-bounce-pattern`.


### group-edit-remove-pattern
**To remove members from an existing Group: select the fixtures to remove, hit Store, choose the group, hit Remove**
*when:* Before editing an existing Group's membership down (removing specific fixtures) rather than rebuilding it from scratch


**Dave's pattern:** to remove members from an already-stored Group — select the fixtures that should come OUT, hit **Store**, choose the target group, then choose **Remove** (rather than Overwrite or Merge) in the resulting dialog.

**Companion patterns:** this sits alongside `Store` → **Overwrite** (replace the group's contents entirely) and the subtraction-at-selection-time method documented in `group-subtraction-preserves-grid-coords` (build the reduced set via `Group A - Group B` before storing, rather than storing a Remove against an existing group). Same family of choices also appears in the `Store Default` popup (Overwrite/Merge/Remove/Cancel — see `store-default-values-keyword`), suggesting Remove-as-a-store-mode is a consistent idiom across MA3's Store dialogs.

History: none — pattern dictated live by Dave, 2026-07-15.


### group-subtraction-preserves-grid-coords
**Group selection subtraction (`Group A - Group B`) preserves the surviving fixtures' original grid coordinates — gaps show as hollow rows, not a repack**
*when:* Before using Group subtraction to build a section Group from a larger recalled Group — the result keeps its source grid shape (useful when the grid layout itself is meaningful, e.g. a time-map design), it does not compact-pack the survivors


**Verified live:** `Group 125 - Group 126 ; Store Group 127` → **384 selected** (576 − 192, exact) — the surviving fixtures **keep their original grid coordinates** from the recalled group they came from. Where the subtracted members had occupied a row (a strobe row in this build), that row renders **hollow** in the resulting selection rather than the remaining fixtures repacking to fill the gap.

**Ratified as a design-relevant behavior (Dave, 2026-07-15):** the fact that subtractive group math preserves shape (rather than compacting) matters because the grid doubles as a time-map (see `grid-is-a-time-map-doctrine`) — a hollow row left by subtraction is a different, meaningful thing from a repacked one, and Dave confirmed this is the wanted behavior, not a bug to work around.

**Companion method, ratified same session:** direct dot-range entry (`Fixture 301 Thru 312.33 Thru 48 ; Store Group x`, see `subfixture-thru-range-syntax`) is the primary lane for building section Groups directly; subtractive group math is the complementary lane for carving a section back OUT of an already-recalled larger group.

History: none — subtraction behavior and its design-relevance both confirmed live in one session, 2026-07-15.


### group-xml-export-selectiondata-census
**`Export Group <n>` writes full SelectionData (per-item ID + X/Y/Z grid coords) to XML — a numeric census + shape-verification lane for Groups**
*when:* Before trusting a Group build (especially a multi-paste or GS-propagated one) without export-verifying it — this is the group-level counterpart to the grandMA3-XML/MVR diff loops used for patch and layout


**`Export Group <n>`** writes to `gma3_library/datapools/groups/<name>.xml`, with a full `<SelectionData Size...>` block containing a per-`<Item>` `ID` plus `X`/`Y`/`Z` grid coordinates for every member.

**Proven live:** used to census a built Group — caught missing fixtures (407/408 silently absent from a multi-paste build) AND numerically verified every present block's coordinates against the intended layout. Extends the existing `export-diff-verification-loop` pattern (patch/layout) to **Groups** as a third verification lane.

**Bridge:** Desktop-Commander reads the exported XML Mac-side for inspection.

**Filename gotcha:** MA3 lowercases and underscores the Group name for the export filename — e.g. a group named `cLD` exports as `c_ld`.

**Why Export is the ONLY reliable member census (paid for 2026-07-21):** `handle:Children()` returns **0** for GROUP objects — a group's members live in its SelectionData, not as pool child handles, so `:Children()` (which only gives a line-count on Macros) cannot count them. A related Lua-handle trap hit the same readback: `.Count` is a **METHOD, not a property** — `handle.Count` returns a function (live concat error); use `handle:Count()` or `#handle:Children()`. Net: for group member census the ONLY reliable readback is `Export Group` → read the `SelectionData Size` attr from the XML (proven on G51/101/109/601). Never try to census a group via `:Children()`.

History: none — export lane proven live in one session, 2026-07-15, catching a real silently-dropped-fixture bug (see `paste-round-verification-protocol` for the paste-hygiene half of this same finding). Extended 2026-07-21: pinned WHY this is the only lane — `:Children()` returns 0 for groups and `.Count` is a method, so Lua-handle census fails; Export is the reliable path.


### layout-cli-assign-and-posxy-syntax
**Building a Layout entirely by CLI: Assign Layout <n> creates it from a selection; Set Layout n.e "PosX"/"PosY" places elements; the editor doesn't need to be open**
*when:* Before building or editing a grandMA3 Layout view from the command line instead of by hand


**All live-verified on 2.4.2.2.**

**Create a layout from a selection:**
```
Assign Layout 2
```
With fixtures selected, this creates Layout 2 and adds the selection **as elements, in selection order**, addressed `Layout 2.1` .. `Layout 2.n`.

**Place/move an element:** position properties are **`"PosX"`** / **`"PosY"`** (quoted). Chained properties in one `Set` work:
```
Set Layout 2.1 "PosX" 0 "PosY" 600
```

**Scale confirmed:** a 64-element plot was placed in **3 clipboard pastes** (batched `;` chains — see `macro-line-syntax-and-batching-rule`).

**Verifying mass sets without the canvas:** the layout header's **`Used X/Y/W/H`** fields are a **live bounding-box readout** — after a batch of `Set Layout n.e "PosX"/"PosY"` calls, check `Used` to confirm the placements landed in the expected bounding box, without needing to look at the canvas.

**The Edit Layout editor is a viewer/verifier, not a required context:** it auto-closed mid-session (2026-07-14, either from Dave's UI activity or a `SaveShow`) and `Set Layout` commands continued to work fine with the editor **closed**. Don't assume the editor needs to be open for CLI layout work.

**Related:** property names for things like borders/IDs are **not** the same as the sheet's column headers — see `layout-element-property-names-vs-sheet-headers`. `Set` with a wrong property name fails silently — see `set-command-unknown-property-fails-silently`; always confirm via `Used` bounds or an XML export, not just a clean prompt.

**If Layout `<n>` already exists, `Assign Layout <n>` behaves differently** — instead of creating cleanly, it pops an Overwrite/Merge/Remove/Cancel dialog. See `assign-layout-merge-dialog-behavior` for the dialog options, the overlap-triggers-dialog rule, and a live 47/48-merge anomaly.

History: none — first built live, 2026-07-14 (Layout 2 "SPOT PLOT").


### layout-division-of-labor-sheet-vs-cli
**Division of labor confirmed: the property SHEET wins for bulk uniform toggles (3 clicks beats 64 CLI sets); CLI wins for generated/computed geometry**
*when:* Before deciding whether to script a bulk Layout/element property change via CLI or just do it in the sheet — a uniform change across many elements is a sheet job, not a CLI-loop job


**Worked example — Layout 2 "SPOT PLOT" (saved as `cLD_SANDBOX_v0.2`):** 64 elements placed exactly via CLI (4 truss rows at `y=600/400/200/0`, `x=0-1100` step 100; wings at `x=-200 & 1300`, `y=0-560` step 80 — this initial wing placement was later re-specced, see `tourshow-template-rig-patch-and-layout-state`).

**Strays:** elements 63/64 got dragged out of place during Dave's manual "Setup" play; restored via CLI. (A reminder that manual UI interaction can knock CLI-placed geometry out of position — CLI is also the reliable restore path.)

**The division-of-labor lesson:** Dave then set **all 64 elements'** `VisibilityBorder=Visible` + `VisibilityID=Visible` + `ObjectName=Hidden` in **three clicks** via the property **sheet's column mass-edit** — faster and simpler than 64 individual (or even batched) CLI `Set` calls would have been.

**Rule: sheet for bulk uniform toggles, CLI for generated/computed geometry.**
- **Sheet lane:** when every element needs the *same* value for a property (uniform toggle/style change across the whole set) — use the sheet's column mass-edit.
- **CLI lane:** when each element needs a *different, computed* value (placement math, per-element geometry) — that's what CLI batching (`Assign Layout` + `Set Layout n.e "PosX"/"PosY"`, see `layout-cli-assign-and-posxy-syntax`) is for.

History: none — division of labor observed and confirmed live in one session, 2026-07-14.


### layout-element-defaults-tab-is-user-profile-wide
**DANGER: the Layout editor's "Layout Element Defaults" tab edits USER-PROFILE-WIDE defaults (Edit UserProfile 1 'Default'.LayoutElementDefaultsCollect), not the current layout**
*when:* Before clicking into the Layout editor's Layout Element Defaults tab — a stray edit there changes every future element's defaults, not just the layout you're working on


**Danger area:** the Layout editor's **"Layout Element Defaults"** tab actually opens **`Edit UserProfile 1 'Default'.LayoutElementDefaultsCollect`** — this is **user-profile-wide**, not scoped to the layout you're currently editing. A stray click/edit here **rewrites the defaults for every future element you ever create**, in any layout.

**Treat this tab as read-only reference.** Do not make changes there unless the intent is specifically to change the standing user-profile defaults for all future layout elements.

**Dave's rule (feedback, generalizes beyond this tab):** take a **good backup BEFORE any mass property change** — `SaveShow /Enumerate` first. See `saveshow-enumerate-versioning` for the versioned-save mechanics.

History: none — danger area identified live 2026-07-14; no incident occurred (caught before a stray edit happened), but flagged as a standing hazard.


### layout-element-property-names-vs-sheet-headers
**Layout element sheet column headers are NOT always the real property names — the border-visibility toggle is "VisibilityBorder", not "Border"**
*when:* Before writing a Set Layout command targeting a layout element's visibility/border/ID properties — the sheet's column header is not reliable as the literal property-name string


**The gotcha:** the layout element sheet displays a column header of just **"Border"** (grouped under a "Visibility" heading) for the border on/off toggle — but that header is **not** the property's real name. The actual property name, confirmed live, is **`"VisibilityBorder"`** (`Visible`/`Hidden` enums). **Headers ≠ property names** — do not assume a sheet column's displayed label is what you pass to `Set`.

**Full element visibility family** (confirmed): `VisibilityElement` / `VisibilityBar` / `VisibilityObjectName` / `VisibilityID` / `VisibilityCID` / `VisibilityValue` / `VisibilityIcon` / `VisibilityIndicatorBar` / `VisibilitySelectionRelevance` / `VisibilityBorder` — reflecting the pattern `Visibility<Element>`. (Verbatim from source: "VisibilityElement/Bar/ObjectName/ID/CID/Value/Icon/IndicatorBar/SelectionRelevance/Border" — read as the `Visibility` prefix applying across that slash-separated list.)

**Separate, genuinely-named styling properties** (found directly as sheet columns, not affected by the header/property mismatch above): **`"BorderSize"`** (observed value `2`), **`"BorderColor"`** (observed value `999999FF`).

**Other sheet columns seen** (not yet individually confirmed as literal property-name strings, since the "Border" case shows headers can differ from names): Bar, ObjectName, ID, Icon, Value, IndicatorBar, SelectionRect, ObjectText, CustomText, FullResolution.

**[VERIFY] PositionX vs PosX:** a forum post (hoss, forum #3991) gives the position property as **`"PositionX"`**: `Set Layout 1.2 "PositionX" 500`. The finding as recorded states "both PositionX and PosX work on 2.4.2.2" — but this confirmation traces to the forum post, not an independent console readback in this session (unlike `"PosX"`/`"PosY"`, which this session's own `Assign Layout`/`Used`-bounds work directly exercised and verified — see `layout-cli-assign-and-posxy-syntax`). Treat "PositionX works as an alias" as **verify**, not fully console-confirmed by us, until a live `Set ... "PositionX"` + readback is run and checked directly.

**Always verify any property set by readback** — `Set` with a wrong/unknown property name fails silently. See `set-command-unknown-property-fails-silently`.

History: 2026-07-14 same-day correction — an earlier pass in this session listed "Border" (default Off) as if it were the literal toggle property name; a closer look at the same element sheet corrected this to `VisibilityBorder`, with "Border" being only the displayed column header. Folded into one file per the librarian's correction-collapse rule.


### layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle
**Lasso-selecting in a Layout view puts the full 2D shape into the selection grid — Preserve GridPositions toggles compact-pack vs literal sparse coordinates**
*when:* Before building a Group from a Layout's visual arrangement — this is the fast lane for turning a shaped Layout selection into a 2D Group via the selection grid


**LAYOUT→GRID LOOP CLOSED (Dave-demonstrated, screenshot-confirmed, 2026-07-14):** lasso-selecting fixtures/elements inside a Layout view puts the **full 2D layout shape** into the selection grid — the grid isn't limited to manually-typed `Grid X/Y` moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`); a visual lasso in Layout carries its shape straight into grid coordinates.

**`Preserve GridPositions` toggle controls how:**
- **OFF** → **tight compact pack**: gaps between elements are compressed while the overall shape is kept (observed result: the DS+wings line plus 3 truss rows packed tight).
- **ON** → **literal sparse layout coordinates**: the grid preserves the actual (gappy) layout spacing as-is.

**This is the fast lane for shaped selections → Grid → Store Group** — lasso the shape in Layout, then `Store Group` captures the 2D arrangement without hand-typing `Grid X/Y` moves. Per Dave: "the quick-and-easy way."

Relevant to the pending `tourshow-festival-group-theory` work item ("groups off the layout") — this is the mechanism that ratifies the "layout/plot first, then group contract" workflow order.

**Extended beyond Layout-lasso, 2026-07-19 (Dave, console live):** the same append/`Preserve GridPositions` mechanics govern plain group-recall composition, not just a Layout lasso selection. Recalling groups with an existing selection appends per the normal append rules — with nothing selected first, multiple rows (e.g. DS+MS, or more) can be built up together grid-fashion one recall at a time. With `Preserve GridPositions` OFF, the combined recall COLLAPSES to a single compact grid — no sparse offset cells at the start of the grid, same compaction behavior as the Layout-lasso case above.

History: none — demonstrated and screenshot-confirmed live, 2026-07-14. Extended 2026-07-19: confirmed the same mechanics apply to plain group-recall composition, not just a Layout-view lasso selection.


### layout-xml-export-schema-and-import-lane
**Export Layout writes the full element schema to gma3_library/datapools/layouts/<name>.xml — this is the off-console layout-generation lane (author XML → Import Layout); GUID-on-import is untested**
*when:* Before authoring a Layout's XML off-console for import, or when you need the exact attribute vocabulary a Layout/Element XML file uses


**`Export Layout 2 "name"`** writes to:
```
~/MALightingTechnology/gma3_library/datapools/layouts/name.xml
```
(Mac onPC path — pairs with the plugin/macro path rows in `project-file-locations`.)

**Full element schema captured from a live export:**
- **Layout attributes** include arrange-tool state: `LayoutType`, `Columns`, `Rows`, `Intervals`.
- **Element attributes:** `Object` (a path into `ShowData.LivePatch` — i.e. the element points at the actual patched fixture object), `FixtureID`, `PosX`/`PosY`/`Width`/`Height`, the `Visibility*` family (see `layout-element-property-names-vs-sheet-headers`), `BorderColor`, `CustomText*`, `IDType`.

**Per-element XML tag is `<Element>`, not `<LayoutElement>`** (confirmed live 2026-07-14) — the Layout's root element is what carries the arrange-tool state (`LayoutType`/`Columns`/`Rows`/`Intervals` above).

**Newly-added elements inherit the layout's current arrange-tool state until repositioned (confirmed live 2026-07-14):** when elements are added by a `Merge` (see `assign-layout-merge-dialog-behavior`), they're auto-placed according to whatever arrangement is currently active on the layout — e.g. a Line arrangement with `x` step `50`, `y=−75` — rather than landing at a fixed default. They stay there until explicitly moved with `Set Layout n.e "PosX"/"PosY"` (see `layout-cli-assign-and-posxy-syntax`).

**This is THE off-console generation lane:** author a Layout's XML from any external plot/tool, then `Import Layout` — no need to place elements one-by-one via CLI or by hand for large/generated plots.

**Exemplar file (host-side, persists):** `~/MALightingTechnology/gma3_library/datapools/layouts/cld_spotplot_v3.xml`.

**[VERIFY] GUID-on-import behavior is untested.** It's not yet known what happens to element/object GUIDs on `Import Layout` — whether imported elements get fresh GUIDs, whether re-importing the same XML twice creates duplicates or updates in place, or whether GUIDs need to be omitted/regenerated by the authoring tool. **Verifies with:** export a layout, re-import the same XML, and inspect whether GUIDs (and element identity) survive the round-trip or collide/duplicate.

History: none — schema and lane both captured live 2026-07-14; GUID behavior flagged verify at the same time, not yet tested. Updated 2026-07-14 (evening session): added the `<Element>` tag-name confirmation and the arrange-state auto-placement behavior for newly-merged elements, both surfaced during the Assign-Layout Merge drills — see `assign-layout-merge-dialog-behavior`.


### mcp-layout-probe-2026-07-14
**Layout-by-MCP is architecturally viable (same Cmd() strings + XML-import lane); Set/Assign classify Tier 2; live probe found console-side OSC prerequisites still unmet**
*when:* When deciding whether to do Layout work via the MCP instead of clipboard/CLI, or when reasoning about which Tier a Layout-building command classifies as


**Dave asked: is Layout work doable from the MCP?** Answer: **YES, architecturally** — the same `Cmd()` strings used for the clipboard-pasted Layout work, and the XML-import lane (`layout-xml-export-schema-and-import-lane`), are both viable MCP routes.

**Command classification:** `Set` and `Assign` (the two commands this session's Layout work depended on) **classify as Tier 2** → require `confirm_gate` per command.

**Live probe result (server 0.2.1, fresh):** `udp_sent=true`, **`lua_roundtrip_ok=FALSE`**. Console side is **dormant** — no active Session, and OSC SONG_S unconfigured — matching the server's own checklist, i.e. our `osc-inbound-config-requirements` (Network-window Session + SONG_S enable/interface layers were never set up this session).

**Also gates when live:** `dry_run`→live is a **Dave-side config** decision, separate from the OSC prerequisites above.

**This session's actual Layout work went via the clipboard lane instead** (not MCP) — **zero blockage**, since the clipboard/CLI paste loop (`computer-use-input-loop`) was already the established input method. Activating the MCP lane for Layout work is described as "a 10-minute desk task with Dave" (per the wrap), not yet done.

History: none — probe run and result recorded same session, 2026-07-14.


### source-timing-is-the-tempo-grid
**{LD}'s SONG_T timing layer is a pure 139-BPM beat grid — 15 part-0 CueInFades all beat-locked (2/4/8/16 beats), riding only the >> travel cues; TrigTime never used**
*when:* Before reading or reverse-engineering {LD}'s SONG_T (or any {FESTIVAL} song's) fade timing — the whole timing layer decodes to round beat counts at the song BPM, not arbitrary seconds, and only rides the >> travel cues


**{LD}'s entire SONG_T timing layer is 15 part-0 `CueInFade` values, and every one of them is beat-locked to the song's 139 BPM** — not a hand-typed seconds value:

| Seconds | Beats @ 139 BPM |
|---|---|
| 0.863 | 2 |
| 1.727 | 4 |
| 3.453 | 8 |
| 6.906 | 16 |

(6.906 rides the intro travel cues 2.1/3.1.) **`Mark` fades in at a flat 2.0s; `OffCue` releases at a flat 3.0s** — the two structural bookends are the exceptions to the beat-lock, timed in plain seconds instead.

**Cue 26.1 is dual-layer:** `CueInFade` (intensity) = 1.73s while `Preset4Fade` (color) = 3.45s — **color lags intensity by exactly one beat-doubling** (1.73 ≈ 4 beats, 3.45 ≈ 8 beats).

**Fades ride ONLY the `>>` travel cues** — a third independent confirmation of the phrase-envelope split (named cue = the look/chord, `>>` cue = the movement/voice-leading; see `cue-structure-is-tonal-harmony`). The named section cues themselves carry no fade of their own.

**`TrigTime` is absent everywhere in this song** — every cue is a bare `Follow`, firing on completion of what precedes it, never on a timed trigger.

**Parts do NOT inherit the part-0 fade automatically** — the part-0 `CueInFade` must be (re-)applied to every part explicitly on any regeneration/rebuild; it is not a cue-level default that cascades.

**Method note:** this is a spec-read for starting values, the same posture `tourshow-authoring-contract-v01` rules for {LD}'s phasers (read for the musical figure, then re-author) — round-trip the beat math against the target song's own BPM rather than copying the raw seconds.

**Relation:** `source-spread-is-one-full-wave` is the spatial half of the same six-phaser/timing decode; `tourshow-seq1510-build-record` is the build this timing layer was authored into.

## Corroborated on the AUX layer, 2026-08-05 [0805cLD]

SONG_L's aux release fades are beat-locked the same way: OffCue fades read **0.536/0.540**
(= 1 beat at 112 BPM, 60/112 = 0.5357) and **1.070/1.071** (= 2 beats), kept VERBATIM from
{LD} rather than recomputed. Same law as the main-sequence timing layer this concept
documents, now confirmed on an aux for the first time — see
`tourshow-seq2210-song-l-build-record`.

History: none — decoded in one pass, 2026-07-28, from the Sequence 1500 (SONG_T) export.


### tourshow-gesture-groups-on-demand-doctrine
**Bank D gesture groups build ON DEMAND, song by song — never mass-generated; each gets Stored the moment it's actually used**
*when:* Before mass-generating Bank D gesture groups (HALO/SPINE/FRAME/WALL/CANOPY/CORRIDOR/JAB/CURTAIN) up front, or before deciding whether a live/ad-hoc grid sketch needs to become a stored Group


Dave's ruling: the Bank D gesture vocabulary (HALO/SPINE/FRAME/WALL/CANOPY/CORRIDOR/JAB/CURTAIN — see `tourshow-festival-group-theory` for the vocabulary itself) builds **ON DEMAND, song per song** — start with whichever ones a given song actually needs, develop more as the build goes. It is explicitly **NOT** mass-generated up front the way the contract groups are.

**Two-layer model this establishes:** contract groups (spots/washes/pix/JDC/beams by century+scope, see `tourshow-group-contract-v01`) are the **always-there layer** — built once, complete, before any song work starts. Gesture groups are the **story layer** — accumulated incrementally, per-song, as the actual need for a given gesture shows up.

**Storage discipline that follows from this:** live/ad-hoc grid composition (recalling groups or selections, appending, clicking to place the cursor for the next recall — see `grid-cursor-cli-recipe-for-2d-group-layouts`) is fine for **sketching** a gesture shape, but it is exploration only. Recipes bind Selection to a **stored Group object**, so the moment a sketched shape is actually going to be used in a repeatable recipe, it has to be Stored as a Group first — "store whatever we're gonna use." Practical rule: sketch live, then store before it enters a cue. This is why gesture groups get stored **at first real use**, not pre-built and not deferred indefinitely.

Suggested numbering home when a gesture group actually lands: century **7xx**, labeled `cLD GESTURE <name>` (per `tourshow-group-contract-v01`'s open/deferred notes) — not yet allocated as of this session.

**Relation:** the storage discipline here is a consequence of choosing recipe-based programming, not an MA3 technical requirement — see `tourshow-recipe-based-show-style-ruling` for that mode-vs-law distinction.

History: none — ruling stated live 2026-07-19, alongside the group contract design session.


### tourshow-group-contract-v01
**Group Contract (v0.3): Group# = FID century + scope slot, 28×4 frame/category; her-key carveout = Group 51 (FID 51-54, re-FID'd for rig-position identity); backlight Groups 60-64 (FID 55-60, MVR-ratified membership); + the subfixture cell layer — built + census-verified**
*when:* Before creating, numbering, or recalling any template-rig or subfixture-cell Group, before touching the her-key or backlight FID/group blocks (51-60), or before assuming Groups 101-110 still include FID 55-60 after the 2026-07-23 carve


**Numbering — one arithmetic rule, no lookup needed:** Group number = **FID century + scope slot**. Same ten ones-digits in every category century:

| ones | scope | members |
|---|---|---|
| x01 | ALL (full 2D frame) | 64 |
| x02 | DS row | 12 |
| x03 | MS1 row | 12 |
| x04 | MS2 row | 12 |
| x05 | US row | 12 |
| x06 | WINGS both | 16 |
| x07 | WING SR | 8 |
| x08 | WING SL | 8 |
| x09 | HALF SR (movers only) | 32 |
| x10 | HALF SL (movers only) | 32 |

Centuries mirror the FID patch exactly (Dave's ruling, see `tourshow-festival-group-theory`): **1xx SPOTS · 2xx WASHES · 3xx PIX · 4xx JDC · 5xx BEAMS**. Halves (x09/x10) exist only for the pan/tilt-capable categories (spots/washes/beams — 1/2/5). Labels follow `cLD <CAT> <SCOPE>`.

**6xx composites (members-only, compact grid — MAtricks does the shaping, not the grid):** `601 cLD AIR ALL` (v0.2: **252** with her-key 51–54 excluded, **316** with beams folded in — was 256/320) · `602 cLD MOVERS` (v0.2: **124**, key-excluded, rebuilt with beams like 601 — was 128/192) · `603 cLD FX` (pix+JDC, 128) · `604 cLD POP` (JDC+beams, 128 — beams-macro only). **601/602 were explicitly NOT extended the backlight carveout on 2026-07-23** (see the CARVE ruling below) — Dave's call, key-precedent symmetry not extended this round; treat 601/602's FID 55-60 membership status as current/unchanged unless a future ruling says otherwise.

**The frame — identical shape stamped per category:** X spans **0–27** (SR wing outboard→in 0–7, main truss 8–19, SL wing in→outboard 20–27, mirror seam between columns 13/14); Y spans **0–3** mapping DS→US. **Wings ride Y0** — same plane as DS (Dave's ruling, 2026-07-18: wing Y = 0). All coordinates stay **≥ 0** by design; negative grid coordinates are unverified on the CLI, so the frame is shifted rather than centered on zero. This 2D frame is exactly what makes whole-category POSITION WIZ runs able to depth-grade Blind — see `tourshow-position-wiz-blind-depth-grade-root-cause`.

**Stale groups resolved:** Groups 104/105 (stale since the 2026-07-10 multipart drill — see `tourshow-template-rig-patch-and-layout-state`) are deleted and re-pointed as SPOTS MS2/US by the builder macro, closing that flag. Grid-drill exemplars 121–124 and the JDC set 128–130 (125–127 empty) are left untouched by the contract.

**v0.2 her-key carveout (Dave ratified 2026-07-21):** her key group is **Group 51 `cLD {ARTIST} KEY`** (group number from FID-block arithmetic, deliberately below 100 on Dave's side of the pool; her four key spots are FID 51–54). **FIDs 51–54 are EXCLUDED from `601 AIR ALL` and `602 MOVERS`** — the key is carved out of the programmable field at the GROUP level, so any look that includes her references Group 51 deliberately. The contract builder was regenerated to carve out 51–54, leaving DS-row rests at grid X10/12/15/17 (the positions the four key spots used to occupy — authored rests, see `gap-is-a-rest-doctrine`); sim census PASS; the regenerated builder XML supersedes the pre-swap one.

**Re-FID rationale (07-20 bridge, Dave, dictated) — why 51–54 and not new units:** the four original candidates (FID 103/105/108/110) were chosen for their **RIG POSITIONS**, not their serials — the hang points those FIDs sat at make the pictures on her that Dave wants her key coming from in the show. So the key block's identity is **four positions in the rig**, not four fixture serials; re-FID'ing preserves that identity (on a house rig, spread-fill would pick the units nearest those same hang points). This is what decided Option A (re-FID 103/105/108/110 → 51–54) over Option B (add four new units at 51–54): keys are carved from the real rig, not added to it. Patch executed 2026-07-21; 103/105/108/110 vacated.

**Per-song fluid key layer (Dave, 07-21, dictated — supplements the fixed 51-54, does not replace it):** beyond the fixed her-key block, some fixtures per song may stay SOLID on her (not chase) depending on where she is on stage, or a couple as additional {ARTIST} specials — a per-song adjustable layer, not fixed doctrine. Lives alongside the manual-reserve handle (see below).

**Spares / manual reserve — CLOSED, no group slots reserved.** No manual-reserve layer exists in the show file, so the contract allocates nothing for it. Full ruling and the superseded 07-20 proposal: `tourshow-spares-no-manual-reserve-ruling`.

**v0.3 backlight Groups 60–64 (FID 55–60) — proposed 2026-07-22, RATIFIED from MVR geometry 2026-07-23:**

- **Origin:** backlight fixtures = **FID 55–60**, six units spread across the upstage catwalk/riser, siblings to Group 51 on Dave's side of the pool (below 100, outside the cLD 101+ namespace). Design rule these groups serve: whenever her key runs saturated/semi-saturated color, the white backlight must be ON so she still reads — see the design-side doctrine and position-based fixture picks in `tourshow-her-key-and-backlight-doctrine`.
- **Physical map (MVR `cld_patch_v4`, verified 2026-07-23):** FID 55 = unit30, MS2, Y+6 X−0.6, SR-inner · 56 = unit31, MS2, X+0.6, SL-inner · 57 = unit39, US, Y+9 X−4.2, SR-outer · 58 = unit41, US, X−1.8, SR-mid · 59 = unit44, US, X+1.8, SL-mid · 60 = unit46, US, X+4.2, SL-outer. All **MAC Encore Perf CLD**, Z+8.
- **Penciled-then-corrected:** the first dictated proposal (contiguous ranges: 61 BL SR=55-57 / 62 BL SL=58-60 / 63 CTR DS=57+58 / 64 CTR US=56-59) was **geometrically WRONG against the MVR** — a contiguous-range guess, not a geometry read. Superseded in-body, not deleted.
- **RATIFIED membership (Dave, from MVR geometry, 2026-07-23) — current truth:** **G60 `cLD BACKLIGHT ALL`** = 55-60 (the widener) · **G61 `cLD BL SR`** = {55, 57, 58} · **G62 `cLD BL SL`** = {56, 59, 60} · **G63 `cLD BL CTR DS`** = {55, 56} (the MS2 pair) · **G64 `cLD BL CTR US`** = {58, 59} (tight US inner pair). This supersedes the dictation-era contiguous ranges everywhere they appear, including in `SONG-E_BUILD_NOTE` / `SONG-E_BINDING_TABLE` prose — those docs still carry the old ranges as of 2026-07-23 and are owed a docs round-trip (cLD's, not the librarian's).
- **Proven idiom used to build these:** `Store Group 60 "cLD BACKLIGHT ALL"` (inline name, no separate Label line — see `macro-xml-schema-cracked`'s quote-dialect fix, since Label lines are exactly where the quote-truncation bug bites).

**CARVE ruling (Dave, 2026-07-23) — purge FID 55-60 from the spot contract:** because these six units were **re-FID'd FROM 130/131/139/141/144/146** (originally MS2/US-row spots inside the 1xx contract), and **group membership follows the fixture OBJECT through a re-FID, not the FID number** (see `group-membership-follows-refid-not-number`), they silently remained members of `G101` (ALL spots, showed 60 incl. 55-60), `G105` (US row, showed 57-60 present), and `G601` (AIR ALL, showed 316 incl. all six) after the re-FID. Dave ruled: **purge FID 55-60 from the FULL spot contract block, Groups 101-110 (ALL/rows/wings/halves)** via `Store Group <n> /Remove` on each, export-census-verifying each group afterward. **601/602 were explicitly LEFT AS-IS this round** — the her-key (51-54) precedent of excluding from 601/602 was **NOT extended** to the backlight block; that's Dave's call, not an oversight, and it means 601/602's current census (252/124 etc., above) may still include 55-60 pending a future ruling.

**v0.2 subfixture cell layer (built + census-verified, v0.23→v0.24):** on top of the contract categories, the multi-cell fixtures (ACME pixel lines 3xx/13xx, JDC1 4xx) got a full cell-group layer. Numbering, by scope:
- **Uniform layer** (whole-rig, membership only — the uniform tier of `subfixture-cell-architecture-doctrine`): `x20` = color/plate, `x21` = beam/tube → **320 PIX COLOR / 321 PIX BEAM · 420 JDC PLATES / 421 JDC TUBES · 1320 PLINE COLOR / 1321 PLINE BEAM**.
- **Laid-out per-truss cells** (2D grid coords baked, effect-capable): color **32x**, beam **34x**, plate **42x**, tube **44x**, by scope DS/MS1/MS2/US → **322–325 PIX COLOR · 342–345 PIX BEAM · 422–425 JDC PLATE · 442–445 JDC TUBE** (JDC groups 144 members each; 322 DS COLOR verified 384 members, X0–191, 192@Y0 + 192@Y1). Floor: **1322/1323 (BAND/UPPER COLOR) · 1342/1343 (BAND/UPPER BEAM)**.
- **JDC masters** (must be ON for any cell output — see `jdc1-standing-order-plate-master-full`): **426 cLD JDC PLATE MASTER** (`401 Thru 464.1`) · **446 cLD JDC BEAM MASTER** (`401 Thru 464.2`).
- **Dave's hand-built full-rig combined GRID pictures** (whole-rig versions of the per-truss cells; Dave-authored — verify existence, do NOT rebuild): **334 cLD PIX COLOR GRID · 335 cLD PIX BEAM GRID · 434 cLD PLATES GRID · 435 cLD(C) TUBES GRID** (note the BEAM-vs-TUBE label split, see `beam-not-strobe-terminology`).
- **Floor scope/composite groups** also built: **1101 Lucius · 1301–1303 P-Lines** (Fourline v11 numbering; see `tourshow-floor-package` for the full floor FID scheme, extended to 1304-1309 upper-deck).
The uniform layer is kept beneath the laid-out cells; a laid-out group also serves uniform recalls (strictly more capable). The physical X/Y cell mapping is a chosen convention pending warehouse verification — see `acme-pixel-line-ip-anatomy`, `subfixture-cell-architecture-doctrine`.

**Implementation — two builder macros generated, self-verified; contract + subfixture layers BUILT + census-verified (v0.23→v0.24):**
- `cLD_GROUP_BUILDER.xml` — 39 main groups, deployed to `gma3_library/datapools/macros/`.
- `cLD_GROUP_BUILDER_BEAMS.xml` — 13 more groups (including a 601/602 rebuild to fold beams in, plus 604 POP), gated behind the beam patch (FID 501–564, see `tourshow-template-rig-patch-and-layout-state`) landing first.

Generation self-verified: member census matches this contract exactly, XML valid, no batching, all coordinates ≥ 0. **Desk process (was v0.1-pending; RUN in v0.23→v0.24):** empty-slot census on Groups 101-110/2xx/3xx/4xx/6xx first (an occupied slot stalls the macro on a popup — only 104/105 are pre-deleted), import via `ChangeDestination Macro` → `Import Library "cLD_GROUP_BUILDER.xml"` → `ChangeDestination Root`, fire it (~4 min of stores), then `Export Group` census-verify 101/109/601 against the member table above. The contract layer (40 scope+composite groups + 13 beam groups + 4 floor groups) plus the full subfixture cell layer above are now built and census-verified in v0.24 — Dave also built the full-rig GRID pictures from the cells himself. Wings (pixel 349–364, JDC 449–464) deferred — Dave said add wings later.

**Status:** the subfixture cell layer queued in v0.1 is now BUILT (see the v0.2 section above) — done via the reliable Grid-cursor-baked-into-Groups lane, NOT GS (GS bakes didn't survive the v11 repatch; see `grid-cursor-cli-recipe-for-2d-group-layouts`, `gs-multifixture-recall-unreliable`). Still deferred: pixel/JDC **wing** cell groups (349–364 / 449–464), Dave said add later. Gesture-layer groups (Bank D — see `tourshow-gesture-groups-on-demand-doctrine`) get a suggested home at century **7xx**, labeled `cLD GESTURE <name>`, once actually built. The old v2 idea of baking the 6xx composites with grid **Z** as a category layer is **dropped** — Dave ruled cells are X/Y only, layers go in separate groups, no Z (see `subfixture-cell-architecture-doctrine`). **NEW v0.3 status note (2026-07-23):** the backlight block (Groups 60-64) is RATIFIED and the spot-contract CARVE (101-110) is ruled — both owed a desk re-fire/verify pass; a smith proof-run already confirmed the ratified backlight membership is EXACT in the authored foundation XML (`cLD_ST_FOUNDATION.xml` v0.1.3) ahead of that desk pass.



## ⛔ CORRECTED 2026-07-31 [0731cLD] — the JDC chain-opener group numbers above are STALE

**Live desk-clear read, 2026-07-31:** the JDC master groups are **415 `cLD JDC PLATE MASTER`** and **422 `cLD JDC BEAM MASTER`**. **426 and 446 are EMPTY.** The "426 PLATE / 446 BEAM" numbers in the v0.2 subfixture-cell-layer section above are wrong and must not be used — `CROSSWALK_CHEAT_SHEET_v0.1.md` and `generated/crosswalk_prep/SUBMAP.md` already carried the correct pair. SONG_A's Mark cue ships `cLD JDC PLATE MASTER` + `cLD JDC BEAM MASTER` as its gate-openers on this basis (see `tourshow-seq1010-build-record`).

**⚑ FLAGGED, NOT FIXED — the 4xx block looks renumbered wider than this one pair.** This file's own arithmetic defines **422 as `cLD JDC PLATE DS`** (the `42x`-by-truss cell scheme), which collides with the live read; and the cheat sheet reads **416/417 = PLATES/TUBES GRID** where this file's arithmetic says 434/435. A full live 4xx census is owed before any other number in this file is trusted. Do not auto-resolve — surface it.

**⚑ SEPARATE, SAME SESSION — the arithmetic describes the SANDBOX, not the inherited file.** In `EXAMPLE_SHOW gov bal_cLD`, cLD's contract groups sit **relocated**: `cLD SPOTS ALL` is **Group 181**, not the predicted 101 — slot 101 there is {LD}'s `PL FL [RGBMM] (Grid)`. Every bind cLD authors into that file is **name-form** for exactly this reason. Treat the century arithmetic as the design of the clean sandbox; in an inherited file, read the live name. See `inherited-file-membership-is-ground-truth`.

History: v0.1 designed 2026-07-19; **v0.2 landed 2026-07-21** — added the her-key carveout (Group 51; 51–54 excluded from 601/602) and the full subfixture cell layer (uniform x20/x21; laid-out color 32x/beam 34x/plate 42x/tube 44x; masters 426/446; Dave's full-rig grids 334/335/434/435), all built + census-verified in cLD_SANDBOX v0.23→v0.24. Original v0.1 note: contract designed and both builder macros generated in the 2026-07-19 session, Dave-delegated ("lay it out the way that makes sense for you... you're the one that's gonna be using them"). **Extended 2026-07-20 (07-20 bridge):** added the re-FID rig-position rationale for Group 51 (why 103/105/108/110 → 51-54) and the per-song fluid key layer note; recorded (then 07-22-superseded) the original manual-reserve proposal. **Extended 2026-07-22/23 ([0722-2cLD]):** spares/manual-reserve question CLOSED (no such layer exists — physical spares, unpatched); backlight Groups 60-64 (FID 55-60) proposed with contiguous ranges. **v0.3 landed 2026-07-23 ([0723cLD]):** backlight physical map MVR-verified, penciled contiguous ranges found geometrically wrong and corrected, final membership RATIFIED from geometry; CARVE ruling purges FID 55-60 from the 101-110 spot contract block (601/602 explicitly not extended the same treatment). 2026-07-31 [0731cLD] — chain-openers corrected 426/446 -> 415/422 from a live console read; wider 4xx renumber flagged for census; relocated-groups caveat added from the SONG_A build.


## LUA & PLUGINS

### appearance-image-swap-blocking-cards
**Swapping an image on a layout card: the layout element WEARS an appearance, the appearance's Image property holds a handle, and `a.Image = <image handle>` assigns clean — so one appearance + one image pool = a per-song picture that changes itself**
*when:* Before building any layout view whose picture must change per song/cue — the indirection (element → appearance → image) is the whole mechanism, and the assign form is proven


## The mechanism

```
layout element  →  wears an Appearance  →  Appearance.Image = <image handle>  →  the picture
```

The layout element is never touched at runtime. **Swapping the appearance's `Image` swaps the card.**

- The image reference property is literally **`Image`**, and renders as `Image <pool>.<slot>` — proven by a property-schema dump, not guessed.
- **`a.Image = <image handle>` assigns clean.** Scratch-proven by cycling an appearance through two images and back, readback exact each time.
- User images live in the **MediaPools image pool**; `ImageMode` (Bar vs Stretch), tint and transparent-back are appearance properties set once at design time.

**⚠ Read the appearance's number from a NAME CENSUS, not from memory.** The build initially targeted the wrong slot; the live name census gave the right one. Pool labels and remembered numbers both lie (`pool-labeling-doctrine-inherited-risk`).

## The per-song lane

A toolbox function takes the song token (defaulting to the `selectedsong` global), **hunts the image pool for a name matching `upper(token)`**, and points the appearance at the hit; **no match = no-op**. Called from the shared song macro, it costs zero per-song code (`automator-tc-architecture`).

**Exact-match law:** the images had to be **renamed to the macro tokens** for the match to run clean — one card's name differed from its token and was renamed, taking the match to 18/18 (`name-token-single-holder-cutover-law`).

## Package notes worth carrying

- The card set was delivered as small PNG8 images in **show order**, with a manifest carrying per-file sha256 and an authority reference. **Show order ≠ track numbering** — two songs were swapped relative to the session's own numbering, which is exactly the kind of mismatch a slot-math error is built on. **Derive slot from the manifest's order, and write the mapping down** (card NN → image slot NN+offset).
- A deliberately blank card is a legitimate entry (blocking not yet authorised); when its content lands, **rebuild that one card and re-import that one image** — the machine is unchanged.
- The manifest's route summaries doubled as the per-song zone progressions used elsewhere in the design work — a package can carry more than its stated payload.

**Relation:** `automator-tc-architecture` · `layout-element-property-names-vs-sheet-headers` · `layout-cli-assign-and-posxy-syntax` · `pool-labeling-doctrine-inherited-risk` · `plugin-code-runs-at-showfile-load`.

History: none — designed, corrected by census, built and verified in show conditions, 2026-08-08.


### classifier-plugin-token-false-positive-block ⚠ VERIFY
**MCP classifier gap: a READ-ONLY ObjectList('Plugin *') call auto-blocks as Tier 2 purely on the 'Plugin ' token — a false positive on a census-only, non-mutating call**
*when:* When a plainly read-only Lua call unexpectedly gets classified Tier 2/blocked — check whether it contains the literal 'Plugin ' token before assuming the call itself is dangerous


**The gap:** a read-only census call, `ObjectList('Plugin *')`, auto-blocks at the MCP classifier as if it were a Tier-2 (write/dangerous) operation — purely because the literal token `Plugin ` appears in the command string, not because the call does anything mutating. `ObjectList` itself is a pure read/enumeration function.

**Distinction from other classifier gaps in the corpus:** this is neither the `lua-body-write-api-classifier-gate` mechanism (write-API calls like `SetVar(`/`Delete(` inside a Lua body) nor the `classifier-tier-gap-edit-and-bare-layer-keywords` ruling (CLI-native mutating keywords under-classified as Tier 1) — this is the OPPOSITE failure shape: a harmless read call OVER-classified as Tier 2 because of a keyword substring match, most likely because `Plugin` also appears in genuinely dangerous plugin-install/-run commands and the classifier's word-list isn't scoped to the verb position.

**Status:** `verify` — flagged as a gap during a live session, not yet triaged against the classifier's actual word-list logic or fixed. Queue for the same classifier word-list review that `classifier-tier-gap-edit-and-bare-layer-keywords` and the [0723cLD] Delete-inside-Cmd gap (see `delete-command-classifier-tier-gap`) are already queued against.

History: none — observed live in one session, 2026-07-22, attempting a plugin-pool census on {LD}'s AR showfile.


### gpdf-console-killer
**GetPresetDataFast() segfaults onPC 2.4.2.2 on a freshly built preset/phaser — banned from generated Lua**
*when:* Before generating any Lua that reads preset internals; when an MCP round-trip times out unexpectedly after a fresh Store


**Two hard crashes this session (11:34 + 11:42),** each the instant `GetPresetDataFast(handle,...)` ran on a **freshly built preset/phaser**.

Crash logs at `~/MALightingTechnology/gma3_2.4.2/onpc/temp/crashlogs/processed/` show identical **`_sigtramp` (signal/segfault) faults in the LUA thread**, with a recursive native stack — this is a **C-side crash, NOT a Lua error**, so:
- **`pcall` cannot catch it.**
- The MCP round-trip just **times out** (the console dies before writing the sentinel file) — see `segfault-manifests-as-mcp-timeout` for the diagnostic signature this produces.

**Ban `GetPresetDataFast()` from generated Lua entirely.** Verify stored phasers with SAFE reads only (`.Name`, `.Addr()`, pool-slot counts) or inspect the exported showfile XML offline instead.

**Likely root cause (investigate, not yet confirmed):** boot log shows `attribute import error 'PresetMode'='Default' : illegal value` during preset compression. CLI-stored presets may carry an illegal v2.4 `PresetMode` that sends GPDF's recursive serializer off a cliff — v2.4 removed the "Auto" preset mode (see `v24-migration-facts`), and "Default" may also be an illegal value now. Check `PresetMode` on `Store Preset` before trusting programmatic preset builds.

**Investigation update (2026-07-05, read-only probe):** a CLI-stored color preset, `cLD Red` (4.101), reads `PresetMode=Global` — a **LEGAL** value. The boot-log's illegal `'Default'` did **NOT** reproduce on this object. Root-cause hypothesis is therefore not yet confirmed by this probe; still needs a fresh phaser-candidate probe (SAFE property reads only — **never GPDF**) during the next attended console session to actually catch an illegal `PresetMode` in the wild.

**Enforcement update (2026-07-05): classify() now denies GPDF at the classifier, closing a B1 hole.** Until today, `GetPresetDataFast` classified as **Tier 1** ("Lua read-channel") and would pass `send_lua` **ungated — even in `dry_run`** — because the console-killer ban above lived only in a plugin-source scan, which the classifier path never reached. **Fix:** `classify()` now denies GPDF tier-99 (hard-deny) before any other rule is evaluated (`safety.py` gpdf-ban). Every current and future tool that routes through `classify()` inherits the ban. Found by a second-look Fable cross-check subagent review — not by the 67-green unit test suite in place at the time.

History: first-observed, live, 2026-07-04 (standalone crash-avoidance rule; escalated as a bug report to MA Lighting/ACT support, see project task list). 2026-07-05: classifier-level enforcement added after a cross-check review found the ban wasn't reaching `send_lua`'s gating path; fixed same session, suite now 80 green.


### hook-api-surface
**Hook API (v2.3.2) — HookObjectChange, Unhook (not UnhookObjectChange), UnhookMultiple, DumpAllHooks**
*when:* Before writing code that registers or removes an object-change hook — the unhook function name is easy to get wrong


| Function | Status |
|---|---|
| `HookObjectChange(callback, handle)` | returns a token |
| `Unhook(token)` | correct unhook call — **NOT** `UnhookObjectChange`, which does not exist |
| `UnhookMultiple(...)` | batch remove |
| `DumpAllHooks()` | inspection — useful for debugging |
| `PatchFixturesChangedCallback`, `PatchGridColumnFilterChangedCallback`, `PatchSettingsChangedCallback` | specialized patch-domain hooks |

Recall also: any hook registered inside a `Plugin <N>` invocation's `Main()` is unhooked automatically the instant that invocation ends (see `plugin-lifecycle-autocleanup`) — this Hook API is for use in persistent-lifecycle plugins, not one-shot `Plugin <N>` calls.

History: none — recorded 2026-05-27, no later corrections found in corpus.


### lua-api-surface-inventory
**Lua API surface: 242 global functions + 617 enums on stock MA3 onPC 2.3.2.0**
*when:* When you need the full inventory of available MA3 Lua globals/enums, or want to confirm a function/enum exists before using it


Live-captured on a stock MA3 onPC 2.3.2.0 install: **242 global functions** + **617 enums**.

Full inventory: `WORKING/generated/ma3/snapshots/api_dump_*.json` (produced by the `alchemease_api_dump` plugin, pool slot 3 — see `plugin-pool-slot-reservations`).

Notable named functions/objects worth remembering directly (rather than searching the dump every time): `Cmd*` family, `HookObjectChange`/`Unhook`, `CreateUndo`/`CloseUndo`, `CallRealtimeLockedProtected`, `ChannelTable`, `ConfigTable`, `SelectionTable`, `CurrentUser`, `CurrentProfile`.

History: none — captured 2026-05-27 against onPC 2.3.2.0; the count may drift under v2.4 (2.4.2.2) but no corpus entry re-ran the dump against that build.


### lua-body-write-api-classifier-gate
**Classifier scans Lua bodies for embedded write-API calls to force Tier 2 — prefix rules alone let writes slip Tier 1**
*when:* When modifying or auditing the MCP command classifier's Tier 1/Tier 2 rules, or wondering why a Lua payload landed in Tier 1


**Gap found:** `SetVar(` and similar write calls could slip Tier 1 classification because the classifier's prefix rules require a **trailing space** to match — a call written without one (or embedded mid-Lua-body rather than as a bare command prefix) wasn't caught.

**Fix applied:** the classifier now additionally **scans the body of Lua payloads** for write-API call signatures and forces **Tier 2** if any are found, regardless of the top-level prefix match. Scanned call signatures (verbatim from the fix):

```
SetVar(
DelVar(
CreateUndo(
Delete(
Acquire(
SetAttribute(
SetFader(
```

This closes the gap where a Lua string could carry a mutating call past the surface-level prefix check. Complements — does not replace — the mandatory `CreateUndo`/`CloseUndo` wrapping already required for Tier 2 Lua (`undo-and-realtime-safety-primitives`) and the word-boundary deny-list fix (`saveshow-discipline-and-mcp-tier`): those two govern *what Tier 2 must do*; this concept governs *what gets routed to Tier 2 in the first place*.

History: none — found and fixed same session, 2026-07-05.


### lua-command-line-bridge-functions
**Lua → command-line bridge functions (Cmd, CmdIndirect, CmdIndirectWait, CmdObj)**
*when:* Before deciding how a generated Lua artifact should invoke MA3 command-line strings — synchronous vs async vs object-scoped


| Function | Use |
|---|---|
| `Cmd("…")` | Execute MA3 command-line string synchronously; result available in System Monitor |
| `CmdIndirect("…")` | Async / queued |
| `CmdIndirectWait("…")` | Async with wait barrier |
| `CmdObj(obj, "…")` | Execute command in the context of a specific object handle |

Prefer these over OSC round-trips when codegen targets a Lua artifact — no UDP latency, no echo parsing.

History: none — recorded 2026-05-27, no later corrections found in corpus.


### lua-global-drawer-is-session-not-file
**The Lua _G drawer belongs to the RUNNING SESSION, not the file — quit/relaunch or a show reload empties it, and it has NO window from the desk; SetGlobalVariable is a different cabinet that DOES have one**
*when:* Before relying on anything held in Lua globals across a reload, or when trying to inspect what a plugin has left in memory — and before confusing the Lua drawer with the console's user-variable store


## Persistence

**The drawer is session-scoped.** onPC quit and relaunch = empty drawer, **even on the same saved file**. A show load or reload = empty drawer. A PSR carries the plugin **code** (the pool object) but it arrives **unfired**.

**This is not a problem**, because load re-runs every plugin's top-level code and rebuilds the drawer (`plugin-code-runs-at-showfile-load`). **SaveShow saves the recipe, never the meal.**

## Two drawers, different cabinets

| | Console user variables | Lua `_G` |
|---|---|---|
| Written by | `SetGlobalVariable` | plugin top-level code |
| Visible from the desk | **yes** — `List Global Variable` | **no window at all** |
| Read by | CLI and Lua | Lua only |

The song-fire chain uses both: the token and BPM go into **user variables** (visible, inspectable), while the toolbox functions live in **`_G`** (invisible unless you ask Lua).

## What a live census looks like

Roughly **34 tables**, of which the named toolboxes map one-to-one onto plugin pool slots, alongside the stock ones (`Enums`, `ButtonApi`, `LedApi`, `lfs`, `__CallbacksRegistry`…). 279 functions, 3 userdata.

**The jewel in the census:** a plugin's **configuration constants sit in `_G` as plain globals** — the song macro range, the song page range, the song timecode range, the song view and view-button numbers, the sequence range, the pool number, plus a debug flag. **Decoding an inherited plugin's numbering scheme can be a memory read rather than a source read.** Assorted crumbs also accumulate there (current image pool name, element numbers, counters) — useful, unreliable, not a contract.

**Resident vs parked:** hooks and timers are the genuinely-running class (the MCP hook host is one). The song path has none — it is a pure native chain. **An audit lane for "is anything actually running" is reading plugin source**, not reading `_G`.

**Offered artifact:** a one-press census macro that prints the inventory to the System Monitor — the drawer gets a window.

**Relation:** `plugin-code-runs-at-showfile-load` · `uservariable-cli-and-lua-surface` · `lua-api-surface-inventory` · `hook-api-surface` · `automator-tc-architecture`.

History: none — censused live 2026-08-08.


### lua-pool-walk-allocation-law
**Lua #pool returns the pool's ALLOCATION, not its occupied count — holes read nil; always guard a pool walk with 'if o then'**
*when:* Before writing any Lua that walks a whole pool (for i=1,#pool do ... end) — #pool is the allocation size (e.g. Dimmer=1000), not how many slots are actually occupied, and empty slots return nil rather than being skipped


**`#pool` in Lua returns the pool's ALLOCATION size, not the number of occupied slots.** Observed on the Dimmer preset pool: `#pool` = **1000**, regardless of how many of those 1000 slots actually hold a preset.

**`pool[i]` is SLOT-addressed, and an empty slot returns `nil`** rather than being skipped or omitted from the count. **Every walk over a pool must guard each read** — e.g. `local o = pool[i]; if o then ... end` — or a hole throws on the next line that assumes a real object.

**Confirmed:** `pool[i].no == i` (the object's own slot-number property matches its index) verified across Dimmer slots 1-16.

**Consequence for census/generator scripts:** never use `#pool` as "how many objects exist" — it will wildly overstate occupancy on a sparsely-filled pool (a 1000-slot Dimmer pool with a handful of real presets still reports `#pool == 1000`). Walk the full allocation and count only the non-nil hits for a true census.

**Relation:** distinct from `macro-scratch-slot-idiom-generalizes-to-any-pool` (that concept is about deliberately using a disposable slot to author into — this one is about safely *reading/walking* an existing pool's contents).

History: none — confirmed live, 2026-07-28, while building the SONG_T phaser template set census.


### matricks-negative-value-lua-uint32-wraparound-gotcha
**Lua :Get() on a negative MAtricks value returns the uint32 wraparound — export readback is the honest lane for signed values**
*when:* Before trusting a Lua :Get() readback of any MAtricks property that might be negative (e.g. YShift) — the live Lua read silently wraps to a huge unsigned int instead of showing the true signed value; the export re-serializes it correctly


**Finding (card-candidate, CARD_DESK):** reading a **negative MAtricks value via Lua `:Get()`** returns the **uint32 wraparound**, not the signed value — `YShift -1` read back as `4294967295`.

**The export lane is honest for signed values:** exporting the same object and reading the XML re-serializes the value correctly as `-1`.

**Same family as the sign-eating patch-`Set` trap** (a bare negative losing its minus sign on write), but a **different mechanism** — this is a read-side DISPLAY problem, not a write-side value-storage problem. The value is stored correctly; only the live Lua read of it lies.

**Practical consequence:** when verifying any MAtricks property that could plausibly be negative, verify via **export readback**, not a live `:Get()` call.

**Relation:** `tourshow-whole-fixture-block-law` (the MAtricks retune session this was caught during, on `144 SHUFFLE 5`'s `YShift`). `patch-set-one-prop-quoted-values` (existing concept, not staged this run — the sibling write-side sign-eating trap in the same family).


## Scope narrowed 2026-08-01 [0801cLD] — the uint32 wraparound is YShift-specific, NOT a blanket negative-value rule

Two corroborating live imports narrow this concept's scope. **`MX 153 cLD S5 X-45`** live-read `PhaseToX=-45.0` exact after import — **PhaseToX is signed-clean on the live Lua read.** A second case landed the same magnitude that originally motivated worrying about wraparound: **negative phase at magnitude 360 also landed EXACT and read exact via live Lua** (`MX 158 PhaseToX=-360.0`) — further corroborating that the uint32 wraparound described in this concept's body is **YShift-specific**, not a phase-wide hazard. Three new MX spatial shapes are proven importable off the back of this: reverse lap (`-360`), double lap (`+720`), and a phase-OFFSET form (`PhaseFromX=180` with no `ToX`).

**Practical narrowing:** treat the wraparound risk as scoped to `YShift` (and other non-Phase* attributes proven to share its mechanism) until a further live case shows a `Phase*` attribute wrapping too. `PhaseToX`/`PhaseFromX` reads via live `:Get()` are trustworthy at least at the magnitudes tested (±45, ±360).

**Serialization asymmetry, separate mechanism, worth keeping alongside this scope note:** the desk dialect writes NEGATIVE phase WITHOUT a degree sign (`PhaseToX="-180.00"`) while positive phase keeps the degree sign (`"360°"`). Authored-with-degree negatives still import correctly (proven on `MX 153`, and again on SONG_J `163`/`164`/`165`/`167`) — but an export-back byte-diff comparison MUST normalize the degree-sign difference before comparing, or a clean import reads as a false failure.


### matricks-property-clear-encoding
**Clearing a MAtricks block/group: assign 0 — m.XBlock=0 / m.XGroup=0 reads back 'None', which IS the clean clear; wings survive, and Copy carries the SOURCE's Name so re-Label after**
*when:* Before minting a 'flat' MAtricks twin from a block/group-carrying source — how to clear a property, what the readback should say, and the Copy-carries-the-name gotcha that follows every twin mint


**The clear:** assign **`0`**.

```lua
m.XBlock = 0
m.XGroup = 0
```

**The readback says `None`** — that is the *correct* cleared state, not a failed write and not a stored zero. Verified on every flat twin minted across four venues.

**Wings and phase survive a block/group clear.** `XWings`, `PhaseFromX/ToX`, `PhaseFromY/ToY` and shuffle are untouched — which is precisely what makes the 1-cell adaptation possible (`mx-cell-geometry-law`: strip the cell geometry, keep the population geometry).

**⚠ Copy carries the SOURCE's Name — always re-Label after.** Minting a twin by `Copy … At <slot>` brings the source's name with it, so the new object silently masquerades as the old one until relabelled. This is the same behaviour proven in the colour pool (`Copy Preset /o /nc` carried the source name into the crowned base — see `color-consolidation-crowning`). **Mint → Label → verify the label reads back** before anything else references it; a stale label is what a later name-lookup will match.

**And verify sources by NAME before copying.** The venue kit's mint step looks its sources up by name rather than slot, because pool labels lie (`pool-labeling-doctrine-inherited-risk`) and slot contents drift between file lineages — at {FESTIVAL} the plain `SHUFFLE 5` source was simply absent from that lineage and had to be minted from a different parent.

**Relation:** `mx-cell-geometry-law` · `matricks-pool-reusability-and-block-structure` · `pool-labeling-doctrine-inherited-risk` · `macro-lua-label-race-needs-wait` (what happens when a later line reads a label the console has not finished writing) · `copy-at-occupied-slot-dialog-trap`.

History: none — clear encoding banked 2026-08-26, re-attested at three further venues through 2026-08-28.


### measure-not-a-safe-lua-property-part-or-preset
**Measure lives at neither the recipe-part NOR the Preset object surface — not a safe-Lua-readable property anywhere; step data (where it actually lives) stays GPDF-gated**
*when:* Before assuming Measure can be read or set as a plain object property via Lua on either a recipe cue-part or a Preset — it can't at either level; also before reaching for GetPresetDataFast as a workaround to get at step data


**Not a recipe-part property (Dave, dictated, paraphrased):** Measure is a PHASER/PRESET property, not a sequence-recipe-line property. The full ~149-prop recipe-part dump (`recipe-part-property-surface-lua-dump`) confirms it — no MEASURE among them. Measure edits happen in the preset-edit lane, not on the cue part. **Consequence:** the bridge battery item "Measure 2 on the part" was mis-scoped and is retired.

**Not a Preset object property either:** preset-lane probes (Copy Preset 21.1→21.121, Label, both via MCP, verified — see `preset-copy-label-mcp-and-century-scratch-slots`) also found Measure is **NOT** a property on the Preset object surface — only transform props (Speed, Phase From/To, etc.) are exposed there. The Preset object shows **0 children**, so step data (where Measure actually lives — see `baked-phaser-preset-xml-schema` for its file-side location and encoding) is **unreachable via safe Lua**. The `GetPresetDataFast()` ban (`gpdf-console-killer`) stands as the only door to that data, and it remains closed.

**Relation:** `phaser-layer-cli-grammar-measure-keyword` is the one lane that DOES reach Measure — the bare `Measure 2` CLI keyword — but only once a phaser is loaded into the programmer via `Edit Preset`, a different mechanism entirely from object-property access.

History: none — both findings landed live 2026-07-17, same session, folded into one concept since together they establish "Measure is unreachable via safe-Lua object properties at any level."


### mighty-flippa-plugin-discovery-and-status ⚠ VERIFY
**Mighty Flippa plugin (Chris Thoms/Chris.UK) found and v0.6 downloaded — free pixel-instance inverter, relevant to pix-RotX-flip / JDC1↔JDC2 swap; no 2.4.2.2 compat statement, sandbox-test first**
*when:* Before working the pix-RotX-flip or JDC1↔JDC2 swap decision, or before installing/trusting Mighty Flippa on the sandbox console


**What it is:** a free grandMA3 plugin by Chris Thoms (Chris.UK) that inverts pixel-instance grid locations/layout positions **inside parent fixtures**. Four modes, including flip-by-group and a "Selection 2" mode.

**Source:** sole source found is `addondesk.com/product/mighty-flippa/` — 0 EUR, WooCommerce checkout (likely needs an email/account — Dave-side to complete). Tutorial: `youtube.com/watch?v=gNX_2rBPdMg`.

**Relevance:** directly applicable to the pending **pix-RotX-flip** / **JDC1↔JDC2 swap** decision — flipping instance grid positions inside a fixture is exactly the kind of correction that decision needs.

**Compatibility caveat:** **no published 2.4.2.2 compatibility statement.** Sandbox-test before trusting it on the working show.

**Status (2026-07-17):** **v0.6 RELEASE already downloaded Dave-side** at `~/Downloads/ChrisUK_MightyFlippa_0.6_RELEASE` (mounted in this project's working directories). **Next-session action:** read the actual Lua source, then run a sandbox install test — in that order, code read before install.

History: created 2026-07-17 — plugin found and Dave downloaded the v0.6 release in the same session; not yet read or installed. Status `verify` until the code read + sandbox test happen.


### object-name-assignment-asymmetry-cues-vs-others
**⛔ Renaming by Lua is asymmetric: on a CUE, direct .Name= SILENTLY FAILS and :Set('Name',…) works — groups, sequences, appearances, images and macros all accept .Name= fine**
*when:* Before renaming any object from Lua — cues are the exception and fail silently, so a rename batch that mixes object classes needs the Set form for its cue members


| Object class | `obj.Name = "x"` | `obj:Set('Name', "x")` |
|---|---|---|
| **Cue** | ❌ **silent failure** | ✅ works |
| Group | ✅ | ✅ |
| Sequence | ✅ | ✅ |
| Appearance | ✅ | ✅ |
| Image | ✅ | ✅ |
| Macro | ✅ | ✅ |

**The silent half is the problem.** A cue rename by direct assignment reports nothing and changes nothing, so a mixed rename batch appears to succeed while leaving its cue members untouched — and cue names are load-bearing, because timecode events address cues **by name** (`automator-tc-architecture`, `tc-track-target-cutover`).

**Attested fix:** the hand-added automator cue read `In _N_OUT` with `CMD Go+ Macro "SONG_S"`. Corrected via `:Set('Name', 'SONG_S')` plus the CMD respelling, and verified by readback. **Exact-spelling law** applies throughout that chain — the whole song-fire path resolves by exact token, no case-insensitivity bets (`speedmaster-name-token-exact-match-gotcha`, `name-token-single-holder-cutover-law`).

**Standing lane:** any future cue relabel — the `[Release]` relabels parked on the trick sequences, for instance — uses `:Set('Name', …)` and reads back.

**A related silent no-op in the same family:** a **macro-LINE handle's `:Delete()` also silently no-ops** (an empty line left by a PSR import survived every attempt). Macro *objects* rename fine; macro *lines* do not delete from the wire — leave them for the desk when the macro is critical.

**Relation:** `cue-names-not-round-trip-stable-content-derived-labels` (the other cue-naming trap: auto-labels derived from content) · `set-command-unknown-property-fails-silently` · `macro-cli-creation-and-edit-lane` · `name-token-single-holder-cutover-law`.

History: none — found and fixed 2026-08-12; macro-line `:Delete()` no-op corroborated 2026-08-12 the same arc.


### objectlist-thru-vs-wildcard-gotcha
**ObjectList Thru ranges silently return empty — use wildcard (*) for pool censuses instead**
*when:* Before using ObjectList() with a range expression for a pool census or bulk readback — Thru fails silently, wildcard is the correct form


`ObjectList('Preset 22.1 Thru 22.46')` returned an **EMPTY list — no error, no exception** — a silent-failure trap.

`ObjectList('Preset 22.*')` **wildcard** form returned all 51 occupied slots correctly.

**Rule: use wildcard, not Thru, for pool censuses via ObjectList.**

**Relation:** companion to `recipe-lane-lua-readback-grammar`'s Get/PropertyName grammar; both fed the same live pool-22 census that cross-checked clean against the XML census (see `tourshow-stock-recipe-library-inventory`).

History: none — established live 2026-07-17.

**[0805-2cLD] EXTENSION — the Delete echo lies on Thru ranges:** `Delete Preset 21.2720 Thru 2722` echoed "Illegal object" while ACTUALLY deleting the range — the follow-up single delete's "Illegal object" was honest (already gone). Wildcard ObjectList census is the truth channel, not the echo. Same family: single-slot `ObjectList('Preset 21.2720')` returns no handle even when the object exists.

History: extended 2026-08-05 [0805-2cLD] — Thru-range Delete echoes "Illegal object" while deleting; single-slot ObjectList returns no handle on an existing object; wildcard census is the only truth channel.


### osc-line-property-surface
**OSC line property surface (live-verified via :Dump()) — one PORT controls both inbound and outbound**
*when:* Before scripting Set OSC N property commands, or when looking for a 'destination port'/'echo port'/'reply port' field that does not exist


`Lua "ObjectList('OSC 1')[1]:Dump()"` returns these properties: `NAME, NOTE, TAGS, DESTINATIONIP, MODE, PORT, PREFIX, DATAPOOL, PAGE, FADER, EXECUTORKNOB, KEY, FADERRANGE, RECEIVE, SEND, RECEIVECOMMAND, SENDCOMMAND, ECHOINPUT, ECHOOUTPUT`.

**There is no hidden "destination port" or "echo port" or "reply port" field.** One `PORT` property controls both inbound listen and outbound send destination for that line.

**Capitalization gotcha:** in `Set OSC N "Property" "value"`, the property name string must match the **visible UI label**, not the dumped uppercase form — use `"Receive"`, not `"RECEIVE"`.

History: none — standalone live-verification result, 2026-05-27 evening.


### plugin-code-runs-at-showfile-load
**⛔ MA3 COMPILES AND EXECUTES EVERY PLUGIN'S TOP-LEVEL CODE AT SHOW LOAD — no fire step exists or is needed; the pool object is a SEED that replants itself every load, and the real kill-switch is deleting it**
*when:* Before assuming a plugin toolbox must be 'fired' before a show, before designing a pre-show ritual around one, or when reasoning about what survives a quit, a reload, a PSR or a file fork


## The law

**Every plugin's top-level code runs automatically at show load.** There is no install step, no fire step, no pre-show ritual.

**How it was established:** the inherited show's control plugin had **never been fired by anyone** — it simply came working in the handed-over file — and the Lua global table nonetheless held toolboxes from a dozen plugins. Reading the component's source confirmed it: the toolbox build is **top-level code**, written with the re-load-safe `X = X or {}` idiom.

## The corrected lifecycle

```
LOAD    → every plugin's top-level code compiles and runs (auto-install, EVERY time)
PARKED  → nothing runs while the session lives
CALLED  → a function runs for milliseconds when the native chain calls it
QUIT    → the Lua drawer evaporates
LOAD    → reinstalls, identically
```

**`SaveShow` persists the CODE only — and that is enough**, because load re-cooks the meal. **Self-healing by design:** a console restarted minutes before doors comes back with the whole toolbox intact.

**Two lives, not one:** *install* (fires once at load, builds the toolbox, the code ends) versus *use* (the native chain calls a function per song). It is a **subroutine, not a service** — nothing is resident. If the toolbox vanished mid-show the automator would still fire every macro on time; they would simply error at their last line. **Clockwork and toolbox are separate.**

## Component anatomy (banked)

- Source lives in the component property **`FILECONTENT`** — *not* `Content`.
- `FULLPATH` = the show file; `INSTREAM = true`; `FILEEXISTS = false` ⇒ **the code is EMBEDDED in the show file** and travels with it (a PSR or import carries it).
- A per-component **`SYNTAXERROR`** flag exists.
- **Fork-proof, attested:** a file rebuilt by PSR onto a different rig carried **both** toolboxes, auto-installed at load, with zero rebuild.

## Kill-switch truth

`X = nil` lasts only until the next load. **The real off is DELETING the plugin from the pool** — that removes the seed from the file. **The pool object is not a running program; it is the seed that replants itself every load. Protect the seed.**

## What this retired

An earlier same-week finding concluded a **pre-show ritual line was owed** — "fire the control plugin once per session." **WITHDRAWN — wrong.** No fire step exists. Recorded here because the wrong model is the intuitive one.

**Note the distinction from `plugin-lifecycle-autocleanup`:** that concept covers invoking a plugin explicitly as `Plugin <N>`, where MA3 runs `Main()` then immediately `Cleanup()`. This concept covers the *load-time* execution of top-level code, which is a different entry point and is what makes a persistent toolbox possible at all.

**Relation:** `plugin-lifecycle-autocleanup` · `lua-global-drawer-is-session-not-file` · `automator-tc-architecture` · `plugin-install-loop` · `plugin-import-verify-name-match` · `plugin-xml-schema`.

History: replaced the [0808-5] "no plugin at runtime" model and withdrew that block's pre-show-ritual conclusion, 2026-08-08; corroborated on a forked file 2026-08-12.


### plugin-import-verify-name-match
**Import verify read-back must compare slot object Name == expected — any-occupant truthiness false-positives on already-taken slots**
*when:* Before writing or trusting a round-trip verify step after Import Plugin <slot> — any check weaker than an exact Name comparison can misreport success


**`Import Plugin <slot> "<name>"` does not overwrite an occupied slot.** A round-trip verify that only checks "is *something* present in the slot" (any-occupant truthiness) will **false-positive** when the slot was already taken by a different plugin before the Import call ran — the slot reads as occupied either way, so a naive presence check can't tell "my import succeeded" from "someone else's plugin was already sitting there."

**Rule:** the verify read-back must compare the slot object's **`Name` == the expected plugin name** (not just presence/truthiness). This is the check implemented in `install_plugin`'s round-trip verify (2026-07-05 build, see the wrap).

**Premise to console-verify (status: verify):** the imported **pool object's `.Name` equals the folder name** used at import time (i.e., the plugin's folder/`<UserPlugin Path="…">` name, not some other label field). This has not yet been confirmed against a live console read — it's the working assumption the Name-match check depends on. Verifies via the reviewer's attended console-verify list: attempt an occupied-slot Import and read back `.Name` against the expected folder name.

History: none — found by a second-look Fable cross-check subagent review (not by the 67-green unit test suite in place at the time) and fixed same session, 2026-07-05.


### plugin-install-loop
**Full plugin install → run sequence (write files, ReloadAllPlugins, Import Plugin, Plugin N)**
*when:* Before installing or refreshing a Lua plugin on-console — the exact 4-step sequence and its two common failure modes


The full install → run sequence, live-verified:

1. Write `<name>.lua` + `<name>.xml` pair to `~/MALightingTechnology/gma3_library/datapools/plugins/<name>/`. Folder name must match `<UserPlugin Path="…">` in the XML; the `.lua` filename must match `<ComponentLua FileName="…"/>`.
2. `ReloadAllPlugins` — refreshes pool entries already present; does **NOT** auto-import new ones from disk.
3. `Import Plugin <slot> "<folder_name>"` — materializes into pool slot. Slot must be empty (`Delete Plugin <slot> /NoConfirmation` first if needed).
4. `Plugin <slot>` — runs `Main(display_handle, arguments)`.

Failures to remember:
- `Import "name" At Plugin <slot>` → returns **"Illegal object"**. This is wrong syntax — use step 3's form instead.
- `Enums.PathType.UserPlugin` → **does not exist**. Use **`CustomPluginLibrary`** (user-level) or **`PluginLibrary`** (system-level).
- Path resolution at runtime: `Lua "for k,v in pairs(Enums.PathType) do Printf(k..'='..tostring(GetPath(v))) end"`.

See `plugin-xml-schema` for the XML shape referenced in step 1, and `plugin-lifecycle-autocleanup` for what happens the instant `Plugin <slot>` finishes running.

History: none — live-verified 2026-05-27, no later corrections found in corpus.


### plugin-lifecycle-autocleanup
**Plugin <N> auto-runs Cleanup() immediately after Main() — kills persistent state same call**
*when:* Before writing a plugin that needs to persist state across command invocations (hooks, retained handles, coroutines, push channels, observers) — one-shot plugins are unaffected


When invoked via `Plugin <N>` from the command line, MA3 runs `Main()` and then **immediately runs `Cleanup()`** in the same synchronous call. Consequences:

- Persistent state (registered hooks, retained handles, coroutines) is torn down before the next command runs.
- `HookObjectChange` registered inside `Main` will be **unhooked by the time the user changes the target** — a hook set up this way is already dead.
- For **persistent** plugins (push channels, observers) you need a different lifecycle: the v2.3 plugin pool's **`Toggle`** pool-action, or `Execute(type, ...)` with a long-lived registry, or registration at showfile-load time.
- For **one-shot** plugins (snapshot, API dump, codegen), the auto-Cleanup is exactly the behavior you want — no special handling needed.

History: none — recorded 2026-05-27, no later corrections found in corpus.


### plugin-pool-slot-reservations
**Plugin pool slot reservations — alchemease_* in 1-20, production show plugins 21+**
*when:* Before assigning a new plugin to a pool slot on Dave's onPC — check this reservation convention first to avoid collisions


Currently on Dave's onPC:
- Slot 1: `alchemease_hello` (probe)
- Slot 2: `alchemease_snapshot` (state export)
- Slot 3: `alchemease_api_dump` (API inventory)
- Slot 4: `alchemease_hook_demo` (lifecycle probe)

**Convention:** keep the `alchemease_*` namespace in slots **1–20**; production show plugins (PatchExport, PhaseCalc, ShowShuffle) get **21+**.

History: none — established 2026-05-27; no later corpus entry records additional slot assignments beyond these four.


### plugin-xml-schema
**Plugin XML schema (v2.3.2) — UserPlugin element, not Plugin**
*when:* Before writing the .xml companion file for a Lua plugin


```xml
<?xml version="1.0" encoding="UTF-8"?>
<GMA3 DataVersion="2.3.2.2">
  <UserPlugin Name="<name>" Author="…" Version="0.1.0.0" Path="<folder>">
    <ComponentLua Name="<name>" FileName="<name>.lua"/>
  </UserPlugin>
</GMA3>
```

The root plugin element is **`<UserPlugin>`**, not `<Plugin>`. `<Plugin ContentType="Usercontent">` is a *different* shape used for the showfile-embedded portability form of a plugin — do not confuse the two.

History: none — recorded 2026-05-27, no later corrections found in corpus.


### preset-objectlist-dot-range-silent-empty-hazard
**ObjectList('Preset X.Y Thru X.Z') returns EMPTY silently even when occupied — census presets via PresetPools:Ptr(pool) walk with nil guard instead**
*when:* Before using ObjectList with a dotted Preset range (e.g. 'Preset 4.59 Thru 4.62') to census or verify preset pool contents — dot-form preset ranges are unreliable in ObjectList even when the slots are genuinely occupied


**Read-lane hazard (corroborated a second/third time, on SONG_C):** `ObjectList('Preset 4.59 Thru 4.62')` returns an **EMPTY list, silently** — no error — even though all four slots are occupied. Dot-form Preset ranges are unreliable in `ObjectList`.

**Scope of the hazard, refined this session:** this is specific to **Preset** dot-ranges. **Sequence / Timecode / MAtricks `ObjectList` ranges are fine** — do not over-generalize the caution to every pool type.

**Correct census method for presets:** walk `DataPool().PresetPools:Ptr(pool)` directly, with a **nil guard** — `Ptr(i)` can return `nil` mid-iteration and will throw if not guarded.

**Relation to existing corpus:** this corroborates and extends `objectlist-thru-vs-wildcard-gotcha` (existing concept, not staged this run — its documented case was `Preset 22.1 Thru 22.46`; this session's `4.59 Thru 4.62` is a second live data point on a different pool). cLD should consider folding this file's scope-refinement (only Preset ranges affected) and its pool-walk alternative into that concept's body directly at next edit, since its body wasn't staged for a merge this run.


### recipe-lane-lua-readback-grammar
**Lua readback grammar for recipe lines — ObjectList('Seq x Cue y Part z')[1]:Get('Prop'); PropertyName(i) is 0-based; wrap before tostring**
*when:* Before writing generated Lua that reads back recipe cue-part properties — the exact ObjectList/Get/PropertyName grammar and its gotchas


**Readback pattern:** `ObjectList('Seq x Cue y Part 0.1')[1]:Get('PropName')` returns live values as strings (e.g. `'false'`, `'Group 123'`, `'Preset 22.9'`).

**`PropertyName(i)` is 0-BASED** — a 1-based loop over it errors.

**Wrap in parens before `tostring`** — a zero-return index crashes a bare `tostring()` call; `tostring((...))` guards it.

**`handle.no` / `handle.name`** work correctly in an `ipairs` loop over an `ObjectList`.

**Relation:** pairs with `recipe-part-property-surface-lua-dump` (what to read) and `objectlist-thru-vs-wildcard-gotcha` (how ObjectList ranges behave) — load together when generating any recipe-lane Lua readback.

History: none — established live 2026-07-17.


### recipe-line-creation-not-wire-reachable
**⛔ Recipe LINES are born at the desk: part:Append/Acquire/Create all silent-no-op and Insert dialog-cancels headless — but EXISTING lines' Selection/Values/Preset/MAtricks all reassign cleanly by Lua**
*when:* Before planning any batch that needs NEW recipe lines — creation is a desk/macro job, not a bridge job; reassignment of existing lines is fully automatable


## The hard boundary

**Creation is not reachable over the wire.** On a cue part, all of these failed:

- `part:Append(...)` — silent no-op
- `part:Acquire(...)` — silent no-op
- `part:Create(...)` — silent no-op
- `Insert` — opens a dialog, cancels headless (`"User Canceled Command"` family)

**⇒ A new recipe line is born at the desk** — Recipe editor, new line — or through Dave's **Assign lane**: recipe fields *are* assignable by macro line, so a macro artifact can carry the work even where raw Lua cannot (`many-lines-ride-macros-not-lua`).

## What IS fully automatable

**Every field on an EXISTING line reassigns cleanly by Lua**, readback-exact:

- `rl.Selection = <group handle>`
- `rl.Values = <preset handle>` and `rl.Preset = <preset handle>`
- `rl.MAtricks = <matricks handle>`

Handle assignment — not pool numbers, not name strings — is the proven form (`assign-cli-recipe-line-grammar`). This is what carried **407 colour repoints**, **65 master-migration repoints**, **39 pan-shell repoints** and every venue MX repoint of the leg.

## The planning consequence

Design surgeries around **repointing what exists**, never around **conjuring what doesn't**. Where new lines are genuinely required — the mark-cue MM shell rows are the standing example — the work is **handed to Dave's fingers with an exact per-part recipe** rather than attempted from the bridge (`mm-shell-empty-preset-armor`).

**Relation:** `assign-cli-recipe-line-grammar` · `many-lines-ride-macros-not-lua` · `mm-shell-empty-preset-armor` · `recipe-line-cli-addressing-and-list-readback` · `recipe-step-level-cli-write-path`.

History: none — four creation lanes attested dead 2026-08-26; Dave's Assign-lane note added 2026-08-27.


### recipe-part-property-surface-lua-dump
**Recipe-part (StandardRecipe) full property surface — ~149 props via handle:PropertyName(), six bind slots, part carries its own full MAtricks prop set**
*when:* Before writing Lua/MCP calls that read or Set properties directly on a recipe cue-part object — the full live-dumped property inventory and bind-slot map


Live property dump via `handle:PropertyName()` on a StandardRecipe cue-part surfaced **~149 properties**. Six bind slots identified: **SELECTION / VALUES / PRESET / MATRICKS / FILTER / GENERATOR**.

The part carries its **own full MAtricks property set** as first-class part properties (**XWINGS, PHASEFROMX/TOX, XBLOCK**, etc.) — meaning the store-time `/MAtricks` embed (see `live-selection-matricks-cli-set-syntax`'s "two carriers" finding) likely lives as directly Set-addressable part properties, not just an embed baked at Store time. **Untested** — not yet confirmed by an actual `Set` call against one of these MAtricks part-properties.

**Relation:** this is the raw Lua-object-model property inventory underlying `assign-cli-recipe-line-grammar`'s routing table (Group→Selection, Preset→Values, MAtricks→MAtricks slot). It surfaces a potential fourth recipe-MAtricks carrier alongside the CLI Selection-object form, the store-time `/MAtricks` embed, and the recipe-line MAtricks editor already mapped in `live-selection-matricks-cli-set-syntax`.

History: none — first dumped live 2026-07-17.


### selection-count-probe
**Cheap group-membership census: Cmd a Group select, read Lua SelectionCount(), announce, ClearAll after — no export, no walk**
*when:* When you need to know how many fixtures a group actually holds on THIS file/rig before trusting a repoint, a recipe selection or a wings/block calculation — and a full export would be overkill


**The probe:** issue the group selection over the command line, then read the count from Lua:

```
Cmd('Group <n>')      -- select
SelectionCount()      -- read
Cmd('ClearAll')       -- tidy (ending-law)
```

It is a **write-effect operation riding the read channel** — the selection is real console state — so the **announce-always law applies** (see `classifier-tier-drift`), and **`ClearAll` afterwards is not optional**: leaving a live selection behind is exactly the shared-command-surface hazard `desk-clear-callout-before-console-write-rule` exists for.

**Why it matters more on tour than in the shop.** Group membership is the one number every venue adaptation depends on — wings divide it, blocks partition it, phase spreads across it. It is also the number that changes silently when a rig is cloned. Receipts from the leg: `cLD JDC PLATE MASTER` / `BEAM MASTER` / `ALL` = **52** each at {FESTIVAL}; **G416 plates = 18, G417 tubes = 0 (dormant)** at {FESTIVAL}; **24 and 24** at {FESTIVAL}; **11 and 11** at {FESTIVAL}. Each of those numbers changed the doctrine call that followed (`mx-cell-geometry-law`).

**Relation:** `inherited-file-membership-is-ground-truth` (never trust a group's *label*) · `mx-cell-geometry-law` · `group-xml-export-selectiondata-census` (the export-side alternative when you need membership, not just a count).

History: none — used repeatedly across the EU leg, 2026-08-26 onward.


### send-lua-expression-payload-rule
**⛔ send_lua payloads must be a bare Lua EXPRESSION, not a statement — the server wraps every payload as pcall(function() return (<code>) end), so local/return payloads syntax-error before the round-trip file is ever written**
*when:* Before writing ANY send_lua payload, and immediately if a send_lua call times out with 'no-roundtrip-file' while get_console_info reads the channel as healthy — check payload SHAPE (expression vs statement) before suspecting the wire


**⛔ ROOT CAUSE (the wire was NEVER down — Dave read the console echo, which is what cracked it):** the `send_lua` server wraps every incoming payload as `pcall(function() return (<code>) end)`. Any payload that starts with `local` or `return` assembles into `return (return ...)` — a Lua **syntax error** (`[1: unexpected symbol near 'return']`). The whole Lua line dies **before** the round-trip file is ever written, so the server only ever reports a **no-roundtrip timeout** — which looks exactly like a dead channel, a suspended session, or a crashed console, and is none of those.

## The rule

**Send bare EXPRESSIONS**, e.g.:
```
ObjectList(...)[1]:Get(...)
tostring(...)
Cmd([[...]])
```

**Wrap multi-statement code as an IIFE** (immediately-invoked function expression) instead of a `local`/`return` block:
```
(function() <statements> return <val> end)()
```

## Wrapper mechanics (banked)

The wrapper writes `Library/alchemease_rt.txt` via a `.tmp` file + `os.rename`, nonced per call. This is why the failure is silent from the caller's side — nothing ever gets far enough to write the file, so there's no partial/corrupt artifact to inspect, just an absence.

## What this explains

**All 6 of this session's send_lua failures**, and — just as importantly — **why 2026-07-17 and 2026-07-28 reads and writes worked fine**: those payloads happened to already be expression-shaped. Nothing about the transport, the MA-Net session, or the OSC interface changed between then and now; the difference was always payload shape.

**Verified fixed live:** `tostring(BuildDetails().BigVersion)` → `2.4.2.2` @ 66ms.

**End-to-end re-verification, same session, once the rule was applied:**
- Tier-1 read: `2.4.2.2` @ 66ms.
- Tier-2 `confirm_gate` flow clean: `SaveShow /Enumerate` v.37→v.38 **verified on disk** (113,287,266 B, 18:22).
- `Export Sequence` 1501 `'gb_fill1'` + 1502 `'gb_fill2'` OK @ 65-67ms, both landed in `datapools/sequences` and copied to the repo (`showfiles/festival_recon/sequences/`, 617,262 / 487,527 B).
- `/Enumerate` trailing-version increment now **9-for-9**.

## What this was mistaken for, and why that mattered

Before the root cause was found, the same symptom (probe reads healthy, send_lua times out with no round-trip file) was chased down two other paths in the same session: (1) a suspicion that the reachability **probe itself** was giving a false positive — that strand is real and stands independently, see the refinement in `out-ok-is-send-not-reachability`; and (2) after Dave's IP/network reset, a live suspicion that the **MA-Net Session** had dropped or the **OSC line Interface** had gone orphaned by the network change — investigated and **not** the cause this time. **Refined diagnostic order:** probe-true + send_lua-timeout ⇒ check payload **SHAPE** first (this concept), then session/interface health (`out-ok-is-send-not-reachability`), then crash-as-timeout (`segfault-manifests-as-mcp-timeout`).

**Companion process lesson:** the expression-only rule was already stated in the `send_lua` tool's own description the whole time — see `reread-tool-description-on-misbehavior`.

**Relation:** `out-ok-is-send-not-reachability` (the probe-trustworthiness question, one layer removed from this payload-shape question) · `saveshow-discipline-and-mcp-tier` (the companion quoting rule for dotted show names inside `send_lua`) · `reread-tool-description-on-misbehavior` (the process lesson this saga produced).

History: none — root cause found, fixed, and verified end-to-end in one session, 2026-07-29.


### settle-before-export-crash
**Export Preset on a freshly Copy+mutated preset segfaulted onPC (Program Error Memory) — same crash family as gpdf-console-killer; settle with a SaveShow before exporting anything just written**
*when:* Before running Export Preset (or any Export) on an object that was Copied/Assigned/Set in the last few seconds — settle state with a SaveShow first, and verify fresh objects via Lua :Get() readback rather than Export, until this is fully trigger-isolated


**`Export Preset` on a freshly Copy+mutated preset segfaulted onPC** — `Program Error Memory`, a `_sigtramp` fault in the LUA thread with a recursive native stack — **the same crash family as `gpdf-console-killer`** (a C-side crash, not a catchable Lua error: `pcall` cannot help, and the round-trip just times out rather than returning an error).

**Sequence that crashed:** `Copy 21.51 → 21.53`, then `Assign Shape`, then `Set PlaybackDirection`, then `Export` **~30 seconds later**.

**Contrast:** the identical `Export` survived minutes earlier on a different object (21.52) that was freshly-Assigned but NOT copied. This isolates the trigger toward the **fresh-COPY step, or the `Set PlaybackDirection` write** specifically — **but this is one data point; do not over-conclude which exact step is the cause.**

**Mitigation adopted (both data points support it):**
- **Never `Export` an object in the same breath as writing it.** Verify freshly-written objects with **safe Lua `:Get()` reads only.**
- **`Export` only after a `SaveShow` has settled the state.** A second data point the same session (the phaser template-set import, see `tourshow-seq1510-build-record`) confirms: Export of freshly-imported presets is clean when it runs after a SaveShow.

**Recovery:** the crash reverted cleanly to a checkpoint (`v.25`) taken minutes before — the standing pre-write `SaveShow` checkpoint discipline (`saveshow-discipline-and-mcp-tier`) paid for itself in full; zero rework lost beyond the crashed step itself.

**Relation:** `gpdf-console-killer` for the sibling crash family (same signature, different triggering call — `GetPresetDataFast()` there vs `Export Preset` here); both are C-side crashes that an MCP round-trip only sees as a timeout (`segfault-manifests-as-mcp-timeout`). The CLI grammar that led into this crash (`Assign Shape <n> At Preset <pool>.<slot>.1` — the `.1` addresses the preset's `PhaserRecipe` child; the bare preset address without `.1` is a loud `Illegal object`) is recorded in `tourshow-seq1510-build-record`.

History: none — first (and so far only) occurrence, 2026-07-28; trigger not yet fully isolated, flagged for verification.


### split-and-guard-per-sequence-walk-law
**⛔ SPLIT-AND-GUARD is the scan law: one concern per pass, pcall per sequence, capped output — and on a file whose sequence pool reports Count()=9999 a full-pool nested walk DIES outright while a single-sequence walk runs in ~70ms**
*when:* Before writing ANY show-wide Lua scan or audit, and immediately when a scan times out or silently kills the round-trip — the payload's SHAPE (one big nested walk vs per-sequence guarded calls) is the first suspect, not the wire


## The law

A show-wide scan is **not** one big nested walk. It is:

1. **One concern per pass.** Values in one pass, selections in another. The audit that combined values + selections + a per-song rollup in a single payload **silently killed the round-trip** — the wire itself was fine.
2. **`pcall` per sequence.** Each sequence's walk is its own protected call, so one bad object cannot take the pass with it.
3. **Capped output.** Lists are truncated at the source; counts come back, not bodies. (Compare `tourshow-context-health-never-read-bulk-xml-rule`.)

**Rebuilt that way, the same audit completed clean:** **6201 value refs, 0 errors, 0 dead** (Dimmer 2910 · Color 1027 · Phaser 895 · Beam 703 · Position 455 · Focus 203 · pool 22 ×8) and **6075 group refs, 0 errors, 0 dead** — the pre-flight that made walking onto a festival stage with no rig time safe.

## The attested kill, and the working budget

On the **{FESTIVAL}** file the sequence pool reports **`Count() = 9999`**. Against that number:

- a **full-pool nested walk DIES** — repeat timeouts, every attempt;
- a **single-sequence walk runs in ~70 ms**.

**⇒ Portability warning:** the all-sequences sweep that worked on the base file is **not portable**. On any file with an inflated pool count, the only lanes are **per-sequence calls** or **export + Mac-side python** (`export-plus-python-bulk-lane`). The rule of thumb the leg settled on: **bulk questions go export+python, targeted writes go per-sequence calls.**

**Relation:** `lua-pool-walk-allocation-law` (the sibling truth about `#pool` reporting allocation, not occupancy — the two together explain why pool-count-driven loops are hazardous) · `export-plus-python-bulk-lane` · `wire-timeout-vs-console-busy` (the other reason a scan times out) · `send-lua-expression-payload-rule` · `saveshow-discipline-and-mcp-tier` (the 1800-char transport cap that forces chunking).

History: born as the scan law after the 2026-08-22 full-show audit crashed the round-trip; extended 2026-08-26 with the Count()=9999 attested kill and the ~70ms single-sequence budget.


### undo-and-realtime-safety-primitives
**CreateUndo/CloseUndo and CallRealtimeLockedProtected — required safety wrappers for generated Lua**
*when:* Before generating any Lua that mutates console state, especially Phasers, MAtricks live values, or executor state — these wrappers are mandatory for Tier 2 generated Lua


- **`CreateUndo("description")` / `CloseUndo()`** — wrap mutations to make them a single `Oops` step. **Tier 2 generated Lua MUST use this.**
- **`CallRealtimeLockedProtected(fn)`** — protected entry point for code that touches realtime output (Phasers, MAtricks live values, executor state).

History: none — recorded 2026-05-27, no later corrections found in corpus.


### v23-lua-renames
**MA3 v2.3 renames to remember: Acquire, Autos, Cue, If, plugin pool Toggle**
*when:* When old syntax/shortcuts from MA2-era muscle memory or older docs don't work — check this rename table first


- `Aquire()` → **`Acquire()`** (typo fixed in v2.3)
- `AS` shortcut → **`Autos`** (AutoStore)
- `C` shortcut → **`Cue`**
- `I` shortcut → **`If`**
- Plugin pool gained the **`Toggle`** pool-action (relevant to persistent-plugin lifecycle — see `plugin-lifecycle-autocleanup`)

History: none — recorded 2026-05-27, no later corrections found in corpus.


### version-string-functions
**Getting the real MA3 version from Lua: BuildDetails().BigVersion (HostRevision() is just a build tag)**
*when:* Before writing Lua that needs to detect or report the running MA3 version programmatically


- `HostRevision()` returns a short string (e.g. **"Rev1"**) — **NOT** the user-facing version.
- `_VERSION` returns **"Lua 5.4"** — confirms the Lua runtime only, not the MA3 build.
- **`BuildDetails()` is the real answer** (live-verified 2026-07-04, onPC 2.4.2.2, over the MCP wire, 34.9 ms RTT): returns a table —
  `BigVersion=2.4.2.2` (the user-facing version) · `SmallVersion=2.4.0.0` · `GitHash` · `GitDate` · `CompileDate` / `CompileTime` · `CodeType=Release` · `IsRelease=true` · `HostType=onPC` · `HostSubType=Undefined`.
- Programmatic version check: **`BuildDetails().BigVersion`**.

History: was `status: verify` ("BuildDetails() in the api dump — try it", 2026-05-27). Cleared live 2026-07-04 — the first concept verified through the library's own loop (index flagged it → one Tier-1 Lua expression → active).


## MACROS

### cld-position-wiz-generic-v01-authored-and-deployed
**cLD POSITION WIZ generic v0.1 — first cLD-authored macro XML, imported and run live on console; DS-row clean, whole-rig Blind not yet depth-graded**
*when:* Before running, editing, or extending cLD's own position-wizard macro, or before citing it as proof the macro-XML authoring lane works end to end


**Authored + deployed:** `cLD POSITION WIZ generic v0.1`, composed entirely from factory-verbatim grammar (see `factory-position-wiz-anatomy-and-porting` for the techniques it borrows). Design choices versus the factory original:
- **Selection-based, not handle-based** — no Handles, no Groups baked into the macro itself; it operates on whatever's selected when it fires. Sidesteps the factory version's #1 porting caveat entirely (no show-specific handles to dangle).
- **Slot-addressed stores at 2.121–2.127** — follows cLD's own century-scratch-slot convention (see `preset-copy-label-mcp-and-century-scratch-slots` for the pool-21 preset instance of the same convention; this is that convention's pool-2 application), plus a Label pass on each stored preset.
- **Self-gating Lua Confirm kept** — same control-structure idiom as the factory original (see `macro-control-structure-workaround-idioms`).
- **Cross / UP-Cross DROPPED from the generic version** — Cross needs a half-selection, which a plain selection-based macro can't derive on its own. A base-show variant queued behind air-group creation will get real Cross via mirror-half groups instead.

**Files:** repo master `generated/cLD_POSITION_WIZ_generic_v0.1.xml` (xmllint-valid); deployed via Desktop Commander to `gma3_library/datapools/macros/cLD_POSITION_WIZ.xml`.

**✅ LIVE-VERIFIED (Dave, console, 2026-07-19):** imported and ran clean — the **first cLD-authored macro XML run live on console**, putting macros alongside presets and sequences in the proven file-side XML authoring lane (see `xml-file-side-authoring-import-lane-proven`). DS-row run: fine. **Whole-rig run: stored everything correctly EXCEPT no depth-graded Blind tilt** — see `tourshow-position-wiz-blind-depth-grade-root-cause` for the diagnosed cause and the fix (2D grid groups per category, tracked in `tourshow-group-contract-v01`).

**[VERIFY] still open at desk:**
- Whether `Store .../Merge` auto-creates a preset slot that doesn't already exist, or requires the slot to pre-exist.
- `Grid Rotate` scope on cLD's own version specifically (as opposed to the factory original).
- A fuller verify checklist beyond the DS-row spot-check was raised live but not yet run in full.

History: none — authored, deployed, and given its first live run all in the 2026-07-19 session.


### factory-position-wiz-anatomy-and-porting
**POSITION_WIZ.xml (factory demo-show position builder) anatomy: 8 group blocks building Straight/Fan In/Fan Out/Cross/UP×4/Blind into Preset pool 2 via /Merge — plus its porting caveats**
*when:* Before reading, porting, or modeling a new macro on POSITION_WIZ — its file-side anatomy, the grammar techniques it demonstrates, and the three things that break on a naive import into another show


**Location & identity:** `gma3_library/datapools/macros/POSITION_WIZ.xml` — a **user datapool** file, already sitting in the console's macro import path (no relocation needed to use it). `DataVersion 2.4.2.2`, macro name "Position Wizard." Carries a "Red Back" Appearance via an embedded `DependencyExport` (see `macro-xml-schema-cracked` for the schema-level fact that macro XML can carry dependencies at all).

**What it produces:** universal position presets — **Straight, Fan In, Fan Out, Cross, UP Straight, UP Fan In, UP Fan Out, UP Cross, Blind** — written into stock **Preset pool 2** (Position), accumulated **per-group over Groups 1–8** using name-addressed `/Merge` stores (`Store Preset 2. "Name" /Merge` — each of the 8 group blocks merges its own values into the same named preset rather than overwriting).

**Line 1** is the self-gating Lua Confirm control-structure idiom — see `macro-control-structure-workaround-idioms` for the mechanism.

**Then 8 near-identical blocks, one per Group 1–8, each:**
1. Selects the group plus a second object via raw **Handle** references (`#000000027e001379`-style hex) — see `macro-handle-persistent-object-reference` for what Handles are and how this hex form ports.
2. `Attribute "Pan" At Absolute Physical 0` + `Tilt At Absolute Physical -45` → `Store Preset 2. "Straight" /Merge`.
3. `Pan At Absolute Physical 30 Thru -30` → "Fan In"; `-30 Thru 30` → "Fan Out". Negative-bound `Thru` spreads work fine here — this is a programmer-attribute value-spread, not the patch-`Set` CLI spread that rejects negative bounds (see `patch-set-one-prop-quoted-values` for that scope boundary).
4. Cross: one half-selection at Pan −30, the other half at +30 → "Cross".
5. UP family: `Tilt At Absolute Physical -95`, then a **single-attribute preset recall** — `Attribute "Pan" At Preset 2."Straight"` — pulls just the Pan value back out of the already-stored preset to compose "UP Straight" (new Tilt + inherited Pan), and likewise for UP Fan In / UP Fan Out / UP Cross.
6. Blind: `Grid 'Rotate' 'Right'` + `Tilt -90 Thru -45` → "Blind", then `ClearAll`. See `tourshow-position-wiz-blind-depth-grade-root-cause` for what happens when this block runs against a selection that isn't a real 2D grid.

**Porting caveats (all three matter before running an adapted copy against any other show):**
1. **Handles are show-specific** — they point at the demo show's own Groups 1–8 and selection objects; imported elsewhere they dangle or resolve to the wrong objects. Any port must replace every `#...` handle line with explicit `Group <n>` / MAtricks calls. This is THE key POSITION_WIZ porting caveat.
2. **Tilt angle semantics (−45/−95/"UP") assume the demo rig's own hang orientation** — re-derive the angles for a different rig's overhead trusses before trusting the preset names.
3. It writes into Preset pool 2 with `/Merge` and issues **no SaveShow** of its own — checkpoint first (hard rule: SaveShow before any XML import, see `saveshow-discipline-and-mcp-tier`).

cLD's own port of this macro is `cLD_POSITION_WIZ.xml` — see `cld-position-wiz-generic-v01-authored-and-deployed` for what changed in the port and its live-run status.

History: none — anatomy read whole 2026-07-19 from the factory file, `MACRO_LIB_CATALOG_v0.1.md` §5.


### macro-call-and-nesting-lifetime-semantics
**Macro X.Y addressing calls ONE line, not 'start at line Y'; bare-called sub-macros share the parent's lifetime; nested calls do NOT block**
*when:* Before calling one macro from another, or before assuming a called sub-macro's timing/lifetime works like a function call — three gotchas apply


Three related gotchas about macros calling other macros:

**1. `Macro X.Y` addressing calls that ONE line as a standalone unit** — it does NOT mean "start macro X at line Y" (i.e. it doesn't begin executing macro X from line Y onward). MA dev Andreas corrected this live on the forum, 2023 (thread 7844).

**2. Lifetime differs by call style:**
- **Bare-called** sub-macros (referenced directly, not via `Call Macro`) share the PARENT macro's lifetime — they die if the parent stops or finishes first.
- **`Call Macro X`** gives the sub-macro an INDEPENDENT lifetime instead, decoupled from the parent.

**3. Nested/called macros do NOT block.** The parent's next line fires immediately — it does not wait for the sub-macro to finish. Two independent forum threads agree on this (8456 + 5998). **Fix:** pad the parent's `Wait` column to a duration sized to the sub-macro's real runtime, or move to Lua for real sequencing.

History: none — all three facts first captured 2026-07-17, macro deep-dive session.


### macro-cli-creation-and-edit-lane
**CLI macro creation/edit lane: ChangeDestination Macro → Store [N] → ChangeDestination [N] → Insert → Set [Line] Property 'Command'/'Wait'**
*when:* Before authoring or editing a single macro live via CLI/MCP — same shape as the proven preset/sequence CLI-first authoring pattern


Live CLI lane for creating/editing a macro, one line at a time:

```
ChangeDestination Macro
Store [N]
ChangeDestination [N]
Insert
Set [Line] Property "Command" "..."
Set [Line] Property "Wait" [...]
```

Same shape as the MCP/CLI-first authoring pattern already used for presets and sequences (see `recipe-step-level-cli-write-path` for the analogous recipe-line pattern) — one property per `Set`, address the line, write the property.

History: none — first captured 2026-07-17, macro deep-dive session, official manual `macro_create.html`.


## EU tour leg truths, 2026-08-12

- **A macro OBJECT's `.Name =` assignment WORKS** by direct Lua assignment — unlike a **cue**, where it silently fails and `:Set('Name', ...)` is required (`object-name-assignment-asymmetry-cues-vs-others`).
- **A macro LINE handle's `:Delete()` SILENTLY NO-OPS.** An empty line left behind by a PSR import survived every attempt and was left for the desk — a critical macro is not the place for ambiguous CLI delete experiments.
- **`Export Macro <n> /File "<name>.xml"` writes clean XML** (431 bytes for a one-line macro), which makes a macro a portable artifact between file lineages — the basis of the venue-adaptation kit (`venue-adapt-macro-pattern`). Re-import with the filename **quoted** (`import-file-argument-must-be-quoted`).
- **A macro Lua line must not consume names minted by earlier `Cmd` lines in the same macro without a `Wait`** — `macro-lua-label-race-needs-wait`.

History: extended 2026-08-28 (librarian, tour leg).


### macro-conditional-branching-not-implemented
**True if/then/else branching does NOT exist in native macro CLI syntax — Lua is the only path; If/EndIf is scope-restriction, not branching**
*when:* Before trying to build conditional (if/then/else) logic into a macro using native CLI syntax — it isn't possible; before assuming If/EndIf in a macro branches execution


**True conditional branching (if/then/else) is NOT implemented in native macro CLI syntax.** MA staff gave the same answer twice, three years apart (confirmed 2020, confirmed again 2022) — a settled, repeatedly-confirmed limitation, not a one-off forum opinion. **Lua is the only path** to real conditional branching in MA3.

**What `If`/`EndIf` actually does in a macro:** it's **scope-restriction** — a WHERE clause limiting which objects a subsequent command applies to — **not branching**. Don't read an `If` line in a macro as a programming-language conditional.

Cross-reference: the If family is also covered structurally (command surface + scoping-stack model) in `IF_AT_FILTERS_WORLDS_STUDY_v0.1.md` — see `at-filters-worlds-manual-gap-and-study-doc` for that doc's manual-gap findings on At/Filters/Worlds.

**Workarounds exist, but don't contradict this ruling (added 2026-07-19):** MA's own shipped macros use two operator/Lua-assisted idioms that approximate control structures without any native branching primitive — a self-referential Go-loop for iteration, and a self-gating Lua `Confirm()` for a real yes/no gate. See `macro-control-structure-workaround-idioms` for both. Both still require an operator Go+ or a one-line Lua evaluation to advance; neither is native macro-CLI branching, so MA staff's ruling above stands unchanged.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: cross-referenced the two factory control-structure workaround idioms (`macro-control-structure-workaround-idioms`) — they work around this limit, they don't lift it.


### macro-control-structure-workaround-idioms
**Two factory idioms approximate if/then/else and loop control around macros' missing native conditionals — operator-stepped, not real branching**
*when:* Before assuming a macro needs true branching/looping and reaching for Lua — these two factory-verified idioms cover the two most common cases (repeat-until-operator-stops, and a real yes/no gate) without leaving macro-CLI syntax


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


### macro-entry-helper-mechanisms
**Macro entry-helper mechanisms: Execute=No, inline (), AddToCmdline, and the MA2→MA3 Rosetta mapping**
*when:* Before building a macro that needs to pause for operator input or assemble a command interactively — or before porting an MA2 macro (@ syntax) to MA3


Two distinct entry-helper mechanisms, plus the cell that pairs with them, plus the MA2 translation:

**1. `Execute=No`** stages the line's command on the live command line and waits for the operator to hit Please/Enter — the primary entry-helper mechanism (official v2.4 QSG; factory example `help context sensitive.xml` is built this way).

**2. Inline empty `()`** opens a value-entry text-input-field popup at that spot in the command. Officially documented (`extended_command_line.html`, "Use Parentheses () to open the Text Input Field"): the text INSIDE the parens is the prompt label (shown in the field's title bar after "Please enter"); the operator's entry replaces the parens and is processed. Quoted text `("x")` = string type; unquoted numeric `(x)` = number type; free text with no matching keyword = string. Worked example: `Fixture (the FID of the fixture)` → prompts "Please enter the FID of the fixture" → operator enters `5` → selects Fixture 5. The manual states this is "especially useful for creating macros." (Originally forum-discovered and flagged live-unconfirmed; CONFIRMED by this official doc passage the same session.)

**3. `AddToCmdline` macro-line cell:** `Yes` appends that line's command to EXISTING command-line content rather than replacing/firing it — pairs with `Execute=No` to assemble a multi-part command for the operator to finish (official `macros.html`, "Elements in a Macro").

**MA2→MA3 Rosetta** (forum 5563 + `macros.html` + `extended_command_line.html`):
- MA2 `@` at END of a macro line = MA3 `Execute=No`
- MA2 `@` at START of a macro line = MA3 `AddToCmdline=Yes`
- MA2 macro input pop-ups = MA3 inline `()` text-input field

History: created 2026-07-17 from the macro deep-dive session; folds together the initial Execute=No/() discovery with its same-session official-doc confirmation.


### macro-handle-persistent-object-reference
**Handles #[Object] — persistent object reference that survives rename/renumber**
*when:* Before hard-coding an object reference inside a macro that might get renamed or renumbered later — Handles are the survives-renumber alternative


`#[Object]` creates a **Handle** — a persistent reference to that object that keeps resolving correctly even after the object is renamed or renumbered (unlike a bare number/name reference, which breaks).

**Command editor "Create Handle" toggle** auto-converts the last object reference typed into a Handle.

**Multi-object handle refs** need the object keyword repeated per number — there's **no `Thru`-range shorthand** for handles (unlike a normal reference, where `Fixture 1 Thru 10` works fine).

**File-side (XML) form, added 2026-07-19:** in stored macro XML, Handles appear as raw hex references (`#000000027e001379`-style). This form is **show-specific** — imported into a different show, these hex refs dangle or resolve to the wrong object. Any port of a macro containing Handle references must replace every `#...` line with explicit `Group <n>` / object calls before it's safe to run elsewhere. This was THE key porting caveat for POSITION_WIZ (see `factory-position-wiz-anatomy-and-porting`) and applies to any handle-bearing macro.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: added the XML/hex-ref serialization form and its show-specific porting caveat, found reading POSITION_WIZ.xml file-side.


### macro-ization-doctrine
**Macro-ization doctrine: anything done more than once on console becomes a macro; repeated chat-driven entry work becomes one Lua-triggered macro call instead of re-streaming long Lua/CLI each time**
*when:* Before repeating a console entry task a second time, or when deciding whether to build a reusable macro/plugin/script instead of streaming another one-off Lua/CLI block from chat


**Standing rule (Dave):** anything cLD does more than once on the console becomes a **MACRO** — built properly, with variables and conditionals, "the whole nine yards," not a quick hack.

**Why:** repeated entry work should become a macro **trigger fired from chat via one Lua call** — change the variables and run — instead of streaming a long Lua/CLI block from the chat every time the task recurs. This is a token/time economics call as much as a reliability one: one short trigger call beats re-authoring and re-sending the same long payload repeatedly.

**Same rule extends to tooling generally:** scripts and plugins should be built as reusable tooling **wherever repetition appears** along the way — don't wait for a dedicated "build a tool" moment; catch repetition as it happens and macro/script/plugin-ize it on the spot.

Cross-reference: `macro-line-syntax-and-batching-rule` for the mechanical Store/Set macro CLI syntax this doctrine builds on; `plugin-install-loop` for the install→run cycle when the reusable unit is a plugin rather than a bare macro.

History: created 2026-07-17 from Dave's dictated standing rule, paraphrased per the project's dictation-capture house style (meaning preserved, coined shorthands kept verbatim: "MACRO-IZATION," "the whole nine yards").


### macro-library-file-lane-and-bulk-authoring-workaround
**Macro library file location + import CLI; bulk-authoring workaround (build one, export, edit XML, reimport) since the macro XML schema itself is still uncracked**
*when:* Before importing a macro library, locating macro XML files on disk, or trying to bulk-author many macros at once


**File location — CORRECTED 2026-07-19, version-scoped:** `gma3_2.4.2/shared/resource/lib_macros/` (207 XML files) — one macro per XML file. This is also where MA's factory/predefined macros live (e.g. `help context sensitive.xml`). The path is versioned per install; an earlier note recorded it as `grandma3/shared/resource/lib_macros`, which was imprecise.

**Import CLI:** `ChangeDestination Macro` (or `CD Macro`) → `Import Library "*.xml"` → `ChangeDestination Root`. The wildcard imports every XML file in the targeted library folder. **Correction to older forum assumption:** the DataPool path segment is the pool's ACTUAL name (e.g. `"Default"` in a fresh show) — it is not always literally `"Global"` as older forum posts assumed.

**Bulk-authoring workaround (MA staff-confirmed):** build one macro by hand, export it, edit the XML directly (search/replace), reimport. Same lane already proven for preset/sequence XML authoring (see `xml-file-side-authoring-import-lane-proven`). **Update 2026-07-19: the macro XML schema is no longer uncracked** — it fell out file-side from 13 of these 207 factory files, no console export needed. See `macro-xml-schema-cracked` for the schema itself; this closes the open item forum thread 5283 flagged.

History: first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: version-scoped path correction (207 files, from `grandma3/...` to `gma3_2.4.2/...`) and the schema-cracked resolution folded in (see `macro-xml-schema-cracked`).


### macro-line-syntax-and-batching-rule
**Macro Store/Set syntax, and where semicolon batching does (and does not) work**
*when:* Before generating grandMA3 macro lines, or before writing multi-command CLI sequences — the batching rule differs between macro lines and interactive CLI


**Macro line syntax:** `Store Macro X.Y` then `Set Macro X.Y "command" "text"`.

**One command per macro line — this rule still holds, unchanged:** semicolons between `Set MAtricks` (and other) property commands do **NOT** batch inside a macro line; each command must be its own macro line. This was the original 2026-04-01 rule and remains true.

**Refinement (verified live, onPC 2.4.2.2, 2026-07-04):** the no-batching behavior is specific to **macro-line authoring**. **Interactive CLI entry DOES support `;` to batch distinct commands** — verified live on 2.4.2.2. The two contexts are genuinely different:
- Macro line: one command per line, no semicolon batching, ever.
- Interactive/live CLI: `;` batches distinct commands.
- In **both** contexts, `Set <obj>` property chains stay semicolon-free internally (i.e. don't put semicolons inside a single `Set` command's property list).

Also unchanged: **MAtricks recall MUST be a separate macro line from Group/Preset** — do not combine them on one line.

**Gotcha when a batched command pops a dialog:** if one of the `;`-batched commands in interactive CLI triggers a blocking dialog (e.g. an `Assign Layout` Merge/Overwrite prompt), the remainder of the line is not dropped — it suspends and resumes once the dialog is resolved, even on Cancel. See `dialog-suspend-resume-batched-lines`.

**Factory short-form option keywords (noted, NOT adopted) — 2026-07-19:** shipped factory macros use `/NoConfirm` (short form) and `cd` (shorthand for `ChangeDestination`), plus quoted symbol tokens for Align modes (e.g. `Align "><"` for butterfly). These are valid MA-shipped short forms, recorded here verbatim for reference — but our own SaveShow standing rule keeps the long `/NoConfirmation` form (see `saveshow-discipline-and-mcp-tier`), and that rule is unchanged by seeing the short form in factory content.

History: originally stated (2026-04-01) as a blanket "no semicolon batching" rule for MA3 generally. Scoped 2026-07-04 after live verification on 2.4.2.2: the rule is macro-line-specific; interactive CLI entry does batch with `;`. The macro-line rule itself did not change. Flagged-not-resolved 2026-07-17: a 2021 forum report describes semicolon-separated commands working as one synchronous unit within a SINGLE macro line, on an older pre-2.2 build. This does **NOT** supersede the rule above — Dave's live verification on 2.4.2.2 (2026-07-04) stands as current truth. The 2021 thread is recorded here as historical context only, not as a correction (behavior may genuinely have changed across builds, or the old report may describe a different mechanism — unconfirmed either way). Extended 2026-07-19: factory short-form option-keyword usage (`/NoConfirm`, `cd`, quoted Align tokens) noted verbatim, explicitly not adopted.


### macro-lua-label-race-needs-wait
**⛔ A macro Lua line that CONSUMES names minted by earlier Cmd lines in the same macro needs a Wait — the Cmd queue and the Lua object tree are not synchronous (attested 14/19, fixed at Wait 0.50)**
*when:* Before writing any macro whose later line looks objects up BY NAME that an earlier line in the same macro created or relabelled — without a Wait the name snapshot is taken too early and the misses are silent and partial


**The race, exactly.** Macro line 1 mints four MAtricks twins and labels them (via `Cmd` lines). Macro line 2 is Lua that repoints recipe lines, looking its targets up **by name**. On the maiden run line 2's **name snapshot caught three of the four fresh labels but not the fourth** — so **14 of 19** repoints landed and the **5 lines targeting that fourth object were silently skipped**. Razor thin: **the `Cmd` queue and the Lua object tree do not settle in lockstep.**

**The failure shape is the dangerous part:** no error, no dialog, a partial success with a plausible count. Only the verification sweep ("still-broken = 0") caught it.

**The fix:** a **`Wait` between the lines** — the macro XML was patched from `Wait 0.00` to **`Wait 0.50`** and re-imported, and the pool artifact is future-proof. (Use the macro-line `Wait` column — the first of the three unrelated "wait" mechanisms, see `macro-wait-and-delay-keyword-disambiguation`.)

**General law:** **name-consuming Lua never immediately follows name-producing `Cmd` in the same macro.** Either interpose a `Wait`, or split the work into two macros, or resolve by handle captured at creation time rather than by name lookup afterwards.

**And always verify by count.** The five stragglers were finished by direct call after the run. A macro that reports a count is worth more than one that reports success — this one Printf's its counts for exactly that reason.

**Relation:** `macro-wait-and-delay-keyword-disambiguation` · `matricks-property-clear-encoding` (the Copy-carries-the-name behaviour that makes the label step necessary at all) · `venue-adapt-macro-pattern` (the artifact this fixed) · `many-lines-ride-macros-not-lua`.

History: none — found on the maiden run, root-caused and patched the same session, 2026-08-28.


### macro-manual-gap-and-study-doc
**06_Macros.md manual gap inventory + MACROS_STUDY_v0.1 closes it; corrects MA2-carryover 'Trigger type' drift**
*when:* Before hunting the repo manual for macro documentation, or before trusting a repo-manual macro-CLI claim (e.g. a 'Trigger' line type) as current — cross-check MACROS_STUDY_v0.1 first


**Repo manual gap inventory:** `06_Macros.md` is stubbed for Overview / Editor / CommandDelay / Echo / Conditional-If — only the Variables section and the v2.4-updates section are real content.

**Specific drift caught:** the manual's §2 stub outline lists macro-line cell types as "Command/Wait/Trigger" — **there is no "Trigger" macro-line type in MA3.** Macro rows are uniform command rows with exactly five cells: `Command` / `Wait` / `Enabled` / `AddToCmdline` / `Execute` (official `macros.html`, "Elements in a Macro"). The "Trigger" listing is MA2 carryover — flagged as repo manual drift, fix on backfill.

**Resolution:** all five stub topics (Overview, Editor/line-cells, CommandDelay, Echo, Conditionals) are now fully answered from the official manual in `MACROS_STUDY_v0.1`. No console-only verification remains for the stubbed content. **Update 2026-07-19: the one item this concept originally left open — exporting a real macro to crack the macro XML schema — is now closed too, and without needing a console export at all.** The schema fell out file-side from 13 factory `lib_macros` samples; see `macro-xml-schema-cracked`.

This joins the running manual-gap list alongside `measure-layer-math` (Measure) and `at-filters-worlds-manual-gap-and-study-doc` (If/At/Filters/Worlds).

History: created 2026-07-17 from the macro deep-dive session. Extended 2026-07-19: noted the schema-cracked resolution (see `macro-xml-schema-cracked`), closing this concept's own last open item.


### macro-phaser-at-layer-edit-grammar-reference
**At-layer phaser edit grammar has factory file-side ground truth (flyout phaser.xml): Step n / Attribute "X" At Transition/Phase/Width as macro lines**
*when:* Before writing or verifying macro-line syntax that edits a phaser's layer attributes (Transition/Phase/Width/Speed/NShot) — factory content proves the At-layer grammar works as macro lines, a known-good reference before spending console time


MA's own `flyout phaser.xml` builds an entire flyout phaser from 15 macro lines using the `At <layer>` edit-mode grammar — direct factory ground truth that this grammar works as plain macro-line `Command` text, not just as live CLI entry:

```
Step 2
Attribute "Dimmer" At Transition 15
At Phase 0 Thru 360
At Width 50
...
```

`Step n` moves to a phaser step; `Attribute "X"` selects the attribute being edited; `At <LayerName> <value>` (or `<value> Thru <value>` for a spread) sets that layer directly, chainable across successive lines without re-stating the attribute each time.

**Why this matters:** it's a known-good reference for the same `At <layer>` family used live at the CLI (`Measure` is one member of this family — see `phaser-layer-cli-grammar-measure-keyword`) — specifically for the **Transition/Phase/Width** layers here, and by extension the sibling **Speed/NShot** layers, all now provable from factory content before any console time is spent verifying them live.

History: none — captured 2026-07-19, read file-side from factory `lib_macros` content.


### macro-scratch-slot-idiom-generalizes-to-any-pool
**MA's shipped RemOff / World Is Selection macros both use the same delete→store→use→delete scratch-slot idiom — generalizes to any pool type**
*when:* Before writing a macro that needs a disposable temp object (a scratch Group, World, or similar) — MA's own factory macros establish the idiom


MA's own shipped **"RemOff"** and **"World Is Selection"** example macros both implement the same scratch-slot idiom, applied to two different pool types:

`delete temp object /NoConfirmation` → `store` → `use` → `delete again`

RemOff applies this to a **Group**; World Is Selection applies it to a **World**. Since the idiom is identical across two different pool types, it generalizes: any pool type can use a disposable numbered slot the same way — delete first (clean slate, no confirmation prompt), store into it, use it, then delete it again to leave no trace.

(Distinct from `preset-copy-label-mcp-and-century-scratch-slots`, which is about cLD's own century-numbered scratch-slot ALLOCATION for presets — this concept is about the delete/store/use/delete IDIOM itself, as demonstrated in MA's shipped macros.)

**Confirmed 2026-07-19 on a third pool type:** the factory `circular copy x plus.xml` macro uses `Selection 1`/`Selection 2` pool objects as scratch slots inside its self-referential Go-loop (see `macro-control-structure-workaround-idioms`) — Group and World were the first two pool types observed using this idiom; Selection is the third, exactly as this concept predicted.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: third pool type (Selection) confirmed via the factory circular-copy Go-loop macro.


### macro-wait-and-delay-keyword-disambiguation
**Three distinct 'wait' keywords in MA3 (macro-line Wait, /Wait option, CommandDelay) — don't conflate; macro-line Wait='Go' is a third pacing mode**
*when:* Before writing or reading ANY 'wait'/'delay' keyword in MA3 — macro-line Wait column, the /Wait option keyword, and CommandDelay are three unrelated mechanisms with overlapping names


**Three distinct "wait" keywords — do not conflate:**
1. **Macro-line `Wait` column** — pacing between lines within a macro.
2. **`/Wait` option keyword** — latency in milliseconds for `Store`/`Reboot`/`Restart`/`Shutdown`.
3. **`CommandDelay`** — delay before a cue's own embedded CMD line fires on playback.

A fourth, unrelated same-named term: the plain **`Delay`** keyword is a completely different, fixture-attribute fade-delay concept — don't fold it into the "wait" family above.

**Macro-line `Wait` column has three pacing modes** (official `macros.html`; Dave corroborated from live console knowledge):
- **Numeric seconds value** — waits that many seconds before the next line.
- **`Follow`** — effectively wait 0 (falls straight through).
- **`Wait="Go"`** — halts the macro after that row until it receives a new Go+; re-firing the macro steps it forward exactly one line. [CONFIRMED official + Dave operator]

History: none — first captured 2026-07-17, macro deep-dive session.


### macro-xml-schema-cracked
**Macro XML schema cracked file-side from 13 factory samples: GMA3→Macro→MacroLine, Command/Wait/AddToCmdline/Execute, DataVersion 0.0.175.0–2.1.1.5 all import clean at 2.4.2**
*when:* Before hand-authoring or generating any macro XML file, or before trusting/rejecting an old-dialect macro file based on its DataVersion — QUOTE DIALECT IS LOAD-BEARING: read this before writing a single Command= attribute with an embedded quote


**The schema (cracked file-side, no console export needed):**

```xml
<?xml version="1.0" encoding="UTF-8"?>          <!-- UTF-8 BOM present -->
<GMA3 DataVersion="1.4.52.4">
    <Macro Name="World is Selection" Guid="...">   <!-- Guid OPTIONAL -->
        <MacroLine Command="Delete World 999 /NoConfirm" />
        <MacroLine Command="Store World 999" />
        <MacroLine Command="World 999" />
    </Macro>
</GMA3>
```

Root is `GMA3` + `DataVersion` — the same envelope every other export dialect uses (sequence, preset, patch) — **NOT** `<UserPlugin>` (plugins only, see `plugin-xml-schema`). `Macro` takes `Name` (required) and an OPTIONAL `Guid`. `MacroLine` attributes seen in the wild: `Command` (always present), `Wait="Go"`, `AddToCmdline="Yes"`, `Execute="No"`, plus an optional per-line `Guid`. **Absent attribute = default** (Execute=Yes, AddToCmdline=No, Wait=follow) — GUIDs are optional at both the Macro and MacroLine level (oldest factory files have none, newest have both), consistent with the proven GUID-strip→fresh-GUID import lane (see `xml-file-side-authoring-import-lane-proven`). **Inner quotes must be XML-escaped: `Command="Set Selection 1 MAtricks &quot;XShift&quot; &quot;-1&quot;"`.**

**⛔ FAILURE MODE — the `&quot;`-escaping rule above is LOAD-BEARING, not cosmetic (paid for hard, 2026-07-23 [0723cLD]):** a **raw double-quote character inside a single-quoted `Command` attribute is XML-legal and parses fine in Python** — and the import even **echoes OK** — but **MA3's own IMPORT silently truncates the Command string at the first raw quote**. Observed: `Command='Label Group 60 "cLD BACKLIGHT ALL"'` landed on console as the bare fragment `['Label]` — everything after the first raw `"` vanished. **Symptom signature:** truncated `Label`/`Store`-type fragments execute as stray standalone tokens (e.g. `[Illegal object:Fixture 'Store']`); groups get stored unlabeled or with default names, preset-store lines silently no-op. **Import always echoes OK regardless of the truncation — only a post-import LINE-READBACK DIFF (console Command strings vs. the authored file) or the Command Line History audit trail (see `console-cli-feedback-channels`) catches it; screen echo alone will not.** **Doctrine lint addition:** any authored macro XML needs an explicit quote-dialect check — double-quoted `Command` attrs, `&quot;`-escaped inner quotes, zero raw double-quote characters inside a single-quoted attribute — as a check distinct from structural/schema validation.

**Proven workaround idiom:** prefer inline `Store <Object> <n> "Name"` over a follow-up `Label` line — `Label` lines are exactly the line type this bug hits hardest. Full idiom (including its use outside the XML-quote context): `store-with-inline-name-labels-object-idiom`.

**Retrieval-miss lesson (2026-07-23):** this exact escaping fact already lived in this file's body (above) before a session hit the truncation bug — twice, in the same night. The miss was **not missing knowledge, it was missing retrieval**: this concept's INDEX line never surfaced the word "quote," so a mid-session task-type shift (desk-work → macro-authoring) never re-armed on it. See `authoring-gate-doctrine-retrieval-miss-lesson` for the standing process fix this drove. This is also the direct reason this concept's index line was rewritten to carry explicit quote/escaping trigger words — see the librarian's STAGING_REPORT for the proposed line.

**DataVersion range:** shipping factory files span **0.0.175.0 → 2.1.1.5** — a decade of dialect vintages — and all still import cleanly at 2.4.2. Old macro DataVersions are safe to import.

**Optional `DependencyExport` child:** macro XML can embed a `DependencyExport` block the same way sequence exports do (seen on POSITION_WIZ, which carries its "Red Back" Appearance this way — see `factory-position-wiz-anatomy-and-porting`).

**[VERIFY]** `Enabled` never appears in any of the 13 sampled files — presumed default-omitted like the other attributes, but this is not yet confirmed against a real console export (MACRO_LIB_CATALOG_v0.1.md §6 open item). Also **[VERIFY]**: both cLD-authored goldens referenced in the 2026-07-23 smith proof runs use a `MacroLine Name` attribute (e.g. `Name="CONFIRM GATE"`) not documented in this schema write-up — confirm whether `Name` is a real, meaningful `MacroLine` attribute or cosmetic, and fold it in.

**cLD MAker consequence:** the macro export dialect is now specifiable — same GMA3 envelope, a trivial line model — closing cLD MAker's remaining export-lane gap in principle (generation is unblocked whenever it's picked up).

Catalog + worked fixture: `MACRO_LIB_CATALOG_v0.1.md` (full write-up); `generated/factory_macro_fixture_circular_copy_x_plus.xml` (sample fixture). Closes the open item flagged in `macro-manual-gap-and-study-doc` and `macro-library-file-lane-and-bulk-authoring-workaround` — see both for what was true before the schema was cracked.

History: none — schema cracked and captured whole 2026-07-19, from 13 factory `lib_macros` files read file-side (no console export required). Extended 2026-07-23 [0723cLD]: added the ⛔ FAILURE MODE (raw-quote silent-truncation-on-import, symptom signature, catch lanes), the proven inline-Store-name idiom, the retrieval-miss lesson that drove this index-line rewrite, and a [VERIFY] flag on the undocumented `MacroLine Name` attribute.


### many-lines-ride-macros-not-lua
**Dave's method law: 'easier to execute by macro or script than lua lua lua' — many-line desk batches ship as re-runnable MACRO artifacts, and recipe fields ARE assignable by macro line (the Assign lane)**
*when:* When a batch of desk writes is about to be issued as a chain of individual Lua calls — if the batch will ever repeat, it should be born as a macro artifact instead


**Dave, verbatim:** *"easier to execute by macro or script than lua lua lua."*

**The law:** a many-line desk batch is delivered as a **desk-native, re-runnable artifact** — a macro (or a script that writes one) — not as a chain of individual bridge calls. Two reasons, both proven on tour:

1. **Dave can re-fire it himself**, on any file, without cLD or a wire. `cLD MASTERS TX` re-ran the entire masters treatment on a fresh file lineage from one press.
2. **A chain of calls leaves nothing behind.** The batch that ran as Lua exists only in a session log; the batch that ran as a macro exists in the pool and in `gma3_library/datapools/macros/` as an XML.

**Corollary — the Assign lane (Dave's note, same ruling):** **recipe fields (`Preset`, and the rest) ARE assignable by macro line.** This matters because recipe *line creation* is not wire-reachable at all (`recipe-line-creation-not-wire-reachable`) — the macro lane reaches further into the recipe layer than raw Lua does, which is a second reason to prefer it.

**Where the boundary sits.** Bulk *analysis* still goes export + Mac-side python (`export-plus-python-bulk-lane`) — the macro lane is for **writes that repeat**, not for questions. A useful split: **questions → export+python · repeated writes → macro · one-off targeted writes → per-sequence Lua calls.**

**Macro artifacts must report counts, not success** (`macro-lua-label-race-needs-wait`), and must be import-verified after landing (`import-file-argument-must-be-quoted`, `plugin-import-verify-name-match`).

**Relation:** `macro-ization-doctrine` · `venue-adapt-macro-pattern` (the kit this law produced) · `recipe-line-creation-not-wire-reachable` · `export-plus-python-bulk-lane` · `macro-library-file-lane-and-bulk-authoring-workaround`.

History: none — ruled 2026-08-27 and applied for the remainder of the leg.


### store-with-inline-name-labels-object-idiom
**Store <ObjectType> <n> "Name" labels the object inline at creation time — a separate Label line is unnecessary in builders**
*when:* Before writing a builder macro/CLI sequence that creates an object (Group, Preset, etc.) and needs it labeled


**PROVEN IDIOM (re-proven, GROUP_BUILDER precedent):** `Store Group 60 "cLD BACKLIGHT ALL"` creates the object AND labels it in one command — a separate `Label` line is unnecessary in builders. This generalizes to other storable object types using the same `Store <Type> <n> "<Name>"` inline-name form.

**Corroborating evidence:** in the same session's v0.1.2 partial re-fire (a macro otherwise mangled by the quote-truncation bug — see `macro-xml-schema-cracked`), the quote-free `Store` lines using this idiom executed correctly even inside the damaged macro — `G61` export-verified with members `{55,57,58}`, Size=3, confirming the inline-name idiom itself is not what the quote bug breaks; it's specifically raw double-quotes inside XML `Command` attributes that break on import.

**Caution:** when this idiom is authored inside macro **XML** (not typed live at the CLI), the embedded quotes around the name MUST use the `&quot;`-entity escaping documented in `macro-xml-schema-cracked` — a raw double-quote in the XML `Command` attribute truncates the command silently on import. The idiom itself is sound; the transport (live CLI vs. authored XML) determines how the quotes must be written.

History: none — captured 2026-07-23 [0723cLD] digest run.


### tourshow-position-wiz-blind-depth-grade-root-cause
**Blind depth-grade root cause: a 1-wide Thru selection degenerates Grid Rotate's spread to uniform tilt — depth grading needs a real 2D grid group**
*when:* Before running POSITION_WIZ's (or any Grid-Rotate-based) Blind/depth-grade block against a selection — a plain Thru range across one truss row will NOT depth-grade; only a true 2D grid selection will


**Root cause (live-confirmed):** a plain `Fixture A Thru B` selection auto-fills as a **1-wide grid strip** (single X row, see `grid-cursor-cli-recipe-for-2d-group-layouts`). Running `Grid 'Rotate' 'Right'` against a 1-wide selection makes a width-1 column — there's nothing for the subsequent `Tilt` `Thru` spread to distribute across, so it collapses to one uniform value instead of grading. This is exactly what happened on cLD POSITION WIZ's whole-rig run (see `cld-position-wiz-generic-v01-authored-and-deployed`): the DS-row run (already effectively 1D) worked fine, but the whole-rig Blind block produced no depth grade.

**Depth grading REQUIRES a selection carrying a real 2D grid.** MA's own demo groups have grids baked in already; {TOUR}'s category groups don't yet (as of this session).

**The fix:** build each category as a proper **12×4 2D grid group** (one row per truss position: DS/MS1/MS2/US) via the already-proven `Grid X/Y` + `Fixture Thru` one-paste recipe (see `grid-cursor-cli-recipe-for-2d-group-layouts`). This is exactly what `tourshow-group-contract-v01`'s per-category ALL groups (x01, the 28×4 frame) are built to provide — its own "Consequences" note ties the two together directly: whole-category POSITION WIZ runs against the x01 groups should produce real depth-graded Blind, DS→US.

**[INFERRED, verify at desk] Mechanism detail for WHY Grid Rotate produces this specific effect:** `Thru` spreads distribute along grid X. Rotating 90° via `Grid 'Rotate' 'Right'` reassigns which stage axis a subsequent spread walks — turning a left-to-right Pan-style spread into a front-to-back (DS→US) Tilt spread, i.e. depth-graded tilt, uniform per row. In POSITION_WIZ's Blind block specifically, Pan is fanned BEFORE the rotate and Tilt is spread AFTER it — two perpendicular spread axes composed into one look. This explanation is consistent with everything observed live (rotate itself confirmed running; the degeneracy on a 1-wide selection matches the theory) but the exact axis-reassignment mechanics haven't been isolated at the desk yet. Dave's "Next" framing (stepping through the grid) is believed to walk the same grid-X mechanism, unconfirmed.

**Consequence for cLD's own macro:** run the Blind block only against full-category 2D grid groups (12×4, all 4 truss rows) — per-row/per-truss runs are fine for everything else in the wizard, just not Blind.

History: none — root cause diagnosed live 2026-07-19 from the whole-rig POSITION WIZ run's failure mode; fix designed the same session as the geometric justification for `tourshow-group-contract-v01`'s per-category frame shape.


### uservariable-cli-and-lua-surface
**UserVariable surface (P1, settled): CLI Set/Get/DeleteUserVariable typing trap + Lua GetVar/SetVar zero-not-nil gotcha + macro $ recall grammar**
*when:* Before reading or writing a UserVariable from CLI or generated Lua, or before recalling a variable's value inline inside a macro command line — typing (INTEGER vs TEXT), missing-variable behavior, and $ vs $"" recall all have gotchas


**CLI side:**
- `SetUserVariable` / `GetUserVariable` (supports wildcards `*`) / `DeleteUserVariable`.
- **Typing trap:** `SetUserVariable X 9` stores an **INTEGER**; `SetUserVariable X "9"` stores **TEXT** — these differ in subsequent math. (Source: manual 06_Macros.)
- **Object-property capture (added 2026-07-19, factory-verified):** `SetUserVariable "Name" At <Object> Property "PropName"` captures a console object's property value straight into a variable without touching Lua — e.g. `SetUserVariable "CurrentCueNumber" At Cue Property "No"` (factory `current cue number to user_variable.xml`). Paired lifecycle idiom (factory `off page 1 thru 10 - current page.xml`): `SetUserVariable` → use inline as `$VarName` (see the macro $ recall grammar below) → `DeleteUserVariable` cleanup, three lines total.

**Lua side:**
- `GetVar(UserVars(), 'name')` / `SetVar(UserVars(), 'name', value)`.
- **Live-proven, onPC 2.4.2.2:** a missing/unset variable returns **ZERO values, not `nil`**.
- Bare `tostring()` on that return **errors "value expected"** — wrap in parens to normalize: `tostring((GetVar(UserVars(),'name')))`.

**Macro $ recall grammar (third access surface, not in repo manual or previously pinned here):**
- `$VarName` substitutes as a raw command fragment (parsed as tokens).
- `$"VarName"` substitutes as one literal quoted string.
- Using the wrong form breaks the command. (Source: official manual, `macro_variables.html`.)

All three sides are recorded together because they always load together for UserVariable work — same underlying storage, three different access surfaces (CLI Set/Get, Lua GetVar/SetVar, macro-line $ recall).

History: none — first-observed/settled, live, 2026-07-05. Extended 2026-07-17: macro $ recall grammar added from official manual (macro deep-dive session). Extended 2026-07-19: added the `At <Object> Property` capture form and its paired set→use→delete lifecycle idiom, both from factory macro content.


### venue-adapt-macro-pattern
**The venue-adaptation kit: mint-if-missing + repoint as a TWO-LINE MACRO, its exact reverse as a twin, the masters treatment as a third — hand surgery at the first venue, one tap by the last**
*when:* When the same desk surgery is about to be performed at a second venue — that is the moment it becomes a macro pair, not the fourth time; also the reference for what a re-runnable adaptation artifact must contain


## The arc

The same adaptation was performed four times in one week. Venue one was **hand surgery over the wire**. Venue four was **one macro tap**. The kit that closed that gap:

| Macro | Job |
|---|---|
| `cLD MASTERS TX` | the masters migration sweep — one Lua line wrapping the generalised repoint, Printf reports the count. Re-fireable on **any future file**. |
| `cLD MX 1CELL` | two lines: **mint-if-missing** the flat twins (sources looked up **by name**, not slot) + **repoint** the known cell-geometry lines, per-sequence maps, plate and tube families scoped, Printf counts. |
| `cLD MX RESTORE` | the **exact reverse**, per-sequence so same-target ambiguity resolves. |

## What makes an adaptation artifact trustworthy

- **Mint-if-missing, by name.** Slot contents differ between file lineages; a source that exists in one fork may be absent in another and have to be minted from a different parent. Name lookup plus mint-if-missing survives both.
- **Per-sequence maps in both directions.** Several sources collapse onto one twin, so the reverse is only exact if it is written per sequence.
- **Printf the counts.** A macro that reports "14" when the map says 19 is what caught the label race (`macro-lua-label-race-needs-wait`); a macro that only reports success would have shipped a partial adaptation.
- **A `Wait` between a name-producing line and a name-consuming one.** Learned the hard way on the maiden run; the pool artifact is patched and future-proof.
- **XMLs live in `gma3_library/datapools/macros/`** and are staged import-ready before the file that needs them exists. Import with quoted filenames (`import-file-argument-must-be-quoted`).

## The decision tree the kit serves

When a new venue's plot lands:

- **1-cell strobes/blinders** → tap `MX 1CELL`, done.
- **Real multicell matching the build number** → the file needs **nothing**.
- **Different multicell count** (e.g. 14-cell plates) → mint block twins at the new number and repoint, per `mx-cell-geometry-law`.
- **Odd counts** → census first (`selection-count-probe`), then the same doctrine.
- **Masters treatment** inherits from the base file in any fork; re-fire `MASTERS TX` if the lineage predates it.

**Dave's method law behind all of it:** many-line desk batches ride better as **macro or script artifacts** than as long Lua chains — deliver desk-native and re-runnable wherever a batch repeats (`many-lines-ride-macros-not-lua`).

**Relation:** `mx-cell-geometry-law` · `many-lines-ride-macros-not-lua` · `macro-lua-label-race-needs-wait` · `venue-position-crowning-and-shell` (the position half of the kit) · `macro-ization-doctrine` · `import-file-argument-must-be-quoted`.

History: none — assembled across the last week of the EU leg, 2026-08-26 → 2026-08-28, and proven on its maiden run at the final show.


## METHOD & VERIFICATION

### at-menu-is-at-filter-menu-reading ⚠ VERIFY
**'At menu' in Dave's dictated curriculum ≈ the At Filter menu (long-press control-bar filter icon; At key flashes on a non-All filter) — pending Dave confirm**
*when:* Before assuming what Dave means by 'At menu' in dictated curriculum/notes — this is a working interpretation, not yet confirmed with him


**Working interpretation:** "At menu," as referenced in Dave's dictated curriculum, is almost certainly the **At Filter menu** — opened by a long-press on the control-bar filter icon, which pops a temporary At Filter window. The **At key flashes** when a non-`All` filter is currently selected/called, giving a visual tell for filter state.

**[VERIFY — pending Dave confirm]:** this reading has not been confirmed with Dave directly. Do not treat it as settled until he ratifies it.

Cross-reference: `at-filters-worlds-manual-gap-and-study-doc` — this interpretation came out of the same study session, prompted by the repo manual's thin coverage of At.

History: created 2026-07-17; status `verify`, explicitly flagged pending Dave's confirmation.


### clean-authoring-and-persistence-doctrine
**Clean-authoring / persistence doctrine — CORRECTED 2026-07-21: the template show is a durable KEEPER we build upon; 'wipe/rebuild fresh' was a ONE-TIME inherited-work reset, not a per-song/per-session law**
*when:* Before designing a generation tool (e.g. cLD MAker) that produces console objects, before starting a new song's programming session, or when weighing whether overlapping recipe/hard-value layers are a real runtime risk in Dave's actual programming practice


**CORRECTED 2026-07-21 (Dave) — we do NOT wipe and rebuild everything fresh every time.** The **TEMPLATE SHOW** (the spine plus all accumulated programming on it) is a **durable KEEPER** that programming sessions **build upon**, reusing all prior programming wherever possible. The earlier "fresh slate" framing (see the ORIGINAL claim, preserved below) described a **ONE-TIME start-of-run reset** — clearing INHERITED previous-programmer work ({FESTIVAL} / {FESTIVAL} artifacts) at the very start of this rebuild — not a per-song or per-session rebuild law. This resolves a rebuild-vs-keeper contradiction an external review (Codex) flagged directly against the original wording. **KEEPER wins:** treat prior sessions' sequences, cues, recipes, groups, and presets as durable work to extend, not scratch to discard.

**Programming-time precedence doctrine (Dave) — unaffected by the correction above:** at real programming time, sequences are authored deliberately. There is no runtime mystery about which value takes precedence, because ambiguous overlapping layers are never deliberately created in the first place. `recipe-output-precedence-and-cooking-doctrine`'s flowchart is a GUARDRAIL — so a generation tool doesn't accidentally emit conflicting layers — not a resolution problem anyone is at the mercy of during a show.

**cLD MAker design consequence (revised):** the app assumes the template show (patch + layout + accumulated prior programming) already exists as the stable substrate, and generates NEW content onto it each pass — it does **not** assume everything downstream of patch/layout gets discarded on every run. Reframes external reviewers' "which value wins" anxiety as a non-issue: values are authored deliberately by a human/tool that isn't creating the ambiguity, not resolved at runtime by the console.

**Relation:** `cld-maker-identity-rename-and-scope` for where this doctrine landed in the spec pack. `recipe-output-precedence-and-cooking-doctrine` for the flowchart this doctrine reframes.

**ORIGINAL claim (2026-07-17) — SUPERSEDED IN-BODY 2026-07-21, kept for history, do not act on this paragraph:** "At real programming, everything gets WIPED and rebuilt FRESH — sequences, cues, recipes, groups, presets are all disposable — EXCEPT the PATCH and the LAYOUT, which persist as the stable substrate across a rebuild. Test sequences (e.g. Seq 102) and their exports are scratch, deleted after use once their extracted SCHEMA has been captured." This overstated a one-time inherited-work reset as a standing per-session law — see the correction at the top of this file.

History: created 2026-07-17 from Dave's dictated standing doctrine, paraphrased per house dictation-capture style — stated the same session as the Export Sequence/Timecode captures and applied directly to the cLD MAker spec-pack meld. **CORRECTED 2026-07-21 [0721-3cLD]:** Dave clarified the "wipe/rebuild fresh" framing was a one-time inherited-work reset (clearing {FESTIVAL}/{FESTIVAL} artifacts at run start), not a per-song/session law; the template show is a durable KEEPER built upon across sessions — resolves a rebuild-vs-keeper contradiction Codex flagged in external review. Original wording preserved above verbatim, marked superseded, not deleted, per gardener rule. Any other doc still stating the old "wipe/rebuild fresh except patch+layout" framing (SONG_BUILD_SPEC, MEMORY) is flagged here for a cLD audit pass — out of the librarian's write scope.


### compose-at-bind-time-principle
**Keep orthogonal layers separate and compose them at recall/bind time — never pre-multiply combinations into objects (the architecture landed on this four independent times)**
*when:* Before creating any new set of console objects — presets, phasers, positions, groups. If the set's size is the PRODUCT of two independent axes, you are pre-multiplying and should be composing instead.


**The rule: when two properties vary independently, store them as separate objects and let the
recall or the bind multiply them. Do not author the cross-product.**

This was not designed up front. The architecture arrived at it **four times independently** in
a single session, which is what promotes it from a convenience to a principle.

| Instance | Axis A | Axis B | Composed at |
|---|---|---|---|
| The recipe contract | **Group** (who) | **Preset** (what) | the cue-part recipe line |
| Phaser / spatial split | **phaser preset** (the temporal figure) | **MAtricks** (spatial distribution) | the sequence recipe line |
| Position system | **universal TILT ladder** (7) | **selective PAN set** (4) | preset recall — presets stack |
| Fixture portability | **GROUP** absorbs the rig | **PRESET** absorbs the fixture type | `/Universal` resolution |

## Why it pays

**Object count collapses from a product to a sum.** 7 tilts × 4 pans = 28 positions from
**11 objects**. A phaser template set only has to vary in TIME (figure, direction, measure)
because MAtricks carries the spatial layer — so the phaser set stays small AND the MAtricks set
stays small, instead of one exploding to cover the other.

**Portability comes free.** A pre-multiplied object has both axes baked in, so a rig change
invalidates the whole cross-product. Composed layers let one axis change while the other holds
— which is exactly why `recipe-layer-is-fixture-agnostic-doctrine` works, and why a rig
shrinking hits the FILL layer instead of the CONTENT layer.

**Editing stays local.** Change one MAtricks and every recipe bound to it moves; change one
tilt and every position built on it moves. A pre-multiplied set needs N edits.

## The deliberate exception — and why it does not break the rule

`tourshow-authoring-contract-v01` rules **one phaser preset PER USE-SITE**: copy the template
rather than share a reference, so a single cue's figure can be tuned without touching the
others. That is DRY at **authoring** time (one template set to copy from) and copies at **use**
time. **Compose the axes; duplicate the instances.** The two are not in conflict — the
composition rule is about not authoring cross-products, not about forbidding copies.

## The smell test

If you are about to create a set of objects whose SIZE is the product of two things that vary
independently, stop — you are pre-multiplying. Find the bind point that could multiply them
instead.

History: none — synthesised 2026-07-28 after the same shape appeared in four unrelated rulings
in one session (recipe contract, phaser/MAtricks split, tilt×pan positions, fixture-agnostic
portability).


### design-lock-vs-build-evidence-authority-precedence
**When a design lock and the shipped build disagree, ask which one has more INFORMATION behind it, not which one is older — a lock is a hypothesis with a date on it, the build is evidence**
*when:* Before flagging a build's output as 'drift' from a written design lock/ruling — check whether the lock predates evidence the build was made with; the newer, more-informed artifact may be the one that should update the rule


**Standing lesson, generalises well beyond the colour case it was paid for on:** when a design lock and the shipped output disagree, **ask which one has more INFORMATION behind it, not which one is older.**

**The paid-for instance:** a per-song colour census was flagged as "drift" from a written palette-lock rule (the rule said retune a small fixed set of global anchor presets; the build had instead grown many more per-song presets). The lock was written off an early transcription; the output was built against ten songs of real screen content. Reading "output != lock" as drift was wrong — it was **LEARNING**. See `tourshow-palette-and-groove-v2` for the concrete colour-authority ruling this produced.

**The general rule: a lock is a hypothesis with a date on it; the build is evidence.** When they disagree, the newer artifact built with more real information is the one that should usually win — the older document should be updated to match, not the other way around.

**This is the INVERSE failure to the dropped-review-sheet lesson** (`tourshow-cue-century-review-sheet-doctrine`): there, an existing PRACTICE should have held and got dropped in error. Here, an existing RULE should have moved and was instead defended as though the build were violating it. Both are failures of not re-checking a standing artifact's currency at the moment it collides with new information — one where the old thing was right and got abandoned, one where the old thing was wrong and got defended.

**Relation:** `tourshow-palette-and-groove-v2` (the concrete colour-authority ruling this lesson produced). `tourshow-cue-century-review-sheet-doctrine` (the inverse-shaped failure this lesson is explicitly paired against).


### device-file-hunt-full-sweep-law
**DEVICE HUNT LAW (Dave): hunt files with ONE comprehensive sweep from the top of the allowed roots — never serial single-path probes off remembered paths, because mounts and repo roots drift between sessions**
*when:* Before looking for any repo/project file on the device from a fresh session — especially INBOX, wraps, staging folders — and immediately if a remembered path 'doesn't exist'


**Dave's teach, paraphrased:** when hunting for a file on the device, run **one comprehensive sweep from the top of the space** — search the allowed roots — rather than a string of single-path probes off paths remembered from a previous session. **Mounts and repo roots drift between sessions**; a remembered path that fails tells you nothing about whether the file exists.

**The failure this prevents:** filing into a stale copy. Ground truth established the same day —

- **live INBOX = `My Drive/Documents/MA_PROGRAMMING/WORKING/findings/INBOX.md`**
- `cld_maker_sandbox/REVIEW/corpus/findings/INBOX.md` is a **2026-07-21 snapshot, STALE — never file there.**

A serial probe would have found the stale copy first and written to it silently.

**Compounding hazard:** the same directories are Drive-synced, where list tools already false-negative and staged copies can read stale — see `glob-false-negative-on-drive-synced-dirs`. A full sweep plus a live `ls`/`grep` cross-check is the pair that gets to truth.

**Relation:** `glob-false-negative-on-drive-synced-dirs` · `project-file-locations` · `empty-census-deserves-selector-suspicion`.

History: none — taught and applied 2026-08-08.


### executable-per-song-contract-doctrine
**Executable, closed per-song contract doctrine (Codex ADOPT): zero pick-at-desk; verify via a vertical-slice audition (SET + hardest cue + one gesture) before fanning out; a circuit-breaker gate re-fires the review whenever a silent failure or workaround occurs**
*when:* Before treating a song's idea-file/build package as 'done' and ready for desk import — check it against the closed-contract + vertical-slice + circuit-breaker tests below first


**The big idea (Codex, ADOPTED by Dave):** the SONG_G first-pass miss wasn't a lack-of-knowledge problem — it was a lack of an **EXECUTABLE, CLOSED per-song contract**. A build package is not ready for desk time unless it requires **zero "pick at desk"** decisions — every WHO/WHAT/HOW/level choice is already resolved in the authored deliverable, so console time really is pure translation (see `idea-file-design-programmer-boundary-doctrine`). This diagnoses the SONG_G miss more precisely than "the doctrine wasn't loaded" — the doctrine WAS loaded (`recipe-lane-end-to-end-verified`, `v24-phaser-model`) and still didn't get applied, because nothing forced the plan to be a closed, checkable artifact before programming started.

**VERTICAL SLICE + AUDITION (Codex sharpening):** before fanning a build out to every cue, build and fire a minimal vertical slice first — **SET cue + the hardest cue + one representative gesture** — and audition it on the desk. **A clean IMPORT is not the same as programming success**; only firing and looking at the slice proves the contract actually translates to a good look. This generalizes `review-plan-gate-precedes-programming-doctrine`'s "plan for the hardest moment first" heuristic into a concrete verification step.

**AUDITION TUNE-BACK (Codex sharpening):** because the build is a clean-rebuild-onto-a-keeper (see `clean-authoring-and-persistence-doctrine`), any desk edits made during the audition must **round-trip back into the authored contract** — a look tuned live at the desk and never folded back into the source deliverable is a look that will be lost or contradicted on the next rebuild.

**CIRCUIT BREAKER (Codex sharpening — names the real SONG_G failure mode):** the gate must **RE-FIRE mid-session** after ANY silent failure or workaround — this is what actually derailed the SONG_G first pass: one hard blocker (the `ColorAdd` silent-empty-preset trap, see `baked-phaser-preset-xml-schema`) tunneled the session into "just make it import" mode, and the review→plan gate never re-triggered to pull it back out. A circuit breaker means: the moment a workaround gets improvised to get past a blocker, STOP and re-run the review/plan check before continuing, rather than letting "just make it work" become the session's new mode.

**Scope caution (Dave, same session):** take the THINKING from this review, not a 4-document hash-ceremony — keep the actual process to a 2-page plan + checklist. The point is a closed, verifiable contract, not more paperwork.

**Relation:** `review-plan-gate-precedes-programming-doctrine` — the original, narrower "load doctrine before programming" gate this review sharpens into a testable contract + circuit breaker. `idea-file-design-programmer-boundary-doctrine` — the idea-file this contract is the executable, closed version of. `external-cross-vendor-review-lane-pattern` — the review mechanism (Codex clean-room) that produced this finding.

History: none — Codex review run and ADOPT decision made in one session, 2026-07-21 [0721-3cLD]; full review at `cld_maker_sandbox/REVIEW/FINDINGS_LOCAL.md`.


### idea-file-design-programmer-boundary-doctrine
**The idea-file is the ONLY handoff between design and programming: design-side knows music/story/programming-concepts and writes the idea; the programmer is a pure translator carrying the full mechanical toolkit but zero aesthetic judgment — ratified as 'deliverable-at-the-boundary'**
*when:* Before starting any song's programming session, or when unsure whether a decision belongs on the design side or the programming side of the pipeline


**STAR PRINCIPLE (Dave, 2026-07-21 [0721-3cLD]) — separate the pipeline by WHAT EACH SIDE KNOWS; the idea-file is the ONLY handoff:**

- **BEFORE programming (design/concept side):** knows the music/beatgrid, the story, what good lighting looks like, AND the programming CONCEPTS (device vocabulary, recipe story, groups=WHO, grid=time-map, functional/flavor). Does **NOT** know console mechanics. Produces exactly one thing: **the IDEA, in a file**, written in programming-concept language.
- **AT programming (the PROGRAMMER = pure translator):** knows only how to take that idea-file and render it into the console (macro/XML/CLI). Does **NOT** know beatgrid, does **NOT** know "what good lighting looks like," and **decides nothing**. It renders.
- **The file is the entire boundary/contract.**

**CLARIFICATION (Dave, same session) — "almost nothing" was imprecise:** the programmer does **NOT** carry "almost nothing." It carries the **FULL MECHANICAL TOOLKIT**: everything figured out how to DO — connect/get inside the console, review the show file, export, import, CLI + MCP syntax, SaveShow + console-killer safety rules. **ALL** of that rides along, every session. What it does **NOT** carry is the **DESIGN hall** — music/beatgrid, aesthetics, "what good looks like," theory, strategy. Split: **MECHANICS/HOW-TO → programmer side; WHAT/WHY/DESIGN → before side.** The idea-file is written in design-side programming-CONCEPT language; the programmer renders it with the mechanical toolkit alone.

**DESIGN/BUILD framing this rides alongside (same session):** DESIGN = decide the look (creative, human/cLD); BUILD = construct it (deterministic → macro/XML/skill). Because programming builds UPON the durable template show (see `clean-authoring-and-persistence-doctrine`), builds must be **re-runnable** — i.e. mechanized. The deterministic BUILD column is exactly the skill/macro backlog.

**Ratified as standing doctrine, 2026-07-22 [0722-2cLD] — "deliverable-at-the-boundary":** the programming step = receive the design file → **author EVERYTHING off-console as a deliverable** (builder-macro XML / import file), using concept lookups to structure it → **desk time is import + verify only.** Dave: this is the step he'd been hunting for days. **Corollary:** timecode is explicitly NOT part of the content-import step — TC is the LAST step, its own dedicated desk session (at minimum for song #1). Spec: `WORKING/SONG_BUILD_SPEC_v0.1.md`.

**Test for every future build:** does it make THIS simpler? If a proposed process step doesn't clarify or protect the design/programmer knowledge split above, it's probably the wrong complexity.

**Relation:** `review-plan-gate-precedes-programming-doctrine` for the concrete REVIEW→PLAN procedure this boundary doctrine implies at the design side. `executable-per-song-contract-doctrine` for the sharpened, externally-reviewed version of what a "complete" idea-file needs to guarantee. `cld-maker-identity-rename-and-scope` — cLD MAker is explicitly a BEFORE-side (design-side) tool, not the programmer.

History: none — STAR PRINCIPLE and its clarification stated in one session, 2026-07-21 [0721-3cLD], as the session's closing reframe. Ratified into standing "deliverable-at-the-boundary" doctrine the next session, 2026-07-22 [0722-2cLD], with the TC-is-last-step corollary and the SONG_BUILD_SPEC pointer.


### old-song-g-artifacts-desk-cleanup-doctrine
**Old SONG_G build artifacts (Macros 6-8, [0721-2cLD] cLD SONG_G/SLIDE POP sequences) traced as the false-alarm source behind a doctrine-compliance audit — ruled for deletion, SaveShow checkpoint first, step 0 of SONG_E Session A**
*when:* Before auditing console state for doctrine-compliance symptoms (global-colors/plain-sequences), or before starting the next desk session's Session A runbook


**RECORD STRAIGHTENED (Dave):** an audit finding of "global colors / plain sequences" on the console traced to OLD programming still resident — builder Macros 6-8 from the failed [0721-2cLD] SONG_G first pass (days colors / days sequences / days SLIDE POP) — NOT the new SONG_E deliverables. Dave reviewed the new binding table + build: on doctrine. The separate `/Universal` store-scope catch (see `universal-presets-emitter-aware`) stands as real regardless of this false alarm — both findings are kept, the false-alarm diagnosis does not undo the real one.

**DESK CLEANUP RULING (Dave):** the old SONG_G artifacts GO — Macros 6/7/8 (days colors, days sequences, days slide-pop) plus the [0721-2cLD] "cLD SONG_G" / "cLD SLIDE POP" sequences if still resident. Execute at the next desk session; **SaveShow checkpoint before the deletes**; this is step 0 of the SONG_E Session A runbook.

Relation: `saveshow-discipline-and-mcp-tier` for the checkpoint mechanics; `universal-presets-emitter-aware` for the still-standing separate lesson this record-straightening does not erase.

History: none — captured 2026-07-23 [0722-2cLD] digest run.


### operators-eyes-are-the-census-of-record
**OPERATOR'S-EYES LAW: for desk state, Dave's eyes are the census of record — instruments confirm afterwards. Three eyes-beat-instruments events in one tour, each catching a class of truth no scan could reach.**
*when:* When a scan reports clean and the operator says something is wrong — believe the operator and go find which class of truth the instrument was blind to; also before claiming a state is verified on instrument evidence alone


## The law

**For desk state, the operator's eyes are the census of record.** Instruments — exports, greps, reference scans, command echoes — are how a finding gets *confirmed and quantified*, not how it gets *found*.

## The three events, each a different blind spot

1. **Echoes lied.** Thirteen clean `OK` responses against a `.show` file nine hours stale. Dave saw "not saved up." The instrument reporting success was the thing that was wrong (`saveshow-enumerate-headless-cancel-class`) — and the ritual that came out of it is *disk-verify every save* (`save-disk-verify-mtime-delta`).
2. **The plan was mechanically right and semantically wrong.** A consolidation sweep executed perfectly — counts exact, zero dangling refs — and snapped the show to stale base looks, because the *content* of the survivors was not what the tour wore. No count could have caught it (`color-consolidation-crowning`).
3. **The scan was pattern-blind.** A grep for colour references inside phasers matched only `Preset 4.x` text; a GUID cross-reference later showed phasers never bound the colour pool by reference at all. What Dave actually saw was the phasers' **baked step content** owing the consolidation — invisible to *any* reference scan (`reference-scan-blind-spots-guid-and-baked-content`).

**By the third event the instruments concurred on every axis** — after being pointed at the right question by an eye.

## How to hold both

- **Never argue a clean scan against an operator report.** Ask which layer the scan could not see: echo vs disk, reference vs content, count vs semantics.
- **Then build the instrument that would have caught it** and re-run it. Each of the three events produced a permanent lane: the disk-verify ritual, the crowning order, the GUID + content-semantics scan rule.
- **Honesty is part of the law.** The pattern-blind grep was corrected in the log the same session, in public, with the method lesson attached. A finding that quietly becomes right is worth less than one that shows its correction.
- **State the scope with the count** (`state-the-scope-with-the-count`) — an unqualified number invites exactly this class of over-trust.

**Relation:** `saveshow-enumerate-headless-cancel-class` · `color-consolidation-crowning` · `reference-scan-blind-spots-guid-and-baked-content` · `probe-called-unreliable-is-not-evidence` · `state-the-scope-with-the-count` · `deferred-conclusion-is-not-a-held-conclusion`.

History: none — named after three events inside one day, 2026-08-19.


### pool-labeling-doctrine-inherited-risk
**Renaming stock pools for a show is fine — the risk is INHERITING a file where someone else already did it undocumented**
*when:* Before renaming a stock pool, or before trusting pool numbers/contents at face value in an inherited/handed-off show file


Dave's ruling: renaming a stock pool for a show is fine on its own — e.g. pool 22 → "Recipe Phasers" is a live candidate, still pending Dave's decision (see `NEXT_ACTIONS_A0716.1.md`, "pool-22 rename" under decisions pending Dave). The risk isn't renaming; it's **inheriting a file where a different programmer already renamed/customized pools without documenting it** — those custom pools become a dependency trap for whoever inherits the file next, since pool numbers/contents can no longer be trusted at face value.

This was the concrete trigger for the {TOUR} rebuild: the other-programmer custom pools found in the {FESTIVAL} predecessor file were what forced Dave's hand — "random pool creations don't travel."

**Extends `pool-discipline-stock-vs-custom`:** that concept's rule is "use stock unless a fantastic reason not to"; this finding sharpens *why* — not because renaming itself is risky, but because renaming without provenance is what breaks the next person's ability to trust the file.

History: none — doctrine stated 2026-07-16, prompted by the {FESTIVAL} file's custom pools.


### reconciliation-identity-per-song-verification-method
**Reconciliation identity: a per-song crosswalk QC shape stronger than a count census — every per-cue line-count difference must land on a NAMED cause**
*when:* Before trusting a crosswalked song's total line count as 'close enough,' or before building/reading a per-song QC/RECONCILE sheet — a count match alone is a weaker proof than accounting for every per-cue difference by name


**The reconciliation identity, exact and residual-free on SONG_J's 37 content cues:**

```
{LD} 245 − 1 HELD − 1 Position-on-QX40 law drop + 12 QX40-STB expansion + 2 JDC gate-openers = 257 cLD
```

**Every per-cue difference lands on one of those named causes.** This is a stronger check than a count census: it proves not just that the TOTALS agree, but that each INDIVIDUAL difference is explained. Reusable per song — a `RECONCILE` sheet tab is the shape to build for any crosswalked song.

**⚠ Forward-looking note:** the `+2 JDC gate-openers` term is scheduled to disappear from this identity on future songs — `master-default-doctrine` now retires the `JDC_OPENERS` emitter behavior (masters are never programmed; see that concept). Expect the identity's cause-list to shrink by one term on any song built after that change lands.

## Predecessor method (08-01): constraint-propagation bind census

Before the reconciliation identity was named, the same verification goal was reached a different way: a **constraint-propagation bind census** (global group -> selection function, plus per-cue multiset equality) proved 27/32 SONG_I cues **bind-for-bind** file-side, zero conflicts. Also **stronger than a count census**, and **reusable pre-import** on any crosswalk emit — a companion technique to the reconciliation identity, useful when a full named-cause accounting isn't yet built.

## Sheet-freshness rule: the cLD side of a QC sheet must be a FRESH desk pull, not the as-built export-back

**Paid-for lesson:** the 08-01 export-back for SONG_J went stale the moment Dave started cleaning at the desk. `Export Sequence 2010` taken live on 08-03 read **225 SRs against the shipped 257** — 34 line-instances removed, 2 changed by hand. **A sheet built off the as-built file describes a console that no longer exists.** Standing rule: pull the sequence fresh at sheet-build time, and keep the as-built export as its own separate tab so the chain **{LD} -> as-built -> now** stays readable and each stage stays honest about its own age.

## Process rule: corrections found during a reconciliation pass are DEFERRED, not fixed in place

**RULED (Dave):** corrections surfaced by a reconciliation/QC pass are **deferred to an end-of-build circle-back**, not fixed during the run. Breadcrumbs + method get logged as they are found. Landed as `TOURSHOW_CORRECTIONS_LEDGER_v0.1.md` (WORKING root) — as of this backlog, 11 entries, each with exact sites and the method, so the circle-back is **execution, not rediscovery**. Anything found during a build run gets **APPENDED** to that ledger rather than fixed in place — the whole point of the rule is that a run session makes no correction decisions of its own.

## Reconciliation vocabulary pinned — `Enabled`, not `Active`, 2026-08-05 [0805cLD]

**{LD}'s recipe lines carry TWO enable-ish attributes — pin which one a "live SR" count
means.** `Enabled` reads Yes on all 109 of SONG_L's lines; `Active` reads Yes on only 21,
No on 88. **"109 live SRs" = the `Enabled=Yes` / direct-child count, NOT `Active=Yes`.** The
one HELD line (Follow Spots, cue 1) is itself `Active="No"` — the same state as 87 lines that
WERE carried into the build — so `Active` is not a hold criterion at all. **Pin the vocabulary
to `Enabled=Yes` / direct-child count**, so a future reconciliation pass doesn't re-derive this
from scratch. See `tourshow-seq2210-song-l-build-record` for the identity this vocabulary
was pinned on (`{LD} 109 − 1 HELD = 108 cLD`).

**Relation:** `tourshow-recipe-line-redundancy-taxonomy` (the duplicate/redundancy classes a reconciliation pass will surface). `tourshow-cue-century-review-sheet-doctrine` (the sibling per-song review artifact — that one is for TASTE verification, this one is for crosswalk-completeness verification; they are different sheets serving different checks). `tourshow-seq2010-song-j-build-record` (the song this identity and its evidence were first proven on).


### replay-portable-strobe-doctrine
**Build strobe as a shutter open/closed chase effect for replay-portability — native fixture strobe only when genuinely fast**
*when:* Before building a strobe-style look — decide whether a portable two-state chase effect serves better than the fixture's native strobe function


Dave's standing preference for strobe-style looks: build the effect as a two-state chase — shutter OPEN / shutter CLOSED — rather than reaching for a fixture's native strobe function by default.

Why: an effect built this way is **replay-portable**, both show-to-show and type-to-type. The same chase concept carries from one rig or tour to the next, and from one fixture type to another, because it's built from generic shutter states rather than a specific fixture's strobe implementation.

Known ceiling: the two-state chase is bounded by DMX refresh rate, so it cannot reach the very fast flicker speeds a fixture's native strobe function can hit. When a look genuinely needs that kind of speed, native fixture strobe is still the right tool — this is a default preference, not an absolute ban on native strobe.

The actual win isn't raw speed, it's musical timing control: building strobe as a chase means it inherits the console's chase/phaser timing machinery, so it can be driven to quarter-note taps and other musically precise placements — something a fixture's built-in strobe rate doesn't give you.

This doctrine is general — it isn't tied to {TOUR}'s specific rig, and should apply to any future rig with strobing fixtures.

History: none — dictated live 2026-07-15; the concrete application is `worked-strobe-figure-tap-tap-kill`.


### source-profile-inheritance-and-reuse-doctrine
**Land {TOUR} content in {LD}'s ({FESTIVAL}) pool slots to inherit his profile's view/button bindings for free; import his functional macros/plugins rather than rebuild; his skill ceiling is the floor, not the target**
*when:* Before choosing which pool slots to build {TOUR} song content into, or before deciding whether to rebuild vs. import a source-authored macro/plugin


**PROFILE + SLOT-MIRROR DOCTRINE (Dave):** Dave is running a COPY of {LD}'s user profile (no show macros/plugins in it yet). RULE: land {TOUR}'s per-song content in {LD}'S pool slots — the profile's views/buttons already bind those addresses, so songs jump to the right screen spaces for free. Saves roughly 1 hour of layout config per setup. Dave's framing: "no reason to do it twice; they have an okay system." See `festival-slot-numbering-pattern-confirmed` for the confirmed slot formula (sequence base = 1000 + 100×(setlist_index−1)) this doctrine builds on.

**IMPORT-DON'T-REINVENT ruling (Dave):** {LD}'s show macros and song plugins are functional — grab and import them from the {FESTIVAL} AR file (a desk errand) rather than rebuild them from scratch.

**AMBITION DOCTRINE (Dave):** matching {LD}'s level is "junior college" — if that were the goal, the show would just load his file and go. His pool slots are plumbing to reuse; his CEILING is not the target. The {TOUR} spine (subfixture cells, 2D grid, cross-type groups, recipe system) exists specifically to go past whole-fixture dimmer/tilt effects — "university level." Do not equate {TOUR}'s style ambition with the reference show's basics; the reference is the floor, not the ceiling.

**Why this matters (→packet):** the specific {LD}/{FESTIVAL} pool-slot addresses {TOUR} content lands in, and which of his macros/plugins get imported, are show-operative facts that belong in the show packet once the import errand runs — not just in this doctrine concept.

History: none — captured 2026-07-23 [0722-2cLD] digest run.


### state-the-scope-with-the-count
**State the scope with the count — a bare number is not checkable, and the mistake shape recurs at every new count**
*when:* Before reporting, shipping, or acting on ANY headline count or workload number this project produces — recipe counts, figure counts, backlog/INBOX line counts, correction-surface counts. Read this before trusting your own first-pass tally, and before repeating a count you did not personally recompute.


**The discipline: state the scope with the count, always.** A bare number ("122", "47 figures", "~85 INBOX lines") is not checkable by anyone reading it later — what was counted, what was deliberately excluded, and why, has to travel with the number or the count silently rots into an unverifiable claim the moment a later session repeats it without rechecking.

**The same mistake shape recurs — it is not learned once, it needs re-applying at every new count.** This session alone produced two further self-caught instances (the source material labels the first of these its own **third instance** of the pattern, implying at least two earlier instances already exist in the corpus — not independently re-sourced by this run; see Relation):

1. **Same-name-reuse conflated with different-name-same-content.** v1 of the cross-song phaser figure-hash reported ONE cross-song number that silently mixed "{LD} reused one object under one name across songs" (not a discovery — already treated as one figure) with "DIFFERENT names, IDENTICAL content" (the actual finding). Caught by validating the output rather than just reporting it; v2 reports the two counts apart. See `tourshow-phaser-figure-duplication-across-songs`.
2. **Figure NAMES counted under a header that read as figure COUNT.** The batch prework's first run labelled a per-song header with the number of figure *names* while the header read as the number of distinct figures. {LD} gives one figure content several names per song, so a name-count overstates the mint workload every time (SONG_K's first pass showed 6 REUSE + 2 NEW against only 6 truly distinct figures). Caught pre-ship, before the CSVs were finalized.

**A third example the same session, same shape, different domain — bookkeeping, not a shipped artifact:** the INBOX backlog was carried forward session to session as "~85 lines" (per `CURRENT_STATE_A0803.1`) or "~55" (per the LOCK plan) — both undercounts, neither rechecked. An actual count of the file found **140** lines. Count the file; don't quote the last state file's estimate.

**A fourth instance, 2026-08-05 — the scope resolved an apparent contradiction rather than being the mistake itself.** SONG_L's gear counts: 23 phaser LINES sit across 20 cue PARTS. cLD first reported "Div2 x15" (the PARTS scope) and the phaser smith separately reported "Div2 x18" (the LINES scope, pre-ruling). **Both were correct at their own scope; neither was the other's error.** Speed Scale is a PART knob, so PARTS is the operative unit for a desk gear list — but the disagreement itself is a reminder that a count mismatch between two honest passes is often a scope disagreement, not a defect. See `tourshow-seq2210-song-l-build-record`.

**The rule, stated for reuse:** before shipping any count — in a findings doc, a CSV header, a state-file estimate, or a run report — state what was included, what was excluded, and whether the number was actually recomputed or just carried forward from the last time someone said it. State the scope alongside the count, every time, not just the first time it's derived.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (home of the first instance above) · `recipe-layer-is-fixture-agnostic-doctrine` (carries an earlier, 2026-07-27 count-correction — 105 vs. 50 live recipe lines — plausibly one of the earlier instances this session's material numbers itself against, though this run did not independently verify that specific cross-reference).


### tourshow-crosswalk-prework-alias-gap
**18-song crosswalk prework DONE — the SONG_T substitution map holds everywhere, but the other 17 bind a RENAMED group layer; a NAME-ALIAS extension + 3 rulings are owed before it's usable**
*when:* Before starting crosswalk work on any of the 18 remaining songs — the prework is done, where its tables live, what the NAME-ALIAS extension + 3 owed rulings are, and which songs (SONG_S, maybe SONG_R) are full-authors rather than crosswalk jobs


**Prework complete.** Tables and per-song detail live in **`SETLIST_CROSSWALK_PREP_v0.1.md`** (WORKING root) + **19 sheets** in `generated/crosswalk_prep/` — **load those for the actual data; this concept is the headline and pointer, not a duplicate of the tables.**

## Headline

The SONG_T substitution map (the crosswalk that closed SONG_T) **holds everywhere** — but the other 17 songs bind a **RENAMED group layer** that SONG_T didn't have to deal with:

- **JDC1 US/DS/SW** = the **old Strike M rows**, now pointing at **QX40** / groups `511`/`512`.
- **CL** = **PL, renamed** — ghost-group + phaser-binding proof on file.
- **Spots + Beam `[Sym]` combos** also need the renamed-layer treatment.

**A NAME-ALIAS extension (mapping the renamed layer back to the substitution map) closes an estimated 50-70% of currently-"unmapped" bindings without needing any new Dave rulings.**

## Genuinely-new rulings still owed (not closeable by aliasing alone)

- **Sym treatment** — how `[Sym]` combos resolve.
- **Beam-pool MM walls** — `RateFast`/`Open` 12-19-group walls, a pattern that repeats across the setlist.
- **Dimmer `'20'`/`'30'` slots.**

## SONG_R (2800) — status uncertain, needs a desk check

**SONG_R's main sequence is an EMPTY SKELETON:** 17 named cues, zero content, and no other SONG_R sequence appears anywhere in the TC exports. Needs a **console-side content check** — if there's genuinely nothing there, SONG_R joins SONG_S as a full-author song rather than a crosswalk job. (Separately, SONG_R's **aux-layer count is 0** per the per-song architecture decode — see `tourshow-fill-layer-rebuild-method` — consistent with either reading.)

## SONG_S builds LAST — the other full-author song

**SONG_S has no {LD} TC to retarget at all** — it's authored (song + timecode) entirely from scratch, and is scheduled as the **final slot** in the 19-song build order specifically because of that. The TC-authoring lane needed for it is already proven: cLD's SONG_G TC was hand-authored and imported clean, and the beatgrid `startSec` → `CmdEvent Time` bridge is banked (`tc-bump-button-architecture`, `export-timecode-tc-event-xml-schema`).

## Cross-song structural facts (confirmed across the 19-export scan)

- **Mono-part cues: the P1-P8 per-fixture-class part scheme is OURS**, not inherited.
- **`Note` attribute = BPM**, consistently.
- **Beat-locked fades** throughout (consistent with the SONG_T timing decode, `source-timing-is-the-tempo-grid`).
- **Phaser gears ÷1/÷2/÷4/÷8** appear in the defs across songs (see the speed decode in `tourshow-fill-layer-rebuild-method` for the mechanism).
- **`Active=No` on 70-89% of objects** — a cook-state artifact, not a meaningful flag.
- **`Strict` on MM marks**, consistently.
- **Hazard labels observed:** `U+221A JDC1 DS MM` · `'Guitar Swell '` (trailing space) · `'I I'`.

## Design-input pipeline

**COLORS FROM {DESIGNER}:** per-song color palettes come from {DESIGNER}'s simplified design handoff sheets; Dave is pulling them. This is the design-side input the 18 rebuilds are waiting on — the sheets carry per-song distinct-color-slot counts to author against.

**Relation:** `tourshow-fill-layer-rebuild-method` (the per-song build method this crosswalk feeds) · `inherited-file-membership-is-ground-truth` (why a renamed-but-truthful group layer is expected, not a surprise) · `tc-track-target-cutover` (the cutover mechanic each crosswalked song will use once its groups resolve).

History: none — prework completed and headline captured in one session, 2026-07-29.


## ⭐ WHOLE-SHOW CROSSWALK NOW EFFECTIVELY LOCKED 2026-08-03 [0803-1cLD] — 100% group coverage, zero unmapped

**All 18 {LD} song sequences run against the ratified submap, file-side, zero console contact: 2,636 sequence recipe lines across 384 cues — 100.0% of groups MAPPED, ZERO unmapped.** The crosswalk is effectively already locked at the group layer for the ENTIRE show, not just the 10 songs built so far — this is the fact that makes a "lock the crosswalk, then speed-run the remaining builds" plan viable rather than aspirational.

**Show-wide inventory, same pass:** 2,636 lines · 384 cues · 106 phaser figure uses · 17 distinct {LD} colours. Biggest colours by line count: Deep Saturated Blue 86 (8 songs) · Soft Desaturated Blue 63 (4) · Pastel Pink 33 (3) · Lite Blue 33 (2) · Saturated Pink 33 (2) · Neutral White 32 (6) · Lavender 32 (1). The Key CTB / Key White / Key CTO trio appears in 5-7 songs each at 1 line per song — these ride the HELD Follow Spots lane.

**Repo debt found by the same pass:** only 4 preset gaps exist show-wide, and **3 of them have been getting patched LOCALLY, per-song, instead of promoted into `cld_submap.PRESETS_FIXED`**: `Position.I I` (14 songs, 17 lines), `Position.Side Wash [Forte SW]` (17 songs, 17 lines), `Position.Stage Wash [VL3600 + Strike M SW]` (17 songs, 17 lines). Every build so far has carried these as a per-song local dict rather than a promoted fix — promote once, delete the local patches. (The 4th gap, `Position.Release Relative`, is not debt — it is the release-dialect exemplar, see `release-relative-universal-preset-exemplar-proven`.)

**Template-mapping precedent (Dave), keep separate templates for near-identical-looking source phasers:** {LD}'s `Dim_PWM` maps to **cLD WIPE IN** (`21.71`); `Dim_PWM_THIN` maps to **cLD TRAPEZE** (`21.56`). The two PWM variants deliberately map to DIFFERENT templates — plain PWM is a 50/50 square Dave reads as a travelling wipe ("it's a good look"), THIN is the sliver. **Do not collapse them into one template.**

## ⛔ RULED 2026-08-03 [0803-1cLD] — SONG_R is confirmed empty, and SONG_R + SONG_S are NOT full-authored from scratch after all; the crosswalk key for both is TIME, not groups

**SONG_R ({LD} 2800) is confirmed EMPTY: 0 cues, 0 recipe lines** (the export is a 6 KB stub) — this settles the "status uncertain, needs a desk check" open item above; either it was never programmed or the export didn't capture it, and Dave confirmed before it was counted as a build target.

**RULED (Dave) — SONG_R and SONG_S are NOT authored from scratch. Crosswalk a like song instead; the crosswalk key this time is TIME, not groups.** Method as planned: SONG_R keeps its own 17-cue NAMED skeleton ({LD}'s 2800 cue names, though contentless, ARE the section map) -> a donor song's content maps on by SECTION NAME -> then re-time everything to SONG_R's own target beatgrid, with fades regenerated from the target BPM, never copied as raw seconds. **SONG_S has no skeleton at all**, so it needs a donor AND an all-new cue spine — it remains the one genuinely new build in the setlist, now with a defined method (donor content + built spine) rather than pure invention. Donor selection for both is Dave's call, not yet made as of this backlog.


## SONG_S donor decision deferred, 2026-08-03 [0803-2cLD]

Dave picks the donor later. Source line does not elaborate what "donor" refers to beyond the deferral itself — flagged, not inferred further. **No change to run order:** SONG_S stays LAST (see "SONG_S builds LAST," above); no other work blocks on the deferred decision.


### tourshow-no-warehouse-day-previz-proof-lane
**RULED: there is NO warehouse day — MA3 3D previz run against timecode audio is the proof lane before first load-in, and JDC1 viz stays untrustworthy so the DMX viewer is readback truth**
*when:* Before scheduling, deferring, or gating ANY verification item to 'warehouse day' — that day does not exist on this tour's plan; also before trusting onPC visualization during a previz proof pass


**Dave's ruling, 2026-07-30: no warehouse day.** The tour goes straight to **first load-in**. The proof lane before that is **MA3 3D previz run against the timecode audio** — which is exactly how SONG_T and SONG_A were both confirmed, so the method is already exercised, not aspirational.

**This supersedes the show packet's "warehouse proof day, before 2026-07-31" milestone** and every verify item parked against it.

## What that re-homes

Items previously gated on warehouse day go to **previz where the answer is visible there, else load-in day**:

- ACME pixel-line **cell-convention verify** (FID->X direction, top/bottom colour rows) — `acme-pixel-line-ip-anatomy`
- JDC1 **ch8-vs-ch20 hardware gate** question — `jdc1-standing-order-plate-master-full`
- **Palette-lock** session and **fixture-colour pre-match** — `tourshow-warehouse-day-fixture-color-prematch`

## ⚠ The caveat that rides with the lane

**JDC1-class visualization is structurally untrustworthy** — its GDTF declares no relation for plate/beam master gating, so onPC cannot render the real gate chain in either direction (`jdc1-gdtf-no-gating-relations-root-cause`). During a previz proof, the **DMX viewer** — or the real unit at load-in — is the readback truth for any multi-instance output judgement. Previz proves timing, structure and the shape of a look; it does not prove JDC1 output.

**Consequence for every remaining build:** each song has to arrive *previz-provable* — TC track re-targeted and audio offset clean — because there is no physical rig between now and the first look.


### tourshow-songbuild-kit-and-runbook
**The per-song build line is a PROVEN kit, not a memory — generated/songbuild/ + SONG_BUILD_RUNBOOK_v0.1 regression-reproduce a shipped song byte-exact and drive every remaining build**
*when:* Before starting ANY remaining song's build — the kit and the runbook are the order of operations; also before hand-authoring anything the kit already emits, or before trusting a kit edit


After SONG_A went end to end, the mechanical half of the line was extracted into a kit so song #2 starts from tooling rather than recall.

## What exists

- **`generated/songbuild/cld_submap.py`** — the ratified {LD}->cLD map as data. **NAME-keyed**, because G-codes are assigned per prework sheet in order of use and differ per song; {LD}'s group NAMES are the stable join key. Also carries the dimmer ladder, position retargets, beam slots, the phaser template table, and the per-song numbering arithmetic.
- **`generated/songbuild/cld_songbuild.py`** — parse the prework sheet, read {LD}'s cue skeleton (carrying **every** fade attribute verbatim), `decode_phasers()` for the spec-read, emit sequence / aux / builder-macro XML, and a doctrine `lint()`.
- **`generated/songbuild/regress_ig.py`** — the proof.
- **`SONG_BUILD_RUNBOOK_v0.1.md`** (WORKING root) — the 9-step order of operations with the gated command chain and the ranked gotcha list.

## Why it is trustworthy: it is regression-proven, not merely written

`regress_ig.py` rebuilds SONG_A from the same inputs and **sha-matches all five artifacts that actually shipped to the console** (the 122-line main sequence and four aux sequences). **Re-run it after any kit edit — a kit that stops reproducing SONG_A is broken regardless of what it does on the new song.** This is the same discipline as diffing an authored artifact against a live golden, applied to the generator instead of the output.

## The scope limit is deliberate — keep it

The kit does the mechanical join. It does **NOT** pick phaser template classes, MAtricks binds, or speed gears; `decode_phasers()` hands over the spec (steps, baked speed as BPM, Measure, phase span, and whether rows are cell-level) and the call stays human. That boundary is `idea-file-design-programmer-boundary-doctrine` in tooling form: the mechanics ride along, the taste does not.

## First evidence it generalises

Dry-run against **SONG_B** (seq 1100, 212 live lines): **210/212 auto-resolvable**, one blocker (`All FX Color`, 2 lines, needs a ruling). Preset coverage complete after the dimmer ladder closed. **Dry-running the map before authoring anything is now step 1** — it costs two minutes and tells you exactly which rulings the song needs.

Relation: `tourshow-crosswalk-prework-alias-gap` (the prework the kit consumes) · `tourshow-seq1010-build-record` (the build it was extracted from) · `import-resolver-laws` (the laws its lint enforces).


## ns_emit.py: an XML-direct emit lane for a HUMAN-dialect prework sheet, no G-code section — 2026-07-31 [0731-3cLD]

**Prework sheets come in (at least) two dialects.** SONG_D's prework sheet is the
**HUMAN-dialect batch** (no G-code section) — unlike whatever prior sheet(s) carried a
G-code section for `parse_prework` to consume. For this dialect, **`ns_emit.py` builds
binds directly from `gb_s1300.xml`** ({LD}'s own export) under the **same live-SR parse
law** as the rest of the kit, rather than via the prework sheet's G-code section. Census
cross-checked **143 vs. sheet**, exact.

**Runbook note:** check which dialect a song's prework sheet is in **before** assuming
`parse_prework` consumes it — a G-code-section assumption will not hold for a HUMAN-dialect
sheet.

**Regression re-confirmed the same session:** after a 3-row submap patch, the SONG_A regression
(`regress_ig.py`) was re-run — **BYTE-EXACT 5/5** (main + 4 aux). The kit edit is proven
inert against the shipped golden, per this concept's standing "re-run after any kit edit"
discipline.


## Kit gotcha found 2026-08-01 [0801cLD] — asterisk-prefixed fixed-point values crash decode_phasers(), local guard in place ~~, permanent fix still owed~~ **FIXED, see 2026-08-05 note below**

**`gb_s1400.xml` (SONG_E) phaser embeds carry `*`-prefixed fixed-point values** (e.g. `Measure="*67108864"`) — the first file seen doing this. The kit's `decode_phasers()` crashes on a bare `int()` conversion when it hits one. **A local `lstrip('*')` guard was used to get through the session**, but this has not yet been promoted into the kit itself. ~~**Still owed: a permanent kit patch plus an SONG_A regression re-run** to confirm the fix doesn't disturb the byte-exact regression this concept's body describes.~~ **CORRECTED 2026-08-05 — the permanent fix is already in the kit; see below.**


## ⭐ SUBMAP DEBT PAID — L1 / LEDGER C7, 2026-08-03 [0803-2cLD]

**Root cause was subtler than a missing row.** All three Position presets flagged as ledger item C7 (`Position.I I`, `Position.Side Wash [Forte SW]`, `Position.Stage Wash [VL3600 + Strike M SW]`) were in `cld_submap.PRESETS_FIXED` **all along** — but keyed by the **prework-sheet ABBREVIATION** (`I_I`, `SideWashFSW`, `StageWashVL`), never by **{LD}'s FULL preset name**. The lookup missed silently every time a build resolved by full name, so every build patched the full names in **locally**, in a separate per-build dict, instead of hitting the shared fixed map. **A local patch applied N times is a missing row** — the map looked complete because each build quietly worked around the gap rather than failing loudly.

**Fix:** promoted all three full-name keys into `PRESETS_FIXED`; deleted `recipe_extract.LOCAL_PRESETS` (the per-build local patch dict) entirely. `PRESETS_FIXED` is now **29 rows**. SONG_A regression re-run after the patch: **BYTE-EXACT 5/5**, unchanged.

**Verified paid, not just patched:** a show-wide coverage re-run after the promotion found preset gaps drop **4 → 1**, and the one survivor (`Position.Release Relative`, SONG_H, 1 line) is not a gap needing a fix — it is the RELEASE EXEMPLAR (a Universal preset carrying `Relative="Specials:Release"`, bound by an ordinary StandardRecipe) that unblocks the STB (R) release work. Confirmed by the same script that originally found the debt.

**Relation:** `never-edit-the-golden-gate-behind-a-flag` (the sibling kit-integrity rule paid for the same session, same regression discipline) · `tourshow-stb-white-release-ruling` (the STB release work this submap fix unblocks).


## RUNBOOK v0.2 — per-song RUN LIST, ordered cheapest-first off the figure hash — 2026-08-03 [0803-2cLD]

**RUNBOOK v0.2 written, superseding v0.1** (`SONG_BUILD_RUNBOOK_v0.1.md`, referenced above under "What exists," is now superseded by v0.2). `NEXT_ACTIONS` was rewritten as the per-song RUN LIST (A0803.3), ordered **CHEAPEST-FIRST off the figure hash**:

SONG_N (0 new figures) → SONG_P (1) → SONG_K (1) → SONG_Q (2) → SONG_O (2, but 7 of the 9 remaining STB sites) → SONG_L (5) → SONG_M (5) → SONG_R/SONG_S last.

This front-loads the songs the figure hash made nearly free, so the first run session proves the line at low risk before spending effort on the expensive songs.

**LOCK EXIT CONTRACT met for everything not needing a console: 6 of 7 items closed, only L5 (mint the STB pair) needs the desk.**

**Relation:** `tourshow-stb-white-release-ruling` (L5, the STB pair this run list still owes the desk).

## Mark grid independently re-proves the submap promotion — 2026-08-03 [0803-2cLD]

The L7 Mark-cue position grid (`tourshow-mark-position-grid-flow-pass-signal`) re-proves the submap promotion (above, "SUBMAP DEBT PAID — L1 / LEDGER C7") works show-wide, independent of the SONG_A regression test: three preset names that would have printed blank now resolve to a cLD ref — `Side Wash [Forte SW]` (16 lines), `Stage Wash [VL3600 + Strike M SW]` (16), and `I I` (15) — **47 lines total** that previously printed `(no row)`.

**Relation:** `tourshow-mark-position-grid-flow-pass-signal` (the census this re-proof was read off).

## Kit gotcha found 2026-08-04 [0803-3cLD] — cld_songbuild.py:226 omits strict= on the phaser branch

**CONSTRAINING (G=0.7), scoped to a phaser targeting a wash: `cld_songbuild.py:226` omits
`strict=` on the phaser branch.** Same shape as the shared-path lesson already on file
(`parts-per-century-emit-pattern-and-et-gate`'s "protective transforms must live in the SHARED
emit path, not per-lane") — **patch the site locally until the shared path carries the fix.**
Still owed: promote the fix into the shared path and re-run the SONG_A regression, per this
concept's own "re-run after any kit edit" discipline.

## ⚑ STALE CORPUS NOTE CORRECTED 2026-08-05 [0805cLD] — the asterisk-prefix fix is already in the kit

The "still owed" note above (2026-08-01 gotcha) is **NO LONGER TRUE**. `cld_songbuild.py:106`
already carries `_fp = lambda v: int(re.sub(r'^[\\*\\?]', '', str(v)))`, handling `?` as well as
`*`. Confirmed against `gb_s2200.xml`, which carries **89,349** asterisk-prefixed attribute
values. No further action owed on this gotcha.

## Kit gotcha found 2026-08-05 [0805cLD] — `mx_of()` substring matching is a latent trap, patched

**Emitter fragility (smith F6): `mx_of()` dispatched on `'US' in sel`**, which also matches
`Forte US (Grid)` and `Strike M US [STB] (Lin)` — correct only by accident of the SONG_L
`Intro` figure having exactly three populations. **Replaced with exact population-name tests
that raise on anything unexpected.** Substring tests on {LD} group names are a latent trap;
use exact names and fail loud — same shape as the shared-path lesson already on file for the
`strict=` gotcha above.


### tourshow-two-pass-build-method
**RULED: the 19-song build is TWO PASSES — pass 1 crosswalks the background and deliberately EXCLUDES her-key/backlight (Groups 51, 60-64); pass 2 ('{ARTIST} time') overlays her afterward. The empty groups are not a gap.**
*when:* Before flagging any song's her-key (Group 51) or backlight (Groups 60-64) content as missing, or before deciding when to build {ARTIST}'s key/backlight layer — this is the ruled sequencing, not an oversight


**⭐⭐ STANDING METHOD, RULED (Dave). The 19-song build runs in TWO PASSES:**

- **Pass 1 = the crosswalk.** Paint the whole background — body and field content only. **EXCLUDE Groups 51 (her-key) and 60-64 (backlight) entirely.**
- **Pass 2 = "{ARTIST} time."** Overlay the main character for focus, once the background is fully painted. Dave, verbatim: *"pass 2 is {ARTIST} time, it's for focus with all the background painted, we overlay of main character."*

## This RETRACTS an earlier same-day finding

An earlier reading of the same evidence had been logged as a **"CROSS-SONG GAP"**: her-key (Group 51) and backlight (Groups 60-64) showing **ZERO content in all nine songs built so far**, read as an unused/undelivered architecture. **That framing is retracted.** The emptiness of Group 51 (and 60-64) across every song built under pass 1 is **deliberate sequencing, not an omission** — nothing crosswalks into those groups because {LD}'s file has no equivalent (51-54 and 55-60 are cLD's own re-FID carve-outs) and pass 1 is scoped to exclude them on purpose.

## The evidence that originally surfaced the question

A Creative-Director-side note ({COLORIST}, on a {FESTIVAL} still, filed `ARTIST_TOURSHOW_assets/SONG-J_where_is_artist_festival.png`): *"We really lost her at one point in the set, light wasn't illuminating her"* + *"She is on the SR stairs for part of this song."* The still shows {ARTIST} on the SR stairs, swallowed by a deep-blue field — exactly the failure `tourshow-her-key-and-backlight-doctrine` exists to prevent, now evidenced from a real show rather than only as design theory. This note is what pass 2 will answer, not evidence that pass 1 is broken.

**SONG_J's specific her-position input for pass 2 (→packet):** her position is known — **SR STAIRS** for part of the song. Per the backlight pick-logic that resolves to **Group 61 `cLD BL SR` {55,57,58}**, and the song body runs saturated cobalt throughout, so the "saturated key colour => white backlight ON" rule (`tourshow-her-key-and-backlight-doctrine`) fires hard here. (Separately, communicating the SR-stairs position to Follow Spot Ops is an advance/comms item, not console/show-file content.)

## Consequence

**No song's pass-1 build is "missing" her layer**, and **no retrofit sweep is owed** to any of the nine (now more) songs already built. Pass 2 becomes its **own future workstream**, undertaken only after the pass-1 background is closed across the setlist — and it is where the {FESTIVAL} "we lost her" note gets answered directly, with each song's her-position note (e.g. SONG_J = SR stairs) as its per-song input.

**Relation:** `tourshow-group-contract-v01` (the Group 51/60-64 numbering this method scopes). `tourshow-her-key-and-backlight-doctrine` (the design WHY this method eventually serves — design-role, summoned). `tourshow-seq2010-song-j-build-record` (the song whose her-position note is the first concrete pass-2 input on file).


### v24-migration-facts ⚠ VERIFY
**v2.4 facts from the manual (PSR/MVR flow, v2.3->v2.4 migration behavior) — unverified live at time of writing**
*when:* Before opening an old (pre-2.4) showfile on v2.4, or before using the new PSR/MVR import/export flow


These facts come from reading `MA_V2.4.2_MANUAL` and were **not yet live-verified on-console** at the time they were recorded (2026-07-02). Treat as banked-but-unconfirmed until checked against actual v2.4.2.2 behavior:

- MVR **import** moved into **Partial Show Read** (Menu → Show Creator); MVR **export** into the patch Export dialog; the old patch-menu buttons were removed.
- PSR matchmaking order: **FID → CID → GUID → Name**; partial property import (Patch / Position / Rotation individually); fixture types are exchangeable in Prepare.
- **PSR MVR import clears the programmer.** MA+ESC (or Shift+ESC) held 5 s cancels a running GDTF/MVR import.
- `Export Patch /MVR` works from the command line (outbound half is scriptable).
- v2.3→v2.4 migration: old-show load **wipes the programmer**; `IDType` Universal → Generic; "Auto" preset mode removed; Lua core **5.4.8**.

Related: `store-recall-recipe-toggle-rules` and `v24-phaser-model` cover the recipe/phaser side of v2.4 changes, live-verified 2026-07-04 (those are `status: active`, this file remains `status: verify` since the migration/PSR-specific claims here were not the ones tested that session).

History: none — status remains `verify`; would be confirmed by walking the PSR/MVR runbook (`WORKING/HOWTO_PSR_MVR_v0.1.md`) on-console and by loading an actual pre-2.4 showfile under 2.4.2.2.


## PATCH & RIG

### beam-not-strobe-terminology
**BEAM names the JDC1/ACME center element — 'strobe' names only the function run on it**
*when:* Before labeling a group, cue, or fixture element on JDC1 or ACME — or when tempted to call a center-row element 'strobe' instead of 'beam'


Dave's terminology ruling, dictated live and then explicitly widened mid-session: the center element on both JDC1 and ACME is named **BEAM**. "Strobe" is not the element's name — it's the name of the FUNCTION run on that element. A beam can be strobing or not; the hardware/grid-cell identity stays BEAM either way.

The ruling started on JDC1, where the naming was already correct in practice — Dave cited the group label "cLD JDC DS BEAM" as the existing model to follow. It was then extended explicitly to ACME: the pixel-line's center row is the same class of element and gets the same name.

Consequence: Group 126, the ACME center-row group, is currently labeled "cLD PIX DS STROBE" — under this ruling that label names the function instead of the element, the same mistake the JDC1-side naming had already avoided. It's flagged for relabeling; Dave hasn't yet given the exact replacement label or executed the change as of this run.

Practical rule going forward: any new group/cue label touching a center beam element should say BEAM, and "strobe" should only appear in a label when it's naming the strobing behavior itself (e.g., a cue that runs the strobe function), never as a stand-in for the element.

**⚠ Unresolved BEAM-vs-TUBE inconsistency (surfaced 2026-07-21, do NOT auto-resolve):** this ruling says the JDC1 center element is BEAM, but the naming is now genuinely split. Dave's own 2026-07-21 hand-built full-rig grid group is labeled "cLD(C) TUBES GRID" (group 435), and cLD's per-truss JDC center cell groups (442–445) stand as "… TUBE" to match Dave's latest — and `jdc1-anatomy-ground-truth` also calls them "tube segs." cLD first corrected those groups TUBE→BEAM per this ruling, then reverted to TUBE to match Dave's hand grids. Net split: the ACME/pixel side uses BEAM (335 "PIX BEAM GRID"), the JDC side currently uses TUBE (435 "TUBES GRID"). Left as-is pending Dave's reconciliation — he has not ruled which term wins for the JDC center. Do not auto-relabel either way.

History: none — dictated live 2026-07-15, extended from JDC1 to ACME within the same session. 2026-07-21: surfaced an unresolved BEAM-vs-TUBE naming split on the JDC center (Dave's hand grids + cLD's per-truss groups use TUBE); flagged for Dave, not auto-resolved.


### dmx-viewer-address-edit-calculator
**DMX viewer's Address field opens an Edit Address calculator popup (keypad + Please) to jump straight to a universe.channel**
*when:* Before manually scrolling a DMX viewer to find a specific universe/channel — use the Address field's calculator popup to jump straight there


**Verified live:** clicking the DMX viewer's **Address** field opens an **Edit Address** calculator popup — keypad clicks to enter the target address, confirmed with **Please**. Worked example: entering **202.320** jumped the viewer straight to the JDC block at that universe/channel, confirming the fixture's channel-map position (see `jdc1-anatomy-ground-truth` for the JDC1 SPix channel ranges this lines up against).

History: none — confirmed live in one session, 2026-07-15, while verifying the recipe build's cooked DMX output.


### export-diff-verification-loop
**Export-diff verification loop: compute an expected-positions table, then confirm it two independent ways (grandMA3 XML diff, MVR matrix parse) after every major geometry pass**
*when:* After any major batch of 3D-position writes, before trusting the rig is correct — this is the milestone-level check that sits above per-paste hygiene


**The method:** compute an expected-positions table ahead of time from the design math (not from the console's own state), then verify the console actually matches it by exporting and diffing — not by trusting the UI or a clean CLI echo. Two independent export lanes are available and were used redundantly this session:
1. **grandMA3 XML export**, diffed programmatically against the expected table (schema: `patch-xml-export-lane-and-schema`).
2. **MVR export**, parsed (position/rotation per fixture via its matrix encoding) and checked the same way (schema: `patch-mvr-export-import-lane-and-schema`).

Agreement across both lanes is the confidence signal — this is a genuine cross-check, not just running the same test twice, since the two export formats encode position/rotation differently (attribute-based vs. matrix-based).

**Applied twice this session as the template rig's geometry evolved:** the first pass confirmed **192/192 truss fixtures exact** via the grandMA3-XML diff, right after the initial alternating-hang cut. After the mirror-cut and a wing-JDC repair, a full MVR parse confirmed **all 256/256 overhead fixtures exact** — the final, fully-verified state (see `tourshow-template-rig-patch-and-layout-state`).

**This is the loop that catches phantom writes.** A 16-command wing-JDC position paste echoed clean in the CLI but had silently not landed — the census/diff step is what surfaced that, not the paste's own echo (see `paste-round-verification-protocol` for the per-paste-round discipline this loop sits above). The lesson generalizes: **census-diff after every batch is the law**, not an occasional sanity check.

**Ground-truth and export artifacts from this session:** `outputs/expected_positions.json` (the computed expected-positions table used as the diff target); exported/parsed patch files `showfiles/cld_patch_v1/v2.xml`, `cld_patch_v3/v4.mvr`, `cld_l2_final.xml`.

History: none — the two-lane loop was assembled and run twice live, 2026-07-14, verifying the template rig's 3D positions first at 192/192 and finally at 256/256.


### gridstore-keyword-and-fixture-type-write
**`GS` (GridStore) bakes the current selection-grid sub-layout INTO THE FIXTURE TYPE — every instance of that type inherits it on Down**
*when:* Before using GS to save a subfixture grid layout, or when deciding whether a layout needs to live on the fixture TYPE (GS) vs. a single Group (bake-at-Store) — see `gs-multifixture-recall-unreliable` before relying on GS for a multi-fixture build


**`GS` = short form of the `GridStore` keyword** (confirmed live, 2.4.2.2).

**What it does:** lay out subs on the selection grid (Grid-cursor moves + sub-range selections, per `grid-cursor-cli-recipe-for-2d-group-layouts` / `subfixture-thru-range-syntax`), then fire `GS`. A popup appears, verbatim:

> "Do you want to store the grid positions into the fixture type?" — OK / Cancel

Choosing OK writes the current programmer sub-layout **into the fixture TYPE itself**, not just the selected instances — every fixture of that type inherits the stored layout from then on.

**Propagation confirmed:** after `GS`, selecting the parent fixtures and expanding with `Down` (e.g. `Fixture 301 Thru 312 ; Down`) propagates the stored layout **tiled side-by-side per fixture** — worked example, 12 ACMEs (301–312) → 576 subs laid out as 12 blocks of 16 columns × 3 rows each (equivalently, 192 total columns × 3 rows).

**Typing caveat:** `ShCuts` (console keyboard shortcuts) must be **OFF** to type `GS` in the docked command line — otherwise the two letters risk being intercepted as a shortcut. The Edit Command popup lane is unaffected by this.

**Relationship to other layout-storage lanes:** GS writes to the fixture TYPE (all instances, always-on inheritance via Down). This is a different, stronger-reaching mechanism than baking a layout into a single Group at `Store` time (per-instance, only that Group) — see `grid-cursor-cli-recipe-for-2d-group-layouts`. **Before relying on GS for anything beyond a single fixture, read `gs-multifixture-recall-unreliable`** — multi-fixture Down-recall of a GS-stored layout is not always faithful.

**Not durable across a repatch (2026-07-21):** a GS type-bake does NOT survive a fixture-type repatch. The 2026-07-15 GS bake of the ACME 16-col × 3-row color/beam/color sandwich was **gone** in cLD_SANDBOX_v0.23 — probing `ClearAll ; Fixture 301 ; Down ; Store scratch ; Export` returned all 48 subs stacked at X=0,Y=0 (default parent-cell stacking), i.e. the type had reverted. Most likely the v11 repatch re-imported/reset the ACME FixtureType 4. **Consequence:** GS is not a durable carrier — build the layout FRESH via Grid-cursor baked into Groups (the reliable per-Group lane, see `gs-multifixture-recall-unreliable`). This is a second, independent reason — on top of nondeterministic multi-fixture recall — to prefer Groups over GS for anything that must persist.

History: none — GS keyword, popup text, and single-fixture-type propagation confirmed live in one session, 2026-07-15 (Dave's drill). Extended 2026-07-21: the 2026-07-15 type-bake was found wiped after the v11 repatch — GS bakes are not durable across a repatch.


### group-membership-follows-refid-not-number
**Group membership FOLLOWS a re-FID — groups bind the OBJECT, not the FID number (export-census confirmed 2.4.2.2); contrast with GS type-bakes, which do NOT survive repatch**
*when:* Before or after re-FIDing patched fixtures — to know whether existing group memberships need to be manually carved, and to distinguish this from GS-bake behavior


**CONSOLE FACT (export-census confirmed, 2.4.2.2):** group membership **FOLLOWS a re-FID**. Fixtures re-FIDed 130/131/139/141/144/146 → 55-60 REMAINED members of every group that owned them before the re-FID: G101 (60 fixtures incl. 55-60), G105 (57-60 present), G601 (316 fixtures incl. all six). **Groups bind the OBJECT, not the FID number.**

**Corollary:** after ANY re-FID, the moved fixtures do NOT automatically leave groups that logically no longer own them (e.g. a general "spot contract" group that a repositioned fixture no longer belongs in) — this has to be carved out manually.

**Applied (Dave's CARVE RULING, same session):** purge FID 55-60 from the FULL spot-contract block Groups 101-110 (ALL/rows/wings/halves) — since those six now belong to the her-key/backlight doctrine, not the general spot contract. Groups 601/602 were left as-is for now (the key-precedent carve was deliberately NOT extended to them — Dave's call). Mechanism: select the six fixtures, `Store Group <n> /Remove`, export-census verify each group afterward.

**Contrast — the opposite durability:** GS (Group/Selection-scoped) type-bakes do **NOT** survive a repatch — the reverse of this fact. Don't assume patch-time durability generalizes across group-membership and GS-bake mechanisms; they behave oppositely.

Relation: `tourshow-group-contract-v01` for the resulting Group 60-64 backlight membership this carve produced; `tourshow-her-key-and-backlight-doctrine` for why FID 55-60 needed carving out in the first place.

History: none — captured 2026-07-23 [0723cLD] digest run.


### gs-multifixture-recall-unreliable
**GridStore (GS) multi-fixture recall is unreliable — nondeterministic per-child propagation on Down; Groups (baked at Store) are the reliable layout carrier**
*when:* Before trusting a GS-stored layout to propagate correctly across MULTIPLE fixtures via Down — verify the resulting shape before storing any Group built from a GS-propagated selection; safe to trust GS for single-fixture/ad-hoc use


**⚠ Dave's live observation:** a sub-layout was correct at build time, stored via `GS`, and then a later `Down`-recall of that same stored layout **broke** it — in Dave's words, "console problem, not a you problem; it does not always work."

**Failure signature (seen on a 288-sub grid):** on multi-fixture recall, per-fixture blocks propagate **inconsistently** — some fixtures keep the correctly stored layout, others compact-pack or merge instead. The failure is **nondeterministic per child fixture**. Single-fixture GS recall, by contrast, is reliable.

**Consequence / doctrine (Dave):**
- **Groups are the reliable layout carrier** — coordinates baked into a Group at `Store` time hold up on recall.
- **GS is single-fixture / ad-hoc convenience only** — do not lean on it for a multi-fixture build.
- **Reliable lanes for multi-fixture layout work:** direct CLI dot-range layout per rig (see `subfixture-thru-range-syntax`), or Layout-view + lasso (see `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle`).
- **Always verify shape** before storing any Group built from a GS-propagated multi-fixture selection — see `group-xml-export-selectiondata-census` for the export-based verification lane.

**Durable facts (agent web-research 2026-07-15, key facts preserved in the 2026-07-15 wrap):** this exact nondeterministic multi-fixture GS-recall failure is **not publicly documented anywhere**; there is **no fix in any shipped or announced version**; **2.4.2.2 is the current version** as of 2026-07-15. The full research report was written to a session-mortal outputs path (`outputs/GRIDSTORE_BUG_RESEARCH.md`) and is not part of the durable corpus — these three facts are what survive from it.

**Second failure mode confirmed (2026-07-21) — GS bakes don't survive a repatch:** beyond the nondeterministic multi-fixture recall above, a GS type-bake is also not durable across a fixture-type repatch. The 2026-07-15 ACME sandwich bake was found wiped in cLD_SANDBOX_v0.23 after the v11 repatch (a `Down` probe returned all 48 subs stacked at origin). Two independent reasons now point the same way: **Groups baked at Store are the durable carrier; GS is not.** See `gridstore-keyword-and-fixture-type-write`.

History: none — failure observed and doctrine set live in one session, 2026-07-15; web research the same day found no public documentation or fix. Extended 2026-07-21 with the repatch-wipe failure mode (GS bake gone after the v11 repatch).


### jdc1-anatomy-ground-truth
**JDC1 anatomy ground-truth: 24 subs = 12 plate pixels (2×6 RGB) + 12 tube segments (white); SPix ch21-56 plates, ch57-68 tube — full map in JDC1_SPIX_MAP_v0.1.md**
*when:* Before addressing individual JDC1 subs/channels by hand — read the full channel map in WORKING/JDC1_SPIX_MAP_v0.1.md first; this concept is the pointer + headline facts, not the full table


**Cross-verified from two independent sources that agree:** the GDTF pulled out of the MVR export (see `patch-mvr-export-import-lane-and-schema` for how every patched fixture type's `.gdtf` is embedded there) and the official GLP manual.

**Headline anatomy:** 24 subs total = **12 plate pixels** (2 rows × 6, RGB — "1st Plate" = subs 1–6, "2nd Plate" = subs 7–12) + **12 tube segments** (white, no color mixing).

**SPix channel ranges:** channels 21–56 = the plate RGB pixels; channels 57–68 = the tube segments.

**Open point carried with the anatomy, not yet resolved:** channel 7 carries **pixel-orientation inversion flags** (an "all" inversion and a "2nd-plate-only" inversion) — mirroring for a symmetric layout can be done either in the FIXTURE's own channel/orientation setup or in the GRID layout itself; the anatomy data doesn't dictate which lane to use, that's a pending pick.

**Full map:** the complete sub-by-sub / channel-by-channel table lives in `WORKING/JDC1_SPIX_MAP_v0.1.md` — load that file directly for the full detail; this concept is intentionally just the pointer plus the headline facts, not a duplicate of its tables.

**Related but distinct (2026-07-16):** this concept is the fixture's channel/sub *anatomy*. A separate question — how those channels *gate* each other — turned out to have a gap: the same GDTF declares no relation for plate/beam master gating over cells, only per-cell virtual dimmers. That's a different fact about the same profile; see `jdc1-gdtf-no-gating-relations-root-cause` (and `jdc1-output-gated-chain` for the real, non-viz gating levels: fixture master × plate master × cell).

History: none — anatomy dug out and cross-verified live in one session, 2026-07-15, immediately put to use for the JDC1 GS grid layout that session. 2026-07-16: cross-referenced the separately-discovered GDTF gating-relations gap (see body) — anatomy facts here unchanged.


### jdc1-gdtf-no-gating-relations-root-cause
**JDC1's GDTF declares NO relation for plate/beam master gating cells — only per-cell virtual dimmers — so onPC viz structurally cannot gate; layout/stage intensity is untrustworthy, DMX viewer + real unit = truth**
*when:* Before trusting JDC1's Layout/Stage-view intensity for ANY output judgment call — read this first. Also useful as a template for root-causing any other multi-instance fixture that looks visually wrong: check the GDTF's relations, not just its channel map


Read directly from the GDTF (**GLP@GLP JDC1.gdtf**, pulled out of `cld_patch_v4.mvr` — every patched fixture type's GDTF is embedded in an MVR export, see `patch-mvr-export-import-lane-and-schema`): JDC1's **ONLY** dimmer relations are per-cell **VIRTUAL** dimmers — a single `PLATE_Dimmer` **Multiply** relation over that cell's own R/G/B — plus 7 **Grand**-master follows.

**No relation in the profile declares** ch8 plate master, ch20 PLATE MASTER, or ch3 beam master as gating their cells. That gating is real — it exists in the physical fixture's electronics — but it is **ABSENT from the GDTF profile**.

**Consequence:** onPC's visualization structurally CANNOT gate JDC1 the way the real fixture does, in either direction:
- **dark-with-values:** the programmer/cue holds correct values but the profile doesn't render the intended output, because it isn't multiplying through the (electronics-only) master chain.
- **lit-without-output:** the profile renders a defaulted/full master level as visible output even when the true master chain would actually leave the real fixture dark.

Both directions are **structural** — not a display bug fixable by switching views, and not something an MA3-side workaround changes, because the information the visualizer would need simply isn't present in the profile.

**Practical rule:** layout/stage intensity readings on JDC1 are **UNTRUSTWORTHY** with the stock profile. The DMX viewer and the real unit are the only sources of truth for JDC1 output. See `jdc1-standing-order-plate-master-full` for the standing operational workaround during output tests, and `jdc1-output-gated-chain` for the separate, *real* (non-viz) fact about how many gate levels the actual DMX output chain requires.

This root cause directly explains and supersedes the two prior symptom/suspicion observations from the same investigation — see `jdc1-display-weirdness-symptom-history`.

History: none — root-caused live 2026-07-16, same session as the symptom and suspicion that preceded it.


### jdc1-output-gated-chain
**JDC1 output is a gated chain — fixture master × plate master (401.1) × cell (401.1.1..12) — any level at zero is dark even while other levels show values**
*when:* Before running or troubleshooting ANY JDC1 output — cells or plates showing no light despite values being set almost always means one gate level in the chain is still at zero; working recipe below opens the whole chain


JDC1's real output — this is the actual gating behavior of the fixture/console chain, not a visualization artifact; contrast with `jdc1-gdtf-no-gating-relations-root-cause`, which is about why onPC can't *show* this correctly — multiplies through three gate levels: **fixture master × plate master (401.1) × cell (401.1.1..12)**. Any one level at zero produces dark output even while the other levels show set values.

**Why this bit us:** post-`Store Default` (per `store-default-values-keyword` / `master-default-doctrine`, which defaults cells to zero), a pool preset that doesn't explicitly open EVERY level in the chain outputs nothing — even though the preset's own values look correct. Highlight mode bypassed the chain entirely, which is what produced the earlier "only Highlight shows it" symptom (see `jdc1-display-weirdness-symptom-history`).

**Working recipe (live-verified):** `401.1 At Full` AND `401.1.1 Thru 12 At Full` — opens the plate master AND every cell.

**Refines `master-default-doctrine`:** that doctrine says masters should ride full by default so cell-level recipes carry the look alone — this finding sharpens WHICH intermediate masters that applies to on a multi-instance fixture: plate masters are included, not just the top-level fixture master. On JDC1 specifically, the plate master (401.1) is itself an intermediate gate that must also default full, or cell-level recipes underneath it go dark regardless of their own values.

History: none — solved live 2026-07-16, same session as the JDC display-weirdness investigation.


### jdc1-standing-order-plate-master-full
**Standing order: until JDC1 viz is resolved, every output test puts plate master at 100 in the programmer**
*when:* Before running any JDC1 output test/verification pass — apply this standing order first; also the reference for the stored plate/beam master group handles (426/446) that gate all cell output, and for the open warehouse hardware question below


Until `jdc1-gdtf-no-gating-relations-root-cause` is resolved (i.e., until the profile itself is fixed or replaced), the standing order for any JDC1 output test is: **put the plate master at 100 in the programmer first.**

**[VERIFY] Hardware question carried to warehouse day:** on the real unit, ch8 (401.1 Dimmer) AND ch20 (the PLATE MASTER attribute, which gates the pixel layer ch21-56) both appear to act as gates. Which one — or whether both — the hardware actually demands is not yet confirmed; verify at warehouse day.

**Both masters gate output — stored as group handles (2026-07-21):** the JDC1 intermediate nodes carry the masters you MUST turn up to see ANY cell output. `Fixture 401 Thru 464.1` = all PLATE masters (the MAIN PLATE `.1` node — its intensity/strobe); `Fixture 401 Thru 464.2` = all BEAM masters (the MAIN BEAM `.2` node). Cell pixels (`.1.n` plate / `.2.n` tube) output nothing unless the matching master intensity is up — this is also how you reach the plate/beam STROBE function and drive intensity. Stored as reusable groups **426 cLD JDC PLATE MASTER** (`401 Thru 464.1`, 64 masters) and **446 cLD JDC BEAM MASTER** (`401 Thru 464.2`, 64 masters). Extends the plate-only standing order below to the beam branch and to a stored handle; consistent with `jdc1-output-gated-chain` (fixture master × plate/beam master × cell) and `master-default-doctrine`.

**Related tool:** for actual programming sessions (not just one-off output tests), `jdc1-utility-sequence-plate-masters-pattern` describes a deletable utility sequence (Seq 103) that holds plate masters full while working. Per its own source note it supersedes the raw per-test programmer workaround described here for that use case. This standing order remains the right call for quick verification passes, and it still carries the independent hardware-gate VERIFY question above, which the utility sequence doesn't resolve.



## ⛔ CORRECTED 2026-07-31 [0731cLD] — master group numbers, and the warehouse gate is gone

**Live read:** the stored master handles are **Group 415 `cLD JDC PLATE MASTER`** and **Group 422 `cLD JDC BEAM MASTER`**; **426/446 are EMPTY**. Any reference above to 426/446 is stale — use 415/422.

**The `[VERIFY]` ch8-vs-ch20 hardware-gate question is re-homed:** there is **no warehouse day** on this tour (ruled 2026-07-30). It resolves at **previz, else first load-in** — and note that JDC1 is exactly the fixture whose visualization cannot be trusted for the answer, so the DMX viewer or the real unit is the only readback. See `tourshow-no-warehouse-day-previz-proof-lane` and `jdc1-gdtf-no-gating-relations-root-cause`.

History: none — established live 2026-07-16; cross-referenced later the same session once the utility-sequence tool was built. Extended 2026-07-21: both the plate (.1) and beam (.2) masters confirmed as output gates and stored as reusable groups 426/446. 2026-07-31 [0731cLD] — 426/446 -> 415/422 (live read); hardware-gate VERIFY re-homed off warehouse day to previz/load-in.


### jdc1-utility-sequence-plate-masters-pattern
**Deletable utility sequence holds JDC plate masters full while programming cells — Seq 103 'cLD JDC UTIL', ON while working, OFF/deleted at cleanup**
*when:* Before a JDC1 plate/cell programming session (not just a one-off output test) — turn this sequence on first so the gate chain stands open while you work


Pattern: store a **DELETABLE** utility sequence holding JDC plate masters at full. Turn it **ON** when programming plates/cells (the chain stands open, everything reads correctly per `jdc1-output-gated-chain`), turn it **OFF** when done, **delete** it at cleanup.

Built live as **Sequence 103 "cLD JDC UTIL"** — `401 Thru 464.1 At Full`.

Per its own source note, this pattern supersedes the raw per-test "put plate master at 100 in the programmer" workaround (see `jdc1-standing-order-plate-master-full`) for actual programming work — a real sequence that toggles on/off is more robust than remembering to hand-set the programmer every time. The standing order's independent hardware-gate VERIFY question (ch8 vs ch20) is untouched by this tool and remains open.

History: none — built live 2026-07-16, same session as the JDC gating root-cause work.


### ma3-3d-stage-coordinate-conventions
**MA3 3D stage axes: +X = stage left, +Y = upstage, +Z = up; RotX+ tips a fixture's top downstage; four lanes exist for editing patch positions**
*when:* Before computing, writing, or interpreting any fixture Pos X/Y/Z or Rot X/Y/Z value — or before deciding which UI/CLI lane to use to place a fixture in 3D


**Axis convention (per the 2.4 manual):** **+X = stage left**, **+Y = upstage** (so downstage is negative Y), **+Z = up**. Units are meters for position, degrees for rotation. The patch sheet's position columns are **Pos X/Y/Z** and **Rot X/Y/Z**, matching the XML attribute names (`PosX`/`PosY`/`PosZ`/`RotX`/`RotY`/`RotZ`).

**Rotation convention:** positive **RotX** tips a fixture's top toward **downstage**. Practically, **RotX = −90** faces a hung, non-moving-head fixture (a strobe or batten-style unit) out toward the crowd — this is exactly the value used on the template rig's JDC1 and ACME pix, both patched at RotX −90 (see `tourshow-template-rig-patch-and-layout-state`). Moving-head fixture types (spots, washes) aim via pan/tilt in the programmer rather than RotX, and this corpus doesn't record a RotX value for them.

**Four lanes exist for editing patch fixture positions**, each suited to a different job:
1. **Patch sheet, Full-columns mode** — direct cell entry, best for reading/spot-checking or small manual edits.
2. **3D Setup-mode Arrangement tool** (Line / Grid / Circle, with spacing encoders) — an encoder/UI lane for auto-arranging a selection in 3D space. No CLI equivalent is documented for it, and this session didn't end up using it (positions were written by CLI `Set` instead).
3. **CLI `Set`** — e.g. `Set Fixture 101 "PosX" "0.6"`. Works from LivePatch context; property names match the XML attrs; `Thru` ranges are supported for bulk addressing. See `patch-cli-set-command-gotchas` for the failure modes this lane has (one property per command, mandatory quoting, no negative-bound spreads).
4. **Patch sheet cell-editor spreads** — the sheet's cells embed a `Thru`-capable calculator (e.g. typing `-7 Thru *` spreads a value across the selected rows). This is Dave's mass-edit idiom, and it's the only lane confirmed to handle **negative-bounded** spreads (CLI `Set` can't — see `patch-cli-set-command-gotchas`). **[VERIFY]** whether the editor's ✗-close button commits or cancels a pending spread is untested — treat it as commit until verified.

History: none — coordinate convention and lane inventory both captured live 2026-07-14, cross-referenced against the same session's 3D rig build.


### master-default-doctrine
**Masters ride full by default so cell-level recipes carry the look, not the master level**
*when:* Before building cell-level recipes on a multi-instance fixture — default the type's master to full first so recipes aren't fighting a dimmed master


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


### mm-shell-empty-preset-armor
**⛔ NO HARD ZEROS ON MASTERS (Dave: 'same issue') — point mark-cue master rows at an EMPTY dimmer preset instead; an empty preset asserts nothing, and filling it once makes every mark follow**
*when:* Before arming a mark cue against multi-module fixtures — the instinct is to store master=0 and that is the wrong armor; the shell is the right one


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


### patch-mode-census
**Patch DMX-mode census (cld_patch_v2.xml): JDC1=SPix ×118, MacUlWsh Mode 0 ×64, MACEncPerCLD Basic ×64, Lucius Extended Pan630 ×10, BMFL Mode 1 ×6 — fixture-TYPE index ≠ FID century**
*when:* Before assuming a fixture type's DMX mode/personality from its FID range, or before reasoning about total instance counts per fixture type across the whole show (overhead + House/floor combined)


**Census, from `cld_patch_v2.xml`:**
- **JDC1 = SPix (68CH) × 118** — explicitly **NOT** Mode 13 (that mode number belongs to the ACME PIXEL LINE × 100, a different fixture type).
- **MacUlWsh (MAC Ultra Wash) Mode 0 × 64** — has `[Instance2]` subs.
- **MACEncPerCLD (MAC Encore Performance CLD) Basic × 64.**
- **Lucius Extended Pan630 × 10.**
- **BMFL Mode 1 × 6.**

**Cross-check:** the 64-count entries match the template rig's overhead spot (MACEncPerCLD, FID 101–164) and wash (MacUlWsh, FID 201–264) categories one-for-one; the Lucius (10) and BMFL (6) counts match the House/floor folder's unpositioned fixtures exactly (see `tourshow-template-rig-patch-and-layout-state`). JDC1's 118 = the overhead JDC (64, FID 401–464) plus the House/floor JDC1 (54) — the two JDC populations summed.

**The rule to hold onto:** **fixture-TYPE index (the mode/personality slot a type is patched under) is NOT the same number space as FID century** (the hundreds-digit convention used for FID ranges/century-numbering schemes — see `tourshow-festival-group-theory` for a related but distinct century-numbering cross-check, that one about Group numbers vs. FIDs). Don't conflate the two when reasoning about the patch.

History: none — census pulled live from the patch XML in one session, 2026-07-15.


### patch-mvr-export-import-lane-and-schema
**MVR: export via the same Patch Export dialog (its default tab); import lives in PSR and CLEARS THE PROGRAMMER; zip schema with matrix-encoded position/rotation; embeds every patched type's GDTF as fixture-anatomy ground truth**
*when:* Before exporting or importing an MVR file, before writing/parsing an MVR's GeneralSceneDescription.xml, or before needing a fixture type's internal sub/channel anatomy without console or web access (the embedded GDTFs cover it)


**Export:** the same Patch Export dialog used for grandMA3 XML (see `patch-xml-export-lane-and-schema`) has an **MVR format tab, and it's the dialog's default on every open** (the manual documents this default, and live behavior confirms it — the dialog does NOT remember a prior grandMA3-tab click across opens). Output path (exact filename pattern not yet captured — observed `<name>.mvr`):
```
gma3_library/mvr/
```

**Import — ⛔ danger:** MVR import lives in **PSR (Show Creator)**, and importing there **CLEARS THE PROGRAMMER** (documented in both manuals; not yet exercised live — only export has been run so far, so treat the import flow itself as manual-sourced until a live PSR run confirms it). Either way, treat any MVR-import step as destructive to whatever's live in the programmer.

**MVR file schema (from a live export/parse):** an MVR is a **zip archive** containing `GeneralSceneDescription.xml` plus per-fixture-type **GDTF** files. Each fixture's position and orientation are encoded as a **`Matrix` = {u}{v}{w}{o}** — four vectors, values in **millimeters**. `o` is the position vector; **`RotX` is derivable from the `v` basis vector via `atan2(v3, v2)`**. **Fixtures with no `Matrix` attribute are implicitly at the origin.**

**Why this matters as a verification lane:** the MVR being cleanly parseable makes it a **second, independent verification lane** alongside the grandMA3-XML diff — export both, compute the same fixture positions two different ways, and treat agreement as the confidence signal (see `export-diff-verification-loop`). It's also the ready exemplar for future PSR-import tooling work, since its schema is now captured.

**Context:** the repo's 08_PatchAndSetup manual's Patching section is a stub — it doesn't cover positions, CLI patch-position workflow, or this MVR lane at all, which is why both the export mechanics and the schema above had to be reverse-engineered live rather than looked up (see `patch-xml-export-lane-and-schema` for the parallel grandMA3-XML side and the CLI "Illegal object" bug).

**GDTF payload confirmed as fixture-anatomy ground truth (2026-07-15):** the embedded GDTF files aren't just present per-type — the MVR export carries **every patched fixture type's `.gdtf`** (a zip nested inside the MVR zip). This makes a single MVR export a **complete, file-side, console-and-web-free source of fixture anatomy**: each GDTF's geometry tree gives the sub/instance structure, and its DMX-mode section gives the channel map. Used in practice to build the JDC1 SPix channel map (see `jdc1-anatomy-ground-truth`; full tables in `WORKING/JDC1_SPIX_MAP_v0.1.md`) without touching the console or the web.

History: none — MVR export/import mechanics and schema were captured live in the same session, 2026-07-14, as the second verification lane for the template rig's final 3D positions (256/256 exact). 2026-07-15: confirmed the embedded-GDTF detail is complete (every fixture type, zip-in-zip) and used it as an offline fixture-anatomy ground-truth source for the JDC1 SPix map.


### patch-set-one-prop-quoted-values
**Set on patch fixtures: ONE property per Set (chains silently drop), QUOTE every value (bare negatives silently flip sign) — CLI value-spreads also reject negative bounds**
*when:* Before generating or running ANY Set command against patch/fixture objects (PosX/PosY/PosZ/RotX/RotY/RotZ etc.) — read this before trusting a chained Set or an unquoted negative value


**⛔ Hard rule — MEMORY.md hard rule #10 points here.** Everything below is live-verified, 2026-07-14, onPC 2.4.2.2.

**Context:** `Set Fixture` operates from the LivePatch prompt, addressing patch-fixture objects whose property names match their XML attribute names (`PosX`, `PosY`, `PosZ`, `RotX`, `RotY`, `RotZ` — see `patch-export-dialog-and-mvr-lane`).

**One property per `Set` on patch fixtures.** Unlike `Set Layout n.e "PosX" 0 "PosY" 600`, where chained properties work fine (see `layout-cli-assign-and-posxy-syntax`), chaining multiple properties onto one `Set` against a **patch fixture** silently drops everything after the first property/value pair. No error, no partial-success notice — the prompt returns clean. Issue one `Set` per property when writing patch-fixture attributes.

**Quote every numeric value, always — especially negatives.** A bare (unquoted) negative value in a patch `Set` has its minus sign silently eaten and the POSITIVE value gets applied instead — a command meaning `-0.5` lands as `+0.5`, with no warning. Quoting fixes it: `"-0.5"` applies correctly (live-verified). Treat this as absolute: quote every value sent to a patch `Set`, not just the ones that look negative.

**`Thru` ranges work fine with `Set`** on patch fixtures — this part behaves as expected.

**CLI value-spreads (`a Thru b`) parse but reject negative bounds.** A spread like `-5.5 Thru 5.5` is read as spread grammar, but the leading negative sign is eaten the same way as the single-value case — the result degenerates to a flat `5.5 Thru 5.5` (no real spread; every fixture gets `5.5`). Quoting the whole expression doesn't rescue it either — quoting kills the spread semantics entirely and applies the leading number flat, negative sign intact this time (`"-5.5 Thru 5.5"` → every fixture gets `-5.5`). **Net result: CLI-side `Thru` spreads only work for non-negative bounds.**

**Scope boundary pinned, 2026-07-19: this negative-bound trap is specific to patch-`Set` CLI spreads — it does NOT extend to programmer attribute spreads.** Factory macro content proves negative-bound `Thru` spreads work fine on programmer attributes: `Pan At Absolute Physical 30 Thru -30` (POSITION_WIZ's Fan In preset, see `factory-position-wiz-anatomy-and-porting`) runs correctly. The failure mode documented above is specifically about `Set` against **patch fixture** objects (PosX/RotX/etc.) — a different command context from attribute-value spreads issued against the programmer.

**Negative spreads: use the patch sheet's cell editor instead.** The patch sheet's cell editor (click into a Pos/Rot cell) is itself a `Thru`-capable calculator — typing an expression like `-7 Thru <value>` into the cell spreads that range across every selected row directly (this is how a 1.309 m spread got applied across a run of DS spots this session). This is Dave's mass-edit idiom for exactly the case the CLI can't do. **Open question:** what the cell editor's ✗-close button does (commit vs. cancel the typed expression) is unconfirmed — treat any ✗-close as a commit until tested, and verify the result either way.

**Never trust a clean echo on a patch `Set`** — verify by census/readback after every batch (see `paste-round-verification-protocol` and `export-diff-verification-loop`).

History: none — all four failure modes (chain-drop, sign-eat, spread-sign-eat, quoted-spread-degenerate) paid for live in one session, 2026-07-14; this is the concept MEMORY.md hard rule #10 points to. Extended 2026-07-19: scope boundary confirmed — the negative-bound trap is patch-Set-specific and does not apply to programmer attribute spreads (factory macro evidence).


### patch-xml-export-lane-and-schema
**Export Patch to grandMA3 XML: CLI keyword is Illegal object (repo manual 08 §9.2 is wrong for 2.4.2.2) — use the Patch Export dialog's grandMA3 tab instead; folder nesting + zero-attr-omission schema**
*when:* Before exporting a patch to grandMA3 XML, before trusting the repo manual's 08_PatchAndSetup CLI instructions for patch export, or before writing/parsing a patch XML file


**The CLI route documented in the repo manual doesn't work.** `Export` can't address `Patch` as a CLI object — it fails with **"Illegal object"** on 2.4.2.2. The repo's **08_PatchAndSetup manual's §9.2 CLI line for this is wrong for 2.4.2.2** (its Patching section is otherwise a stub — positions and CLI patch-position workflow aren't covered there at all, which is why this had to be reverse-engineered live). `Menu "Patch"` does correctly open the patch menu from the CLI as a way in.

**The working route is the Patch Export dialog:** format tabs **grandMA3 | MVR** × scope tabs **EntirePatch | SelectedFixtures**. **The dialog resets to MVR format on every open** (the manual documents MVR as the default, and live behavior confirms it) — click the **grandMA3 tab explicitly, every time**, or the export silently comes out as a `.mvr` instead (see `patch-mvr-export-import-lane-and-schema`). grandMA3-format output path:
```
gma3_library/patch/stages/<name>.xml
```

**Name-field behavior:** `Cmd+A` select-all works in the dialog's name field. **Triple-click does NOT select/grab the `<Default>` placeholder token** — a paste at that point appends to it instead of replacing it. Clear the field with `Cmd+A` before pasting a name; don't rely on triple-click.

**grandMA3 patch XML schema (from a live export):** folder structure is represented as nested `<Fixture>` nodes (per `Mode 5.Grouping`). **`PosX`/`PosY`/`PosZ`/`RotX`/`RotY`/`RotZ` attributes are omitted entirely when their value is zero** — absence means zero, not an error or an unset value. The `RotX` attribute's string value carries a **leading space** in its serialized form, e.g. `" -90.00"`.

History: none — export mechanics, the CLI bug, and the XML schema were all captured live in the same session, 2026-07-14, while exporting the template rig's patch for position verification.


### recipe-layer-is-fixture-agnostic-doctrine
**Recipe layer is FIXTURE-AGNOSTIC: author Group x Preset and nothing else — the GROUP absorbs the rig, the PRESET absorbs the fixture type, and no recipe ever names a cell count or address**
*when:* Before authoring ANY cue part or recipe line — this is the standing rule for what a recipe is allowed to reference. Also load before deciding whether a rig change (fewer fixtures, different type, no cell split) breaks existing content: it almost certainly does not, and this concept says why.


**Dave's ruling, stated as the portability test:** the same programming must work on
**anything from a simple flood (LEDJ Q40 — which has a strobe channel) through a
LOW-channel-mode JDC1 or Strike M up to a HIGH-channel-mode JDC1 or Strike M.**

**The rule: a recipe line references a GROUP and a PRESET. Nothing else.** It never names a
cell count, a cell address, a subfixture depth, or a fixture type.

## Three layers, each absorbing a different kind of difference

| Layer | Absorbs | How |
|---|---|---|
| **RECIPE** | nothing — it is the invariant | `Selection = Group` x `Values = Preset` |
| **GROUP** | the **RIG** | the same role slot holds JDC1 cells at one venue and bare floods at the next |
| **PRESET** | the **FIXTURE TYPE** | `/Universal` store mode resolves per profile's emitter engine |

This is the mechanism that makes **author-once-fill-per-rig** real, and it is why the
festival leg is tractable at all: at each stop you re-fill the contract groups against
whatever is hanging, and the content lands unchanged.

## It is already true of the inherited content

Live-verified across **all 105 live recipe lines of SONG_T** ({FESTIVAL}, Sequence 1500):
every one is `Group x Preset` — `G70 x Preset 4.4`, `G70 x Preset 1.5`, `G71 x Preset 1.15`,
`G11 x Preset 21.1504`. **Not one recipe references a cell count or address**, even though
several of those groups contain 228+ cells.

**⚑ COUNT CORRECTED 2026-07-27 [0727-2cLD]: 105, not 50.** The original figure of 50 (repeated
in `CURRENT_STATE_A0727.1` and that session's NEXT_ACTIONS) undercounted by more than half. A
parser census of the export found **105 `StandardRecipe` elements that are DIRECT children of
a Part** — plus 10 more nested inside `DependencyExport` blocks, which are embedded dependency
COPIES, not live recipe lines, and must not be counted. **The doctrine was re-tested against
all 105 and returned ZERO violations**, so the correction makes the claim better evidenced,
not weaker. The cell-ness of a group is invisible to the
recipe; it only determines how many things receive the value.

## Corollary — the gated chain is a GROUP/DEFAULTS problem, not a content problem

`jdc1-output-gated-chain` (output = fixture master x branch master x cell) looks like it
threatens portable cell content. It does not, **provided masters are defaulted full** per
`master-default-doctrine` (`Store Default`: master full, cells zero, on every multi-cell
type). Then `Group x Full` behaves identically whether the group holds cells behind a
master or bare floods. **The gate bites a naive clone of someone else's file; it does not
bite content authored this way.**

## Corollary — a shrinking rig hits the FILL layer, not the CONTENT layer

First real test: 19 upstage JDC1 replaced by 7 LEDJ Q40 (budget-driven). Nothing in the
content breaks. Phaser resolution **degrades gracefully** — a phaser across 228 cells is a
fine chase and across 7 floods a coarse one; same recipe, still correct, reads differently.
**The correct response to a rig shrinking mid-advance is to re-fill the group, not to
re-author the song.**

**One thing this doctrine REQUIRES to hold:** no baked N anywhere in the recipe — see
`no-baked-n-portable-phaser-doctrine`. A MAtricks carrying a phase literal computed for a
specific fixture count is the one thing that genuinely does break across rigs.

Relation: `tourshow-group-contract-v01` (the role-based group scheme the GROUP layer
depends on) · `universal-presets-emitter-aware` (the `/Universal` rule the PRESET layer
depends on) · `replay-portable-strobe-doctrine` (same principle applied to strobe: build it
as a shutter chase so it carries across fixture types) · `tourshow-recipe-based-show-style-ruling`
(the show-level mode ruling this operationalises).

## ⚠ PILLAR TWO FAILS ON THE INHERITED CONTENT — verified 2026-07-28

This doctrine has two pillars: **GROUP absorbs the rig** and **PRESET absorbs the fixture type
via `/Universal`**. The 105/105 recipe-line test above verifies the RECIPE LINE layer only. It
does **not** establish that the presets those lines point at are portable — and on {LD}'s
file they are not.

**Live-read from the export:** `Intro 1/1 Spot Dim` carries `PresetMode="Global"` but its
`PresetData` holds **34 per-fixture `<Phaser ... Selective="Selective">` rows**, one per member
of the 34-fixture Spots group, each with a **baked per-fixture `Phase`** (first row
`IDType=0 ID=101 Attribute=Dimmer Phase="102.857"` — which is `10 × (360/35)`, a literal
computed against their fixture count). **The label says Global; the data is Selective and
fixture-locked.** Swapping the group on a recipe line does NOT re-point it.

**⚠ Do not read `PresetMode` as evidence of portability — read the `PresetData` rows.**

**How the build sidesteps it:** `tourshow-authoring-contract-v01` rules that we never port
their phasers at all — theirs are a checklist of where a phaser belongs, and we author fresh
template ones. The Selective/baked-N problem therefore never arrives.

**Lesson on the testing itself:** when verifying a doctrine with multiple pillars, **name which
pillar the test covered.** Reporting "zero violations" without that scope read as more
portability than had actually been established.
rig-layer difference for a content-layer break. Updated 2026-07-27 [0727-2cLD]: recipe-line
count corrected 50 -> 105 by parser census, and the fixture-agnostic test re-run across all
105 with zero violations. Its required companion `no-baked-n-portable-phaser-doctrine` — cited
by this concept before it existed — was filed the same session. Updated 2026-07-28 [0727-2cLD]: recorded that pillar two (PRESET absorbs fixture type) FAILS on the inherited content — their phasers are Selective despite a Global PresetMode — and that the 105-line test covered the recipe-line layer only.


## ⛔ PILLAR TWO, ONE LAYER DEEPER — a preset's DEPENDENCIES carry fixtures too (2026-07-31)

The section above establishes that `PresetData` rows can be fixture-locked while the header reads `Global`. {LD}'s **Synth Swell** preset (`21.1031`) adds the second half of the trap, and it is worse:

- `PresetMode="Global"` — the label, again, a lie.
- **96 `Selective` rows addressed at CELL-LEVEL dot-IDs of the OLD RIG** (`12204.1.1`, `.1.2`, …), each with baked per-cell `Phase` (6.32° steps) and baked `Speed` (238 BPM), every row stamped `Cooked=`.
- **Its `DependencyExport` embeds the actual GROUP OBJECTS** it was built against — `JDC1 SW [RGB]` and `JDC1 DS [STB]`.

**So the preset carries fixture references two independent ways**, and neither is visible from the recipe line. Swapping the Group on the cue part **re-points nothing** — the preset has to be re-authored on our own objects. (Done: re-authored as `cLD SONG_A SWELL` + Seq 1017, see `tourshow-seq1010-build-record`.)

**How it was missed, which is the actual lesson:** the sequence layer was read, its group binds looked crosswalkable, and the piece was declared compatible without opening the preset. Dave caught it. **Reading one layer is not reading the object.**

**The rule, generalised:** before calling any inherited preset compatible, read **the rows AND the dependencies**, not the header — and if either names fixtures, cells, or groups, the preset is a re-author, not a re-point. The good news is that the musical figure survives the trip: a spec-read of the steps gives the template class, and the baked speed gives the tempo gear.

History: ruled by Dave 2026-07-27 during the {FESTIVAL} recon, after cLD twice mistook a 2026-07-31 [0731cLD] — Pillar Two extended with the DependencyExport group-embedding case ({LD} Synth Swell 21.1031); rule restated as rows AND dependencies.


### resolume-dmx-one-hot-clip-select
**Transport-proof video clip select from the desk: a sequence of per-song cues, each driving its OWN clip shortcut to Full and the PREVIOUS one to 0 (one-hot), fired from the shared song macro — show-proven live**
*when:* When lighting also has to select the video clip per song — this is the shipped pattern, why it beats a per-cue value pile, and how it hangs off the existing show-run chain with zero new wiring


## The shape

- **Patch:** one dimmer channel per clip as a DMX shortcut into the video machine, plus a layer-opacity channel. Twenty clips ⇒ twenty single-fixture groups plus an "all" group for the tidy-up.
- **A sequence, one cue per clip**, each cue **named the song token** (talking-break clips sit at their real show positions in the deck order), with an `All_Off` cue at the end.
- **Each cue's recipe is one-hot:** **own clip @ Full** + **previous clip @ 0**. Deterministic, and it avoids the same-fixture cooking conflict a full "all others at zero" pile would create.
- **Fired by name** from the shared song macro's toolbox call: `Go+ Sequence '<sequence>' Cue '<token>'`.

**Out-of-order fires still work.** The video machine's shortcuts are **edge-triggered**, so a cue fired out of sequence still switches the clip correctly — the one-hot pair is about clean DMX state, not about ordering.

**Receipts:** 21 cues + OffCue/CueZero, SR = 40 exact, all cue names true; generator run twice (container and device) byte-identical before deploy; sha-verified on landing.

## Why it hangs off the song macro

The clip-connect rides the **same single touchpoint** as everything else per-song (`automator-tc-architecture`) — the toolbox function reads the `selectedsong` global and fires the matching cue by name. **Zero new wiring**: timecode in → automator → song macro → toolbox → clip. A manually-fired mark cue will not pull video (accepted trade-off, see the automator concept).

## The alternative lane, and why it wasn't needed

Native OSC out to the video machine is a real option and its address contract is banked (`resolume-osc-clip-connect-address`). The DMX-shortcut lane won because the desk was already patched for it, the state is visible in the show file, and it needs no network configuration on show day. **A single-channel Art-Net/DMX fallback is also viable.**

**⇒ Show-proven.** The full chain — Art-Net TC → automator → song macro → toolbox → one-hot clip select — **ran live in a show and worked.** It is production, not a test rig.

**Standing law it obeys:** show-run signals originate at the desk, never through the bridge (`show-run-signals-originate-at-the-desk`).

**Relation:** `automator-tc-architecture` · `resolume-osc-clip-connect-address` · `appearance-image-swap-blocking-cards` (the sibling per-song action on the same touchpoint) · `tourshow-resolume-scope-and-tc-chain` · `led-wall-anamorphic-fit-math`.

History: none — designed, built, TC-tested and show-proven between 2026-08-08 and 2026-08-19.


### selection-grid-and-fixture-cell-model
**Selection Grid axis convention and one-fixture-one-cell-per-sequence rule**
*when:* Before building or reasoning about MAtricks grid layouts, or when a fixture appears to occupy more than one cell in a single sequence; also check when reading a grid-window screenshot, since zoom level and FID-label readability shift with selection extent


**Selection Grid axis convention:**
- X = horizontal (red)
- Y = vertical (blue)
- Z = depth (green)

**Cell occupancy rule:** each fixture occupies exactly **one cell per sequence**. Multiple sequences can place multiple grids on the same fixtures, resolved by LTP/HTP priority — i.e. cross-sequence overlap is legitimate and expected; it is *intra*-sequence duplication that is the invariant being guarded.

**Grid window render behavior (added 2026-07-14, live drill observation):** the grid window auto-fits its zoom to the current selection's extent. Narrow-to-medium builds render with large cells and readable FID labels — confirmed readable at 16 columns and again at 31 columns; wider builds shrink to a thin, label-illegible strip — confirmed unreadable at 46 columns. The exact threshold between 31 and 46 wasn't pinned down. Practical rule: verify a wide build by its overall shape, verify a narrow-to-medium build by reading the FID labels, and confirm contents by readback when either is in doubt. Separately: clicking anywhere on the grid canvas moves the grid cursor to that cell — normal behavior, but worth knowing because a fullscreen grid window exposes much more canvas area, so incidental/stray clicks land on it (and silently relocate the cursor) far more easily than in a windowed view.

**Grid Rotate (added 2026-07-19):** `Grid 'Rotate' 'Right'` rotates the grid — since `Thru` spreads distribute along grid X, rotating changes which axis a subsequent spread walks (e.g. turning a left-right spread into a front-back one). Live-confirmed running; the precise axis-reassignment mechanics are still being pinned down at the desk — see `tourshow-position-wiz-blind-depth-grade-root-cause` for the worked diagnosis of what happens when this runs against a selection that isn't a real 2D grid.

**Cursor + recall (added 2026-07-19):** confirms and extends the canvas-click note above — clicking a grid cell doesn't just move the cursor, the NEXT recalled Group or selection lands wherever the cursor currently sits. Chaining click→recall→click→recall builds ad-hoc composite grids live (see `grid-cursor-cli-recipe-for-2d-group-layouts` for the storage discipline that governs when an ad-hoc composite needs to become a real stored Group).

History: stable axis/occupancy rule since 2026-04-01. Render-behavior notes (auto-fit zoom, canvas-click-moves-cursor) added 2026-07-14 from live grid-drill observation. Extended 2026-07-19: added Grid Rotate's axis-swap behavior and the recall-lands-at-cursor mechanic, both from live console observation.


### smith-lane-dialect-dispatch-doctrine
**Smith lanes — one scoped subagent per XML dialect, whose arming manifest IS its boot and therefore cannot be skipped**
*when:* Before dispatching any authoring or certification subagent; when deciding whether a task warrants a dispatch at all; when a session is about to author XML while deep in another territory


**THE PAID-FOR ORIGIN.** [0723cLD] authored macro XML twice while the exact fix sat filed in the corpus, unopened — `macro-xml-schema-cracked`, `when_to_load: "before hand-authoring any macro XML"`, four days old. Root cause was **not missing knowledge; it was attention** — task territory changed mid-session (desk → authoring) and the re-arm never happened. Dave's 2 AM insight: *"you need macros, recipes, a whole bunch of stuff; if none of it is loaded you will never see it."* Dave's ruling: make the gate **structural**. A scoped agent cannot skip its manifest — **the manifest IS its boot.**

**THE CUT (Dave-ruled): by dialect.** One smith per XML dialect the project authors, matching how the corpus, golden fixtures and lint rules are already organized:

| Lane | Brief | Dialect | Goldens |
|---|---|---|---|
| MACRO SMITH | `agents/MACRO_SMITH_v0.1.md` | Macro XML | `cLD_GROUP_BUILDER.xml`, `cLD_POSITION_WIZ_generic_v0.1.xml`, factory samples |
| SEQUENCE SMITH | `agents/SEQUENCE_SMITH_v0.1.md` | Sequence XML (+ Timecode secondary) | `cld_seq102_inspect.xml`, `Tc1_Inspect.xml` |
| PHASER SMITH | `agents/PHASER_SMITH_v0.1.md` | Baked-phaser / colour-preset XML + recipe-preset internals | predefined libraries + export-diff pinned samples |

Lanes grow on demand (layout, patch, lookup-smith) on the same template. "Smith" is a working term — Dave may rename.

**ARCHITECTURE.** **cLD = orchestrator**, holding WHO/WHY/WHEN: show context, design rulings, binding tables, slot addresses, the queue. It classifies territory, assembles the packet, judges the report, routes findings, and owns **ALL** memory-system writes and **ALL** console contact. **Smith = HOW**: one dialect, deliberately small context, manifest front-of-attention, never self-directed — a smith exists only inside a dispatch.

**INVARIANTS.** Smiths never fire the console (no MCP/OSC, nothing `mcp__`); never write repo or memory files; every claim cites `file:line`; anything the manifest cannot answer returns as a QUESTION. **Invention is the cardinal sin — "could not verify" is a correct output.** Extends `persona-memory-sovereignty` into standing named lanes.

**DISPATCH THRESHOLD.** Inline (no dispatch): one-line edits, single-value lookups cLD already holds, anything smaller than its own packet. Dispatch: whole-artifact authoring, any pre-desk artifact certification, fan-outs, and **any dialect work while the main session is deep in another territory** — that last one is the exact failure mode this system exists to kill.

**PROOF OF LANE (2026-07-23, same day as the spec).** Two parallel verify dispatches, Sonnet-class, read-only: **foundation v0.1.3 PASS-WITH-FLAGS** (quote dialect clean on all 16 embedded-name lines; ratified backlight members exact on all 5 groups; `/Universal` 11/11) and **`cLD_SONG-E_SEQ.xml` PASS-WITH-FLAGS** (45/45 StandardRecipes, zero PresetData, `UseExecutorTime=No`). Cost ~116k / ~197k tokens, ~8 / ~11 min. **Both smiths independently caught the SAME defect** — binding-table off-by-one (`1.102–1.111` vs 11 ladder values; the XML correctly ships `1.102–1.112`) — unprompted cross-lane corroboration. Zero invented facts; unknowns returned as QUESTIONS exactly per contract, on first exercise of both lanes.

**FIRING-LANE POSTURE (Dave, [0723-2cLD]):** *"we're figuring this out together"* — ownership of desk imports/fires stays a **per-session call made together**. The gates (desk-clear callout, line-readback diff, authoring gate) are **invariant regardless of who fires**. Not a verdict; standing posture until revisited. Smiths never fire, either way.

History: spec + lanes born and proven the same day, 2026-07-23 [0723-2cLD].


### smith-packet-must-stage-multi-part-golden
**Smith packets must stage a MULTI-PART golden, not a single-part one — single-part exemplars can't attest SpeedMaster/SpeedScale/parts serialization**
*when:* Before assembling a smith dispatch packet for any sequence-authoring task — which golden exemplar file to stage so the smith can actually certify parts-per-century facts, instead of burning its manifest re-proving something already closed


**Lesson (SONG_C smith certification):** stage **`cld_song-b_seq_v2.xml`** as the MULTI-PART golden in every future sequence-smith packet. **⚑ Qualified 2026-08-05 — see the bottom of this file: this file is NOT a raw desk export**, so it cannot independently attest everything below; it retains authority for part-attribute ORDER only. A single-part golden **cannot attest** `SpeedMaster`-on-Sequence, `SpeedScale`-on-Part, or multi-part serialization at all — it has no second part to prove any of that against. Without a multi-part golden staged, the smith burns its own manifest re-proving a hole the corpus had ALREADY closed elsewhere (in this case, the proof existed in a desk export that simply hadn't been staged into the packet).

**Also stage the song's `gb_sNN00.xml` export** so the sheet-transcription link closes as part of the same certification pass.

**Consequence observed:** all 4 of the smith's WARNs on SONG_C's certification were closed by evidence found OUTSIDE the smith manifest — evidence that a properly staged multi-part golden would have made available INSIDE the manifest from the start.

**Relation:** `parts-per-century-emit-pattern-and-et-gate` (the architecture whose facts a multi-part golden must attest). `part-attr-order-import-absorption-gotcha` (a fact only a multi-part golden's attribute order can verify). `tourshow-seq1210-song-c-build-record` (the certification run this lesson was paid for on).

## ⛔ `cld_song-b_seq_v2.xml` IS NOT A RAW DESK EXPORT — qualifies the golden above, 2026-08-05 [0805cLD]

**Byte-shape proof (sequence smith F1):** `cld_song-b_seq_v2.xml` carries **0 `Guid=`, 0
`Active=`, 0 `DependencyExport`, 0 `PresetData`, and 6-7 attrs per StandardRecipe** — against a
known console export's 11 Guids / 36 attrs and {LD}'s 33-34. It has the AUTHORED dialect's
byte shape, i.e. it is a scrubbed export-back, not a raw export.

**This partly circularises the lesson above**, which names this file the authority for exactly
the facts an emitter-shaped file cannot independently attest (`SpeedMaster`-on-Sequence,
`SpeedScale`-on-Part, multi-part serialization). **It DOES retain authority for part-attribute
ORDER** — it carries the desk form at both sealed-divergence spots, which our own emitter does
not produce.

**A "golden" is only golden if its byte shape matches a real export** — generalised: before
trusting any file labelled desk-export, check for `Guid=` / `Active=` / `DependencyExport`
presence. Their absence means authored or scrubbed, not a genuine console export.

**Owed:** stage one true multi-part RAW console export for the smith lane, or state SONG_B's
actual provenance explicitly in the packet. Not resolved this session.


### store-default-values-keyword
**`Store Default` (two words) values a fixture type's DEFAULT — Merge mode is the master-default staging pattern for multi-instance cell recipes**
*when:* Before building cell-level recipes/cues on a multi-instance fixture (plate+beam, pix+tube, etc.) — stage the type's Default values first so per-cell recipes can carry the look alone


**Syntax settled live:** `Store Default` — **two words**. `StoreDefault` (one word) is **Illegal object**. The repo manual has **no entry at all** for this command (a doc gap, not a doc error).

Firing it opens a popup, verbatim: **"Store Default values — choose mode"** with options **Overwrite / Merge / Remove / Cancel**. **Merge is the standard call** (Dave's default choice).

**Master-default staging pattern (Dave's doctrine):** before programming cell-level cues on a multi-instance fixture, stage the programmer first — **MASTER** element at **full**, **ALL instances** (e.g. plate + beam cells) at **zero** — then `Store Default` → Merge. This makes the fixture's masters ride at full **by default**, so per-cell recipes only need to carry the look itself rather than also fighting the master level. Applied and Dave-approved on the JDC1 type (Layout 3 + the session's sequence recipes checked and approved against it).

History: an initial pass same session flagged the exact syntax `[VERIFY exact syntax via popup]` after only the doctrine (not the keyword) was confirmed; settled minutes later live — `Store Default`, two words, Merge mode — folded here as the single settled statement rather than carrying the transient VERIFY forward.


### subfixture-cell-architecture-doctrine
**Subfixture doctrine (Dave): the bar/master is a SEPARATE handle from the cells; cells live in X/Y physical space (never a bar-stack, never Z unless architectural); linear selections are uniform-only, spatial effects need baked 2D coords**
*when:* Before building or programming any multi-cell fixture (ACME pixel lines, JDC1) — how to split the bar-master from the cells, why cells must carry baked X/Y grid coordinates for effects, the no-Z ruling, and which rig types actually carry a cell split


Dave's settled architecture for multi-cell fixtures, dictated across the 2026-07-21 subfixture session.

**Two layers, NEVER mixed in one group:**

1. **BAR / MASTER** = the whole-strip parent handle (top-level fixture: master dim/strobe/control). The ACME parent geometry "Body" is the bar master; the JDC1 parent splits into a plate master (`.1`) and a beam master (`.2`). The parent **scope** groups (e.g. PIX 301–308) already ARE the bar handles. The bar goes "somewhere else" — it is NOT part of the cell grid.
2. **CELLS** = the individual zones (ACME 48, JDC1 24), where color and effects live. Cells must be laid out in **X/Y PHYSICAL space**. A logical bar-stack tiling is meaningless because a bar's strips sit on multiple different rig parts.

**Linear = uniform-only; spatial effects need baked 2D coords** (Dave course-correction, cLD had missed it): a subfixture group built as a LINEAR/compact dot-range selection (no Grid cursor) is **UNIFORM-VALUE-ONLY** — good for a single color change or a whole-group pop, useless for effects, because a phaser/MAtricks across a linear selection walks selection order, not space. For ANY spatial effect (chase/wave/figure) the cells must carry **2D grid coordinates baked into the Group at Store**. A laid-out group also serves uniform recalls, so it is strictly more capable than the linear one. The six whole-rig linear subfixture groups (320/321 PIX, 420/421 JDC, 1320/1321 PLINE) are kept as the **uniform layer** beneath the per-truss laid-out cell groups.

Two build lanes for the 2D coords: (1) **GridStore (GS)** per fixture type — elegant, but multi-fixture recall is nondeterministic AND the bake does not survive a repatch (see `gridstore-keyword-and-fixture-type-write`, `gs-multifixture-recall-unreliable`); (2) **manual Grid X/Y cursor baked into the Group at Store** — the RELIABLE carrier (Dave: Groups hold, GS does not). See `grid-cursor-cli-recipe-for-2d-group-layouts`.

**Z ruling (Dave, 2026-07-21):** cells are laid out X/Y, layers go in SEPARATE groups, **NO Z stacking**. Z is not worth it for pixel/cell layouts — a separate group programmed right beats Z, and effects on a Z-stacked layout go "willy-nilly." Reach for Z only for genuine architectural / fancy dimensional lighting. This deprioritizes the standing Z-occupancy verify (`subfixture-down-up-cli-navigation-and-grid-stacking`) as a practical matter — Z is not needed, not disproven.

**Which rig types actually carry a cell split** (live handle census, 2026-07-21): ONLY **JDC1** (plate/beam) and the **ACME / STROBE-3-IP pixel lines** (color/beam) carry a functional subfixture split. **Mac Ultra Wash** (2xx, `MacUlWsh`) has 2 subs (main + Instance2, likely an aura ring) — not single-cell, note for wash pixel work. **Robe Pointe** beams (5xx) and **Proteus Lucius** (11xx) are flat, 0 subs.

The physical X/Y cell mapping is a **chosen convention pending warehouse verification** (FID→X direction, top/bottom color rows) — see `acme-pixel-line-ip-anatomy` for why the GDTF cannot supply it. The per-truss laid-out cell groups built this way live in the subfixture layer of `tourshow-group-contract-v01`.

History: none — doctrine dictated live across the 2026-07-21 subfixture session; the linear-vs-laid-out course-correction and the Z ruling both landed the same session.


### subfixture-down-up-cli-navigation-and-grid-stacking ⚠ VERIFY
**Down/Up navigate into sub-fixtures via CLI; multipart bars stack inside the parent's single grid cell by default — GS changes Down's propagation, dot-range Thru selection is a third lane; Z-occupancy still unverified**
*when:* Before programming multipart/sub-fixture bars (e.g. pixel bars) via CLI Down/Up navigation, before trusting that a Z-axis MAtricks set actually separates stacked subs, or before assuming which of the three sub-layout lanes (Down-stack / GS-propagated / dot-range-selected) is in play


**`Down` works as a pasted CLI keyword** (confirmed OK in command history).

**Verified behavior:** Group 105 (6× Pixel Line ACME) + `Down` → **288 Fixtures Selected = 48 leaf subs per bar** (6 bars × 48 = 288). A second `Down` is a **no-op** (already at the deepest level — there's an implicit `Up` counterpart for navigating back out).

**Sub-stacking rule:** subs do **NOT** spread across the selection grid's X axis — they **stack inside the parent fixture's single grid cell** (the cell display shows a truncated list like `201.1–201.4 + "…"`). Y rows stay empty. This means the one-fixture-one-cell rule from `selection-grid-and-fixture-cell-model` holds at the PARENT level, but multiple leaf subs collapse into that same one cell rather than each claiming their own.

**[VERIFY] Z-occupancy — open question, unresolved as of the 2026-07-14 wrap:** a probe was fired to test whether subs can be separated on the Z axis — `Set Selection MAtricks "Z" 2 ; At Full` (both commands returned OK in command history) — but **visual confirmation never happened**; programmer state was cleared at session handoff before the result could be checked. **Verifies with:** re-fire the same probe on a multipart fixture and visually confirm (screenshot or 3D view) whether the subs actually separate on Z, or whether Z is subject to the same stacking behavior as X.

**Deprioritized 2026-07-21 (Dave's X/Y-only ruling):** Dave has ruled Z out of practical use for pixel/cell layouts — cells are laid out X/Y and any additional layer goes in a SEPARATE group, never Z (Z only for genuine architectural/dimensional work; see `subfixture-cell-architecture-doctrine`). So this Z-occupancy question is now **parked, not blocking** — Z is not needed, not disproven; re-probe only if an architectural Z effect is ever actually wanted.

**Stale cross-reference — 2026-07-14 repatch:** this drill was run against **Group 105 = 6× Pixel Line ACME at FID 201–206** (and Group 104, presumably the JDC1 equivalent at FID 101–104) in the pre-repatch sandbox. The 2026-07-14 template-rig repatch **reassigned FID 101–148 to spots**, overwriting that numbering — **Groups 104/105 are stale** and must be re-pointed at the fixtures they now actually reference before reusing this drill's group numbers. See `tourshow-template-rig-patch-and-layout-state`.

**Three distinct sub-layout lanes clarified 2026-07-15 (multi-instance session):** the `status: verify` on this file is specifically about the Z-occupancy question below — the X-axis behavior is now well characterized across three separate, non-contradictory lanes:
1. **`Down`-expansion, no GS stored** — stacks in the parent's one cell, as described above (the original 2026-07-10 finding).
2. **`Down`-expansion AFTER a `GS` (GridStore) bake** — instead PROPAGATES the stored layout, tiled per fixture, across the grid (see `gridstore-keyword-and-fixture-type-write`). But this propagation is **not always reliable on multi-fixture recall** — see `gs-multifixture-recall-unreliable` for the failure signature and the doctrine that Groups (baked at Store time) are the trustworthy carrier, not GS (2026-07-21: a GS type-bake also does not survive a repatch — a second, independent reason Groups are the durable carrier).
3. **Explicit dot-range `Thru` selection** (e.g. `Fixture 301.1 Thru 16`, no `Down` involved at all) — see `subfixture-thru-range-syntax`. Without `Grid X/Y` cursor guidance this compact-packs onto one row in selection order; paired with Grid-cursor moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`) it lands each sub-range block at its own specified cell. A GS-stored type layout does **not** apply to this lane — GS only engages on `Down`-expansion.

History: none — first run live 2026-07-10; Z-occupancy remains open as of the 2026-07-14 wrap (programmer state cleared at handoff before visual confirm). 2026-07-15: clarified that the stacking rule is the default/pre-GS case specifically, and cross-referenced the two other sub-layout lanes (GS-propagated, dot-range-selected) discovered the same session — Z-occupancy itself still not re-probed. 2026-07-21: Z-occupancy verify deprioritized by Dave's X/Y-only ruling (parked, not blocking); the GS lane also confirmed not durable across a repatch.


### subfixture-grid-compact-collapse-technique ⚠ VERIFY
**[VERIFY] Collapsing a spread sub-layout to compact: remove grid coordinates from the selection, or via toolbar commands — mechanics UNKNOWN**
*when:* Before attempting to collapse/compact a spread-out sub-fixture grid selection back down — this names the technique Dave described, but the exact mechanics are not yet drilled; don't assume a specific command sequence from this file alone


From Dave's layout-ratify dictation: a spread sub-layout can apparently be collapsed back to compact either by **REMOVING THE GRID COORDINATES** from the selection, or **via toolbar commands**.

**Mechanics are UNKNOWN.** This is a named technique, not yet drilled. Do not assume a specific command sequence from this note — it names the destination (spread → compact) and two candidate approaches (coordinate removal vs. toolbar), not verified steps.

**Verifies with:** drill this alongside the toolbar pass (Dave's task 6).

**Not to be confused with** `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle`'s `Preserve GridPositions` toggle — that toggle controls compact-vs-sparse at the moment a Layout-view lasso selection is CAPTURED into the selection grid. This note is about collapsing a selection that's already spread out on the grid — a different (though related-sounding) operation, and on the sub-fixture/multi-instance grid rather than the Layout system.

History: none — dictated 2026-07-15, split off from the same INBOX line that already yielded `jdc-look-a-poppy-and-look-b-paired-beams` and `gridstore-keyword-and-fixture-type-write`. This last remaining fragment was carried forward undigested until the 2026-07-16 run since mechanics were never drilled — flagged, not fabricated.


### subfixture-thru-range-syntax
**Sub-range Thru syntax settled: continuation at the deepest addressed level; multi-fixture ranges distribute the sub-range per fixture; verified through three levels (JDC plate/tube branches)**
*when:* Before writing any CLI Fixture selection that reaches into subfixtures via dot notation (`301.1 Thru 16` style), especially across a multi-fixture range — also check `subfixture-down-up-cli-navigation-and-grid-stacking` for how the result lands on the grid


**Settled rule (live 2.4.2.2):** the `Thru` operand continues at the **deepest addressed level of its left operand**.

- `Fixture 301.1 Thru 16` → subs 1–16 of fixture 301, spread on the grid, **16 Selected** ✔ (left side is sub-qualified — `.1` — so the bare `16` on the right continues at sub level).
- `Fixture 301.1 Thru 301.16` → **Illegal object** ✘ (fully-qualified fixture.sub on BOTH ends fails at sub level).
- `Fixture 301 Thru 301.16` → selects **ONLY the .16 endpoint** (left side is fixture-level/bare, so it does not extend a sub-range the way the first form does).

**Repo manual error (3rd confirmed this session):** the manual's CommandLine sample `Fixture 1.1 Thru 1.6` is **wrong** — it matches the fully-qualified-both-ends pattern above, which is Illegal live.

**Multi-fixture sub-range distribution:** `Fixture 301 Thru 312.33 Thru 48` selects subs **33–48 of EACH fixture** in the 301–312 range — the dot-qualifier applies **per-fixture across the range**, not just to the range's endpoint. Probed on 2 fixtures → exactly 32 selected (16 subs × 2 fixtures), confirming the per-fixture read. This also explains the earlier "endpoint-only" result above: `301 Thru 301.16` only has ONE fixture in its range (301 itself), so "per-fixture across the range" collapses to a single sub.

**Three-level dot addressing verified (2026-07-21, JDC1 branches):** the deepest-level-continuation rule holds at level 3. `Fixture 401 Thru 464.1.1 Thru 12` selects plate-pixel subs `.1.1`–`.1.12` of EACH JDC1 401–464 = **768** (export Size=768, items addressed `401.1.1`, IDType 0). The left operand `.1.1` sets the level, so the bare `Thru 12` continues at the **3rd** level, and the multi-fixture range distributes per fixture exactly as it does at level 2. Working forms: JDC PLATES = `401 Thru 464.1.1 Thru 12`, JDC TUBES = `401 Thru 464.2.1 Thru 12`. The corpus had only two-level (pixel-line) confirmation before this.

**Compact-pack corollary:** an explicit sub-range selection made this way, with **no** `Grid X/Y` cursor calls guiding it, **compact-packs onto one row in selection order** — it does not spread itself across a 2D shape on its own. Pairing the same dot-range selections WITH `Grid X/Y` cursor moves (see `grid-cursor-cli-recipe-for-2d-group-layouts`) lands each sub-range block at its own specified cell instead — both lanes were verified the same session. A `GS`-stored sub-grid layout (see `gridstore-keyword-and-fixture-type-write`) does **not** apply here either — the stored layout only engages on `Down`-expansion, not on explicit dot-range Thru selections.

**Dave ratified this as the primary lane (2026-07-15):** direct dot-range entry (`Fixture 301 Thru 312.33 Thru 48 ; Store Group x`) is the primary method for building section Groups on multi-instance fixtures — faster and more direct than composing every block through Grid-cursor moves. It composes cleanly with Grid-cursor placement (above) when a 2D shape beyond one packed row is wanted.

History: none — syntax settled and multi-fixture behavior probed live in one session, 2026-07-15 (an earlier same-day hypothesis that fully-qualified `Fixture 301.1 Thru 301.16` might work was tested and found Illegal, folded into the settled rule above rather than kept as a separate entry). Extended 2026-07-21: the same continuation rule verified at THREE levels on the JDC1 plate/tube branches (`401 Thru 464.1.1 Thru 12` → 768).


### tourshow-fixture-type-recipe-authoring-gotchas
**Fixture-type recipe gotchas: Wash (Dimmer+Color as CHILDREN) needs recipe mode STRICT; QX40 has no Tilt — never give it a Position part**
*when:* Before authoring or copying a cue-part recipe onto a Wash or QX40 fixture on any {TOUR} song — Wash needs STRICT recipe mode, QX40 must never get a Position part


**WASH RECIPES = STRICT.** The Wash fixture type carries Dimmer and Color as **CHILDREN (subfixtures)**, so any recipe touching it must be set to **STRICT** mode — already applied to SONG_T. Card-candidate: an authoring self-verify lint line.

**QX40 HAS NO TILT.** The Position part of the recipe was **DISABLED** on SONG_T for this reason — **never include a Position part for QX40 on any other song.** Card-candidate: an authoring lint line.

**Relation:** `tourshow-floor-package` (QX40 MKII ×7 patched at FID 1401-1407, 25ch mode) · `tourshow-authoring-contract-v01` (the general recipe-authoring contract these are exceptions within).

History: none — captured live 2026-07-29, SONG_T build.


## WASH STRICT law covers phaser lines too, not just value lines — kit needs a post-pass — 2026-07-31 [0731-3cLD]

SONG_D's main sequence landed 12 Strict all-wash sites, **including 3 phaser lines** —
confirming the WASH-recipe-needs-STRICT law (above) applies to **phaser lines, not only
value lines**. The build kit (`ns_emit.py` / the songbuild kit) **only Stricts value lines
by default**; a manual **post-pass** was needed to also Strict the phaser lines targeting
Wash. Future kit work should extend the auto-Strict pass to cover phaser lines on Wash
fixtures, not just value lines.


### tourshow-stb-white-release-ruling
**RULED: keep JDC1 US [STB] — every use needs a (W) white colour preset + an (R) release; the QX40-STB expansion has been binding the wrong colour**
*when:* Before authoring, censusing, or correcting any JDC1 US [STB] site on any {TOUR} song — the ruling, the value-dependent expansion mechanic, the show-wide census, and the release-mapping rule


**RULED (Dave) — KEEP `JDC1 US [STB]`. Every use needs a (W) WHITE COLOUR PRESET and an (R) RELEASE.** Reason: STB's actual intent is a **WHITE STROBE look**, and the strobe channel returns to open on default or Release. **This supersedes an earlier Dave-floated "maybe safer to drop STB" idea** (his physics for the float: strobe channels on QX40/pixel lines start at default open, and default-or-Release returns them open, so on our rig the RGBW LED intensity drives both his RGB and STB lines — programming both looked like a duplicate intensity drive). The float did not survive the census below; **file the ruling, not the float.**

**Consequence: the QX40-STB expansion has been binding the WRONG COLOUR.** It puts the SONG BASE colour where white belongs.

## The value-dependent expansion mechanic (never written down before this)

A **CONTENT value expands 1 line -> 4**: `QX40 MM ALL @ Dimmer.Full` + the content, `QX40 COLOR @ Dimmer.Full` + the base colour — the MM engine carries the figure, the COLOR engine is opened so the strobe cell reads. But **`Dimmer.0` stays 1 -> 1** (`QX40 MM ALL` only — nothing to open on an off line). SONG_J example: 9 STB sites = 4 content (×4 lines) + 5 off (×1 line) = 21 lines, +12 over source. **Anomaly, flagged not changed:** aux 2012 does NOT apply this expansion — {LD}'s `JDC1 US [STB] @ Dimmer.50` shipped as ONE line where the main sequence would have made four; `SONG-J_WORKUP v0.1` called the expansion out as needed in the aux and it did not land (tracked on the MELD AUX tab).

## Show-wide STB census (the numbers that made the drop decidable)

**64 `JDC1 US [STB]` lines show-wide.** Cues where STB and RGB BOTH carry content (the actual duplicate-drive gotcha) are only **8**: SONG_A 9 · SONG_D 6, 12, 14.1 · SONG_L 12.1 · SONG_O 7, 11, 18. Cues where **STB is the ONLY thing driving the QX40** number **21**, across 7 songs (SONG_D 9, SONG_J 4, SONG_O 4, SONG_C/SONG_E/SONG_I/SONG_Q 1 each). A blanket drop would have silenced the QX40 at 21 cues to fix 8 — hence the surgical ruling above, not a drop.

**The 8 STB/RGB collisions are not one shape:**
- **3 harmless** (SONG_O 7/11/18): RGB and STB carry the SAME phaser — one target, one line is a pure simplification.
- **3 real level conflicts**, {LD} driving the two emitters at different levels on purpose (SONG_D 6 & 12: RGB Full vs STB Dimmer.50; SONG_L 12.1: RGB Full vs STB Dimmer.20) — collapsing picks a level and loses his intent.
- **2 different FIGURES on the two emitters** (SONG_A 9; SONG_D 14.1 runs Chorus STB Sine against Verse RGB Sine, and the cLD build already preserves this correctly as `cLD QX40 MM ALL`=Chorus / `cLD QX40 COLOR`=Verse) — collapsing picks a figure.
Only the first group is mechanical; the other two need per-site judgment.

## (W)+(R) correction surface, censused show-wide

**29 STB content sites total, 18 already in built songs** (SONG_D 12, SONG_J 4, SONG_E 1, SONG_I 1) **and 11 in songs not yet built** (SONG_O 7, SONG_A / SONG_C / SONG_L / SONG_Q 1 each). Two sub-shapes:
- **(a) 8 sites where the expansion fired and bound the song base colour** — SONG_D 3.1/4.1/10.1/14.1 carry `cLD NS DEEP BLUE`; SONG_J 8.1/10.1/15.1/23.1 carry `cLD FR COBALT BLUE`. These are actively wrong and want white.
- **(b) 21 sites that are plain STB dimmer levels** (`Dimmer.50`/`30`/`20`) which crosswalked 1:1 to `cLD QX40 MM ALL` with no colour and no release at all — these need (W)+(R) added from nothing.

## Release mapping, RULED (Dave)

JDC1 needs a **Dim 0 cue after the STB is used** so output returns to default. **For US, the QX40 runs double duty, so (R) RELEASE IS THE PREFERRED NEXT CUE instead.** This settles the release map: at the **13 sites** where {LD}'s very next cue already carries `JDC1 US [STB] @ Dimmer.0`, that line becomes a **RELEASE on our side — a substitution, not an added line.** At the **8 sites** where the STB re-fires on the very next cue, no release belongs there at all.

**The release dialect itself needs no new authoring** — see `release-relative-universal-preset-exemplar-proven`: an (R) is an ordinary StandardRecipe bound to a preset whose content is `Specials:Release`, not a new recipe dialect.

## ⚑ Open items — not yet resolved, need a human/Dave call

1. **HOW the (R) release is expressed on the line** — release on the following cue, a part-level release inside the strobe cue so it self-clears, or a `Release` value on the recipe line itself. Standing dialect rule applies regardless: export a live golden before hand-authoring a release-carrying recipe line, since no full exemplar for the STB case specifically exists in the corpus yet.
2. **WHICH white** — one show-wide `cLD STB WHITE` minted once and referenced at all 29 sites, or each song's own white preset. **Genuinely undecided as of this backlog** — do not assume a specific slot address for this preset until Dave rules and it is read live off the console.
3. **Related, still-open pattern question (cue 23.1 of SONG_J):** Dave removed `cLD QX40 MM ALL @ Dimmer.Full` (an expansion line) and `cLD QX40 COLOR @ Dimmer.0` ({LD}'s own line, which fought the expansion's `Dimmer.Full`) — reading as "when the MM engine also carries a phaser, the expansion's `Dimmer.Full` is redundant." The same pattern still stands **unedited** at SONG_J cues 8.1, 10.1 and 15.1 (`QX40 MM ALL` carrying `Dimmer.Full` + `Swell Sine 2`). If this is a rule it belongs in the emitter and those three want the same treatment; if 23.1 was a one-off taste call, leave them. Not resolved — needs Dave's call.

**Relation:** `source-matricks-wrapper-recipe-encoding` (the `Strike M US [STB] (Lin)` wrapper alias this population is also known by). `release-relative-universal-preset-exemplar-proven` (the release-dialect mechanism). `master-default-doctrine` (a related but distinct "flow from the children" ruling — masters, not STB).


## ⭐ OPEN ITEM 2 CLOSED by cLD, 2026-08-03 — R5: ONE show-wide `cLD STB WHITE` at slot **4.83**

The librarian correctly refused to invent this: the slot number is **not in `findings/INBOX.md`**, so it
was not in that run's corpus. It is nonetheless **ruled**, and it lives in three tier-1 artifacts written
the same day:

- `CURRENT_STATE_A0803.1.md` ruling **R5** — "One show-wide `cLD STB WHITE` → **4.83**."
- `TOURSHOW_LOCK_AND_RUN_PLAN_v0.1.md` R5 — "**One show-wide `cLD STB WHITE`**, not a per-song white.
  Slot **4.83** (verified free live: **78-82 taken, 83+ clear**)."
- `TOURSHOW_CORRECTIONS_LEDGER_v0.2.md` C3 — "`cLD STB WHITE` → slot **4.83** (verified free)."

So: **one white, show-wide, at 4.83, referenced at all 29 sites** — not a per-song white. Open item 2
above is settled; items 1 and 3 stand.

**The process lesson is the durable half, and it is a filing defect, not a librarian error:** a ruling
that lands only in a state/plan/ledger file and never in `findings/INBOX.md` **is invisible to the
librarian and therefore never reaches the corpus.** State files are rehydrated and archived; the corpus
is what survives. **Any ruling written into a state, plan, or ledger file must ALSO get its one raw line
in the INBOX**, or the next spine regeneration silently drops it. Caught here because the librarian
flagged the discrepancy instead of inventing the number.


## ⛔ STANDING RULE — FILING DEFECT FOUND ON THIS CONCEPT, 2026-08-03 [0803-2cLD]

**This concept is itself the paid-for case.** R5 (`cLD STB WHITE` → slot 4.83, verified free, sites 78-82 taken / 83+ clear) was ruled and recorded in `CURRENT_STATE_A0803.1`, `TOURSHOW_LOCK_AND_RUN_PLAN_v0.1`, and `TOURSHOW_CORRECTIONS_LEDGER_v0.2` (ledger item C3) — but it never got a `findings/INBOX.md` line, so it was invisible to the librarian, which correctly refused to invent it rather than file a ruling it had never been shown.

**STANDING RULE: any ruling written into a state file, a plan, or a ledger must ALSO get its own raw line in `findings/INBOX.md`, or the corpus never sees it.** State files get archived; the corpus is what survives. Writing a ruling only into a working document is not filing it — filing means putting it on the librarian's actual input surface. cLD patched this concept by hand this session as the immediate fix; this note generalises it into the standing rule for every future ruling.

## STB EXPANSION IS VALUE-DEPENDENT, 2026-08-03 [0803-2cLD]

The prework-sheet STB expansion note is **value-dependent**, not blanket: a **CONTENT value** (a real colour, not black/off) expands **1→4** lines and needs both **(W)** white and **(R)** release per R3; **`Dimmer.0`** (already off) stays **1→1** and needs **neither**. First pass labelled every STB line as needing (W)+(R) regardless of value, which would have overstated the correction surface by **2x**.

**STB CONTENT sites in the remaining (unbuilt) songs = 9** — SONG_O 7, SONG_L 1, SONG_Q 1. This reconciles exactly with corrections-ledger item C3's 11-site figure for all unbuilt songs, minus the 2 songs it also covered that are already built (SONG_A, SONG_C).

**Relation:** ledger C3 (`TOURSHOW_CORRECTIONS_LEDGER_v0.2.md`) carries the full 29-site release/white map and the 13/8/8 release-disposition split (R4).

---
**⚑ Librarian note (not part of the concept body — for cLD, remove before or on apply):** this run could not confirm `tourshow-stb-white-release-ruling` exists in the accessible `concepts/SPINE.md` snapshot (grepped, zero hits — see RUN_REPORT.md). Writing this amendment on the dispatch brief's explicit word that cLD hand-patched it live this session. If the file does not in fact exist at apply time, promote this content into a new concept instead of appending it.


## STB correction sheet generated, per-site — 2026-08-03 [0803-2cLD]

**`generated/desk_pack/STB_CORRECTION_SHEET.csv` generated: 29 content sites — matches ledger C3 exactly — 20 in built songs, 9 in songs to build.** Release disposition per R4: **12 SUBSTITUTE / 9 ADD / 8 NO-RELEASE.**

**⚑ One-site discrepancy vs. ledger C3's 13/8/8 split** — totals agree at 29, but one site classes differently between the two sheets. This sheet takes the **STRICT reading**: the next cue must carry `JDC1 US [STB] @ Dimmer.0` specifically for a site to count as a SUBSTITUTE. Not reconciled against ledger C3 as of this filing; both numbers stand until a human resolves which site classes correctly.

The per-site sheet names every site individually, so the discrepancy — and the whole correction surface — resolves at previz on one look.

**Relation:** ledger C3 (`TOURSHOW_CORRECTIONS_LEDGER_v0.2.md`, the 13/8/8 figure this sheet's 12/9/8 disagrees with by one site).


## ⭐⭐ (W)+(R) OBJECTS NAMED AND SPECCED — both remaining ⚑ answered, 2026-08-03 [0803-2cLD]

**RULED (Dave).** Final names: **(W) `cLD LED WHITE`** · **(R) colour `cLD LED (R)`** · **(R) beam `cLD RATE (R)`** (`cLD ` prefix confirmed against the standing namespace law — see `cld-sandbox-and-namespace`). **Collision-checked against {LD}'s pools show-wide: zero exact matches** — the silent `#2` auto-suffix trap (`cld-sandbox-and-namespace`) will not fire on any of the three.

**⚑ Naming note, flagged not asserted:** this appears to be the same object OPEN ITEM 2 (below) closed as `cLD STB WHITE` at slot 4.83 (R5) — same slot, a different name now on file. Treat **`cLD LED WHITE`** as the name of record going forward; `cLD STB WHITE` was the working label carried in the state/plan/ledger files R5 was sourced from. This correspondence is a librarian inference from the slot match (4.83), not an explicit renaming statement in the source line — worth a console-side confirm.

**Slots:** **4.83** = (W) `cLD LED WHITE` · **4.84** = (R) colour `cLD LED (R)` (pairing inferred from listing order and consistency with R5's 4.83; both verified clear — 78-82 taken / 83+ clear). ~~**Beam slot UNKNOWN** — {LD} occupies **Beam.1 Open / .2 RateFast / .3 RateMed / .4 RateSlow**, so `cLD RATE (R)` has no home yet. Needs **one console read**, alongside the still-open QX40 strobe attribute name (see `release-relative-universal-preset-exemplar-proven`) — **two reads, one visit.**~~ **Corrected 2026-08-05 — CLOSED at Beam 5.8, see bottom of file.**

## ⭐ OPEN ITEM 1 CLOSED (Dave) — the (R) is a PAIR, not one preset, 2026-08-03 [0803-2cLD]

**Answers "HOW is the (R) expressed."** The QX40-STB expansion drives BOTH the MM/colour engine and the beam rate, so a release takes **one release preset in EACH pool the expansion touches**: a colour release (`cLD LED (R)`) and a beam release (`cLD RATE (R)`). The `Position.Release Relative` dialect (`release-relative-universal-preset-exemplar-proven` — a Universal preset carrying `Relative="Specials:Release"`, bound by an ordinary StandardRecipe) still applies to each — the same mechanism, used twice, not a new dialect. This is more than the corpus held before this ruling.

## ⛔ SCOPED EXCEPTION TO A HARD RULE, RULED AND RECORDED IN THE FOREGROUND, 2026-08-03 [0803-2cLD]

**All three objects above store GLOBAL, not `/Universal`.** Dave: *"global so only our QX40 look at it."* A scoped, deliberate exception to the standing `/Universal`-on-every-store law — see `universal-presets-emitter-aware` for the exception recorded against the rule itself and why the rule's purpose is served, not broken, here. Already written into `cld_submap.py` and `CARD_AUTHORING.md` so a future session does not "correct" it back to Universal. Carried caveat, not a blocker: the Global-anchor portability verify item still applies in principle, but the QX40 is cLD's own floor fixture and travels with the show.

## ⭐ OPEN ITEM 3 NARROWED — cue 23.1 pattern settled as ROUTING, not a rule, 2026-08-03 [0803-2cLD]

**RULED (Dave) — SONG_J is on the clean-up pass.** This settles open item 3 (below) as a **routing call**: the `Dimmer.Full`-beside-a-phaser question at SONG_J cues 8.1/10.1/15.1 is handled **per-site by eye** in the clean-up pass, does **NOT** enter the emitter, and **no other song inherits it**. Ledger C4 + C5 both re-routed. **The general question — is `Dimmer.Full` beside a phaser always redundant? — stays open**, simply not generalised off SONG_J. SONG_J's own build record: `tourshow-seq2010-song-j-build-record`.

## Open items, re-stated 2026-08-03 [0803-2cLD]

Of the original three ⚑ below: item 2 (white naming/slot) closed same day, earlier session; item 1 (HOW the (R) is expressed) closed above; item 3 (cue 23.1 generalization) narrowed to routing above. **Genuinely still open:**
1. ~~**Beam slot for `cLD RATE (R)`** — needs one console read ({LD} holds Beam.1-4, see above).~~ **CLOSED 2026-08-05 — Beam 5.8, see bottom of file.**
2. **QX40's own strobe attribute name** — needs one console read, same desk visit as the beam slot. **Still open as of 2026-08-05** — this was the one console read NOT answered by the beam-slot visit.
3. **Not song-j-scoped:** is `Dimmer.Full` beside a phaser always redundant, in general? Stays open.


## cLD resolves the two inferences the librarian flagged — 2026-08-03 [0803-2cLD]

The pass-4 librarian correctly refused to assert two things the backlog did not state.
Both are cLD's to settle, and both are settled here:

1. **`cLD LED WHITE` IS the object R5 called `cLD STB WHITE` — it is a RENAME, not a
   second object.** R5 ruled "one show-wide white for all 29 STB sites" and verified
   4.83 free; Dave later named the actual objects `LED White` / `LED (R)` / `Rate (R)`.
   Same object, same one-show-wide intent, Dave's name. **`cLD STB WHITE` is a dead
   placeholder — do not mint it.**
2. **The 4.83 → (W) / 4.84 → (R)-colour pairing is cLD's ASSIGNMENT, not Dave's
   ruling.** What Dave ruled is the names and the store mode; what R5 verified live is
   that 78-82 are taken and **83+ is clear**. Which of the two clear slots takes which
   preset is arbitrary and may be re-picked at the desk without breaking anything —
   nothing binds them by slot, every bind is by name.

~~**Still genuinely unknown and needing a console read: the Beam pool slot for
`cLD RATE (R)`.** {LD} occupies Beam.1 Open / .2 RateFast / .3 RateMed / .4
RateSlow. Read it on the same desk visit as the QX40 strobe attribute name.~~
**CORRECTED 2026-08-05 — see the closing section below.**


## ⭐⭐ BOTH REMAINING CONSOLE READS ANSWERED — BEAM SLOT CLOSED, 2026-08-05 [0805cLD]

**`cLD RATE (R)` is programmed at Beam `5.8`** (pool "Beam", slot 8) — closes the "Beam slot
UNKNOWN" open item above ({LD} held Beam.1-4). This was one of the two console reads that
had been owed; **the QX40's own strobe attribute name is the remaining open read.**

**All three (W)+(R) objects the R7 correction pass needs now exist:** `cLD LED WHITE` 4.83 ·
`cLD LED (R)` 4.84 (colour, both already on file above) · `cLD RATE (R)` Beam 5.8 (beam, new).
Storage mode Global for all three, consistent with the scoped exception already ruled on this
concept.

## R7 (W)+(R) correction pass — UNBLOCKED, and SONG_L adds 2 sites, 2026-08-05 [0805cLD]

With the STB trio closed (above), **the R7 (W)+(R) correction pass is unblocked.** SONG_L
contributes **2 sites** to the surface: main sequence cue 12.1 (`Dimmer.20`) and aux 2213
(`JDC1 US [STB] @ Dimmer.30`) — both plain STB dimmer-level lines shipped 1:1 with no colour
and no release, matching shape (b) above ("21 sites that are plain STB dimmer levels... need
(W)+(R) added from nothing"). The aux site matches the SONG_J aux 2012 precedent: the
expansion does not fire in an aux there either. Both logged, not fixed, in
`tourshow-seq2210-song-l-build-record`.

**⚑ Librarian note on the running total:** the last count on file in this concept's own body
("Show-wide STB census" section above) is **29 STB content sites**. State tracking outside
this concept (`CURRENT_STATE_A0805.1.md`) carries the surface at **34** after SONG_L's +2
— i.e. it was already at **32** before this session, per that same state file. That 29→32 step
happened in some earlier session but, per this concept's own STANDING RULE above ("any ruling
written into a state file... must ALSO get its own raw line in `findings/INBOX.md`, or the
corpus never sees it"), it never reached `findings/INBOX.md` and so was never available to any
librarian run to file into this concept's own body. **This concept's own 29-site figure is
therefore stale and the corpus does not currently hold the intermediate 29→32 evidence** — a
repeat instance of the exact filing-defect this concept already documents about itself, not a
new kind of miss. Flagged for a human/cLD decision: backfill the missing 29→32 step (find its
source and file it), or accept the state file as the count of record going forward.

**[0805-2cLD] EXTENSION — emitter scoping law:** the (W) white is a BLANKET law (all correction-sheet rows want it); the (R) release is a PER-SITE disposition — ADD 9 / SUBSTITUTE 12 / NO RELEASE 8 — so any blanket release rule is wrong at 8 sites by construction. First patch cut emitted (R) at every Dimmer.0 STB site; the SONG_A byte-exact regression refused it (122→124 SRs); content-sites-only scoping restored 5/5. The direct-value STB branch gap WAS the correction sheet: all 21 "no colour bound at all" rows were direct-value sites the old emitter shipped bare. **Console-vs-corpus naming (live read):** 4.83 = "QX40 Only W" · 4.84 = "QX40 Only W (R)" · Beam 5.8 = "QX40 STB (R)". None carry the cLD prefix. Slot-form binds unaffected; a census-by-NAME searching corpus names reads ZERO. Fix the corpus, not the console.

History: extended 2026-08-05 [0805-2cLD] — (W) blanket / (R) per-site scoping; content-sites-only emitter restored SONG_A 5/5; direct-value branch gap explained the 21-row correction sheet.
History: corrected 2026-08-05 [0805-2cLD] — live console names for the trio (QX40 Only W 4.83 · QX40 Only W (R) 4.84 · QX40 STB (R) Beam 5.8) replace corpus names; census by NAME must use the live names.


### tourshow-whole-fixture-block-law
**tourshow whole-fixture block law — per-fixture-family MAtricks block size ({LD} Strike M=14, our JDC1=12, QX80/QX40=5), tour-variable**
*when:* Before setting or retuning an XBlock/XShuffle value on any MAtricks pool object meant to read fixture-as-unit — block size is per fixture MODEL, not a universal constant, and should be expected to retune house-by-house as fixture types change on tour


**Whole-fixture block law (Dave, ruled at the desk post-v.67):** for looks meant to read **fixture-as-unit** (the whole fixture moves/steps together, not cell-by-cell), the MAtricks block size is a **per-fixture-family number**: {LD}'s Strike M reads in **groups of 14** = whole fixture together; our **JDC1 blocks in 12s**; our **QX80/QX40 line blocks in 5s**.

**Fixed at the POOL level so binds inherit it automatically:**
- `144` → **`cLD SHUFFLE 5 B5`** (`XBlock=5 XShuffle=5` — QX40/QX80 whole-fixture shuffle).
- `145` **`cLD WING 2`** += `XBlock=12` (plates/JDC1 whole-fixture wings).
- NEW `146` **`cLD SHUFFLE 5 B4 W2`** (`XWings=2 XBlock=4 XShuffle=5` — the spots-verse look).

**Rationale for the Rivale retune (144→371):** the original MAtricks `144` now carries `B5` (QX40-sized blocks) — the wrong unit for Rivale fixtures. `371` **`Diamond Lite`** (`XWings=2 XGroup=3`, a pre-existing pool object) fits Rivale instead. Confirmed exactly right by Dave on readback.

**Generalization (Dave, explicit): block numbers are per-fixture-MODEL and TOUR-VARIABLE.** Expect block retunes house by house as fixture types change — this is not a one-time setting, it is a parameter that travels WITH the fixture inventory, not with the show.

**Future authoring rule:** propose `Block=<family number>` on any phaser/MAtricks sheet entry for a figure meant to read fixture-as-unit, rather than leaving block size implicit or copying another family's number.

**Readback method:** MAtricks Lua properties (`XBlock`/`XShuffle`/`XWings`/`XGroup`) read clean via handle indexing with a `pcall` guard; a `'None'` filter is needed on the walk. The SR-line-level MAtricks property name is `'MAtricks'`, valued as the string `'MAtricks N'`.

**Relation:** `matricks-store-time-embed-travels-with-preset-export` for how to read an INHERITED figure's block/wing/shuffle literals off its export rather than inferring them. `tourshow-seq1210-song-c-build-record` for the desk session this law was ruled in.


## PLINE joins the block-size table at 16 — 2026-07-31 [0731-3cLD]

SONG_D's MAtricks workup confirms **PLINE (P-Line) blocks in 16s** for
whole-fixture-as-unit reads — `B16` on a P-Line figure catches the WHOLE pixel line as a
single unit. PLINE joins the per-fixture-family block-size table: **QX40=5, JDC1=12,
PLINE=16** ({LD}'s Strike M=14 remains the non-cLD reference point). MX `147 SHUFFLE 5
B16` is the pool object carrying this (live-read `B16 S5`).


## ⭐ BLOCK LAW EXTENDED 2026-08-01 [0801cLD] — blocks can be FRACTIONAL, not only whole-fixture

**Dave ruled (on SONG_H): a block can legitimately be a FRACTION of a fixture's whole-block number, and the fraction is a deliberate spatial choice, not a translation error.** Example: **PLINE `B8` = .5 of the whole-fixture 16-cell block** — the half-fixture read IS the intention for that figure. So the per-fixture-family table this concept documents (QX40=5, JDC1=12, PLINE=16 — see also the PLINE=16 addition already in this file's `History:`) gives the WHOLE-fixture number; authoring a deliberate fraction of it (e.g. half) is a legitimate spatial choice to recognize when spec-reading {LD}'s figures, not evidence of a copy/translation error.

**Concrete instances from the same session:** {LD}'s `B8` on his CL/PLINE population was kept as-is on our side — `B8` (`MX 156 cLD S5 B8`). His `B14`/`B7` on JDC/Strike M crosswed to our `B12` (`MX 155`) — the whole-fixture number for our JDC1, per the existing table, since that particular figure was NOT a deliberate fraction.

**Consequence for future spec-reads:** when an inherited figure's block number doesn't match a fixture family's whole-fixture number from the table, check whether it divides cleanly (a plausible deliberate fraction) before assuming it is wrong or needs correcting to the whole-fixture number.

## Family number also rules an XGroup value, not only XBlock — 2026-08-05 [0805cLD]

**RULED (Dave), SONG_L MX 183:** the object binds `cLD QX40 COLOR`, so it takes
**`XGroup=5`** — our QX40's family number from the table above — **NOT {LD}'s `14`** (his
Strike M number), even though `183`'s spatial spec was matched off a Strike M/JDC1 population
of {LD}'s `Intro 1/1 Dim#6`. **The whole-fixture family number governs whichever attribute
carries the fixture-grouping intent on the object actually being built (XGroup here, XBlock
elsewhere) — key it to what the OBJECT binds, not to which {LD} population its spatial
numbers were spec-read from.** Full detail: `tourshow-seq2210-song-l-build-record`.


## Tour-variable, proven — the EU leg, 2026-08

The "expect this to retune house-by-house" caveat above was paid out in full across four venues in one week. The block number is a property of **the venue's fixture**, not of the show:

- venue plates at **14 cells** and tubes at **28** ⇒ mint `B14` / `B28` twins;
- venue units in **1-cell** modes ⇒ **strip Block and Group entirely** (the per-unit texture is automatic), keep wings, shuffle and phase ranges;
- a venue whose fixtures match the file's native cell count ⇒ **nothing to do**.

The doctrine, the selection-scoping rule, the reverse-map discipline and the per-venue receipts are at **`mx-cell-geometry-law`**; the kit that automates it is **`venue-adapt-macro-pattern`**.

History: extended 2026-08-28 (librarian, tour leg) — pointer to the cell-geometry doctrine the tour produced.


## PRESETS & VALUES

### color-consolidation-crowning
**⛔ Colour consolidation law: CROWN the current-stage-truth variant into the base slot BEFORE repointing — repoint every reference first, delete LAST, and save before anything. Skipping the crown snaps the whole show to stale base looks.**
*when:* Before folding a sprawl of per-song preset mints back into one shared version per family — the ORDER is the whole lesson, and the no-crowning variant was executed and rolled back the same day


## Why consolidate at all

Per-song colour mints make a **changeover impossible**: tuning a venue means touching fifty presets instead of one family. The inherited file already contained the intended workflow — a `COLOR_UPDATE` sequence whose cues touch each base colour — and the per-song mint habit had broken that model. Consolidation restores it. Dave's ruling: **one shared version per colour family**.

## The law, in order

1. **SaveShow first.** "A save is better than being careful."
2. **CROWN** — per family, copy the **current-stage-truth** variant (the one Dave has actually tuned) **into the base slot**. Re-Label afterwards: `Copy Preset /o /nc` carries the **source's Name**.
3. **REPOINT** every reference to the survivors.
4. **VERIFY** zero refs remain to the doomed slots. Test-fire.
5. **DELETE LAST.**
6. **SaveShow.**

## The paid-for proof that step 2 is not optional

Round one ran **as-is, no crowning**, on Dave's go. It was mechanically perfect — **407 recipe lines repointed**, per-slot counts matching the scan exactly, zero remaining refs to all 43 doomed slots, 43 deleted, pool 81 → 39. And it **snapped every song to the inherited base looks**, because the bases still held the *original* programmer's content while the tour's look lived in the mints that had just died into them. Dave saw it immediately — *"didn't see you were using the {LD} colors too — now I understand the crowning"* — reloaded, and the run was done again **crowned**: 12 bases crowned from the highest-live-use variants, then the same 407-line sweep, verify, delete, seal.

**The rollback was survivable only because of the export habit.** A hash-diff of the reloaded older file against the pre-surgery pool export showed **all 81 presets byte-identical** — the road's colour tweaks were already in the older file, and nothing had to be reconstructed. Baseline exports saved the day twice in one day.

**What a census cannot see, and must be flagged:** non-colour desk edits made after the reloaded version was cut (cue timing, position tweaks from show notes) are invisible to any file-side check. Only the operator knows (`operators-eyes-are-the-census-of-record`).

## After the fold

- **Legibility is part of the deliverable.** The survivors were renamed with a `cLD` prefix and later relocated into a contiguous, one-screen working palette with a reserve shelf — safe because references are object-bound (`preset-references-are-object-bound-rename-and-move-safe`). The changeover drill became "walk the working palette."
- **Colour-phasers owe the same fold.** Phasers never bound the colour pool **by reference at all** — but their **baked step content** did owe the consolidation, which no reference scan could see (`reference-scan-blind-spots-guid-and-baked-content`). Dave rebuilt nine on the crowned bases and folded seven; verification then ran 4/4 clean, including a full recipe scan showing **233 distinct phaser slots referenced, all resolving, zero dangling**.

**Relation:** `venue-position-crowning-and-shell` (the same crowning move in the position pool) · `preset-references-are-object-bound-rename-and-move-safe` · `reference-scan-blind-spots-guid-and-baked-content` · `pool-discipline-stock-vs-custom` · `save-disk-verify-mtime-delta`.

History: none — planned, mis-run, rolled back and re-run correctly inside one day, 2026-08-19.


### copy-at-occupied-slot-dialog-trap
**Copy At an occupied preset slot pops an overwrite dialog — unattended CLI reads it as 'User Canceled Command' and can leave a default-named husk behind**
*when:* Before running Copy At <pool>.<slot> over MCP/unattended CLI — check the target slot is empty first, or the copy silently fails as a user-cancel and may leave a husk object in its place


**`Copy At` an EMPTY preset slot completes silently (`ok`).** **`Copy At` an OCCUPIED slot pops an Overwrite dialog** — and because the CLI channel is unattended, nothing answers the dialog, so the command returns **`"User Canceled Command"`**, exactly as if a human had actively hit Cancel.

**A husk can be left behind:** if a prior batched Copy was interrupted partway into the dialog (console healthy, PID stable, no crash), the target slot can be left holding a **default-named placeholder object** (observed: a bare `"Preset 1521"`) rather than either the old content or the new copy. A subsequent Copy At that same slot then hits the occupied-slot dialog again, because the husk itself counts as "occupied."

**Fix:** `Delete <pool>.<slot> /NoConfirmation` the husk first, **then** issue the plain `Copy At`. (Alternative: use an `/Overwrite` flag on the Copy command itself, if available for this verb, to skip the dialog entirely.)

**Same family as `assign-layout-merge-dialog-behavior`** — both are cases of a CLI verb behaving silently when the destination is empty and popping a blocking Overwrite/Merge dialog the instant it collides with existing content. Treat "does the target already exist?" as a precondition to check before any unattended batched Copy/Assign/Store-style command, not just for layouts.

**Operational takeaway for batch builds:** after any interrupted or partially-failed batched command sequence, don't assume "no crash, PID stable" means no damage — check every target slot's actual content (name + Guid) before continuing the batch, since a husk reads as legitimate content until inspected.

## Safe lane confirmed 2026-08-01 [0801cLD] — Copy .../Overwrite preserves the bound OBJECT reference through a content swap

**`Copy Preset .../Overwrite` preserves the bound OBJECT** when swapping a preset's content — proven readback: Seq 1410's recipe-line references to `21.1422` survived a baked-content overwrite fully intact. **This is the safe lane for swapping a bound preset's content**: no delete, no re-Assign needed anywhere downstream — every recipe line that already pointed at the preset keeps pointing at it correctly after the overwrite. Distinct from the occupied-slot dialog trap this concept's body documents (which is about an UNATTENDED CLI Copy hitting a blocking dialog) — this is about what happens on a normal, attended Overwrite once the dialog is answered.

## Copy grammar confirmed via MCP `Cmd()`, 2026-08-05 [0805cLD]

**`Copy Preset <src> At <dst>` and `Copy MAtricks <src> At <dst>` both land clean into an
EMPTY slot (7/7 this session)**, confirmed specifically through the MCP `Cmd()` transport (not
just attended CLI). **Occupied-slot behaviour is unchanged** — see the dialog trap documented
above. Note separately: a `Copy` also carries the source object's NAME and can trigger the
silent `#2` auto-suffix even into an empty slot if that name collides — see
`cld-sandbox-and-namespace`'s COPY-verb extension of the `#2` rule; that is a distinct hazard
from the dialog trap this concept documents.

History: none — found live, 2026-07-28, mid-build of the SONG_T phaser template set (`21.1520-1523`); resolved same session. Extended 2026-08-05 [0805cLD]: Copy grammar (Preset + MAtricks, empty-slot case) reconfirmed specifically via the MCP `Cmd()` transport. Relocated to end-of-file 2026-08-05 — `generated/build_spine.sh` truncates a concept's SPINE.md view at the first `History:` line, so the "Safe lane confirmed 2026-08-01" section above had been silently absent from SPINE.md since it was written; this relocation recovers it (gardener rule 4 — nothing deleted, only moved).


## EU tour leg refinement, 2026-08-19 — with `/o /nc` it WORKS, and it carries the SOURCE's NAME

**`Copy Preset <src> At <dst> /o /nc` into an OCCUPIED slot completes cleanly** — the `/o` (overwrite) plus `/nc` pair answers the dialog this concept warns about, and it was the workhorse of the colour crowning (12 bases crowned from live variants in one pass).

**⚠ But the copy brings the SOURCE's Name with it.** The destination silently takes on the source's label, so **every crown/mint must be followed by a re-Label and a readback**. Attested in two pools the same fortnight: crowned colour bases (names restored explicitly afterwards) and minted MAtricks twins (`matricks-property-clear-encoding`). A stale label is what a later by-name lookup will match — and a by-name lookup inside a macro is exactly what a label race breaks (`macro-lua-label-race-needs-wait`).

**Sequence to use: Copy → Label → read the label back → only then let anything reference it.**

History: extended 2026-08-28 (librarian, tour leg) — the `/o /nc` working form and the Copy-carries-the-source-name rule.


### empty-preset-mint-clear-then-store
**Minting a legal EMPTY preset: Clear ×3 then a bare Store into a free slot — an empty preset asserts nothing, which is what makes it a usable SHELL for silencing an ingredient without deleting it**
*when:* When you need a reference target that asserts no values — silencing a pan ingredient, a master row, or any cue ingredient you want to keep structurally but neutralise


**The mint:**

```
Clear
Clear
Clear
Store Preset <pool>.<free slot> /nc
```

Three `Clear`s empty the programmer completely; the bare store then writes a **legal empty preset**. Verified twice: `Preset 2.199 'PAN SHELL'` and `Preset 1.99 'cLD MM SHELL'` (readback `kids = 0`).

**Why an empty preset and not a hard zero.** An empty preset **asserts nothing** — it occupies the reference slot without contributing a value. A hard `0` asserts zero, which on a master is the exact hazard Dave ruled against ("same issue"): a closed gate that someone has to remember to reopen (`master-default-doctrine`, `mm-shell-empty-preset-armor`).

**Why a shell and not a delete.** The recipe line, the cue ingredient and the reference all stay valid and in place. The look is silenced, the structure is intact, and the **restore is a reverse repoint** rather than a rebuild. This is the middle state the whole venue-adaptation kit is built on:

- **pan shell** — 39 refs swept from three pan presets to `2.199` so venue positions could be crowned in without the tour's pan arguing (`venue-position-crowning-and-shell`);
- **MM shell** — mark-cue master rows pointed at `1.99` so every mark opens gate-neutral (`mm-shell-empty-preset-armor`).

**Fill it once and every reference follows.** Because the shell is a single object, giving it content later changes every site that points at it — the reason Dave prefers it to per-site edits.

**Caveat:** a *recipe* line can point at an empty preset (festival-proven). A **raw `AbsPreset` reference is not reachable through the object tree** and cannot be repointed this way — those rows need the desk (`recipe-line-creation-not-wire-reachable`).

**Relation:** `stock-recipe-presets-empty-as-templates` (the *other* kind of empty preset — recipe templates that are empty by design and no-op if called bare) · `venue-position-crowning-and-shell` · `mm-shell-empty-preset-armor` · `store-default-values-keyword`.

History: none — proven at {FESTIVAL} 2026-08-22, reused at {FESTIVAL} 2026-08-26.


### preset-copy-label-mcp-and-century-scratch-slots
**Copy Preset + Label work via MCP; cLD preset scratch slots start at .121 to dodge pool 21's stock occupancy through .113**
*when:* Before creating a new custom preset in pool 21 (or copying a stock preset as a starting point) — the verified MCP copy/label lane and the scratch-slot numbering convention that avoids stock collisions


**Copy Preset 21.1 → 21.121, then Label**, both executed via MCP — both **OK, verified**.

**Pool 21 stock occupies through slot 113** (see `tourshow-stock-recipe-library-inventory` / `tourshow-phaser-pool-identity` for what's in there). The cLD century convention collides with that range, so **cLD preset scratch slots start at 21.121+**.

**Relation:** this is a pool-21-specific instance of the century-numbering convention referenced in `tourshow-festival-group-theory` (Groups/FID domain) — same shorthand pattern, different pool.

History: none — established live 2026-07-17.


### preset-pool-thru-range-syntax
**Preset-pool Thru ranges: `Delete Preset 4.101 Thru 105` = OK; `Delete Preset 4.101 Thru 4.105` (fully-qualified both ends) = Illegal object**
*when:* Before writing a Delete/Copy/Move/Export-style command over a range of preset-pool slots


**POOL-RANGE THRU GRAMMAR (live-verified 2.4.2.2):** `Delete Preset 4.101 Thru 4.105` → **Illegal object**. `Delete Preset 4.101 Thru 105` → **OK**. The right side of a `Thru` must NOT be fully qualified to the same depth as the left side — it continues at the deepest addressed level of the left side (here, the pool-slot number only, not the repeated `4.` pool prefix).

**Generalizes** the existing fully-qualified-both-ends-is-Illegal rule from subfixture addressing (`subfixture-thru-range-syntax`) to PRESET-POOL ranges — this is the same grammar rule, confirmed to apply one level up the addressing hierarchy.

## Export confirmed as a second verb, 2026-08-04 [0803-3cLD]

**PREFERENCE (G=0.3).** `Export Preset <a> Thru <b>` on a fully-qualified-both-ends dotted
range also returns `Illegal object` — the same grammar this concept already documents for
Delete now confirmed on Export too. **Workaround: export per slot** rather than reaching for a
Thru range on Export.

History: none — captured 2026-07-23 [0723cLD] digest run.


### preset-range-export-open-ended-only
**A CLOSED preset range export silently no-ops ('Preset 4.1 Thru 4.103 /File' writes nothing) — the OPEN-ENDED form 'Preset 4.1 Thru /File' works; the echo lies either way**
*when:* Before exporting a preset range for census or baseline — a closed Thru bound produces no file while echoing success; census the disk, never the echo


**Broken (silent no-op):**
```
Export Preset 4.1 Thru 4.103 /File "cld_colorpool.xml"
```
**Working:**
```
Export Preset 4.1 Thru /File "cld_colorpool.xml"
```

The closed upper bound kills the command. The console **echoes success in both cases** — the failure was caught only by listing the target directory and finding no file. This is the same never-trust-clean-echo family as the unquoted import filename (`import-file-argument-must-be-quoted`) and the phantom checkpoint (`saveshow-enumerate-headless-cancel-class`); the tour leg produced three independent instances of it.

**Working practice:** use the open-ended form and let the pool's own extent define the range, then verify the file exists and its byte size is plausible before treating it as a baseline. Pool-baseline exports are the insurance that made two rollbacks survivable this leg (`color-consolidation-crowning`, `venue-position-crowning-and-shell`), so a phantom one is expensive.

**Relation:** `export-sequence-writes-per-name-files` · `preset-pool-thru-range-syntax` · `import-file-argument-must-be-quoted`.

History: none — caught by file census, 2026-08-19.


### preset-references-are-object-bound-rename-and-move-safe
**References are OBJECT-bound, not slot- or name-bound: renaming a preset and MOVING it to another slot both leave every reference intact and re-rendering to the new address**
*when:* Before reorganising a pool mid-show-run — renames and Move Preset At are safe for referenced objects; the risk is elsewhere (hand-typed slot numbers, name-lookup scripts, baked content)


**Proven both directions on a live tour file:**

- **Rename.** The twelve crowned colour bases were renamed to `cLD <colour>`; a repointed reference still rendered `Preset 4.18` afterwards. **Renames do not break references.**
- **Move.** Ten `Move Preset … At …` relocations (e.g. `68→26`, `65→29`, `51→34`, `83→38`) — **references followed the move**, proven by a song's `SUNSET EDGE` reference re-rendering as `Preset 4.29`. Post-move sweep: **zero dead colour refs**.

**Because the binding is to the object, not to its address or its label.** The same family of truth as the `&apos;`-quoting scope finding (`import-resolver-laws`) and the golden exports that survive stale pool names on GUIDs.

## What this makes safe, and what it does not

**Safe:** pool reorganisation for human legibility. The colour pool went from 81 scattered presets to a contiguous, one-screen working palette with a reserve shelf, mid-tour, with no cue edits — the changeover drill became "walk slots 1-22".

**Not safe:**
- **Hand-typed slot numbers.** Anything a human addressed by slot from muscle memory misses after a move. Dave's own note when utilities moved upstairs: recipes ride the objects fine, fingers do not.
- **Name-lookup scripts.** A rename retargets every by-name resolution — including a macro's own mint-if-missing lookup (`matricks-property-clear-encoding`).
- **Baked content.** Anything that *contains* a value rather than *referring* to one is invisible to a reference scan and unaffected by moves — see `reference-scan-blind-spots-guid-and-baked-content`.

**Relation:** `color-consolidation-crowning` (the surgery this made possible) · `reference-scan-blind-spots-guid-and-baked-content` · `pool-labeling-doctrine-inherited-risk` · `import-resolver-laws`.

History: none — rename behaviour confirmed 2026-08-19, move behaviour proven the same day across ten relocations.


### release-preset-design-doctrine
**Our release-preset pattern: a recipe referencing TWO presets (standing color preset + release preset), not stock's baked hard-value pairs**
*when:* Before building a release-color preset — this is the design decision on HOW to build them, distinct from what Release itself does


**Stock behavior (reference point, not our pattern):** pool-21's Release family ships as HARD-VALUE pairs — each preset bakes a color value + a release value together in one 2-step preset. Dave confirmed this live in the phaser editor. See `release-family-ships-stock` for the exact stock inventory.

**Our design:** build release-color presets as RECIPE-style presets that REFERENCE two other presets, instead of baking values —
1. the standing/always-used color preset (the single editable color — one edit point, color authority stays single-sourced), and
2. a release preset.

Editing the standing color preset then propagates everywhere it's referenced, instead of hand-rebaking N hard-coded release presets whenever a color changes.

**Purpose:** this pattern directly serves `tc-bump-button-architecture` — bumps exit via Release, and a recipe-referenced release-color preset keeps that exit color centrally editable rather than duplicated per bump.

**Status:** designed, not yet built — tracked as a console-queue item in `NEXT_ACTIONS_A0716.1.md` ("Build release-as-recipe presets").

History: none — design decided 2026-07-16, captured three times near-identically in the inbox as the session progressed; merged here as one concept.


### release-relative-universal-preset-exemplar-proven
**The release dialect is already in the corpus — Position.Release Relative is a Universal preset carrying Relative="Specials:Release", bound by an ordinary StandardRecipe; an (R) is not a new dialect**
*when:* Before hand-authoring any release-carrying recipe line (an '(R)' on a QC sheet, a bump-exit release, or any other release preset) — a live golden already exists in {LD}'s own file; do not treat release as an unattested dialect


**No desk golden needed — the release dialect is already in the corpus.** Found as the 4th of 4 preset gaps surfaced by the whole-show crosswalk pass (see `tourshow-crosswalk-prework-alias-gap`): `Position.Release Relative` (SONG_H, 1 line) **is a release exemplar.**

**Its embed:** a **Universal preset** whose `PresetData` rows carry `<Step Function='<Attr>' Relative='Specials:Release'/>` — a universal template row (`IDType 2` / `ID 1`, `Selective='Global'`) plus per-fixture rows.

**The SEQUENCE-LEVEL bind is a completely ORDINARY StandardRecipe** — `Preset=`/`Values=` pointing at the preset, nothing special on the recipe line itself.

**Conclusion: an (R) is not a new recipe dialect at all — it is a normal preset bind whose CONTENT is `Specials:Release`.** The whole release mechanism lives inside the preset's own PresetData, not in any special recipe-line syntax. This unblocks the STB (W)+(R) work (see `tourshow-stb-white-release-ruling`) — the only genuinely open item left for that work is the QX40's own strobe attribute name, not the release mechanism.

**Relation:** `release-mechanism-fundamentals` (what Release does at the channel level — falls back to the next claim rather than forcing zero). `release-preset-design-doctrine` (our existing recipe-referencing release-preset pattern — this exemplar confirms the same "reference, don't bake" shape appears natively in {LD}'s file too). `release-family-ships-stock` (the stock hard-value-pair Release family — a different, coexisting release idiom). `tourshow-stb-white-release-ruling` (the downstream consumer of this dialect fact).


### show-color-proof-is-colour-name-authority
**RESOURCES/SHOW_COLOR_PROOF/ is the colour-NAME authority for authoring — never read a colour name off the console**
*when:* Before naming, storing, or cross-checking a colour preset's NAME — consult RESOURCES/SHOW_COLOR_PROOF/, not a console value


**CONSTRAINING (G=0.7).** `RESOURCES/SHOW_COLOR_PROOF/` supplies the colour NAME for
authoring — never a console value. A console read of an existing preset's name/value is not
an authority; if the correct name is needed, it comes from this folder.

**Relation:** `show-direction-doc-and-color-sync-workflow` documents the broader colour-
authority hierarchy (frame-grabs + Color-Sync + palette lock = PRIMARY; {FESTIVAL} showfile
colours = intel-only SECONDARY) — whether `SHOW_COLOR_PROOF/` IS that PRIMARY authority's
storage location, or a separate/later artifact, is not stated by the source and is not
asserted here. `universal-presets-emitter-aware` covers the separate question of how a stored
colour preset resolves across fixture types once named.


### tourshow-dimmer-preset-ladder
**Dimmer preset ladder is fully mapped and CLOSED: Full=1.5 · 75=1.7 · 50=1.9 · 30=1.10 · 20=1.11 · 10=1.13 · 0=1.15 — descending, and NOT contiguous**
*when:* Before referencing any dimmer-level preset by slot in a recipe bind or authored XML — numeric preset NAMES parse as slot indexes, so these must be addressed by the slot numbers below, never by typing the numeral as a name


Read live off pool 1 on 2026-07-31:

| Level | Slot |
|---|---|
| Full | **1.5** |
| 75 | **1.7** |
| 50 | **1.9** |
| 30 | **1.10** |
| 20 | **1.11** |
| 10 | **1.13** |
| 0 | **1.15** |

**Descending, with gaps** — the slot number does not encode the level and the spacing is irregular. Do not extrapolate a missing rung; read it.

**This closes the standing "Dimmer '20'/'30' slots" ruling** carried as owed in `tourshow-crosswalk-prework-alias-gap` and flagged UNKNOWN in `CROSSWALK_CHEAT_SHEET_v0.1.md`. It needed a console read, not a Dave decision — worth noting as a class: some "owed rulings" are just unread facts, and sorting those out of the queue is cheap.

**Why slot-addressing is mandatory here:** several of these presets are *named* bare numerals, and a numeric name in a `Preset=`/`Values=` bind path **parses as a SLOT INDEX, not a name** — so `Dimmer.0` resolves to slot 0 (nil), not to the preset named "0". See `import-resolver-laws`.


### tourshow-fx-preset-dependency-anomaly
**FX White/Red/Green appear in BOTH pool 21 and pool 22 at slots 110-112, despite predefined_phaser.xml having no FX presets — dependency-export routing, not a duplicate import**
*when:* If a preset appears to exist in a pool it shouldn't, per that pool's own source XML — this is the precedent case and its resolution


**Anomaly found during census:** FX White/Red/Green presets sit at pool 21 slots 110-112 AND at pool 22 ("All 2") slots 110-112. But `predefined_phaser.xml` — pool 21's own source file — contains **no FX presets at all**, so their presence in pool 21 isn't explained by pool 21's own import.

**Working explanation:** the pool-22 import (Include Dependencies ON, see `tourshow-stock-recipe-library-inventory`) routed copies to the matching authored addresses in pool 21 as a dependency side-effect, rather than pool 21 having native FX presets of its own.

**Resolution (census closed):** FX Blue — the 4th FX preset, at slot 113 — was confirmed by Dave as something HE created, not a stock/import artifact. This closes the References-section census question (see `tourshow-stock-recipe-library-inventory`).

History: none — anomaly found and closed same session, 2026-07-16.


### tourshow-global-preset-portability-verify-items ⚠ VERIFY
**⚠ VERIFY (data-loss class): GLOBAL preset data reportedly anchors to a real fixture, not the fixture type — can be silently lost on a rig move; countermeasure = Save-Presets-To-FT (untested); posture scoped to careless fixture deletes**
*when:* Before trusting a GLOBAL/universal preset (including any POSITION_WIZ-produced preset) to survive a rig clone or fixture swap — also the home of the (untested) Save-Presets-To-FT portability countermeasure and Dave's 2026-07-21 scoped posture (don't over-gate routine work)


Three practitioner-reported MA3 portability gotchas surfaced by the world-practices research pass (see `tourshow-world-practices-research-intake` for the pass's overall status), all **unverified against our own console** as of this session:

1. **⚠ GLOBAL preset data anchor risk (the one that matters most here):** practitioners report GLOBAL preset data anchors to a REAL, specific fixture rather than to the fixture TYPE — meaning it can be **silently lost** when a rig is cloned or a fixture is swapped/moved. This touches our own universal position presets directly — everything `factory-position-wiz-anatomy-and-porting` and `cld-position-wiz-generic-v01-authored-and-deployed` produce is exactly this kind of GLOBAL/universal preset. **Verify this before trusting the WIZ universals to survive a clone onto a different physical rig** — desk-test a clone/swap and confirm the preset data actually follows the fixture type, not just the original fixture.
2. Converted MA2 profiles reportedly can't travel via MVR.
3. "Stomp" is reportedly no longer an attribute-level technique in MA3 the way it was busked in MA2.

None of these three are adjudicated or desk-verified yet. Citations for all three live in `ARTIST_TOURSHOW_WORLD_PRACTICES_v0.1.md`. Adjudicate and desk-verify before promoting any of them to a hard rule or an active concept.

**Posture update (Dave, 2026-07-21) — scoped, drops out of routine gating:** do NOT let this flag over-gate normal work. It only bites when fixtures are deleted from the patch carelessly; we run backups/checkpoints, and Dave will explicitly call it out when we are actually in could-lose-data territory. Stays `status: verify`, but no longer gates routine programming.

**Designed countermeasure (Dave, UNTESTED in MA3 — verify before leaning on it):** preset data does not persist into the fixture type unless deliberately saved there. Portability lane: **Save Presets To Fixture Type → Export the fixture type** (carry it anywhere) **→ reimport on the target rig → Show Creator setting "Create Presets from FT"** regenerates the presets. Per Dave this mechanism has existed since grandMA v1. This is the designed answer to the anchoring concern above and a candidate lane for the inheritable {ARTIST} file. Sandbox-test queued for AFTER SONG_G programming; patch stays intact until then.

**Messy field alternative (Dave, context):** many show files carry a "DO NOT DELETE" folder holding one unpatched fixture type — keeping the anchor FT resident in the show so global preset data survives, and grabbing a fixture from it when needed. This is the sloppier workaround for the same anchoring problem, vs. the cleaner Save-Presets-To-FT lane above (which requires remembering where your FTs live).

History: none — captured 2026-07-19 from the world-practices research pass; kept as its own concept (rather than folded into the research-intake concept) because of its direct, immediate relevance to the WIZ universal presets already in active use. Extended 2026-07-21: added Dave's deprioritized posture (scoped to careless fixture deletes; stays verify but no longer gates routine work) and the Save-Presets-To-FT → export → reimport → "Create Presets from FT" countermeasure (untested) plus the "DO NOT DELETE" resident-FT field alternative.


### universal-presets-emitter-aware
**Universal presets resolve through each fixture profile's color engine/emitter data — the /Universal store-mode rule applies to ALL preset stores (dimmer included), not just color**
*when:* Before trusting a universal (device-independent) color/dimmer preset to look right across mixed fixture types — especially ahead of a fixture-color pre-match session, before storing ANY preset (dimmer included), or when a universal preset looks off on one profile


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


### venue-position-crowning-and-shell
**Venue position adaptation (Dave's design): take the venue's position set WHOLE and CROWN it into the tour's slots, then SHELL the tour's own pan ingredient — references are object-bound, so restore = re-crown + reverse the map**
*when:* Before adapting a show to a house rig's positions on a festival changeover — this is the system that replaces pointing fixtures by hand, and it is show-proven with ZERO pre-show rig time


## The problem it solves

A festival changeover buys ~25 minutes, of which maybe **five** reach the rig. Washes and spots barely get pointed. Editing cues per venue is impossible; so is re-teaching positions fixture by fixture.

## Dave's design, in four moves

1. **Take the venue's position set WHOLE** — pan *and* tilt. It is a different rig; **their positions are the truth**. Do not synthesise.
2. **CROWN the venue positions into our own preset slots.** One cue ingredient then delivers the full correct position, and **zero cues are edited.**
3. **SILENCE our pan ingredient.** Repoint every cue/recipe reference to our pan presets at **one blank SHELL** (`empty-preset-mint-clear-then-store`). The lines stay, the references stay valid, the touring pan stops arguing with the house rig's geometry.
4. **Leave our pan presets untouched in their slots.** Tour-mode restore = reverse the repoint + re-crown from the baseline export.

## The executed run (receipts)

- **Baseline first:** full pool-2 export (1.3 MB) — **this is the tour restore source** — plus a disk-verified checkpoint.
- **7 crowns:** venue `89→69 · 91→70 · 92→71 · 93→72 · 94→73 · 95→74 · 96→75`, names restored after copy (Copy carries the source's Name).
- **Shell:** `Preset 2.199 'PAN SHELL'` minted empty; **39 references swept** from the three tour pan presets across every main sequence. **The sweep map IS the restore map** and was recorded verbatim, per sequence and per cue.
- **Verify:** zero refs remain to the pan presets; the pan presets themselves intact in their slots; sealed and disk-verified.
- **Result:** the show pointed right with **no rig time at all**. Dave: "Smashed it, with no pre show rig time it was clocked at success."

## Standing notes

- **Record the sweep map as you sweep.** Restore is only exact if the reverse is unambiguous; a per-sequence map resolves same-target ambiguity (the same discipline the venue MX kit needed, `mx-cell-geometry-law`).
- **Full-position shapes carrying old-rig pan can still fight the house.** source-era position presets with pan baked in remained live and referenced — flagged for Dave's eye, with the same shell treatment available in one sweep if they argue.
- **The toggle is the end state:** a FESTIVAL/TOUR macro pair running the saved sweeps in each direction — the same shape the MX kit reached (`venue-adapt-macro-pattern`).

**Relation:** `empty-preset-mint-clear-then-store` · `preset-references-are-object-bound-rename-and-move-safe` (why crowning and shelling are safe) · `color-consolidation-crowning` (the crowning pattern's first home) · `venue-adapt-macro-pattern` · `mm-shell-empty-preset-armor`.

History: none — designed 2026-08-21, executed and show-proven 2026-08-22.


## RECIPES, PHASERS & MATRICKS

### alignment-pairing-vs-proportional-doctrine
**Aligning rig parts with different fixture counts on the grid — pair when counts are close, spread proportionally only when they're far apart**
*when:* Before building a shared-X grid layout for two rig parts with different fixture counts — decide whether to pair or proportionally spread before placing anything


Two techniques exist for lining up rig parts that have different fixture counts onto one shared X window, and Dave's doctrine is about which one to reach for.

**Proportional spread** (the general mechanism): place each part's fixtures across one shared X window at its own step interval (step = window span ÷ fixture count). Any X-axis effect then sweeps all rows at proportionally the same rate, keeping the parts in sync across the window even though their per-fixture spacing differs. Workflow: think through the look, place it on the grid, `Store Group` — chase recipes come later.

**Pairing** (the taste call, drill-verified): when two parts have counts that are *close* (drill case: 16 wings vs. 12 spots), a proportional spread reads as chaotic — the two step intervals only line up at occasional coincidence columns and drift everywhere else. Dave's preferred alternative: align the parts so partnered fixtures share a column and fire together, then place the leftover unpaired fixtures on evenly-spaced columns (drill case: every 4th column). This reads as intentional and clean.

**The rule: pairing beats proportionality when counts are close.** Proportional spreads are reserved for cases with a genuinely large density gap between the two parts (Dave's example: pixel leafs vs. spots), where pairing isn't practical because one part vastly outnumbers the other.

History: none — dictated + drill-verified live 2026-07-14. Worked examples: Group 122 "cLD DS WING ALIGN" (proportional, 12@step4/16@step3 — kept as the density-gap exemplar) vs. Group 123 "cLD DS WING PAIRED16" (paired; later hand-rebuilt mirrored by Dave — see `grid-mirror-symmetry-doctrine`). Full catalog in `grid-drill-exemplar-groups-121-124`.


### assign-cli-recipe-line-grammar
**Assign CLI grammar rebinds recipe-line bind slots live — Assign <obj> At Sequence x Cue y Part z, bare form, object type routes which slot; on an existing empty part it also CREATES the line**
*when:* Before writing or generating an Assign command to rebind a recipe cue-part's Selection/Values/MAtricks live, or to CREATE a recipe line on an existing empty part — the bare-form grammar, the object-type routing table, the create-on-empty-part behavior, and its Recipe-Editor visual readback


**CLI recipe lane CONFIRMED end-to-end (2026-07-17, live 2.4.2.2).** `Assign <obj> At Sequence x Cue y Part z` rebinds a recipe-line bind slot live, in **bare form — no `Property` suffix required**. Demonstrated on `Assign Group 123/124 At Sequence 102 Cue 1 Part 0.1`, live-swapping Selection across a three-characters demo purely by typed command.

**Object-type routing** (`Assign <obj> At Sequence x Cue y Part 0.1`):
- **Group** → Selection slot
- **Preset** → Values slot
- **MAtricks** → MAtricks slot

**Combined with** List readback (dotted recipe-line address form, e.g. `List Sequence 102 Cue 1 Part 0.1`), `Set` Property writes, and the Enabled toggle, this closes recipe lane 2 (previously UNMAPPED in `low-credit-cli-mcp-first-authoring-doctrine`) — now mapped and MCP-payload-ready.

**Visual readback surface:** the Assign/Set confirmations were observed updating live in the RECIPE EDITOR's cells — the editor is a real-time visual readback surface for CLI writes to recipe lines, pairing with `List` as the text-readback lane.

**RESOLVED 2026-07-17** (live Export Sequence 102 capture — see `export-sequence-xml-schema`): after `Assign Preset 22.9`, BOTH the Values prop AND the Preset prop read back "Preset 22.9" — confirmed as a genuine **dual-fill**. The exported `<StandardRecipe>` carries BOTH `Preset=` and `Values=` attrs, both populated with the SAME reference (`"All 2.Wipe In"` in the Seq 102 export) — two attrs actually written, not a single aliased slot exposed under two names.

**Forum-sourced per-type extended forms** (folded from `recipe-line-pool-binding-via-assign`, forum 69993/69919 — Kanarek, robinhood, chrislose; not all live-verified):
- **Core rule:** `Set` with a pool number **silently doesn't bind** — Assign is the verb (consistent with `set-command-unknown-property-fails-silently`).
- **MAtricks ranged:** `Assign MAtricks 6 At Sequence c Cue 1 Thru Part *.*` — Thru-ranged wildcard binds across every recipe line in the cue.
- **Preset at step level:** `Assign Preset a.b At Sequence c Cue d Part 0.1."PhaserRecipeSteps".<step>.<valuesource>` (nests into `recipe-step-level-cli-write-path`).
- **Shape:** `Assign Shape n At … Part 0.1` — trailing `Property "Shape"` suffix optional (chrislose).
- **Group via Programmer:** `Assign Group X At Programmer <part>.<recipe>` (Kanarek) — alternative to the stored Sequence/Cue address, which IS live-verified above.
- Note: the ranged MAtricks Assign may be an alternate write lane into a recipe's own MAtricks (vs the UI editor per `live-selection-matricks-cli-set-syntax`) — not cross-verified for identical results.

## Assign CREATES recipe lines on existing (empty) parts — 2026-07-29, scratch- and live-proven

**On an EXISTING, EMPTY part:** `Assign Group X At Sequence S Cue C Part P.1` **CREATES line `.1`** and binds Selection (readback-verified). A follow-up `Assign Preset ...` binds Values on that same new line.

**On a NONEXISTENT part:** the identical form **fails LOUD** — `"Illegal object"`. **Parts themselves cannot be Assign-created.** (Part-creation mechanic remains unproven — a `Store Sequence Cue Part N` test is queued but not yet fired.)

**Proven twice:** first on scratch (Seq 1990), then at live scale — the SONG_T air-pixel batch created **7 lines** on existing empty `P3 PIX` parts (Mark `G309`×4.52, `2.1`×1.9, `3.1`×4.51, `22`×1.5, `26.1`×4.53, `27.1`×1.15 + `G310`×1.15 dual kill), census **7/7 exact**, `SaveShow v.41` on disk. See `recipe-line-cli-addressing-and-list-readback` for the companion multi-part addressing finding from the same batch (name-form vs numeric-form part addressing).

**Relation:** this is the CLI grammar that promotes lane 2 in `low-credit-cli-mcp-first-authoring-doctrine` from UNMAPPED to PROVEN — see that concept for the full three-lane strategy. See `recipe-lane-lua-readback-grammar` for the companion Lua-side readback grammar, and `recipe-part-property-surface-lua-dump` for the full bind-slot property inventory this routing table is grounded in. `tourshow-fill-layer-rebuild-method` for the SONG_T fill/air-pixel build this create-on-empty-part behavior was proven on at scale.

History: none — established live 2026-07-17. Same day: the dual-fill `[VERIFY]` resolved by a live Export Sequence 102 capture — see `export-sequence-xml-schema`. Extended 2026-07-29: added the create-on-existing-empty-part behavior (and its loud failure on a nonexistent part), proven first on scratch then at live scale on SONG_T's air-pixel batch.


## EU tour leg attestation, 2026-08 — HANDLE assignment is the proven bulk-repoint form

Live on the tour file, readback-exact, on **existing** recipe lines:

```lua
rl.Values   = <preset handle>
rl.Preset   = <preset handle>
rl.Selection= <group handle>
rl.MAtricks = <matricks handle>
```

**Handles, not pool numbers and not name strings.** This form carried every bulk repoint of the leg: **407** colour-consolidation lines, **65** master-migration lines, **39** pan-shell lines, and the per-venue MX repoints (18 / 19 / 19). Piloted on one line with a readback before each full sweep.

**⛔ Boundary:** this reassigns **existing** lines only. Creating a recipe LINE is not reachable from the wire at all — see `recipe-line-creation-not-wire-reachable`. Dave's note the same week: recipe fields **are** assignable by **macro line** (the Assign lane), which reaches further than raw Lua does.

**Pace the batches.** Reassignment invalidates cooked output and triggers recook storms; a timeout right after a write batch indicts console busy-work before the wire (`wire-timeout-vs-console-busy`).

History: extended 2026-08-28 (librarian, tour leg) — handle-assignment attestation and the creation boundary.


### baked-phaser-preset-xml-schema
**Baked-phaser preset XML schema (Export Preset) — Preset>PresetData>per-fixture Phaser>Step; Speed/Measure are 2^24 fixed-point (16777216 = literal 1)**
*when:* Before reading, generating, or hand-authoring a baked-phaser preset XML file (Export Preset lane) — the decoded element shape, encoding pinned: see phaser-preset-xml-measure-speed-fixed-point-encoding


**Export lane:** `Export Preset` → `gma3_library/datapools/presets/<name>.xml`.

**Element nesting:** `<Preset transform-attrs>` → `<PresetData Size=n>` → per-fixture-ID `<Phaser IDType ID Attribute Speed SpeedMaster Phase Measure Selective>` → `<Step Function Absolute Accel Decel Trans Width>`.

A **universal preset ships one `<Phaser>` entry PER PATCHED ID.**

**[VERIFY] Sentinel value:** both `Speed` and `Measure` were observed carrying the value **16777216 (2^24)**, read at capture time as a default/none sentinel. **The literal beat encoding for Measure is UNKNOWN.** Do not hand-author a Measure value in this XML schema until verified — the prescribed verification method is: set Measure via the editor, re-export, and diff against this baseline to read off the actual encoding.

**Relation:** this is the baked/exported-preset schema, distinct from `recipe-xml-schema` (the PhaserRecipe-template schema for recipe presets — a different XML shape entirely). See `measure-not-a-safe-lua-property-part-or-preset` for why this file-side XML is currently the only ground-truth path to Measure's step data (Lua object access is closed). See `export-sequence-xml-schema` for the same cooked/baked `<PresetData>` shape as it appears embedded inside a live Sequence export's Part (alongside a `<StandardRecipe>`, distinguished there by a `Cooked=` attribute) — same cooked dialect, different export lane (Export Sequence vs. Export Preset).

**Color presets use this SAME schema (2026-07-21):** a color preset is just this schema with `Attribute="ColorRGB_R"`/`"ColorRGB_G"`/`"ColorRGB_B"` (three `<Phaser>` entries per fixture, one per channel) and a single static `<Step Absolute=N>` (no motion) — NOT a separate dialect. **`Attribute="ColorAdd"` is wrong and fails SILENTLY on import — empty preset, no error.** The `<Preset>` element carries a `PresetMode` attribute; the exported cLD Amber preset `4.102` reads `PresetMode="Global"` with three `ColorRGB_R/G/B` `<Phaser>` entries — a mechanical example of where that attribute sits in the XML, **not** a recommendation to store show colors that way.

**Store mode — corrected 2026-07-21:** the 19 SONG_G color presets (`4.121-139`) were first authored `PresetMode="Global"` this session, which is the **wrong** store mode for this show. {ARTIST} show colors are RGB *intent* and must be stored **Universal** so they resolve per fixture type through each profile's emitter engine — author as Universal (the `/ForceUniversal` store flag; v2.4 renamed "Universal"→"Generic" in the UI). The store-mode ruling, the Q-value emitter strategy, and the v2.4 global-vs-universal balancing tools all live in `universal-presets-emitter-aware` — that is the home for the color-storage doctrine; this file documents only the XML *shape*.

**Hand-authoring shortcut, corroborated 2026-07-21:** contrary to "one `<Phaser>` entry per patched ID" above (which describes what a console EXPORT produces), when HAND-AUTHORING a preset from scratch for import, a single **universal template row `IDType="2" ID="1"`** is sufficient — it imports and works across every patched ID without enumerating one entry per fixture. Used for both the 19 color presets and the `cLD SONG_G BREATHE` phaser preset (`21.123`) this session. Worked breathe example: 2 `<Step>`s, `Absolute="100"` then `Absolute="30"`, `Accel="-100" Decel="-100"` on both (sine easing) — cloned from the `cld_dimsinus_m4.xml` exemplar. See `phaser-preset-xml-measure-speed-fixed-point-encoding` for this same build's Measure-4 fixed-point corroboration.

**⛔ CORRECTED/EXTENDED 2026-07-28 [0728cLD] — the hand-authoring shortcut above is INCOMPLETE for color presets, and the failure mode is silent.** Cloning only the `IDType="2" ID="1"` universal template row is not sufficient: the `<Step>` element **must also carry `Function="ColorRGB_R"`/`"_G"`/`"_B"`** (re-stating the same attribute value that already lives on the parent `<Phaser Attribute=...>`, this time on the Step itself). **Omit `Function=` on the Step and Import still echoes OK — but lands a NAME-ONLY EMPTY preset** (`Active="No"`, zero `PresetData`): a new silent-failure shape where the **NAME CENSUS PASSES while the content is completely absent** — only an export readback catches it, not a live property/name read. Decimal `Absolute=` values are legal (a live {LD} exemplar carries `98.0026`).

**Working dialect, round-trip verified (v.30, `cLD OW WHITE` 95.7/94.9/92.5 exact):** clone every attribute a live exemplar carries, not just the ones prose describes — `Active="Yes"`, `PresetMode="Universal"`, the universal row's `IDType="2" ID="1"`, plus `GridPos`/`GridPosMatr="2360738"` and `Selective="Global"` on the row, and both `Function=` and `Absolute=` on the `<Step>`.

**Standing rule this forces: export a live golden exemplar before hand-authoring any new dialect variant of this schema** — schema prose (including this file, before this correction) is not itself an exemplar. This is the second live collection to force that rule. See `import-resolver-laws` for the sibling sequence-XML import gotchas found the same session, and `tourshow-seq1510-build-record` for the build this was caught on.

Cross-reference: `set-command-unknown-property-fails-silently` for the same silent-fail-on-bad-property-name class the `ColorAdd` trap belongs to; `xml-file-side-authoring-import-lane-proven` for the import lane this schema is authored against.

History: none — schema decoded live 2026-07-17 from a fresh Export Preset read.

History: encoding [VERIFY] resolved same-day (run 14 merge) — Measure/Speed are 2^24 fixed-point, pinned by export-diff; see `phaser-preset-xml-measure-speed-fixed-point-encoding`. Schema itself export-verified; status promoted verify->active. Run 15 (2026-07-17): removed a stale dispatching-agent flag left over from the run-14 shard merge (its concern was already resolved by the History line immediately above it); cross-referenced `export-sequence-xml-schema` for the sibling cooked-`<PresetData>` shape found inside a live Sequence export.

History: extended 2026-07-21 [0721-2cLD] — color-preset use of this same schema documented (ColorRGB_R/G/B Attribute, PresetMode=Global, ColorAdd silent-fail trap), plus a hand-authoring shortcut (single IDType=2 universal template row) and a worked breathe-phaser Step example, both export-verified live building the SONG_G color presets and breathe phaser.

History: corrected 2026-07-21 (crown-jewels scrub) — the earlier "PresetMode=Global is the store mode" framing was a baked-paradigm artifact and is WRONG for this show; {ARTIST} colors store Universal (RGB intent, emitter-resolved). The ColorRGB-not-ColorAdd fact, the golden-4.102 schema example, the IDType=2 hand-authoring shortcut, and the breathe Step example are all retained — only the Global store-mode endorsement was scrubbed and redirected to `universal-presets-emitter-aware`.

History: extended 2026-07-28 [0728cLD] — corrected the color-preset hand-authoring shortcut: the earlier IDType=2/ID=1-only description omitted the `Step Function=` attribute and several row attributes (Active, PresetMode, GridPos/GridPosMatr, Selective), and omitting Function= produces a new silent-failure shape (name-only empty preset, passes name census, zero PresetData) caught only by export readback.


### cooked-recipe-rows-immune-to-store-remove
**⛔ Recipe-COOKED rows in a cue cannot be killed by Store /Remove or At Remove — recipe data dies by SELECTION/MATRICKS REPOINT, raw data dies by At Remove + /Merge. Repointing also MIGRATES the look intact.**
*when:* Before trying to remove values from a cue — first establish whether the rows are RAW stores or recipe COOKED output, because the two die by completely different mechanisms and the wrong one is a silent no-op


## The revelation

Rows that look like ordinary stored values in a cue may be **cooked output of a StandardRecipe** on a part. In an export they carry the `Cooked=` attribute. **Four removal lanes were tried against cooked rows and all four were silent no-ops:**

- `Store /Remove`
- `At Remove` (default store)
- `At Remove` with `/Merge`
- the `/Remove` option form

**Nothing addressed at the value layer can touch them, because the value layer is not where they live** — they are re-derived from the recipe line every time the cue cooks (`recipe-output-precedence-and-cooking-doctrine`).

## The two kill lanes

| Row kind | Dies by |
|---|---|
| **Recipe-cooked** | **repointing the recipe line's `Selection` or `MAtricks`** |
| **Raw store** | `At Remove` + `/Merge` default-store (scratch-proven), or `Store /Remove` (`store-remove-attribute-scoped`) |

## Migrate-by-repoint: the kill that preserves the look

The tour's masters surgery is the worked example. QX40 "master rows" were **not raw stores** — 147 recipe lines rode a `cLD QX40 MM ALL` selection across 22 sequences, mixing Dimmer values with strobe, tilt and colour. Masters legitimately own strobe/tilt/colour, so **only the Dimmer-pool lines were migrated**: every recipe line whose `Values` parent pool was Dimmer had its **`Selection` repointed from the master group to the cell group** — **65 lines** (`0` ×36, `50` ×14, `Full` ×13, `30` ×2).

**Same presets, same parts, same timing ⇒ the look is preserved exactly**, and the masters leave the dimmer lane. Verse-compliant migrate-then-die in one move (`master-default-doctrine`).

**Proof:** fresh export rescan — master-kind rows **294 → 240**, QX40 dotless **69 → 15**; the 15 survivors are all figure-cooked `abs:100` (phaser-pool values, deliberate swell dynamics), a separate aesthetic question for Dave. The identical 65-line fingerprint reproduced on a second file, which is what let the whole treatment become a one-tap macro (`venue-adapt-macro-pattern`).

**Benign residue to expect:** raw cell rows written by an earlier batch can survive an `At Remove` sweep by landing in a different part via auto-routing (`merge-store-part-auto-routing`). If they hold the same presets the recipes now cook, there is no visual conflict — pure duplication, a calm-day cleanup.

**Relation:** `store-remove-attribute-scoped` · `merge-store-part-auto-routing` · `recipe-output-precedence-and-cooking-doctrine` · `master-default-doctrine` · `assign-cli-recipe-line-grammar`.

History: none — established by scratch test plus live counts, 2026-08-26; reproduced 2026-08-26 on the prep file.


### cuefade-not-a-real-property-gotcha
**Look timing comes from the recipes, not from cue/part fade properties — cue-to-cue follow times live in the cue stack, UseExecutorTime stays OFF, and 'CueFade' is not a real property name (CLI footnote)**
*when:* Before setting or chasing any fade/delay on a cue or part in this recipe-based show — timing is authored in the recipes, not on cue/part fade properties; also before trying to Set a cue's fade via CLI (CueFade is not a property name and no-ops silently)


**The doctrine (Dave, 2026-07-21): fades and delays come from the RECIPES.** In this recipe-based show, look timing — fade in/out, per-attribute delays, the feel of a move — is authored inside the recipe (its preset + phaser + grid), which cooks live. That is the layer to reach for when a look should breathe faster or a color should crossfade slower. Do not bake fade times cue-by-cue.

**Cue-to-cue FOLLOW times are the one exception.** The timing *between* cues — follow/trigger — lives in the **cue management stack** (the cue's `TRIGTYPE` / `TRIGTIME` / `TRIGSOUND`), not in a recipe. So: within-look timing = the recipe; cue-to-cue advance = the cue stack. Cue/part fade *duration* properties are not the layer you author look timing on for this show.

**UseExecutorTime stays OFF for this show.** `UseExecutorTime` is an **override toggle**: turned ON, it makes the executor's time override the fade times stored in the sequence. It is not the normal path to timing, and leaving it ON during programming can produce strange, hard-to-explain output. Keep it **OFF** and let recipe timing (and cue-stack follow timing) stand. This corrects an earlier reading from this session that treated `UseExecutorTime=Yes` as "where cue fade lives" — that was a baked-paradigm artifact.

**Footnote — the `CueFade` CLI gotcha (still true):** `Set <cue> Property "CueFade" <value>` compiles and echoes clean but **no-ops silently** — `CueFade` is not a property name on either the Cue or its Part. Same silent-fail class as `set-command-unknown-property-fails-silently` and `command-enabled-property-name-gotcha`: never trust a clean `Set` prompt on an unverified property name. Real Cue-level properties actually seen: `TRIGTYPE`, `TRIGTIME`, `TRIGSOUND`, `FADERENABLED` (none is a fade *duration*; `FADERENABLED` only gates whether fading happens at all). Real per-part fade property names do exist on the part surface (`RELATIVEFADE`, `FADEFROMX`/`FADETOX` +`Y`/`Z`, `DELAYFROMX`/`DELAYTOX` +`Y`/`Z`, `OFFFADE`, `RELATIVEDELAY`, `DELAYTOPHASE`) — but for this show you do **not** hand-set them cue-by-cue; timing is authored in the recipe.

Cross-reference: `recipe-line-set-property-syntax-and-value-casing` for the recipe-line `Set ... Property` grammar where real timing is authored; `recipe-part-property-surface-lua-dump` for the fuller part-property surface the CueFade footnote is drawn from.

History: created 2026-07-21 [0721-2cLD] — CueFade-not-a-property CLI gotcha paid for live during the cLD SONG_G sequence build.

History: rewritten 2026-07-21 (crown-jewels scrub) — previously claimed cue fade "lives on the executor (UseExecutorTime=Yes) or on the part." Dave corrected: look timing comes from the recipes, cue-to-cue follow times from the cue stack, and UseExecutorTime is an override that stays OFF for this show. The narrow, still-true CueFade-is-not-a-property CLI gotcha was kept as a footnote; the contaminated "where fade lives" framing was scrubbed.


### edit-session-mechanics-and-contamination-risk
**`Edit Preset x` pulls the preset INTO the programmer; exiting edit mode (Escape/Quickey) does NOT clear it — ClearAll is the flush, careless Store after exit bakes/contaminates**
*when:* Before or immediately after using `Edit Preset x` (or the Recipe Editor's equivalent Edit function) to open an existing preset/recipe — read this before your next Store to avoid baking stale edit-session content into it


`Edit Preset x` pulls the target preset **INTO THE PROGRAMMER** — that's the mechanism that lets the editor show and manipulate its values.

Exiting the edit session — via Escape or via `Quickey 20` (see `quickey-20-popup-abort-lane`, since synthetic Escape doesn't reach the console) — closes the edit **MODE**, but the content does **NOT** leave the programmer. The pulled-in values REMAIN there as live programmer values; that's why the editor still shows them after exit. `ClearAll` is the actual flush.

**Danger:** a careless `Store` after exiting an edit session — before running `ClearAll` — bakes/contaminates whatever gets Stored with the leftover edit-session values still sitting in the programmer.

**Distinct from `edit-command-escape-pending-line-trap`:** that concept is about a staged-but-uncommitted CLI **text line** surviving an Escape on the Edit Command popup and later firing with appended junk. This concept is about a committed preset-edit's **programmer values** surviving in the programmer after the edit session's mode is closed. Different objects (a pending keystroke line vs. loaded programmer values), same family of "Escape doesn't mean gone" console danger.

History: none — first captured live 2026-07-16, during the phaser/recipe session (recipe-preset editing via the Recipe Editor's Edit function).


### export-sequence-xml-schema
**Export Sequence <n> XML schema — fully self-contained: Sequence>Cue>Part>{cooked PresetData + StandardRecipe}, dependencies embedded recursively**
*when:* Before reading, generating, or hand-authoring a Sequence-export XML file (e.g. cLD MAker's Sequence-XML export feature, or any parts-per-century multi-part emitter) — the full element/attribute shape, bind-slot ref format, dependency-embedding behavior, and the multi-part census/import gotchas paid for on the SONG_C build


**Ground truth confirmed:** Dave's claim proven live — "the recipe goes along with the sequence." `Export Sequence <n>` produces a **FULLY SELF-CONTAINED artifact**.

**Schema tree:**

```
GMA3
 > Sequence (playback attrs)
    > Cue (OffCue/CueZero: No="0" | named cue: No="1")
       > Part
          > <PresetData Size=N>            — cooked snapshot, per fixture
             > <Phaser IDType ID Attribute Phase Measure GridPos GridPosMatr Selective Cooked>
                > <Step Function Absolute Accel AccelSplineType Decel DecelSplineType Width>
          > <StandardRecipe [inv/align attrs] PhaseFromX PhaseToX Selection Preset MAtricks Values Enabled SelectionFromValue>
```

A Part carries BOTH blocks side by side: the cooked `<PresetData>` snapshot AND the live `<StandardRecipe>` — see `recipe-output-precedence-and-cooking-doctrine` for what "cooked" means and which one wins at runtime.

**Bind-slot refs are DOTTED FULL-PATH strings** on the `<StandardRecipe>` element, e.g.:
- `Selection="Default.Groups.cLD DS WING PAIRED16"`
- `Preset="ShowData.DataPools.Default.PresetPools.All 2.Wipe In"` and `Values="ShowData.DataPools.Default.PresetPools.All 2.Wipe In"` (same ref, both attrs — see the dual-fill note below)
- `MAtricks="Default.MAtricks.Phase X 0-180"`

**Dependencies embed recursively:** a `<DependencyExport Size=3>` on the Part EMBEDS the full definition of every referenced object:
- Group — with its full `SelectionData` grid coords.
- Preset — with its own nested `PhaserRecipe` + an embedded Shape dependency.
- MAtrick — with its own `PhaseFromX`/`PhaseToX`.

**One sequence export = a portable, dependency-complete show fragment** — nothing external needs to be resolved to reconstruct the recipe's bindings.

**Worked-example notes (Seq 102, 2026-07-17):**
- **Dual-fill confirmed:** `<StandardRecipe>` carries BOTH `Preset=` AND `Values=` attrs, both populated with the SAME reference (`"All 2.Wipe In"`) — a genuine dual-fill (two attrs actually written), not a single aliased slot exposed under two names. This resolves `assign-cli-recipe-line-grammar`'s open `[VERIFY]` on exactly this question.
- **Both phase carriers coexist:** Seq 102 Part 0.1's `<StandardRecipe>` has its own `PhaseFromX="0°"`/`PhaseToX="270°"` (a part-level override) sitting in the same file alongside a bound MAtricks `"Phase X 0-180"` whose own `PhaseToX="180°"`. Both carriers are present in the export and neither overwrites the other — but which one actually cooks at runtime is still an open item (see `recipe-output-precedence-and-cooking-doctrine`'s "open item" for the evidence and what would pin it).
- **Measure serializes as a display string with a leading space:** `Measure=" 1.00"`.
- **Recipe widths serialize as display strings:** e.g. `"25.0%"`, `"0.0% Thru 100.0%"`.
- **Golden fixture saved:** the real capture is archived as `cld_seq102_inspect.xml` in the cLD MAker handoff pack (`beatgrid/Meta/cld_maker_handoff/`) — see `cld-maker-identity-rename-and-scope`.

**Multi-part cue-part census + import facts (added 2026-07-31 [0731-2cLD], SONG_C seq 1210 build — parts-per-century is now the standing multi-part shape, see `parts-per-century-emit-pattern-and-et-gate`):**
- **Part attribute ORDER is load-bearing on import for multi-part cues.** `SpeedScale` must sit between `MAgic` and `Mode` in the attribute sequence, on EVERY part including part 0/OffCue/CueZero — an emitter that instead places it after `CueInFade` causes the importer to silently absorb the cue's first content part into part 0. Full mechanism and the paid-for incident: `part-attr-order-import-absorption-gotcha`.
- **`SpeedScale="One"` is DEFAULT-ELIDED on export** — a clean export-back of parts that are all at the default Speed Scale shows ZERO `SpeedScale` attributes at all. This is a genuine exception to the general rule that MA3's export writes exhaustive attribute sets (so absence is normally usable negative evidence): **absence of `SpeedScale` in an export-back is NOT itself evidence that an import dropped it** — it may simply mean the value is `One`. Non-default Div values (e.g. `Div2`/`Div4`) DO serialize and were confirmed to survive import/export round-trips.
- **Export-back bind-slot refs resolve to NAME-FORM, even when the object was deployed/authored in slot-form.** E.g. `Phaser.cLD SONG_C MARK SINE`, `Dimmer.50` — the console always exports references by name. **Any census parser reading an export-back must count by NAME, not by slot** — a slot-form counter silently reads zero and reports a false miss.

**Design implication (cLD MAker):** per `recipe-output-precedence-and-cooking-doctrine`, a hard/cooked value always beats a recipe — so a Sequence export that includes the cooked `<PresetData>` block would PIN an imported recipe to stale frozen values instead of letting it recompute per rig. Consequence: **cLD MAker's Sequence-XML export must be RECIPE-ONLY by default** — strip or make optional the cooked `<PresetData>` block. A separate deliberate "freeze this look" mode can export cooked values on request. This landed as CLD_MAKER_SPEC §6 export scope at the v0.2 meld — see `cld-maker-identity-rename-and-scope`.

**Relation:** `recipe-xml-schema` is the different PhaserRecipe-*template* dialect (a recipe **preset**, not a cue-part's StandardRecipe) — same dotted-path convention for Shape refs, different element shape. `baked-phaser-preset-xml-schema` is the baked/Export-Preset dialect — its `<PresetData>` block is the same cooked-snapshot shape that rides alongside `<StandardRecipe>` here. `shapes-pool-facts` for what a Shape dependency itself holds. `export-timecode-tc-event-xml-schema` for the companion Export Timecode schema cracked the same session, which targets a Sequence by the same dotted-path convention. `part-attr-order-import-absorption-gotcha` for the full multi-part attribute-order incident. `parts-per-century-emit-pattern-and-et-gate` for the standing multi-part architecture this schema now has to serve. `smith-packet-must-stage-multi-part-golden` for the certification consequence of these multi-part facts.

## Extended 2026-08-01 [0801-2cLD] — a cue Part can carry NO Name attribute at all, proven and kit-patched

**Sequence-XML: a cue may carry NO `Name` attribute on its Part at all** — observed on {LD}'s own SONG_J cue 28 (nameless, zero StandardRecipes, a trailing cue). This is broader than the existing OffCue/CueZero no-Name convention already known for this dialect (see `authored-sequence-dialect-vs-desk-golden-fixed-diffs`) — this is a regular, non-OffCue/CueZero cue with no Name at all. The build kit was patched to emit such a cue correctly: no `Name=` on the cue header, and a Part carrying the standard PART attributes plus `Sync`/`Morph` but no `Name`. **Round-trip verified:** export-back reports `nameless=1`, and all 43 other cues in the same file kept their Name. The SONG_A regression stayed BYTE-EXACT 5/5 across both patches to the kit.

## Default-elision family, 2026-08-01 [0801-2cLD]

**Desk exports default-elide `SpeedMaster` on a `Sequence` element entirely** (SONG_I's `gb_s1900.xml` export has none) — the same elision family as `SpeedScale="One"`'s default-elision already noted in this concept. Absence of `SpeedMaster` in a desk export is not itself evidence of anything wrong; it means the value sits at its default.

## Bind census + recipe-line census laws, weighted 2026-08-04 [0803-3cLD]

**GOVERNING (G=0.9) — bind census: count binds by NAME from the export-back `Dependency`
element's `RelAddr` attribute; a slot-form counter reads zero.** This sharpens the existing
NAME-form census law above (2026-07-31) with the exact XML location: the countable bind
reference lives on `Dependency/@RelAddr` inside a Part's `DependencyExport`, not on the
`StandardRecipe`'s own `Selection=`/`Preset=`/`Values=`/`MAtricks=` attributes directly. (A
distinct, numeric `RelAddrNum` attribute also exists — see `recipe-xml-schema` — treat the two
as separate attributes until proven otherwise; don't conflate them.)

**CONSTRAINING (G=0.7), scoped to parsing a {LD} export — recipe-line census: read a Part's
`StandardRecipe` DIRECT CHILDREN only.** Recursive iteration also walks into each Part's
`DependencyExport` and counts the wrapper `StandardRecipe` copies embedded inside a bound
Preset's own dependency tree (see `source-matricks-wrapper-recipe-encoding`) as if they were
additional cue lines — silently inflating the total. This generalizes the parser-census
correction already on file in `recipe-layer-is-fixture-agnostic-doctrine` (105 direct-child
StandardRecipes vs. 10 more nested inside DependencyExport, wrongly countable) into a standing
rule for any new source-export parser.

**CONSTRAINING (G=0.7), scoped to reading an export-back — where binds vs. content live:
binds are in `Dependency`; content is in `Cue/Part/PresetData/Phaser`.** The `<Preset>` stub
that appears nested under a `<Dependency>` is EMPTY by design — it exists to let the resolver
identify which preset is referenced, not to carry that preset's own data a second time. Don't
read an empty embedded `<Preset>` stub as a corruption signal.

## Three more schema/census facts, SONG_L build, 2026-08-05 [0805cLD]

1. **Grep-counting a slot/name string double-counts.** A `<StandardRecipe>` carries the SAME
   reference on BOTH `Preset=` and `Values=` (the dual-fill already noted above), so a raw
   string count like `xml.count('Phaser.NNNN')` reads **2x** the true line count — SONG_L
   read `21.2222 x30` for 15 actual lines. Divide by two, or count `<StandardRecipe` elements
   instead. **MAtricks does NOT double-count** (single `MAtricks=` attribute) — 23 MX binds
   against 23 phaser lines landed exact.
2. **An export-back legitimately carries `PresetData`, and that is normal.** SONG_L's
   export-back holds 75 `PresetData` blocks against an authored file with 0 — the console
   cooks on export and embeds the snapshot alongside the live `StandardRecipe`. **The
   recipe-only authoring doctrine (`universal-presets-emitter-aware`'s doctrine-lint) applies
   to the AUTHORED deliverable, not the export-back read after import** — do not read a
   non-zero `PresetData` count on an export-back as a doctrine failure. Also: never re-import
   an export-back as a restore, since its cooked layer carries `&apos;`-quoted refs that kill
   resolution silently (see `import-resolver-laws`).
3. **A bind authored in SLOT form survives a rename of the bound object; one authored in NAME
   form would not.** MAtricks 183 was renamed (`cLD W2 G14 X-45to-90` → `cLD W2 G5
   X-45to-90`) AFTER a sequence was emitted against it, and the export-back resolved the bind
   correctly with no re-emit needed — because the emitter had written
   `MAtricks="Default.MAtricks.183"` (slot form), a rename of the target object is invisible
   to an already-authored bind. This is the authoring-side complement to the NAME-form
   export-back census law above (export-backs always resolve refs by name on the way OUT;
   this is about what the emitter writes on the way IN).

History: created 2026-07-17 from the live Export Sequence 102 capture — first ground truth on the Sequence-export schema, and the finding that over-resolved the #1 blocking item from both external spec-pack reviews (see `external-cross-vendor-review-lane-pattern`).

History: extended 2026-07-31 [0731-2cLD] — added the multi-part Part attribute-order import hazard, the `SpeedScale="One"` default-elision caveat, and the export-back NAME-form census law, all paid for or discovered during the SONG_C (Seq 1210) parts-per-century build.


### figure-hash-counts-dependencies-not-bind-sites
**A song's figure-hash count is its DEPENDENCY count, not its bind-site count — census actual cue-list bind sites before sizing a build; an unbound figure is often a pool-resident LIBRARY figure, not missing or aux content**
*when:* Before sizing a song's phaser/MAtricks object build off its figure-hash count, or before treating a figure that hashed for a song but shows zero main-sequence bind sites as missing content, aux content, or a gap — check the actual bind census first


**The figure hash tells you what travels WITH a song as a dependency — not what the song's
main sequence actually uses.** A figure can be hashed into a song's dependency export and
bound nowhere in that song's main cue list at all.

**Practical rule: before sizing a song's object build off the figure hash, census the actual
BIND SITES in the cue list.** The hash tells you what travels with the song; the bind census
tells you what the main sequence actually needs. Method: a direct-children-only walk over
Cue>Part>StandardRecipe, reading the `Values=`/`Preset=` leaf token per figure name — never
recurse into `DependencyExport` wrapper copies (see `export-sequence-xml-schema`'s recipe-line
census law for why recursion over-counts).

**An unbound figure is very often a pool-resident LIBRARY figure — the shape dictionary a
song's named figures are built from — not missing content, and not automatically aux content
either.** Do not guess which bucket it falls into; export and read the aux (or wherever else
it might plausibly be used) before concluding.

## Proven on SONG_L, 2026-08-05

Only 5 of SONG_L's 9 distinct content-hashed figures are bound in the main sequence
(`dg_figure_sites.py`, direct-children census): `Verse 1/2` x12 · `Intro 1/1 Dim#6` x3 ·
`Bridge 1/1 Col` x3 · `Bridge 1/1 Dim#5` x3 · `Spot Pan#2` x2 — 23 bind sites total. `Pan
Sin#3`, `Dim_Sin_Bump`, `Dim Sinus` and `Dim_Ramp Minus` show ZERO main-sequence bind sites.

cLD's first guess was that the four unbound figures were the song's AUX layers (`Dim_Sin_Bump`
reads literally as a bump — the aux bump shape). **Wrong, settled by exporting {LD}'s
actual aux (2201-2204) and reading it: the aux carries no phasers at all.** All four are
pool-resident LIBRARY figures, bound nowhere in this song, main or aux. **Generalises: a
figure hashed for a song but bound in neither its main nor its aux is a library object, not
missing content — and not automatically aux content either. Check, don't guess twice.**

## Precedent

Same shape, one step earlier in the chain, as SONG_B's aux-fired figure 658 (pool block
`21.1100-1109`), which the main-sequence export alone had missed entirely — see
`tourshow-seq1110-song-b-build-record`. SONG_B's case resolved when the AUX was checked;
SONG_L's is the harder case, where the figure lives in NEITHER main nor aux.

**Relation:** `tourshow-seq2210-song-l-build-record` (the build this was proven on),
`export-sequence-xml-schema` (the direct-children census law this rule depends on),
`empty-census-deserves-selector-suspicion` (the sibling discipline for trusting a zero once
the selector itself is confirmed correct).


### gap-is-a-rest-doctrine
**A gap on the grid time-map plays as silence — mirrored/bounce gaps are authored rests, not just spacing**
*when:* When placing gaps or dropped cells in a grid build — treat the gap as a deliberate musical rest, not leftover space


Design reframe that follows directly from `grid-is-a-time-map-doctrine`: if a shared grid column is a moment in time, an EMPTY cell in that column is a moment with no stage output — silence. A gap on the grid doesn't just skip a fixture, it plays as a rest.

This reframes every gap pattern already in active use: the mirrored gaps of `grid-mirror-symmetry-doctrine` and the alternating drops of `grid-bounce-pattern` aren't just ways to make an uneven fixture count look tidy — under this doctrine they're **authored rests**, placed on purpose for musical effect, the same way a composer places a rest in a score.

The reframe follows Dave's operator confirmation that empty cells really are respected by MAtricks and phasing (Next steps into gaps produce no stage output that beat, and phase math uses the full grid extent including gaps, not just occupied-cell count). That mechanical verification is tracked in `matricks-phase-distribution-on-gappy-grids-open-question` — **live 100% CONFIRMED 2026-07-16** (Dave, attended, live on Group 124's bounce grid, 2.4.2.2: a gap CONSUMES A BEAT in phaser traversal), corroborated the same session by a structural test (Chase recipe on Group 124 ran single-cell/AdaptiveWidth, honoring the sparse grid with no compaction — positional jumps consistent with gap columns passing dark). This file remains scoped to the design meaning of the result, not the underlying mechanism — but the mechanism itself is now fully closed too, not just this doctrine's framing of it.

Practical consequence: when composing a mirrored or bounce gap layout, the gap placement deserves the same intentionality as the occupied cells — where the rest lands is a musical decision.

History: dictated live 2026-07-15, closing out the open mechanical question from 2026-07-14 (design reframe stated as doctrine ahead of the final live mechanical confirm). 2026-07-16: the queued live 100% confirmation ran (Group 124 bounce grid, Dave attended) — gap-consumes-a-beat confirmed mechanically, not just as operator knowledge; doctrine unchanged, now standing on fully confirmed footing.


### gears-delivery-is-a-list-cld-does-not-set-speed-scale
**Gears delivery ruling: cLD delivers a list of cues + Speed Scale at end of session — Dave applies it at the desk; cLD does not set Speed Scale itself**
*when:* Before deciding whether to issue Speed Scale Set commands at the console for a song's gears, or when a build session is wrapping up and gears are still owed — the standing division of labor is a delivered list, not a console write


**RULED (Dave):** cLD delivers a list of cues + Speed Scale values at the end of each build
session; **Dave applies them at the desk. cLD does not set Speed Scale.**

This is the standing division of labor for the gear/Speed-Scale half of a song's build,
distinct from the mechanical work cLD does own outright (binding phasers, MAtricks, emitting
the sequence). See `tourshow-speed-architecture-standing-ruling` for where the gear NUMBER
comes from (the wrapper `SpeedFromX` ÷ song BPM, read directly off each Phaser Preset) and
`tourshow-seq2210-song-l-build-record` for a worked delivery
(`SONG-L_SPEED_SCALE_0805.md`, 20 parts).

**Relation:** `tourshow-speed-architecture-standing-ruling` (the formula this list is built
from), `state-the-scope-with-the-count` (state PARTS and LINES both when reporting a gear
count — the delivered list is scoped to PARTS, since Speed Scale is a per-part knob).


### grid-cursor-cli-recipe-for-2d-group-layouts
**Grid x/y cursor moves batch inline via CLI — one-paste recipe bakes a 2D fixture layout into a recallable Group**
*when:* Before building a 2D selection-grid layout (rows/columns of fixtures) from the CLI in one shot, or when you need a recallable Group that preserves 2D grid positions


**Verified one-paste recipe (2.4.2.2, live):**

```
ClearAll ; Grid 0/0 ; Fixture 1 Thru 5 ; Grid 0/1 ; Fixture 6 Thru 10 ; Store Group 106 "cLD 5x2" ; ClearAll ; Group 106
```

This builds a 5×2 grid in one semicolon-batched paste (interactive CLI batches `;` — see `macro-line-syntax-and-batching-rule`):
- `Grid X/Y` moves the grid cursor to that cell before the next `Fixture` selection lands there.
- Each `Fixture ... Thru ...` selection is stamped into the current grid cursor position.
- `Store Group 106 "cLD 5x2"` **bakes the 2D positions into the Group** — the grid shape is stored, not just the fixture list.
- `Group 106` (recall) **restores the 2D positions**, confirming the bake round-trips correctly.

Ties to `selection-grid-and-fixture-cell-model` (X/Y/Z axis convention, one-fixture-one-cell-per-sequence rule) — this recipe is the concrete CLI mechanism for populating that grid model.

**Caveat found the same session:** grid coordinates set this way persist through Group storage and later transforms (e.g. MAtricks XWidth re-wrap) — see `matricks-xwidth-wraps-on-absolute-grid-x` for a case where a non-zero grid origin from a build like this produced uneven wrapped rows.

**Further verified 2026-07-14 (grid drill session):** a bare `Fixture A Thru B` with no `Grid X/Y` cursor calls at all auto-fills one X row in FID order (48-wide, live-verified) — the simplest possible case, a single one-wide plane. Grid-cursor placement is only needed once a shape stops being a single line. The recipe also holds for sparse, non-contiguous rows: single-fixture `Grid X/Y` + selection calls can build multiple aligned rows at different step intervals over one shared window, and `Store Group` bakes that sparse 2D arrangement exactly — recall round-trips pixel-identical. Worked exemplars: Groups 121-124, see `grid-drill-exemplar-groups-121-124`.

**Further verified 2026-07-15 (multi-instance session):** the same Grid-cursor + `Fixture ... Thru ...` composition pattern holds unchanged at the SUBFIXTURE level — `Grid 0/2 ; Fixture 301.17 Thru 32 ; Grid 0/1 ; Fixture 301.33 Thru 48` lands each sub-range at its cursor row and selections accumulate across calls (48 subs selected total, live 2.4.2.2). See `subfixture-thru-range-syntax` for the dot-notation Thru rules this composes with, and `gridstore-keyword-and-fixture-type-write` for baking a sub-level layout into the fixture TYPE itself (a stronger, type-wide alternative to the per-instance Group bake this recipe produces).

**Further verified 2026-07-21 (pixel-cell sandwich, live):** the recipe bakes correct per-fixture 2D coords for ACME pixel-line cells. `ClearAll ; Grid X/0 ; Fixture <fid>.1 Thru 16 ; Grid X/1 ; Fixture <fid>.17 Thru 32 ; ... ; Store Group n` — export confirms `301.1`–`16` @X0–15/Y0, `302.1`–`16` @X16–31/Y0 (per-fixture tiling continues across the truss), `301.17`–`32` @X0–15/Y1 (second row). A per-truss ACME cell group thus lands top color subs 1–16 @Y0, bottom color 17–32 @Y1, beam 33–48 @Y0, 16 cols/fixture, FID→X. Generator: `build/gen_pix_cells.py`. The physical convention (top/bottom rows, FID→X direction) is still warehouse-verify — see `acme-pixel-line-ip-anatomy`. This is now the RELIABLE cell-layout lane, after the GS type-bake was found not to survive the v11 repatch (`gridstore-keyword-and-fixture-type-write`).

**Ad-hoc composition is exploration only (Dave, live console, 2026-07-19):** recalling groups/selections with an existing selection appends per the append rules — see `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle` for what `Preserve GridPositions` does to that combined recall. A manual grid-cell click places the cursor where the NEXT recall lands (see `selection-grid-and-fixture-cell-model`), so recall→click→recall builds ad-hoc composite grids live. But this is a sketching tool, not a recipe input: recipes bind Selection to a stored Group object, so anything that's going to enter a repeatable recipe has to be Stored as a Group first. Sketch live, store before it enters a cue — see `tourshow-gesture-groups-on-demand-doctrine` for the doctrine this feeds (gesture groups specifically get stored at first real use, not pre-built).

**Depth-grade corollary (2026-07-19):** this recipe's 2D output isn't just cosmetic — a `Grid Rotate`-based depth-grade effect (e.g. POSITION_WIZ's Blind block) requires a real 2D grid selection to work at all; a flat 1-wide `Thru` selection degenerates it to a uniform value. See `tourshow-position-wiz-blind-depth-grade-root-cause` for the full diagnosis and `tourshow-group-contract-v01` for the 12×4-per-category frame built specifically to satisfy this requirement.

History: first verified live 2026-07-10. Extended and reverified 2026-07-14 with the flat auto-fill and sparse-aligned-row variants (grid drill session — see `grid-drill-exemplar-groups-121-124`). Extended again 2026-07-15 confirming the recipe composes unchanged at the subfixture/dot-range level (multi-instance session). Extended 2026-07-19: added the ad-hoc-composition-is-exploration-only doctrine and the depth-grade corollary (2D selection required for Grid-Rotate-based effects). Extended 2026-07-21: added the ACME pixel-cell sandwich build (per-fixture tiling FID→X, top/bottom color rows, beam center) — the reliable cell-layout lane since GS type-bakes don't survive a repatch.


### grid-drill-exemplar-groups-121-124
**Groups 121-124 — the four canonical grid-drill exemplars (flat plane, proportional, paired-mirrored, bounce)**
*when:* When you need a worked, verified example of a grid alignment technique (flat one-wide plane, proportional spread, paired mirroring, or the bounce pattern) to copy or extend


The 2026-07-14 grid-drill session built four canonical two-part alignment Groups, all saved live in show **cLD_SANDBOX_v0.8**, each demonstrating a different alignment technique end to end (CLI build → `Store Group` → recall round-trip verified):

- **Group 121 "cLD SPOTS 1WIDE"** — a flat 48-wide single-row plane. Built from a bare `Fixture A Thru B` with no grid-cursor calls at all: a linear Thru selection auto-fills one X row in FID order. The simplest possible case — grid-cursor placement is only needed once the shape stops being a single line.
- **Group 122 "cLD DS WING ALIGN"** — proportional spread: 12 spots at step 4 and 16 wings at step 3, sharing one ~46-column window, with coincidence columns every 12. Kept as the worked density-gap exemplar for `alignment-pairing-vs-proportional-doctrine` — this is what proportional spread looks like when it's the right call.
- **Group 123 "cLD DS WING PAIRED16"** — the paired-and-mirrored exemplar. Wings (FID 149-164) fill row y=1, columns 0-15, in one Thru auto-fill; spots (FID 101-112) sit on row y=0, individually cursor-placed to skip columns 3/7/11/15. Originally built flat/unmirrored, then hand-rebuilt by Dave live into a mirrored triplet pattern — see `grid-mirror-symmetry-doctrine` — and stored over the original via `Store /Overwrite`.
- **Group 124 "cLD DS WING BOUNCE"** — the bounce pattern: wings on even columns 0-30, spots filling the odd-column gaps with 3 mirrored drops at columns 7/15/23. Full mechanism in `grid-bounce-pattern`.

All four round-trip verified and readable on-screen at their respective auto-fit zoom levels (Group 124 confirmed readable at 31 columns). Together they form the complete 2026-07-14 grid-drill arc — Dave's "four canonical two-part alignments": **auto-fill row → proportional spread → paired-mirrored → bounce**.

Building recipes (chases/effects fired against these Groups) was deliberately parked for a later session — see `multi-instance-grid-frontier` and the wrap's open threads for what comes next. (That later session arrived 2026-07-16 — see `worked-strobe-figure-tap-tap-kill` and the phaser/recipe concepts for what got built on top of these Groups.)

**Census confirmed 2026-07-16** (live, same numbering block, during the phaser/recipe session): the names above match exactly what a live group census found that night, plus the surrounding range — **125-127 are empty** (unused), and **128-130 are a JDC set**. 128-130 were used that same session for the tap-tap-tap-kill figure's Sequence 104 build: cue 1 taps on 130, cue 2 hit uses 129×FX White + 130×Strobe, cue 3 kill uses 128×Dimmer-0 — see `worked-strobe-figure-tap-tap-kill`.

History: none — all four built and verified live 2026-07-14, session `[0714-2cLD]3DRig-MirrorDoctrine-GridDrills`. 2026-07-16: live census confirmed the same names and extended the picture — 125-127 empty, 128-130 a JDC set, both put to use the same session.


### grid-is-a-time-map-doctrine
**The selection grid is a time map — shared column position sets WHEN fixtures react, not just where they sit**
*when:* Before designing any selection-grid layout — decide what a shared column should mean in time before choosing grid-cursor moves or a MAtricks re-wrap


The selection grid isn't just a spatial arrangement tool — Dave's core framing is that it's a **time map**: fixtures that share a grid column will react at the same moment when a chase or effect sweeps across X. Column position sets *when*, not just *where*; row (Y) is a separate plane/layer.

There are two ways to arrive at a given shape, and which one you use is itself a decision:
- **Cursor-mode at selection time** — the grid cursor's move mode, chosen live as you select, IS the layout decision. The three modes: **no-move** (stay in the current cell), **new-line** (advance to a new row), and **Append X** (advance along the row) — you compose the time map fixture-group by fixture-group as you go.
- **MAtricks reshape after the fact** — the alternate lane: select fixtures flat with no manual cursor placement, then use a MAtricks width re-wrap/collapse to fold the flat selection into the desired grid shape afterward. Same end state, decided in a different order.

Design purpose: use the grid to make spatially different rig parts (DS/MS/US planes, wings) share ONE clean chase — a single shared timeline — instead of each part running its own siloed effect. Dave's standing preference: **tight beats everywhere-at-once** — a small number of purposeful shared moments reads better than maximal simultaneous spread.

Dave's own framing at the close of the drill arc: "temporal, spatial concept locked in — everything compounds on top of this." This doctrine is the foundation the rest of the 2026-07-14 grid work builds on — see `alignment-pairing-vs-proportional-doctrine`, `grid-mirror-symmetry-doctrine`, and `grid-bounce-pattern`.

History: none — dictated live 2026-07-14, foundational doctrine for the grid drill arc.


### import-resolver-laws
**⛔ Sequence-XML import has THREE separate resolver families — Preset=/Values= is a name/slot minefield: numeric preset names parse as SLOT INDEX, &apos;-quoting kills resolution everywhere, and golden exports lie about pool names; a fourth family (SR-level spread attrs) imports clean with no hazard found so far**
*when:* Before hand-authoring or generating ANY sequence/recipe XML for import — Selection=/MAtricks= and Preset=/Values= are resolved by DIFFERENT rules, and a numeric-named preset will silently bind to the wrong (or no) object if referenced by name instead of slot; spread attrs (XShuffle/XBlock/PhaseFromX/ToX) are a separate, so-far-clean fourth family


**The paid-for cost: one full silent half-import.** A 100-recipe-line sequence imported clean (`ok` echo, correct cue/part/StandardRecipe counts) with 50 of 100 preset bindings silently empty. Only a per-line Lua `:Get('Values')` binding census against a known-good line caught it. **Structure census ≠ content census ≠ binding census** — the first two both pass on a damaged import.

## Three resolver families, not one

Recipe-line bind attributes on a `<StandardRecipe>` are resolved by **at least three different rules**, depending on which attribute is being parsed:

1. **`Selection=` (groups)** — tolerant. Both the short form (`Default.Groups.<name>`) and the long `ShowData…` full-path form resolve correctly.
2. **`MAtricks=`** — rides the SAME family as `Selection=` for its SHORT forms: both the name form (`Default.MAtricks.<name>`) and the slot form (`Default.MAtricks.101`) cook. **The long ShowData form silently DROPS** — the recipe imports with no MAtricks bound and no error.
3. **`Preset=` / `Values=`** — strict, and the dangerous one (see below).

## Preset=/Values=: the long form, the live pool name, and the numeric-name trap

Preset/Values bindings require the **long form path using the pool's CURRENT LIVE NAME** — not a cached or historical one. **Pool 21 in this show is currently named `Phaser` (singular)** — even though {LD}'s own exports encode the path with `Phasers` (plural). {LD}'s exports only survive because they resolve by **GUID**, not by the name-path text. **A golden export's name-path is not proof the name is still current — golden name-paths lie**, exactly like group/preset labels do (see `inherited-file-membership-is-ground-truth`).

Within that long path, the trailing preset token resolves two different ways depending on its shape:

- **Non-numeric name** → resolved by NAME. Spaces and trailing spaces are fine.
- **Numeric-looking name** → resolved as a **SLOT INDEX**, not a name lookup — even when a preset is literally NAMED that numeral.

Several of this show's dimmer presets are *named* plain numbers (`"0"`, `"50"`, …). Writing the numeral as if it were the name resolves to the wrong slot (usually nil):

| Want (preset named…) | WRONG (parsed as slot) | RIGHT (its actual slot) |
|---|---|---|
| `"0"` | `Dimmer.0` → slot 0 = **nil** | `Dimmer.15` |
| `"50"` | `Dimmer.50` → wrong/nil | `Dimmer.9` |
| `"Full"` (non-numeric, for contrast) | — | `Dimmer.5` (slot) **or** `Dimmer.Full` (name) — both work |

**Rule: for any preset whose NAME is itself a number, address it by SLOT, never by typing the numeral as a name.** Non-numeric names are safe by either route.

## &apos;-quoting kills resolution — everywhere

Never `&apos;`-quote a bind-path token, on any of the three attribute families. Quoting a name this way **kills resolution silently**, regardless of which resolver is parsing it.

## Resolution is ONE-SHOT at import time

Path/name resolution happens once, at `Import` time. After the import completes and the show is saved, the recipe holds a **resident OBJECT reference**, not a re-evaluated path string. Consequence: **slot-vs-name addressing is only a hazard on a future RE-import of the same XML** — once resident, the live show is safe; renaming the pool or the object afterward does not re-trigger this resolver.

## Fourth family, proven clean — SR-level spread attrs (2026-07-29)

**`XShuffle`/`XBlock`/`PhaseFromX`/`PhaseToX` authored as plain attributes directly on a cue-part `StandardRecipe` import correctly and read back exact via `:Get`** (`XShuffle=5`/`7`, `XBlock=7`, Phase `0→360` all exact) — proven importing the SONG_T Fill 1/Fill 2 sequences (see `tourshow-fill-layer-rebuild-method`). **The flattened lane (spatial attrs written directly on the cue-part line, instead of {LD}'s wrapper-preset pattern) is PROVEN — wrapper presets are unnecessary for spread/shuffle.**

Unlike `Preset=`/`Values=`, **this family has shown no numeric-name/slot trap so far** — it behaves more like the tolerant `Selection=`/`MAtricks=`-short family than the strict `Preset=`/`Values=` family. Not yet stress-tested against the numeric-name hazard specifically (no spread attribute in this corpus is named a bare numeral), so treat as proven-for-the-cases-tested rather than a blanket guarantee.

## Verification method — the only thing that catches it

An `ok` echo, a correct cue/part count, and a correct StandardRecipe count **all pass on a half-bound import.** The only reliable check is a **binding census**: read `:Get('Values')` (or the equivalent bound property) on every recipe line via Lua and compare against what the line is supposed to hold — never trust the import's own report of success.

**Dialect-test method used to establish all of the above:** build a small variant XML file → import it into a disposable scratch sequence (this campaign used **Seq 1990**) → read back via Lua. Six variants isolated the `Preset=`/`Values=` numeric-slot behavior; a further three variants isolated the `MAtricks=` short/long split. Reuse this scratch-sequence method before trusting any new hand-authored bind-path shape.

**Related:** `sequence-xml-ordered-header-law` (a sibling import gotcha on the same XML dialect); `export-sequence-xml-schema` (the general schema these bind attributes live on); `inherited-file-membership-is-ground-truth` (the same "labels/names lie, only live data is truth" pattern, one layer up); `tourshow-seq1510-build-record` (the build these laws were paid for on); `tourshow-fill-layer-rebuild-method` (the build that proved the fourth, spread-attr family).

## Scope pinned 2026-08-01 [0801cLD] — &apos;-quoting is confined to the COOKED export layer; live StandardRecipe binds are clean

**&apos;-quoting scope corroborated, not contradicted:** a console `Export Sequence` writes `&apos;`-quoted name paths ONLY inside the cooked `<Phaser>`/`PresetData` layer (observed 11,540 instances in SONG_G seq 1710) and inside `<Dependency>` blocks (124 instances) — **live `<StandardRecipe>` bind attributes are 0/66 clean**, and 0 of 34 distinct bind values across the sample carried an apostrophe. **Consequence: an export-back file is a READ artifact only — never re-import one as a restore.** Its cooked layer carries `&apos;`-quoted refs that will kill resolution silently on re-import. Always re-import the AUTHORED file, not the export-back. (Three cLD-authored files checked the same session: `&apos;`=0, lint-confirmed clean.)

## Additional dialect facts, 2026-08-01 [0801-2cLD] and 2026-08-03 [0803-1cLD]

**Bind-path pluralization is unstable across exports — another instance of "golden name-paths lie."** `gb_s1900.xml` (SONG_I) writes `PresetPools.Phaser` **SINGULAR**, where earlier {LD} exports wrote `Phasers` **PLURAL**. Slot-form binds are immune to this instability; name-path binds are not — prefer slot-form where the choice exists, and don't hard-code a plural/singular assumption into a parser.

**MAtrick and StandardRecipe do NOT share one attribute order — never port attribute order across element classes.** `XShuffle` sits beside `XBlock` on a `MAtrick` element, but AFTER `ZWidth` on the desk's `StandardRecipe` wrapper element. An attribute-order fact proven true for one XML element type is not transferable to a different element type carrying the same-named attributes.

**Negative-phase serialization asymmetry (verification-method note):** the desk dialect writes negative phase WITHOUT a degree sign (`PhaseToX="-180.00"`) while positive phase keeps it (`"360°"`). Authored-with-degree negatives still import correctly — but an export-back byte-diff comparison must NORMALIZE this asymmetry before comparing, or a genuinely clean import will read as a false failure. (See `matricks-negative-value-lua-uint32-wraparound-gotcha` for the related but distinct live-Lua-read-side wraparound issue this serialization fact is not the same mechanism as.)

## GOVERNING — import order precondition, 2026-08-04 [0803-3cLD]

**Every object a sequence references — groups, presets, MAtricks, shapes — must already
exist in the show BEFORE that sequence is imported.** This is the direct consequence of
"Resolution is ONE-SHOT at import time" above: there is no lazy or retry resolution, so an
import that runs ahead of its own dependencies binds to nothing (or the wrong slot) and does
not self-heal later. Sequence dependency-creation order, not just bind-path correctness, is
load-bearing.

History: none — all three resolver families established in one session, 2026-07-28, via the scratch-import dialect-test method on Seq 1990. Extended 2026-07-29: added a fourth family (SR-level spread attrs), proven clean on the SONG_T fill-sequence import.


### live-selection-matricks-cli-set-syntax
**Setting MAtricks properties: THREE write surfaces — live selection (Set Selection MAtricks "XWidth" 5), a POOL object directly (Set MAtricks <n> 'Prop' <val>, incl. PhaserTransform/XinvW), and a recipe's own MAtricks (separate dedicated editor, not reachable by either Set form)**
*when:* Before generating any CLI command that sets a MAtricks property (XWidth, PhaserTransform, XinvW, etc.) on the current live selection OR on a POOL MAtricks object directly — do not follow the repo manual's ch12 §13b/§15 no-pool-number form, it fails live for the selection case. Also check this before assuming a recipe's MAtricks can be set the same way — it can't; the recipe-line MAtricks editor's full UI map (X/Y/Z tabs, no Wings row) is here too.


**Wrong (confirmed failing live, 2.4.2.2):** both `Set MAtricks XWidth 5` and `MAtricks XWidth 5` return **"Illegal object"** — the parser reads `XWidth` as a pool-object name, not a property.

**Repo manual doc-drift:** `MA_V2.4.2_MANUAL` ch12 §13b/§15 claims a no-pool-number `Set MAtricks <prop>` form works for the live selection. **This is wrong as written** — it drops the required `Selection` object. Correct the manual reference in your head; do not trust that section for this syntax.

**Correct (verified live against the official grandMA3 keyword page):**

```
Set Selection MAtricks "XWidth" 5
```

The object is **`Selection`**, and the property name is **quoted**. Also documented on the same keyword page:
- `Off Selection MAtricks`, `Toggle Selection MAtricks`, `Reset Selection MAtricks`
- `Set Selection 2 MAtricks "prop" val` — numbered-selection variant for a non-current/secondary selection.

**Recipe-mode caveat (2026-07-15, live):** this `Set Selection MAtricks` form does **NOT** reach a recipe's own MAtricks — a silent miss, caught only by an overlay/visual verify pass, not by command echo. A recipe's MAtricks must instead be edited in its own dedicated editor (opened via the recipe UI, not this CLI Selection-object form). That editor's internal property naming was observed via its own UI echo, e.g. **"Set DelayTo for direction X"** — different phrasing from the CLI's quoted `"XWidth"`-style names above. See `recipe-lane-end-to-end-verified` for the build this was caught in, and `store-recall-recipe-toggle-rules` for the EditRecipe bookend pattern it's part of.

**Recipe-line MAtricks editor, fully mapped (2026-07-16, live)** — this is the "own dedicated editor" referenced above: **X / Y / Z tabs**; rows **X / XBlock / XGroup** + **Fade / Delay / Speed** From⇄To pairs + **XShuffle / XShift** + **InvertStyle / Transform / InvertXYZ**. **No Wings row** appears on this surface (a reduced set vs. the full MAtricks editor) — **XWings instead rides the store-time `/MAtricks` embed lane** (the `Store .../MAtricks` flag from `store-recall-recipe-toggle-rules`). So a recipe carries **two distinct MAtricks surfaces**: this recipe-line editor (X/Y/Z tabs, no Wings) and the store-time `/MAtricks` embed (has Wings) — an asymmetry worth flagging in any future LD.md documentation pass. (`menu-matricks-overlay-cli-route`'s CLI-opened `Menu "MatricksOverlay"` editor is presumed to be the general/live-selection MAtricks surface, not this recipe-line one — not independently confirmed identical, but consistent with the "two carriers" split here.)

**2026-07-17 addendum — a CLI write lane into a recipe's MAtricks does exist after all, just not this one:** `Assign MAtricks n At Sequence c Cue 1 Thru Part *.*` is a forum-sourced (Kanarek, forum 69993) CLI form that binds a MAtricks pool object onto recipe lines directly — a different verb (`Assign`, not `Set Selection MAtricks`) reaching what may be the same target this concept's recipe-mode caveat said was only reachable via the dedicated UI editor. Not yet cross-verified against the UI editor for identical results. Full grammar (plus the parallel Preset/Shape/Group Assign forms) lives in `recipe-line-pool-binding-via-assign` — load that concept for the write side; this concept remains the source of truth for the live-selection `Set` form and the recipe-line MAtricks editor's own UI surface.

## ⭐ THIRD WRITE SURFACE — `Set MAtricks <n> 'Prop' <value>` works on a POOL object directly, live-proven 2026-08-05 [0805cLD]

**`Set MAtricks <n> 'Prop' <value>` WORKS on a POOL MAtricks object**, not just on the live
Selection (the `Set Selection MAtricks` form documented above) and not just via file-side XML
authoring + Import (`xml-file-side-authoring-import-lane-proven`). Proven 3/3 with exact
readback: `Set MAtricks 183 'XGroup' 14` → reads 14; `Set MAtricks 184 'XGroup' 4` → reads 4;
`Set MAtricks 182 'PhaseFromX' 90` → reads 90.0. **Property name single-quoted, value bare.**
Far cheaper than the XML lane for a one-attribute change. Classifies Tier 2 (`Set `), gated
normally.

**Lane extended the same session, off MX 186 — three more facts:**

1. **A BARE NEGATIVE SURVIVES on this surface.** `Set MAtricks 186 'PhaseToX' -360` (unquoted)
   read back **`-360.0` exact** — no sign-eating. This CONFIRMS the scope boundary already
   asserted in `patch-set-one-prop-quoted-values`: the minus-sign trap is specific to
   patch-fixture `Set`, and does NOT extend to a MAtricks pool object. Quoting is not required
   here.
2. **`XinvW` IS SETTABLE from this lane** — `Set MAtricks 186 'XinvW' 'Yes'` reads back
   **`true`**. The invert family does not need a desk click.
3. **`PhaserTransform` IS a real property on a MAtricks pool object** — it returns `None`
   (unset) rather than erroring, so the property name is correct and the transform is settable
   in principle.

**⚑ Correct property NAMES pinned by contrast:** **`XinvW`** and **`PhaserTransform`** are
real; **`Xinv`** and **`Transform`** are NOT (both return no-such-property). Don't guess the
short forms.

## `PhaserTransform` enum token attested — `Mirror`, 2026-08-05 [0805cLD]

Dave set `PhaserTransform` at the desk on **MX 186**, and the live Lua read returns
**`PhaserTransform=Mirror`** — the token is literally `Mirror`, matching what {LD}'s own
wrapper XML writes. Property confirmed present, readable and desk-settable on a **MAtricks
pool object** (previously only ever seen as an attribute on {LD}'s `StandardRecipe`
wrappers). **Whether it is also SETTABLE from the `Set MAtricks` CLI lane above is still
untested** — Dave clicked this one at the desk; try `Set MAtricks <n> 'PhaserTransform'
'Mirror'` on a scratch object next time the question comes up. Worked example: MX 186 (`cLD W2
G2 X-360 MIR`) matches {LD}'s `Spot Pan#2` wrapper exactly on `XWings/XGroup/PhaseFromX/
PhaseToX/XinvW/PhaserTransform` — see `tourshow-seq2210-song-l-build-record`.

History: corrected same session, 2026-07-10, after the bare forms failed and the official keyword page was checked. 2026-07-15: recipe-mode caveat added — this CLI form does not reach a recipe's own MAtricks; the recipe MAtricks editor is a separate surface with its own property naming. **2026-07-16:** the recipe-line MAtricks editor's full UI surface mapped (X/Y/Z tabs, row list, no-Wings finding) — confirms and completes the 07-15 caveat. **2026-07-17:** addendum added noting a forum-sourced `Assign MAtricks` CLI form that may reach the same target via a different verb — see `recipe-line-pool-binding-via-assign`. **2026-08-05 [0805cLD]:** third write surface added — `Set MAtricks <n> 'Prop' <val>` on a POOL object directly, plus the `PhaserTransform`/`XinvW` dialect facts and the `Mirror` enum token.


## TWO INVERT LANES — do not confuse them (2026-08-20, festival clone day)

A clone-day rig needs **both**, and they are different mechanisms:

| Lane | What it is | Where | Form |
|---|---|---|---|
| **Live mirror** | MAtricks `InvertStyle` {`Pan` · `Tilt` · `Pan and Tilt` · `All`} + `InvertX` on the **current selection** | the symmetric-rig mirror tool, per selection | `Set MAtricks InvertStyle "Pan"` · `Set MAtricks InvertX 1` (0 = off) |
| **Permanent orientation** | **PATCH invert** — the fixture sheet's `InvPan` / `InvTilt` columns | the fix for fixtures hung backwards | fixture sheet / patch |

**Dave's redirect:** for cloned house fixtures the wanted tool is the **patch/setup** lane — a permanent orientation fix that presets then follow. The MAtricks lane is the *live* mirror, useful at the desk in the moment.

**⚠ The `Set MAtricks InvertStyle "<value>"` value-string form was never live-verified** — the wire was down when the toolbox around it was written, and it stayed unverified through the end of the leg. **Validate on a scratch selection before trusting it.** Manual source: local manual ch.12 §16.

History: extended 2026-08-28 (librarian, tour leg) — the two-lane distinction plus the unverified value-string flag.


### matricks-phase-distribution-on-gappy-grids-open-question
**CONFIRMED 2026-07-16: MAtricks PHASE distribution respects gaps via ABSOLUTE grid coordinates (same model as XWidth) — a gap consumes a beat, live 100% verified**
*when:* Before trusting phase-math formulas on a grid with gaps or a non-zero origin — N = the full grid extent including gaps, not the occupied-cell count; live-confirmed 2026-07-16, no longer an open question (id kept unchanged for stability, see History)


**RESOLVED 2026-07-16 — id and framing below kept as the historical record of the question; see the confirmation paragraph near the end for the answer.**

**Originally unresolved:** `matricks-xwidth-wraps-on-absolute-grid-x` confirmed that XWidth re-wrap uses each fixture's **absolute** grid X coordinate, mod width — a non-zero grid origin produces uneven, wart-carrying wraps. It was **not yet known** whether MAtricks **PHASE** distribution behaves the same way, or whether it instead **compresses to only the occupied cells**, ignoring gaps/origin offsets. (Answer, confirmed live 2026-07-16: PHASE behaves the same way as XWidth — absolute coordinates, not compression.)

This matters directly for `phase-math-formulas`: those formulas assume a clean `N` (effective fixture count). If Phase uses absolute grid coordinates like Width does, a gappy or offset-origin grid could silently produce the wrong phase spread even when N is computed correctly — the formula's N-based math would need a grid-compression step first.

**Verifies with:** build a phaser on a deliberately offset or gappy grid (non-zero origin, and/or a grid with empty cells between occupied ones) and observe whether the phase values land as if the occupied cells were compressed to a clean 0..N-1 run, or as if the raw grid coordinates (including gaps) were used directly.

**Dave's operator answer (2026-07-15, not yet the live 100% confirm):** per Dave's own operating knowledge, **empty cells ARE respected** by MAtricks phase distribution, the same way they are by XWidth — unoccupied grid cells still count as coordinates (a `Next` step landing in a gap produces no stage output that beat). Reframed as design doctrine: a gap in the grid's time-map is a **rest** — mirrored/bounce gap placements author deliberate rests into a chase. Consequence for `phase-math-formulas`: **N in the phase formulas = the full grid extent including gaps, not the occupied-cell count** — the absolute-coordinate model, not the compress-to-occupied model. This **largely closes** the question above, but Dave was explicit he wants a **live 100% confirmation** before treating it as fully settled — `status` was held at `verify` until that run happened (see the confirmation two paragraphs below: it has now happened, and status is `active`).

**Queued verification test (per the 2026-07-15 wrap):** Group 121 (contiguous, no gaps) as the **control**, Groups 124/128 (gappy layouts) as the **test cases** — fire the same phase distribution and visually confirm the gap-as-rest behavior live before flipping this concept to `active`.

**Live 100% confirmation (2026-07-16, Dave, attended, live on Group 124's bounce grid, 2.4.2.2):** a gap on the grid CONSUMES A BEAT in phaser traversal. Per the session's own framing this CLOSES the queued live confirm above. **Structural corroboration, same session:** a Chase recipe run on Group 124 "cLD DS WING BOUNCE" ran single-cell (AdaptiveWidth), honoring the sparse grid with no compaction — positional jumps were consistent with gap columns passing dark rather than being skipped/re-indexed. That's the structural half of the picture; the rhythm half (a gap consumes a full beat, not just a visual skip) is the live confirmation itself.

Consequence for `phase-math-formulas`, now settled rather than hypothetical: **N in the phase formulas = the full grid extent including gaps, not the occupied-cell count** — confirmed the absolute-coordinate model, not the compress-to-occupied model.

See `gap-is-a-rest-doctrine` for the design-doctrine framing of this same result (a gap in the grid's time-map is a rest), now also on confirmed mechanical footing.

History: none — probe fired as an open question 2026-07-10, not yet tested. 2026-07-15: Dave supplied an operator-knowledge answer (empty cells respected, absolute coords, gap=rest) that appeared to close this question — status intentionally held at `verify` pending Dave's explicit live 100% confirmation; test plan queued (121 control vs. 124/128 test). **2026-07-16: live confirmation ran** on Group 124's bounce grid, attended by Dave — a gap consumes a beat in phaser traversal, corroborated the same session by the structural Chase-on-124 test. Status flipped `verify` → `active`; question answered. Title updated to state the answer (id kept stable per the librarian's no-rename rule).


### matricks-pool-reusability-and-block-structure
**MAtricks pool objects are grid-agnostic and reusable; the 30-look block structure convention**
*when:* When porting MAtricks pool objects to a different rig/grid, or when orienting to the Coachella pool-numbering convention (MAtricks/Sequences/Executors all run 1-30/201-230)


**MAtricks pool objects are grid-agnostic** — they are reusable on any rig, provided phase is recalculated for the new grid's fixture count/geometry (see `phase-math-formulas`). A pool object built for one rig's N does not silently work on another rig without recomputing N-dependent phase values.

**30-look block structure** (Coachella-specific numbering convention): **MAtricks 1–30, Sequences 1–30, Executors 201–230** — a fixed 1:1:1 mapping across the three pool types for the 30 looks in the show.

## ⭐ THE SET IS NOW LIVE IN THE BUILD FILE — and its portability is proven

**Dave imported the 30 Coachella Spectra Tower MAtricks to pool 111-140** (2026-07-28), inside
the cLD namespace alongside the 101-104 Full/Half/2-Wing/Quarter block. **They bind to a cue
recipe by `Assign` alone.**

**The "recalculate phase for the new grid" caveat above does NOT bite this set.** Operator
evidence (Dave): *"I've used the same MAtricks on several different shows with several fixture
groups big and small and honestly they all translated well with no adjusting on the phase
settings."* That is stronger than a value-read — it exercises the stored value AND how the
console applies it across differing N. A count-computed literal could not have translated
cleanly; translating with zero adjustment means the values are generic.

**Consequence: adopt wholesale, no genericizing pass.** These are the reference implementation
of `no-baked-n-portable-phaser-doctrine` and the spatial half of
`tourshow-authoring-contract-v01`.
History: none — stable since 2026-04-01. Updated 2026-07-28 [0727-2cLD]: the Coachella 30 are live at pool 111-140 and their portability is confirmed by multi-show operator evidence, so this concept's phase-recalculation caveat does not apply to them.


### matricks-store-time-embed-travels-with-preset-export
**A phaser preset's store-time /MAtricks embed travels with its export as literal XWings/XGroup/XBlock/XShuffle/YShift attrs — grep for them, don't infer phase distribution**
*when:* Before spec-reading ANY inherited phaser preset to figure out its spatial distribution — check the export for XWings/XGroup/XBlock/XShuffle/YShift/Width literals FIRST; phase-distribution inference is the fallback, not the method


**Method (card-candidate, CARD_AUTHORING):** when spec-reading any inherited phaser preset, **grep the export for `XWings`/`XGroup`/`XBlock`/`XShuffle`/`YShift`/`Width` literals FIRST.** The store-time `/MAtricks` embed travels with the preset export as literal attributes — reading them directly is the method; inferring the spatial pattern from phase distribution alone is only the fallback when no embed is present.

**Confirmed across {LD}'s SONG_B pool block 21.1100-1109** (Dave called it — "wings"), per-slot: `1100 XShuffle=5` · `1101 XWings=2` · `1102`/`1107 XWings=2+XGroup=4` · `1103 XWings=2` (5-step 72° observed → matched to our Wings2+Group5) · `1104 XWings=2` · `1105 XWings=2` (all populations) · `1106 XShuffle=5+XWings=2` · `1108 XWings=2+XGroup=16+YShift=-1` · `1109` bare (no embed).

**Cost of learning this the slow way:** two sheet revisions, before the grep-first method was adopted.

**Companion caution:** stock/imported MAtricks pool object LABELS are not evidence of their stored values (`tourshow-stock-matricks-pool-inventory`) — export-verify a candidate match before reusing it, the same discipline this method already applies to reading an inherited figure.

**Relation:** `tourshow-whole-fixture-block-law` (the block-size law this reading method feeds). `matricks-negative-value-lua-uint32-wraparound-gotcha` (why export readback, not a live Lua read, is the trustworthy lane for one of these literals — `YShift`). `tourshow-seq1110-song-b-build-record` (the build this method was proven on).


## PAID lesson 2026-08-01 [0801-2cLD] — probe with an UNFILTERED attribute dump, never a hand-written allow-list

**A phaser-embed probe using a FIXED attribute allow-list silently missed `YShuffle` on Swell Dim#3** — three distinct populations were read as only two signatures, because the allow-list didn't anticipate that attribute. **Lesson: probe with an unfiltered attribute dump — everything starting `X`/`Y`/`Z`/`Phase`/`Speed` — never a hand-written allow-list.** An allow-list can only find what you already thought of; this is the same failure shape as any fixed-vocabulary scan missing an attribute nobody wrote down in advance. Apply this to the grep-first method this concept already documents: the grep/probe pattern itself needs to be a wide prefix match, not a curated list of known attribute names.

**Companion census-methodology note:** {LD} encodes a deliberate NO-SPREAD as `PhaseFromX=0 PhaseToX=0` written explicitly ON the recipe line, rather than omitting the attributes entirely. A bare (absent) authored line and a `0->0` authored line are different artifacts with different meanings — when censusing for "bare" (unspread) figures, compare against the source's own explicit `0->0` marker, not against simple attribute absence.

## XGroup attribute order now attested, 2026-08-01 [0801-2cLD]

When a new X-family MAtricks attribute debuts, no desk-order authority previously existed in the corpus's goldens for where it belongs in the attribute sequence. **`XGroup`'s first use (SONG_I `157`/`161`/`162`) is now proven on import**: it lands correctly at the emitted position **`ShuffleMode -> XGroup -> XBlock -> XShuffle`**, live Lua read-back exact. Export-verify is still owed on any FUTURE first-use of a different new attribute in this family — this only settles `XGroup`'s position specifically.

**[0805-2cLD] EXTENSION:** fuller form of this law, with {LD}'s recipe anatomy and the residue-miscall evidence: `source-figures-are-recipe-presets-spread-read-law` — iterate `pre.iter('StandardRecipe')`, do not just grep the literals.

History: extended 2026-08-05 [0805-2cLD] — cross-ref to source-figures-are-recipe-presets-spread-read-law (the embed is full StandardRecipe lines; iterate them first).


### matricks-xwidth-wraps-on-absolute-grid-x
**MAtricks XWidth re-wrap uses ABSOLUTE grid X position (mod width), not selection order — a non-zero grid origin produces uneven wrapped rows**
*when:* Before applying an XWidth re-wrap to a stored Group — check the group's actual grid X origin first, or a non-zero-origin grid will wrap unevenly; also relevant when deliberately using an XWidth wrap to collapse a sparse aligned multi-row selection into one block


**XWidth re-wrap operates on each fixture's ABSOLUTE grid X coordinate (mod the width value), not on selection/storage order.**

**Observed case:** Group 101 turned out to be stored with fixtures at grid **X = 1..10** (not the expected 0..9 — an off-by-one grid origin baked in at storage time). Applying a **width-5 wrap** against this group produced uneven rows — **(1-4) / (5-9) / (10)** — with an **empty origin cell**, instead of the clean split you'd get from a zero-based 0..9 origin.

**Grid warts persist through group store and survive into transforms.** A grid-coordinate irregularity (like a non-zero origin) baked in when a Group was stored doesn't get normalized away — it silently propagates into any later MAtricks transform (XWidth, and presumably other absolute-grid-coordinate operations) applied to that group.

**Practical rule:** before applying an XWidth re-wrap (or any width/coordinate-based MAtricks transform) to a stored Group, check the group's actual grid X origin — don't assume it starts at 0.

**Open question this raises:** does MAtricks **Phase** distribution behave the same way (absolute grid coordinates) or does it compress to only the occupied cells on a gappy/offset grid? See `matricks-phase-distribution-on-gappy-grids-open-question` (unverified).

**Deliberate use, reframed 2026-07-14 (grid drill session):** the same mod-width wrap behavior, once understood, doubles as a controlled collapse tool rather than just a trap. `Set Selection MAtricks "XWidth" 12` applied to a sparse aligned pair of rows (e.g. two rows built at different step intervals over one shared window) folds both rows into a single 12-wide multi-layer block — Dave's framing: "bring them together." `Reset Selection MAtricks` unwinds the transform cleanly back to the original sparse layout. Same underlying mechanism as the trap above; the difference is knowing the group's grid-X origin going in and choosing the width deliberately.

History: discovered live 2026-07-10 while re-wrapping Group 101 (uneven-wrap trap). Reframed 2026-07-14 as a deliberate collapse tool when the grid origin is known and the width is chosen on purpose — see `grid-drill-exemplar-groups-121-124`.


### measure-attribute-show-wide-census
**Measure attribute, show-wide census: only 28 of 166 figure rows carry one at all, and Measure 4 (one bar) is the ONLY real value anywhere in {LD}'s file**
*when:* Before assuming a song's figures need a Measure fixup, or before treating Measure as a common attribute — it is rare and concentrated on one figure class; check the song's own figure data before asserting a Measure action is owed


**Show-wide census, off `FIGURE_HASH_SHOWWIDE_v2.csv`: only 28 of 166 figure rows carry a
Measure attribute at all.** Of those 28: **7 read `16777216`** — the fixed-point encoding of
literal `1`, i.e. the DEFAULT (not a real measure) — and **21 read `67108864`** — Measure
**4**, one bar.

**Measure 4 is the only real Measure value anywhere in {LD}'s file**, and it lands
specifically on the breathe/swell-class Dim figures: SONG_G `Intro 1/1 Dim`, SONG_D `Swell`,
SONG_J `Swell Dim#3`, SONG_A `Intro 1/1 Strike M US RGB Dim`.

**SONG_L carries ZERO Measure across all 10 of its figure rows** — proven by this census,
not by absence of contrary evidence.

**Consequence — do not reflex a Measure fixup from doctrine.** `phaser-copy-does-not-carry-
measure` documents that a `Copy` doesn't bring a source's Measure along, but that rule only
bites when the SOURCE actually carried one. Check the song's own figure data before asserting
a Measure fixup is owed — see the caution folded into that concept.

**Relation:** `phaser-copy-does-not-carry-measure` (the mechanism this census scopes),
`tourshow-seq2210-song-l-build-record` (the build this census was run for, which the
result cleared of any Measure debt).


### measure-doctrine-time-lease-and-cohesion
**Measure = a phaser's time-to-live in beats, and a lease on song real estate — default ONE measure, and every phaser story must justify its cohesion with the music over exactly that span**
*when:* Before setting a phaser's Measure value, or writing a phaser story that claims more than one measure — the design-doctrine layer on top of the measure mechanics


Two paired rules from Dave, paraphrased (meaning over transcript; his own framing phrases kept verbatim in quotes):

**Framing — default and weight:** Measure is the phaser's time-to-live, counted in beats. The working default is ONE measure (one beat), and most effects should just live there without needing more. Adding a measure spreads the same figure across two beats, with points landing exactly on the grid where authored. This is the direct line from the temporal-relational system (illusions of movement built from relational on/offs in time) down to the actual music — **"the land-inside-the-count knob."** Dave's explicit ranking: measure is **"a cool tool, NOT the center of the curriculum"** — don't overweight it in the drill.

**Cohesion test — the standing question:** Measures TAKE TIME. A measure count is **a lease on song real estate** — claiming N beats obligates the effect to make sense unfolding over exactly that much time. The standing question for every phaser story (see `phaser-story-doctrine`) is: *"whatever measures are used — how is it cohesive with the music?"* Worked example: a Measure-4 Flyout claims 4 beats — it has to earn them and land back on the count, not just run out the clock.

**Relation:** `phasers-via-measures-curriculum` is the separate pedagogical/testing process (read manual → live-test → then build) for LEARNING measures; this concept is the design-content doctrine itself — what a measure means, how to weight it, how to judge it. Load both together for phaser-story work.

History: none — both halves dictated same session, 2026-07-16; merged here as one concept since the framing and its own verification test travel together.


### measure-layer-math
**Measure layer — definition (official manual) and runtime-scale math (MA forum 68396)**
*when:* Before setting a Measure value on a phaser/recipe layer, or before predicting how long a step/loop will actually take once Measure is set — the repo manual does not define this layer, this is the forum-sourced formula


**Definition (official 2.4 manual):** Measure is an optional phaser layer = the number of **beats** in one loop. Combined with Speed, it fixes the loop's real time (e.g. `Measure 4 @ 120 BPM = 2s`). Knocking in Measure with **no value** adopts the current step count. Speed, Speedmaster, Phase, and Measure are all **per-attribute-per-fixture**, and stay **constant across steps**.

**Runtime-scale math (Andreas/MA, forum thread 68396):**
- With **no Measure set**, loop length = `Σwidths / 100` beats.
- With **Measure set**, runtime scale = `Measure ÷ (Σwidths / 100)`. Widths are **NOT rewritten** — proportions are preserved, only the playback rate scales.
- Per-step time: `step_beats = Measure × width ÷ Σwidths`.
- Reading: widths compose the note values (relative proportions within the loop); Measure is the bar — the absolute time budget the widths get stretched or compressed to fit.

**Why this had to be forum-sourced:** the repo manual has **no definition of the Measure layer** (column label only — repo-manual gap #4+). The full manual-vs-live study (15-test matrix) is written up in `PHASER_MEASURES_STUDY_v0.1.md` (WORKING/).

Cross-reference: `stock-measures-grammar-census` for how MA's own stock recipe library actually uses Measure per effect category; `wipe-in-thru-range-anatomy` for a full worked example of widths distributing inside one `Measure=1` loop; `phasers-via-measures-curriculum` for the teaching approach that produced this study.

History: created 2026-07-16, merging the official-manual definition with the forum-sourced runtime formula (two parts of one Measure-math concept) plus the repo-manual-gap provenance note.


### menu-matricks-overlay-cli-route
**Menu "MatricksOverlay" opens the MAtricks editor from the CLI, no click required**
*when:* When you need to open the MAtricks editor programmatically/via CLI instead of clicking the encoder-bar MAtricks button


Clicking the encoder-bar **MAtricks button** echoes `Menu "MatricksOverlay"` in the command line — this is the CLI route to open the MAtricks editor directly, without clicking:

```
Menu "MatricksOverlay"
```

History: none — discovered live 2026-07-10 by observing the echo from a manual click.


### mtricks-phase-vs-encoder-phase
**MAtricks Phase is a literal manual value; Encoder Bar Phase auto-calculates**
*when:* Before setting Phase on any MAtricks pool object destined for preset/cue storage — do not trust encoder-bar-derived values for pool storage


**Phase in MAtricks = LITERAL degree value** — you must apply the `360 − 360/N` (and related) formulas manually; the console does not do this math for a MAtricks pool object.

**Phase in the Encoder Bar = AUTO-CALCULATED** — the console does compute it there, live, during interactive fanning.

Pattern this drives: **phase math is always applied manually before storing to a MAtricks pool object** — never trust encoder-bar-derived values when the destination is MAtricks pool storage, because the two surfaces do not share the same computation path.

See `phase-math-formulas` for the actual formulas.

History: none — stable rule since 2026-04-01.


### mx-cell-geometry-law
**⛔ MX cell-geometry law: Blocks and Groups encode PER-UNIT or SUB-UNIT texture and break when a venue's fixtures arrive 1-cell — strip Block/Group, KEEP wings, shuffle and phase ranges; mint flat twins and repoint SELECTION-SCOPED so other populations are untouched**
*when:* Before adapting a show to a venue whose fixtures have a different cell count than the file was built for — 1-cell strobes, 14-cell plates, 28-cell tubes; this is the doctrine and the whole venue MX kit is built on it


## The distinction that carries everything

MAtricks properties split into two classes:

| Class | Properties | Depends on |
|---|---|---|
| **Cell geometry** | `XBlock`, `XGroup` (B12/B14/B7/B28, G7/G14/G16/G21) | the **cell count of one fixture** |
| **Population geometry** | `XWings`, shuffle, `PhaseFrom/To` ranges | **how many units** are in the selection |

**Cell geometry is what breaks when the venue's fixture is a different animal.** Population geometry is portable.

## The three venue cases

- **1-cell units** (single beam + single colour plate, or a 13-channel basic mode): the per-unit texture the blocks encoded is now **automatic**. **Strip Block and Group, keep wings + shuffle + phase ranges.** Clearing is `m.XBlock = 0` / `m.XGroup = 0`, reading back `None` (`matricks-property-clear-encoding`).
- **Different multicell count** (heritage 12 → venue 14 plates, 28 tubes): **mint block twins at the new number** — `B12 → B14`, tubes `→ B28` — and repoint. Same doctrine, different target.
- **Native multicell** matching the file's build number: the file needs **nothing**.

## Selection-scoping is not optional

The same MAtricks object is used by populations that are *not* affected — spots, the touring pixel line, QX40. Repoints are therefore **scoped to the recipe lines whose Selection is the affected family**, so the untouched populations keep the original object. This is also why the tour file stays pure: the originals are never edited, only new twins are minted beside them.

**Per-sequence reverse maps make restore exact.** Several sources collapse onto the same twin (`W2 FLAT` arrives from both `WING 2` and `G7 FLAT` on different songs), so a naive reverse is ambiguous. Record the map per sequence as you sweep.

## Receipts across four venues

| Venue class | Units (plates / tubes) | Broken lines found | Result |
|---|---|---|---|
| 14-cell plates + 28-cell tubes | 52 | 3-4 | twins `B14`/`B28` minted, repointed |
| 1-cell, tubes dormant | 18 / 0 | 18 | flat twins, still-broken = 0 |
| 1-cell, tubes LIVE | 24 / 24 | 19 (the 18 + one tubes line) | flat twins, still-broken = 0 |
| 1-cell, prime population | 11 / 11 | 19 | one macro tap, still-broken = 0 |

**Verification is always the same:** a fresh export sweep across the plate *and* tube families reporting **still-broken = 0** (`export-plus-python-bulk-lane`).

## Aesthetic notes for the operator's eye

- Stripping blocks spreads a pattern **across the whole population** instead of chunking it per unit — looks read smoother. If a look reads *too* smooth, **small Groups are the grain dial**: pick divisors of the population (G2/G3/G6/G9 at 18; G2/3/4/6/8/12 at 24).
- **Prime populations run wings uneven** — 11 units on W2 is 6+5, a mirror that is functional but slightly asymmetric. Functional call is cLD's, aesthetic call is Dave's.
- A dormant family (tubes with an empty group) makes its recipes **cook to nothing** rather than error — a silent, benign no-op that becomes live at the next venue.

**Relation:** `tourshow-whole-fixture-block-law` (where the per-family block numbers come from) · `matricks-property-clear-encoding` · `venue-adapt-macro-pattern` (the kit this doctrine became) · `selection-count-probe` (how the unit counts are established) · `phase-math-formulas`.

History: none — doctrine formed at the first 1-cell venue 2026-08-26 and re-attested at every subsequent venue through the end of the leg.


### no-baked-n-portable-phaser-doctrine
**NO BAKED N in travelling content — stock MAtricks + generic phase ranges (0-360 / 0-180) + AdaptiveMeasure/AdaptiveWidth, never a phase literal computed for a specific fixture count**
*when:* Before authoring ANY phaser, MAtricks value or recipe that has to survive landing on a different rig — this is the one thing that genuinely breaks across rigs, and it is the requirement the fixture-agnostic recipe doctrine depends on


**Dave's ruling.** Differing pixel counts across rigs are fine. **A MAtricks carrying a
phase literal computed for a specific N is not** — that is the single thing that actually
breaks when content lands on a different rig.

## The worked example

A phase stored for **N=228 cells** is `360 − 360/228` = **358.4°**. Recalled on **7 floods**,
the seven land at 0 / 59.7 / … / 358.4 — putting the last fixture **1.6° off the first**, a
visible collision at the wrap. The correct value for N=7 would have been **308.6°**.

So `360 − 360/N` is **MORE correct on a known N and BRITTLE everywhere else** — the wrong
trade for a show that lands on a different house rig nightly.

## The portable phaser shape

1. **Stock MAtricks pool object** (`tourshow-stock-matricks-pool-inventory` — pool 1-30,
   Reset/Phase/Block/Group/Wing families).
2. **Generic phase range** — `0-360` for a full spread, `0-180` where
   `Direction=Alternate` (bounce doubles the traversal, per `stock-measures-grammar-census`).
   **`PhaseToX=360` is safe: the engine normalises it as one full lap with endpoints
   excluded** — Dave confirmed, resolving `recipe-phase-endpoint-convention`.
3. **`AdaptiveMeasure` + `AdaptiveWidth`**, which per `v24-phaser-model` auto-calculate
   timing and width **from the current selection grid** rather than from stored numbers.
4. **Grid coordinates live in the GROUP**, which the contract already bakes at Store time.

**Net: no N appears anywhere in the recipe**, and the same phaser recomputes itself for 7
fixtures or 228. The adaptive layers are the built-in answer to cross-rig scaling and should
be standard on all travelling content.

## What is NOT superseded

**Keep `360 − 360/N` for locking a KNOWN rig.** `phase-math-formulas` remains correct for
MAtricks **pool storage**, where phase is a literal manual value the console does not
compute (`mtricks-phase-vs-encoder-phase`). Two surfaces, two computation paths, two
different questions — the literal formula for a fixed rig, generic ranges for anything that
travels.

## ⭐ The reference implementation — what "done right" looks like

**Dave's 30 Coachella Spectra Tower MAtricks (imported to pool 111-140) are the positive
exemplar of this doctrine.** Operator evidence, 2026-07-28: *"I've used the same MAtricks on
several different shows with several fixture groups big and small and honestly they all
translated well with no adjusting on the phase settings."* They bind to a cue recipe by
`Assign` alone.

**Why that is proof rather than anecdote:** a phase literal computed for a specific N
**cannot** translate cleanly to a different N — it collides at the wrap or leaves a hole
(see the worked example above). Translating across several shows and several group sizes
with **zero** phase adjustment is only possible if the stored values are generic. And it is a
stronger test than reading a value off one slot, because it exercises the whole chain — the
stored value *and* how the console applies it across differing fixture counts.

**Practical consequence:** adopt the set wholesale, no genericizing pass. And any MAtricks
authored from here should look like these — this is the standard the doctrine points at.

## Why this doctrine is load-bearing

`recipe-layer-is-fixture-agnostic-doctrine` explicitly REQUIRES this to hold. `Group x Preset`
absorbs rig and fixture-type differences, but a baked phase literal smuggles a fixture count
back into the content layer and defeats the whole scheme. First live test: 19 upstage JDC1
replaced by 7 LEDJ Q40 — **phaser resolution degrades gracefully** (a fine chase across 228
cells is a coarse one across 7 floods; same recipe, still correct, reads differently). **The
cut hits the FILL layer, not the CONTENT layer.**

History: ruled by Dave 2026-07-27; filed 2026-07-27 [0727-2cLD], closing the librarian
debt flagged at that session's boot (the fixture-agnostic doctrine had been citing this
concept before it existed). Updated 2026-07-28: gained a positive exemplar — the Coachella 30 (MAtricks 111-140), proven portable across multiple shows and fixture counts with no phase adjustment, promoting the concept from a cautionary rule to one with a reference implementation.


### part-attr-order-import-absorption-gotcha
**⛔ Multi-part cue-part attribute ORDER is not free-form on import — SpeedScale out of desk-export order absorbs the cue's first content part into part 0, silently**
*when:* Before hand-authoring or generating ANY multi-part sequence-cue XML for import (parts-per-century or any other multi-part cue shape) — the Part element's attribute order must clone the desk-export order byte-for-byte, especially SpeedScale's position


**Paid-for lesson (cost one delete+reimport):** a hand-authored multi-part cue's `Part` attributes must follow the **DESK EXPORT ORDER** — `SpeedScale` sits BETWEEN `MAgic` and `Mode`, on EVERY part, including part 0 / OffCue / CueZero.

**Failure mode:** appending `SpeedScale` AFTER `CueInFade` (instead of between `MAgic` and `Mode`) made the MA3 importer **absorb each cue's FIRST content part into part 0** — 33 `StandardRecipe` lines silently moved, part 1 (P1 SPOTS) emptied — while later parts in the same cue survived untouched. Import echoed clean; only a per-part StandardRecipe census against the source sheet caught the miscount.

**Fix / standing emit rule:** clone the golden export's part-attr order **byte-for-byte**. A second census after the reorder confirmed clean with the golden order restored.

**Scope:** this is a MULTI-PART-cue-specific hazard — a single-part golden cannot attest it, because a single-part golden has no second part to absorb into. See `smith-packet-must-stage-multi-part-golden` for the consequence this has for what a smith dispatch packet must stage.

**Relation:** `sequence-xml-ordered-header-law` (existing concept, not staged this run) — same failure family one level up, at the cue-header level: children 1+2 must be OffCue+CueZero or content cue 1 maps INTO OffCue on import. This concept is the equivalent law one level down, at the Part-attribute level. `export-sequence-xml-schema` for the general Part/StandardRecipe export shape this order-law constrains (see this run's `updates/`). `parts-per-century-emit-pattern-and-et-gate` for the sequence architecture this gotcha was paid for while building.


### per-song-phaser-banking
**Phasers are banked per song, not from one big template library — a small shared 'punt page' of basics is the only commons**
*when:* When deciding where a finished phaser/recipe should live, or whether to build a general-purpose effect library — the storage-structure ruling


Each song's phasers get DESCRIBED during that song's exploration pass (the beatgrid + description layer, per `phaser-story-doctrine`) — programming then means building the pre-described set for that song, and the result is **banked per track**, not pooled into a general library.

Dave's explicit ruling: **no big template bank.** The only shared resource is a small **"punt page"** — basic effect stacks kept as commons for quick starts, not a comprehensive catalogue. Programming enters each song already knowing what it's going to write.

**Relation:** extends `phaser-story-doctrine` — this is what happens to the phaser AFTER the story is written and the recipe is built. Together the two describe the full per-song loop: plan (`phaser-story-doctrine`) → store (this concept).

History: none — doctrine stated 2026-07-16.


### phase-math-formulas
**MAtricks phase math formulas — full spread, line-by-line, wings/group/block effective N**
*when:* Before generating any Lua or CLI syntax that sets MAtricks Phase values for a phaser/preset — full-spread, line-by-line X/Y, or wings/group/block distributions


Phase in MAtricks is a **LITERAL degree value** — the console does NOT auto-calculate it there (contrast with the Encoder Bar, which does auto-calculate; see `mtricks-phase-vs-encoder-phase` concept). These formulas must be applied manually before storing.

| Pattern | Formula |
|---------|---------|
| Full spread | `PhaseTo = 360 - (360 / N)` |
| Line-by-line X | `PhaseToX = (360 / Y) × ((X - 1) / X)` |
| Line-by-line Y | `PhaseToY = 360 - (360 / Y)` |
| Wings effective N | `ceil(total / wings)` |
| Group effective N | `= group_count` |
| Block effective N | `ceil(total / block_size)` |

`N` in the full-spread formula is the effective fixture count for the distribution being built — computed via the wings/group/block sub-formulas above depending on which structure you're phasing across.

Concrete worked example (from the v2.4 sandbox, `CLAUDE_SETUP_V0.1.show`): a 1×10 line of generic fixtures, full-spread phase for N=10 = **324°** (i.e. `360 - 360/10`).

History: none — stable since 2026-04-01, reused as the worked-example check in the 2026-07-04 v2.4 sandbox session.

**[0805-2cLD] SCOPE RULING (Dave + message-board history): flat ±360 MAtricks phase literals STAND.** The `360 − 360/N` stop-short law stays scoped to HAND-BAKED per-fixture phases; the formula lane is for pin-specific phase on a fixture set. Do not "correct" a flat ±360 MAtricks knob literal to stop-short.

History: extended 2026-08-05 [0805-2cLD] — stop-short scoped to hand-baked per-fixture phases; flat ±360 MAtricks literals attested and standing (Dave, message-board history).


### phaser-copy-does-not-carry-measure ⚠ VERIFY
**Copying a phaser preset does NOT carry its Measure — a Copy'd Measure-carrying figure needs Edit Preset -> Measure N -> Update -> ClearAll reapplied by hand**
*when:* Before or immediately after Copy'ing any phaser preset that carries a Measure setting (e.g. cloning a template figure into a per-song slot) — and before assuming a clone behaves identically to its source; also before assuming a Measure edit on a RECIPE preset can be verified via export-diff — it cannot, the desk encoder is the only verify lane; use Update /NoConfirmation for the fixup when unattended or bare Update pops a dialog and cancels


A `Copy Preset <src> At <dst>` clones the figure but **does not bring the Measure layer with it**. A copied figure that is supposed to span a bar will run at the template's timing until Measure is set on the copy by hand:

```
Edit Preset <n>
Measure <n>
Update
ClearAll
```

(`Measure` is a first-class CLI layer keyword once a phaser is loaded into the programmer — `phaser-layer-cli-grammar-measure-keyword`. `Update` is mandatory or the edit silently reverts on clear — `recipe-preset-edit-requires-update`. `ClearAll` is the flush that stops the pulled-in values contaminating the next Store — `edit-session-mechanics-and-contamination-risk`.)

**Do not conflate three separate Measure facts:**
- Measure is not readable/settable as a Lua object property, at part or preset level (`measure-not-a-safe-lua-property-part-or-preset`).
- An Edit->Update round-trip rewrites more of the XML than the edited attribute (`phaser-preset-update-after-edit-rewrite-behavior`).
- **This concept:** the Copy operation itself does not carry Measure.

**`status: verify`** — this is on record from the SONG_A build plan, where `cLD SONG_A BREATHE` (21.1021, copied from 21.51 SINE) is queued for exactly this Measure-4 fixup at the desk. The fixup has **not yet been executed and observed**, so the claim is banked from the build reasoning rather than from a completed live round-trip. Confirm on that edit, then flip to active.


## Measure-fixup verify lane: recipe-preset exports carry no Measure attribute — desk encoder is the only verify lane — 2026-07-31 [0731-3cLD]

A SECOND, independent live instance of this concept's mechanism, on SONG_D: `21.1320`
(a phaser copy) needed the identical Measure-4 fixup. Two new operational facts surfaced
doing it:

- **Bare `Update` over an unattended CLI pops a dialog** ("User Canceled Command");
  **`Update /NoConfirmation` echoes OK.** Use the `/NoConfirmation` form for this fixup
  when unattended (same family as `saveshow-discipline-and-mcp-tier`'s SaveShow-dialog
  gotcha).
- **A recipe-preset export carries NO Measure attribute anywhere** — a Measure edit on a
  recipe preset is therefore **NOT export-verifiable**. The desk encoder eyeball is the
  only verify lane. (Contrast `phaser-preset-xml-measure-speed-fixed-point-encoding`, whose
  export-diff verify method is for BAKED phaser presets, which do carry a fixed-point
  Measure attribute — that method does not apply to recipe presets.)
- Measure-4 on `21.1320` was handed to Dave **UNVERIFIED** (no export-verify lane existed);
  Dave's own desk pass then **confirmed `21.1320` Measure=4 at the desk**, closing this
  specific instance live.

**Status: STAYS `verify` (cLD ruling on the librarian's flip proposal).** Tonight's 21.1320 was a file-side IMPORT clone of template 58 — a template that never carried a Measure — so this instance does NOT test the claim that a console `Copy` DROPS a Measure the source had. The CLI fixup chain's own commit was export-unverifiable; Dave set Measure 4 at the desk. The original verify condition (confirm on a real Copy'd, Measure-carrying figure, e.g. 21.1021 SONG_A BREATHE) is still open.


## Scope gap noted 2026-08-01 [0801cLD] — the verified case does not test whether Copy DROPS a source Measure

**Still genuinely open, despite this concept's status having been flipped to `active`:** the SONG_D case that motivated the flip (`21.1720`, Dave-confirmed Measure=4 at the encoder) is itself a Copy of template `21.51`, which carries **NO** Measure of its own — the same shape as the earlier `21.1320` case. **Neither confirmed case actually tests whether `Copy` DROPS a Measure the SOURCE object had** — both source objects were already Measure-less, so a Measure appearing (or not) after the copy says nothing about whether Copy preserves an existing one.

**The test is now cheap, unlike when this concept was first written:** `21.1720` is the first cLD-authored preset on file that DOES carry a Measure. `Copy 21.1720` to a scratch slot, then one encoder read, closes the open question either way — cheaper than waiting for another natural case to arise.

## ⚑ PROCESS CAUTION — check the song's own data before asserting a fixup is owed, 2026-08-05 [0805cLD]

**cLD wrongly asserted "Measure fixup owed on all four copies" for SONG_L**, purely as a
reflex from this concept's rule, WITHOUT checking the song's own figure data. SONG_L
carries **zero** Measure on any of its figures (see `measure-attribute-show-wide-census`), so
nothing was owed — withdrawn. **A standing caution from this concept is not itself a finding
for a specific song — confirm the source actually carries a Measure before invoking the
fixup.** Same shape as the "loaded is not applied" theme: having this rule on file does not
mean it fires correctly without being checked against the case at hand.

**[0805-2cLD] EXTENSION — copy also does not rewrite steps:** a copied template keeps its parent's steps. A new shape (SONG_O's DIP 70/w5/t0 → 20/w100/t60 from SNAP) needs a hand Phaser-Editor edit after copy — same lane as Measure-after-copy.

History: extended 2026-08-05 [0805-2cLD] — copy semantics widened: steps not rewritten either; new shapes take a hand Phaser-Editor edit post-copy, same lane as Measure.


### phaser-layer-cli-grammar-measure-keyword
**Bare `Measure 2` at the CLI sets the Measure layer once a phaser is loaded into the programmer via Edit Preset — a first-class layer keyword like the encoder layers**
*when:* Before typing or generating a bare layer-keyword CLI command (Measure, or other phaser layer keywords) — only works once a phaser is loaded into the programmer via Edit Preset; also before assuming a baked phaser pulled via Edit Preset carries recipe parts (it doesn't)


With a phaser loaded into the programmer (via `Edit Preset x` — see `edit-session-mechanics-and-contamination-risk` for what that pull does and its contamination risk), the bare CLI line **`Measure 2`** sets the Measure layer directly — Dave visually confirmed the change reflected on the encoders. **Measure is a first-class layer keyword**, the same class as the encoder layers.

**Baked phasers pulled via `Edit Preset` show as HARD VALUES** — no recipe parts appear, and `EditRecipe` stays OFF. Recipe mode is **recipe-preset-only**; it does not apply when editing a baked/hard-value phaser preset.

**Relation:** this is the CLI-keyword access path to Measure, distinct from — and currently the only working live path around — the object-property inaccessibility described in `measure-not-a-safe-lua-property-part-or-preset`. See `measure-layer-math` for what the Measure value means once set, and `phasers-via-measures-curriculum` for the broader learning context this was captured in.

History: none — confirmed live 2026-07-17.


### phaser-preset-update-after-edit-rewrite-behavior ⚠ VERIFY
**Update after Edit rewrites a baked-phaser preset's XML: explicit Speed/SpeedMaster attrs dropped, GridPos/GridPosMatr added per fixture; universal template row doesn't take the edit**
*when:* Before diffing or hand-authoring a baked-phaser preset that has been through an Edit→Update round-trip on console — the re-export is not a minimal diff, several structural changes ride along


**Observed on an Edit→Update round-trip (Edit Preset → set Measure 2 → Update → re-export, diffed against pre-edit export):**

- **Explicit `Speed`/`SpeedMaster` attributes get DROPPED** from entries where they were previously present — consistent with the project's zero-attribute-omission convention (defaults aren't written explicitly).
- **`GridPos`/`GridPosMatr` attributes get ADDED** per fixture entry that didn't have them before.
- **The universal template row (`IDType 2 ID 1`) did NOT take the Measure edit** — only the per-fixture **selective** entries picked up the new Measure value. The template/universal row is a separate write target from the per-fixture rows.

**Open corner [VERIFY]:** the full "layer-carry" semantics of Edit/Update — i.e., which layers/attributes an Edit→Update round-trip is guaranteed to preserve vs. silently rewrite/drop — is not yet mapped. Flagged to verify if it ever bites (e.g. if a future Edit→Update round-trip is expected to be a clean single-attribute diff and isn't).

Cross-reference: `phaser-preset-xml-measure-speed-fixed-point-encoding` for the encoding math this round-trip was used to ground-truth; `recipe-preset-edit-requires-update` for the related silent-revert-without-Update behavior on recipe presets specifically (this concept is about baked presets).

History: created 2026-07-17 from the same export-diff session that pinned the Measure/Speed encoding; status `verify` — the layer-carry question is explicitly open.


### phaser-preset-xml-measure-speed-fixed-point-encoding
**Baked-phaser preset XML: Measure and Speed are 2^24 fixed-point ints — stored = value × 16777216; 16777216 alone = literal 1 (default), not a None sentinel**
*when:* Before reading or hand-authoring a baked-phaser preset's Measure or Speed attribute values in exported/imported XML — the fixed-point encoding, ground-truthed by export-diff


**Pinned encoding (export-diff ground truth, zero guessing):** in a baked-phaser preset's XML, the `Measure` and `Speed` attributes are **2^24 fixed-point integers**: `stored = value × 16777216`.

- `Measure 2` at the CLI/encoder → XML value **`33554432`** (2 × 16777216).
- The ubiquitous **`16777216`** seen on default/untouched entries is **literal `1`** (the default value), **NOT** a "None"/unset sentinel — this **corrects an earlier reading** that treated 16777216 as a default/none marker.

**Method (repeatable for future fixed-point questions):** `Edit Preset x` → set the value on the console (`Measure 2`) → `Update` → re-export the preset → diff against the pre-edit export. This ground-truths encoding without guessing at the math.

Cross-reference: `recipe-xml-schema` for the sibling **recipe**-dialect XML shape (display-string phase values, not fixed-point ints — the two dialects diverge here); `measure-layer-math` for what a Measure value means musically at runtime (this concept only covers its on-disk encoding); `phaser-preset-update-after-edit-rewrite-behavior` for what else changes in the XML when an Edit→Update round-trip happens.

**Second data point, corroborated 2026-07-21:** the `cLD SONG_G BREATHE` phaser preset (`21.123`, Measure 4 = one bar) encoded as `Measure="67108864"` — exactly `4 × 16777216`, confirming the `stored = value × 16777216` formula on a second concrete value (the first was `Measure 2 → 33554432`, 2026-07-17). See `baked-phaser-preset-xml-schema` for the full worked breathe-preset example this value comes from.

History: created 2026-07-17, correcting an earlier same-session reading that had flagged the 16777216 sentinel as [VERIFY]/possibly-None — resolved via export-diff. Extended 2026-07-21: second data point corroborates the formula — Measure 4 (one bar) = 67108864, from the cLD SONG_G BREATHE phaser preset build.


### phaser-story-doctrine
**Write the phaser story before console time — phasers are the temporal engine translating concept into music-synced illusion; programming is pure translation, never on-site invention**
*when:* Before any song's programming session — the standing workflow discipline: plan on paper first, console time only translates


**Core doctrine** (paraphrase, meaning over transcript; Dave's coined terms kept verbatim): phasers are the temporal engine that translates a design concept into an observed visual illusion tied to the music. Per song, once the beatgrid landmarks and rhythm structure are known, Dave's rule is to **WRITE THE PHASER STORY before touching the console** — what each phaser is, and where its settings (measure/steps/direction/spread) land against the music. Console time is then pure translation of an already-finished plan into MA3, **never on-site figuring-out**.

This explicitly extends `beatgrid-treatment-transfer-layer-model` — the phaser story is the next layer past that pipeline's Layer 3 (edit judgment), carrying the treatment plan all the way to console handoff.

**The pipeline this implies (the loop), per song:**
1. Look at the song — beatgrid layout, points, rhythm structure.
2. Tell the phaser story — what each phaser is, where settings land — BEFORE console time.
3. Write up the recipes needed.
4. Build the recipe.
5. Assemble.
6. Drop into sequence.
7. Repeat until the song is programmed.

Console time in this loop = translation, not invention.

**Relation:** see `per-song-phaser-banking` for how the resulting phasers get stored/organized once built, and `measure-doctrine-time-lease-and-cohesion` for the cohesion test each phaser-story entry must pass. See `review-plan-gate-precedes-programming-doctrine` (2026-07-21) for the session-level process failure this doctrine's principle got paid for again on — being loaded is not the same as being applied; a REVIEW→PLAN gate now sits above this per-song discipline.

History: none — doctrine dictated 2026-07-16, captured 4 times (3 near-identical restatements of the core rule, 1 extension into the numbered per-song pipeline) — merged into one concept per the librarian's duplicate-merge instruction. Extended 2026-07-21: cross-referenced from `review-plan-gate-precedes-programming-doctrine`, the session-level gate this per-song doctrine's principle now sits under.


### pool21-block-layout-and-copy-source-law
**Pool 21 blocks: <century>00-0N = {LD} originals, <century>20+ = cLD per-song — copy-source slots point at OUR templates, never at {LD}'s composites; figure-hash decode counts over-split on serialization prefixes**
*when:* Before minting, copying, or re-pointing anything in preset pool 21; when resolving a FIGURES-sheet 'COPY SOURCE KNOWN' name; when reading figure_hash2.py decode counts.

Block layout (live census): **21.<century>00-0N = {LD}'s imported originals**
(unprefixed names, e.g. 2700-2706, 2500-2504) · **21.<century>20+ = cLD-authored
per-song recipes** (`cLD <SONG> <ROLE>`).

The FIGURES sheets' "COPY SOURCE KNOWN" names resolve to {LD} ORIGINALS, not
cLD objects. **Dave ruling (08-05): copy-source slot references must point at OUR
templates** — BUMP←21.58 SINE 1/2 · RAMP←21.53 RAMP UP · FILLS←21.56 TRAPEZE ·
TRAP←21.56 · DIP←21.55 SNAP. **NEVER copy {LD}'s originals into our recipe
slots**: his carry cell-level Selective rows + group DependencyExport —
re-author-don't-re-point doctrine (`recipe-layer-is-fixture-agnostic-doctrine`).
Complements `tourshow-authoring-contract-v01` (every song mints its own copies
at 21.<century>20; cross-song binds outlawed).

Hasher caveat: `figure_hash2.py` over-splits — it hashes raw step strings
INCLUDING the export's `*`/`?` serialization prefixes, so numerically identical
figures split into distinct hashes (Intro Dim fc45c43b vs 17e3a36e are the same
shape). The prefix is a serialization artifact, not semantics — one figure can
carry BOTH prefixed and unprefixed rows. Direction is safe (understates
copy-source availability) but it inflates decode counts in every run table.

History: none — minted 2026-08-05 [0805-2cLD]; live pool-21 census + Dave's copy-source ruling after the copied-source-originals rollback + figure_hash2.py over-split diagnosis.


### recipe-lane-end-to-end-verified
**Recipe lane verified end-to-end (2.4.2.2) — two builds: CLI EditRecipe bookend (07-15, standard recipes) and UI Recipe-Editor template-cook (07-16, imported phaser-recipe templates); both cook Group+preset references to correct DMX**
*when:* Before building a recipe-based cue (Group × preset references stored as recipe cue-parts), or before using the Recipe Editor UI to cook an imported phaser-recipe template (Selection/Values pickers, Add Standard Recipe) — this is the full worked, live-verified path for both the CLI and UI lanes


**Full verified path, live 2.4.2.2:**

1. **Show Creator Menu ("ShowCreator")** → create **Universal Dimmer (11)** and **Universal Mixcolor (61)** presets.
2. **`EditRecipe Programmer`** ON (the bookend pattern — see `store-recall-recipe-toggle-rules`) → **`Store Sequence 101 Cue 1 Part 1` / `Part 2`** with **Group + universal-preset references** → `EditRecipe Programmer` OFF. Parts built this way show **recipe markers** in the Sequence Sheet (see `select-sequence-retargets-sheet` for getting the sheet to follow Sequence 101).
3. **`Go+`** → DMX outputs the cooked recipe correctly — verified at universe 202: plates at R255/G0/B0, dimmers at 255 (checked via the DMX viewer's address calculator, see `dmx-viewer-address-edit-calculator`).

**Robustness confirmed:** firing `ClearAll` **inside** recipe-edit mode did **not** break the bookend — toggling `EditRecipe Programmer` off afterward stayed clean and the stored recipe was intact (folded into `store-recall-recipe-toggle-rules` as the canonical statement of this rule).

**Caveat found the same build:** a recipe's own MAtricks is **not** reachable via `Set Selection MAtricks` — see `live-selection-matricks-cli-set-syntax` for the silent-miss detail and the recipe MAtricks editor's own internal property naming.

**Preset behavior this build depends on:** universal presets resolve through each fixture's color-engine/emitter data — see `universal-presets-emitter-aware`.

---

**Second build, live-verified 2026-07-16 (UI-driven Recipe Editor — a different, pixel-driven lane from the CLI EditRecipe bookend above; this one cooks imported phaser-recipe templates, not just standard recipes).** Prerequisite context: MA's stock phaser-recipe presets are empty as bare presets — see `stock-recipe-presets-empty-as-templates` for the diagnostic that forced this lane.

**Template-cook mechanics (the fix):** Recipe Editor → **Add Standard Recipe** on programmer Part Zero → **Selection** cell offers None / From Value / **TAKE SELECTION** (captured selection shows as `<Recipe>` in brackets) → **Values** cell opens a preset picker (tabs confirm **pool numbers**: Phaser=21, All 2=22, All 3=23…) → pick e.g. Chase → cooks to output **immediately** (webinar realtime claim confirmed live). Observed on a single cell traveling across a Group-121 selection: **AdaptiveWidth** moved one cell at a time while **AdaptiveMeasure** paced it to the grid — screenshot-verified motion between frames.

**Recipe Editor UI quirks:**
- **"Add Standard Recipe" no-ops unless the "New Recipe" row is focused FIRST** (click the row, then click the button).
- **Selection-cell picker** = None / From Value / Take Selection + a row of Groups pool tiles — clicking a **tile = REFERENCE**, **Take Selection = captured** (shows `<Recipe>`).
- **Values-cell picker tabs prove pool numbers**: …9 Video, 21 Phaser, 22 All 2, 23-25 All 3-5, Bitmaps, Generators.
- Re-entering the Selection cell takes **two clicks** (first selects the cell, second opens the picker); the picker **remembers pool scroll position** between opens.

**Fully-referenced workflow, end-to-end live:** a StandardRecipe (Selection = **Group 124**, REFERENCE via picker group-tile click; Values = **Chase** template) cooked realtime → `Store Sequence 102 Cue 1` `/Overwrite` → executor playback cooks the chase straight from the cue. Observed: on Store, the recipe row **left Part Zero** (moved to the cue?) — **[VERIFY]** whether the stored cue holds a live recipe *reference* vs. *baked values* (check the Show Recipes column in the sequence sheet). Sequence 102 was assigned to **Executor 401** via the assign-dialog lane (Object → Sequence tab → row click); cue labeled **"cLD CHASE GAPS"**; show saved **v0.14**. This is the live proof of the webinar's fully-referenced doctrine banked in `v24-phaser-model`.

**Three-temporal-characters demo (attended, live):** one StandardRecipe line (Values = Chase template), **Selection reference swapped live 121→123→124** — the same phaser produced three distinct rhythmic characters purely from grid choice (flat march / paired double-hits / bounce-with-rests). Each Selection-cell swap **recooks instantly**. The reference-doctrine demo in miniature: **Groups = WHO, recipe = WHAT, grid = WHEN**.

History: full lane built and verified 2026-07-15 (first recipe build, CLI EditRecipe bookend + universal presets). **2026-07-16:** second build added — UI Recipe-Editor template-cook lane, picker mechanics, the fully-referenced workflow's live proof, and the three-temporal-characters demo.


### recipe-line-cli-addressing-and-list-readback
**A recipe line is addressed as a dot sub-index on the Part — Sequence x Cue y Part <p>.<r> (e.g. Part 0.1) — not a listable named child; List Sequence x Cue y Part 0.1 is the CLI readback lane; on a multi-part cue, address the part by NAME not number**
*when:* Before writing any CLI command that targets a recipe line inside a cue-part (Set/Assign/List) — the address grammar, the List-based readback lane, and — for a multi-part cue — why the part must be addressed by NAME rather than number


**Addressing:** a recipe line lives as a **dot sub-index on the Part**, not as a separately-listable named child object — `Sequence <s> Cue <c> Part <p>.<r>`. Worked example from the live session: `Seq 102 Cue 1 Part 0.1` addressed the chase recipe line.

**Not a listable named child:** you cannot enumerate recipe lines as if they were their own object class. The parent Part shows the recipe line inline — `List` inside the cue displays the part as **`"1 P 0"`** with cue-part columns, i.e. the recipe line surfaces as columns on the Part row, not as a separate row of its own.

**Readback lane, live-confirmed:** `List Sequence 102 Cue 1 Part 0.1` **WORKS** — the dotted recipe-line address is directly listable this way. This is the CLI readback lane for confirming any `Set`/`Assign` write made against a recipe line (see `recipe-line-set-property-syntax-and-value-casing` and `recipe-line-pool-binding-via-assign` for the write side).

## Multi-part cue addressing: NAME form is the reliable lane — numeric form misresolved with a dialog open [VERIFY] — 2026-07-29

**Numeric `Part N.1` on a multi-part cue returned `Illegal object` / misresolved** (`Part 0` resolved to the wrong part — the P4 JDC part) **while a sequence-edit dialog was open at the desk** (Dave's read: the open editor context ate it — possibly the same desk-collision family as `desk-clear-callout-before-console-write-rule`, not confirmed as the same mechanism).

**The NAME form works context-independently:** `Part "P3 PIX".1` resolves, Assign-creates lines, and reads back correctly — proven **×14 live** (see `assign-cli-recipe-line-grammar` for the create-on-empty-part behavior this addressing was exercised through). `AddrNative()` confirms the console's own native addressing is name-path (`Sequences.cLD SONG_T.Mark.P3 PIX`), not numeric.

**`[VERIFY]`: retest numeric part addressing with all dialogs closed before trusting it.** Until then, **NAME FORM IS THE LANE for any multi-part cue.**

Cross-reference: `store-recall-recipe-toggle-rules` for the EditRecipe bookend that builds standard recipes; `recipe-lane-end-to-end-verified` for the full worked recipe build this addressing grammar supports; `tourshow-fill-layer-rebuild-method` for the SONG_T air-pixel batch this multi-part finding came from.

History: none — first captured and live-confirmed in one session, 2026-07-17. Extended 2026-07-29: added the multi-part cue addressing finding — numeric form misresolved with a sequence-edit dialog open (name form unaffected, proven the reliable lane); [VERIFY] retest with clean desk.


## Gotcha added 2026-08-01 [0801cLD] — dotted recipe-line reads return NIL when the part NAME contains square brackets

**A dotted `ObjectList` recipe-line read returns NIL when the addressed part's NAME contains square brackets** — e.g. `ObjectList Part '[Full/...]'.N` choked and returned nothing rather than erroring. This is a distinct failure from a genuinely-empty read: the bracket characters in the name break the dotted-addressing/parse path itself. **Export-back is the reliable census lane for any bracket-named part** — don't rely on a live dotted-address read for these (see `cue-names-not-round-trip-stable-content-derived-labels` for why bracket-named parts are common in this corpus — they are {LD}'s content-derived aux-cue naming convention).

**[0805-2cLD] EXTENSION — MX ASSIGN LANE (v2.4.2.2):** CLI `Assign MAtricks <n> At Sequence <s> Cue <c> Part <p>.<r>` returns "Illegal object" — it does not address a recipe line. What works: Lua handle assignment `r.MAtricks = ObjectList('MAtricks <n>')[1]`, where `r` is the StandardRecipe pointer from Sequence→Cue→Part→`Ptr(k)`. Verified 30/30 (SONG_Q) + 48/48 (SONG_O) with per-line readback. NB: this plain property assignment rides Tier 1 through the MCP gate (`delete-command-classifier-tier-gap`); batch in sub-1800-char send_lua chunks (`saveshow-discipline-and-mcp-tier`). **Live property surface (probe):** StandardRecipe exposes Values / Preset / Selection / MAtricks / Enabled / SelectionMode. Values renders in RESOLVED SHORT FORM ("Preset 21.2720"), NOT the XML path form — grepping live objects for 'Phaser' returns zero on a fully-bound sequence; match `"Preset 21%."` instead.

History: extended 2026-08-05 [0805-2cLD] — MAtricks assign lane (CLI Assign…At fails; Lua handle assignment verified 78/78) + live property surface and resolved-short-form Values readback.


### recipe-line-playback-properties ⚠ VERIFY
**Recipe-line playback properties per forum doctrine (PlaybackNShot/PlaybackDirection/PlaybackAdaptiveMeasure/PlaybackAdaptiveWidth/PlaybackAdaptiveXYRotation) — but live 2.4.2.2 doc-correction: PlaybackDirection does NOT exist on a sequence cue-part recipe line, it's a PRESET-phaser-only function**
*when:* Before writing or reading a recipe line's playback properties (nShot, direction, adaptive measure/width/rotation) via CLI — PlaybackDirection specifically does not apply to a sequence cue-part recipe line on 2.4.2.2, despite forum documentation listing it there


**Forum-documented playback property set (forum 69919):** `PlaybackNShot`, `PlaybackDirection` (`Forward`|`Backward`|`Alternate`), `PlaybackAdaptiveMeasure`, `PlaybackAdaptiveWidth`, `PlaybackAdaptiveXYRotation` — all listed as recipe-line playback properties, presumably via the same `Set ... Property "PropName" <value>` form as other recipe-line properties.

**Live doc-correction, 2.4.2.2 (Dave):** `PlaybackDirection` does **NOT** exist on a **sequence cue-part recipe line**. Playback direction is a **PRESET-phaser** function instead — it rides the phaser **preset** (e.g. `Preset 21.x`), not the recipe line stored in a cue's part. Forum 69919's "Sequence Cue Playback Area" `Set` block, which implies `PlaybackDirection` is settable at the cue-part recipe-line address, **does not hold** on 2.4.2.2.

**[VERIFY]** which version or context the forum's cue-part `PlaybackDirection` form actually worked on (if ever) — unconfirmed whether this is a version regression, a documentation error, or a context the forum thread never actually tested at the cue-part level.

**Practical implication:** the other four playback properties (`PlaybackNShot`, `PlaybackAdaptiveMeasure`, `PlaybackAdaptiveWidth`, `PlaybackAdaptiveXYRotation`) are NOT independently live-verified by this correction — only `PlaybackDirection` has been specifically disproven at the cue-part recipe-line address. Treat the other four as forum-sourced and unconfirmed until independently tested.

History: created 2026-07-17 from the forum-sourced property list, immediately doc-corrected same session by a live finding that one of the five (`PlaybackDirection`) doesn't apply at the address the forum describes — kept together as one concept since both describe the same "what playback properties can I write on a recipe line" surface, and the correction directly narrows the forum's claim rather than standing apart from it.


### recipe-line-set-property-syntax-and-value-casing
**Recipe-line property writes require the Property keyword — Set Sequence x Cue y Part 0.1 Property "PropName" "Value" — text values are case-sensitive per forum doctrine, but live-verified Enabled specifically only takes Y/N, YES/NO, or 0/1 (not mixed-case Yes/No); MCP doctrine is to emit 0/1**
*when:* Before generating any Set command that writes a property on a recipe line (cue-part address) — the Property keyword is mandatory, and text-value casing has a live-verified exception for Enabled-class props that contradicts the forum-sourced general rule


**The `Property` keyword is mandatory on recipe-line writes:** `Set Sequence <x> Cue <y> Part 0.1 Property "PropName" "Value"` — omitting `Property` is not just a stylistic choice, it's required syntax for this address class (forum 69919; live-confirmed by dherderich with `"Enabled" "No"`, June 2026).

**General text-value casing rule (forum doctrine, ACT KB 34108761 via forum 69919):** text property values are case-sensitive — first letter capitalized. `"Yes"` ≠ `"yes"`.

**Live-verified exception, 2.4.2.2 (doc-correction):** for the **`Enabled`** property specifically, the accepted values are **`Y`/`N`**, **`YES`/`NO`** (uppercase), or **`0`/`1`** — the forum/ACT KB's mixed-case `"Yes"`/`"No"` form **did NOT take** live. This directly contradicts the general capitalization rule above for this one property; treat the general rule as unreliable for `Enabled` until each other enable-class property is independently checked.

**MCP doctrine:** emit **`0`/`1`** for enable-class recipe-line properties — this sidesteps the casing question entirely rather than relying on a value form that's been shown to fail.

Cross-reference: `set-command-unknown-property-fails-silently` for the standing rule that a clean `Set` prompt never proves success — always verify recipe-line writes via `recipe-line-cli-addressing-and-list-readback`'s `List` lane. `recipe-line-pool-binding-via-assign` covers the sibling case (pool-object binds, which use `Assign` instead of `Set Property`).

History: none — captured in one session, 2026-07-17; the Enabled-casing exception is a live doc-correction against the forum/ACT KB general rule, not a separate concept, since both describe the same "how do I write a text/enum value on a recipe-line Set" decision.


### recipe-multiset-clear-anomaly ⚠ VERIFY
**[VERIFY] A multi-pair Set was observed clearing several recipe properties in ONE line (Property "Selection" "" "Values" "" "MAtricks" "" "Filter" "") — collides with the patch one-prop-per-Set hard rule; per-object-class behavior unconfirmed**
*when:* Before assuming Set chaining behavior is uniform across object classes — a recipe-line multi-pair Set was observed clearing 4 properties in one command, which contradicts the patch-fixture one-prop-per-Set hard rule; confirm which class you're targeting before relying on either behavior


**Observed form:** a single `Set` line with multiple `Property "name" value` pairs chained together — `Property "Selection" "" "Values" "" "MAtricks" "" "Filter" ""` — was reported to clear all four recipe-line bind slots (Selection, Values, MAtricks, Filter) in one command (HegauLigh, forum source).

**Collision:** this directly contradicts the hard-verified rule in `patch-set-one-prop-quoted-values` — on **patch fixtures**, chaining multiple property/value pairs onto one `Set` silently drops everything after the first pair. If the recipe-line multi-pair form above is real, `Set` chaining behavior is **not uniform across object classes**: it may work for recipe-line property clears while failing for patch-fixture writes.

**[VERIFY]** — not independently live-tested this session. Open questions:
- Does this multi-pair chaining work for **non-empty** values too, or only for clearing (empty-string) writes?
- Is the difference genuinely per-object-class (recipe line vs. patch fixture), or does it depend on something else (e.g. all-empty-value writes behaving differently from real value writes on either class)?

**Practical stance until resolved:** do not assume multi-pair `Set` chaining works on a recipe line just because this one forum report describes it — verify by readback (`recipe-line-cli-addressing-and-list-readback`'s `List` lane) after any attempt, and default to one-property-per-`Set` (the `patch-set-one-prop-quoted-values` discipline) unless this is specifically retested and confirmed live.

Clears with: a live retest on a recipe line — chain 2+ non-empty property/value pairs in one `Set`, then verify via `List` whether all pairs landed or only the first.

History: none — first captured, 2026-07-17, forum-sourced only; flagged verify immediately due to the direct collision with an existing hard-verified rule for a different object class.


### recipe-output-precedence-and-cooking-doctrine
**Recipe output precedence (official manual flowchart): a hard stored value always beats a recipe; COOKING = materializing a recipe into that hard cookover layer**
*when:* Before reasoning about which value a sequence actually outputs when both a recipe and a hard/cooked value exist for the same attribute — or before deciding whether a generated Sequence export should carry cooked values


**Output decision flowchart (official 2.4 manual, Recipes page):**

1. No stored value for the attribute → the sequence sends NOTHING to it.
2. A stored value exists — is it a link to a preset?
   - **YES (preset-link):** is the value stored directly in the preset? Yes → **PRESET value** wins. No → the **RECIPE in the preset** wins.
   - **NO (local, not a preset-link):** is the value stored in the cue part? Yes → **CUE PART value** wins. No → the **RECIPE in the cue part** wins.

**Governing rule: a hard stored value ALWAYS beats a recipe**, resolved at whichever level holds it (preset-link level or cue-part level). The recipe is the fallback — it only outputs where no harder value overrides it. The manual's Recipes page has deeper per-layer detail beyond this flowchart, not yet dug into further.

**COOKING** = materializing a recipe into hard per-fixture values that ride a "cookover" layer and then WIN over the recipe per the flowchart above (Dave's framing). Confirmed directly by the Seq 102 export: a `Cooked="AbsPreset,RelPreset,...,Phase,GridPos,Measure,NShot"` attribute plus a full `<PresetData>` cooked block rode alongside the live `<StandardRecipe>` in the same Part — see `export-sequence-xml-schema`. The export carried the recipe AND the cooked snapshot together.

**Open item — which carrier actually cooks:** Seq 102 Part 0.1 has its own part-level `PhaseFromX="0°"`/`PhaseToX="270°"` override coexisting with a bound MAtricks `"Phase X 0-180"` (`PhaseToX="180°"`). Both attrs are present in the export without overwriting each other. The export's cooked per-fixture phase spanned to 270° (the part-level value) — SUGGESTIVE that the part-level phase drove the cook over the pool's 180°, but this is NOT pinned. Needs the manual's deeper recipe-layer detail plus a clean visual test to confirm. Raw values: see `export-sequence-xml-schema`'s worked-example notes.

**Relation:** `clean-authoring-and-persistence-doctrine` reframes this flowchart as a design-time GUARDRAIL (deliberate authoring prevents ambiguous overlapping layers from ever existing) rather than a runtime resolution problem. `export-sequence-xml-schema`'s design implication — that cLD MAker's Sequence export must default to recipe-only — is grounded directly in this precedence rule: a cooked value would freeze/pin a stale look on import.

History: created 2026-07-17 from the official manual flowchart (Dave-directed) plus the same-session Export Sequence 102 capture that supplied live confirmation of the cooked-vs-recipe carrier behavior.


### recipe-phase-cli-write-syntax ⚠ VERIFY
**Recipe-line Phase properties via CLI: target PhaseFromX/PhaseToX individually; "Swap Phase" is a working per-property special value; a "*-1" multiplier value syntax works; a "0 t 360" range value landed as 0..180, unexplained**
*when:* Before generating a CLI Set command that writes a recipe line's Phase properties — PhaseFromX/PhaseToX are set individually, Swap Phase and *-1 multiplier syntax both work; do not trust a Thru-style range value on a single Phase property until the 0 t 360 → 0..180 anomaly is explained


**Individual targeting:** `PhaseFromX` and `PhaseToX` are set as separate properties, not a combined pair — target each individually via the standard `Set ... Property "PhaseFromX"/"PhaseToX" <value>` form (see `recipe-line-set-property-syntax-and-value-casing` for the Property-keyword requirement).

**Special value confirmed working:** `"Swap Phase"` works as a per-property special value (Kanarek) — swaps the phase on whichever property it's applied to.

**Multiplier syntax confirmed working:** a `"*-1"` value (multiply-by-negative-one) works as a value expression on a Phase property (Stevegiovanazzi).

**[VERIFY] unexplained range behavior:** setting `"PhaseX" "0 t 360"` (a `Thru`-style range value) landed as **0..180**, not the literal 0-360 requested — cause unexplained. Do not assume a `Thru`-range value on a Phase property behaves as a literal pass-through; it may be getting halved, normalized, or otherwise reinterpreted. Needs a live retest with a known fixture count to characterize.

**Related open question:** `recipe-phase-endpoint-convention` separately flags that stock recipes ship a literal `PhaseFromX=0`/`PhaseToX=360` full-circle pair, in tension with this project's `360 − 360/N` MAtricks formula (`phase-math-formulas`) — that concept's collision question and this concept's `0 t 360 → 0..180` anomaly may or may not share a root cause; both are unresolved and should be tested together if a live phase-recipe session is available.

Clears with: a live test setting `PhaseToX` via a `"0 t 360"`-style range expression against a recipe with a known fixture count, checking the resulting per-fixture phase values.

History: none — first captured, 2026-07-17, forum-sourced with one live-observed anomaly; kept at `verify` for the unexplained range-value behavior.


### recipe-phase-endpoint-convention
**RESOLVED (Dave): a recipe's PhaseToX=360 is NORMALISED — one full lap, endpoints excluded, no first/last collision. 0-360 is the standard setting and the portable one; 360−360/N stays correct for locking a KNOWN rig**
*when:* Before choosing a phase range for any recipe — settles that generic 0-360 is safe on any fixture count, and that the 360−360/N literal is a different lane (MAtricks pool storage on a known rig), not a competing answer


**⭐ RESOLVED 2026-07-27 (Dave, operator knowledge) — the engine NORMALISES it.** A recipe's
`PhaseToX=360` is read as **one full lap with endpoints excluded**; fixture 1 and fixture N do
**NOT** land on the same output phase. **0-360 is the standard setting.** This clears the
question below, which had been promoted to ⛔ BLOCKING under the generic-phase-range doctrine
(`no-baked-n-portable-phaser-doctrine`) — **no desk test is needed and nothing gates phaser
authoring.**

**What this does NOT do:** it does not supersede `360 − 360/N`. That formula stays correct for
**MAtricks pool storage on a known rig**, where phase is a literal manual value the console
does not compute (`mtricks-phase-vs-encoder-phase`). Two surfaces, two computation paths, two
different questions — generic `0-360` for travelling content, the literal formula for locking
a fixed rig. The original tension below was real; the resolution is that both are right in
their own lane.

---

Full-spread recipes in MA's stock phaser-recipe library ship `PhaseFromX=0 PhaseToX=360` — a literal full-circle endpoint pair. This is **different** from this project's existing literal MAtricks full-spread rule, `PhaseTo = 360 − (360 / N)` (see `phase-math-formulas`), which deliberately stops short of 360° to avoid the first and last fixture landing on the same phase.

**[VERIFY]** — not yet live-tested: does a recipe's `PhaseToX=360` actually collide the first and last fixture in the selection (same phase, redundant step), or does the recipe engine auto-correct/normalize a literal 360 the way "one full lap, endpoints excluded" would read rather than a literal degree pair? The two systems (MAtricks pool object vs. phaser-recipe `PhaseFromX`/`PhaseToX`) may not share the same computation path — see `mtricks-phase-vs-encoder-phase` for a precedent of exactly that kind of surface-dependent behavior (MAtricks pool = literal/manual, Encoder Bar = auto-calculated).

Would be resolved by: building a small recipe with a known fixture count N, setting `PhaseToX=360`, and checking live whether fixture 1 and fixture N land on the same output phase.

**Corroborated 2026-07-17:** a second, independent source confirms the same convention — a **console-built** recipe (not just the stock library file) exports with `PhaseFromX="0" PhaseToX="360"` at the XML level (see `recipe-xml-schema`'s display-string phase-value format). Two independent readings now agree on the 0→360 convention itself; the collision-vs-autocorrect question remains untested live and status stays `verify`.

History: created 2026-07-16; status `verify` pending a live collision test. Updated 2026-07-17: corroborated by a second, independent console-built-recipe XML read. **RESOLVED 2026-07-27 [0727-2cLD] — Dave ruled from operator knowledge that 0-360 is the standard setting and is normalised (one lap, endpoints excluded); status verify -> active, and the ⛔ BLOCKING flag it had carried that day is cleared.** The two prior XML readings are now explained rather than merely corroborated.


### recipe-preset-edit-requires-update
**⚠ Editing values inside an existing recipe preset does not persist without Update — reverts silently on clear**
*when:* Before editing a value (e.g. Speed) inside an already-stored recipe preset (such as a preset copied Strobe→Strobe 2) — the edit will not survive a selection clear unless committed via Update


**⚠ Paid-for lesson (cost a repeat build cycle).** Editing a value — speed or any other property — inside an **existing** recipe preset (e.g. a preset copied `Strobe` → `Strobe 2`) does **NOT** take effect by editing alone. The change **reverts on selection clear** unless committed through the **Update** function.

This is a **silent-revert class** issue: the encoders show the changed value while you're editing, so the edit visually looks stored — but it isn't, until Update is explicitly invoked.

Related pattern: compare to `set-command-unknown-property-fails-silently` (a different silent-failure surface — wrong property name, vs. this concept's uncommitted edit) — both share the "clean-looking prompt/display, no actual effect" shape and the same defense: verify by readback / re-open, never trust the encoder display alone.

History: created 2026-07-16 from a live paid-for lesson during the second recipe build session.


### recipe-step-level-cli-write-path
**Step-level recipe writes: Set ... Part 0.1."PhaserRecipeSteps".<step>.<valuesource> Property "PropName" value — after "PhaserRecipeSteps" the path is always .Step.ValueSource**
*when:* Before writing a CLI Set command that targets an individual step/value-source inside a recipe (below the whole-recipe-line level) — the address path segment order below PhaserRecipeSteps


**Worked example:** `Set Sequence <x> Cue <y> Part 0.1."PhaserRecipeSteps".1.1 Property "ValueAbsolute" 100` writes step 1, value-source 1 of the recipe on that part.

**Path rule:** once the address descends past the literal segment `"PhaserRecipeSteps"`, the remaining path is **always `.Step.ValueSource`** — a step index followed by a value-source index, both dot-separated integers (robinhood, forum 69919).

**Structural mirror:** this CLI path shape mirrors the XML nesting decoded in `recipe-xml-schema` — `PhaserRecipe → PhaserRecipeSteps → PhaserRecipeStep → PhaserRecipeValueSource`. The CLI address is effectively walking the same tree: recipe-line → `PhaserRecipeSteps` → step → value-source.

Cross-reference: `recipe-line-cli-addressing-and-list-readback` for the whole-recipe-line address this nests under (`Part <p>.<r>`); `recipe-line-pool-binding-via-assign` for the `Assign Preset` form that targets this same step/value-source address for pool-object binds instead of a literal `Set ... Property` value.

History: none — first captured, 2026-07-17, forum sourcing not yet independently live-verified against the console.


### recipe-xml-schema
**Phaser-recipe preset XML schema — PhaserRecipe/PhaserRecipeSteps/PhaserRecipeValueSource, Has= layer knock-in, embedded dependencies**
*when:* Before reading, generating, or hand-authoring phaser-recipe preset XML (e.g. for a file-side authoring/import lane) — the decoded element/attribute shape


**Element nesting:** a recipe preset is `<Preset><PhaserRecipe attrs><PhaserRecipeSteps><PhaserRecipeStep><PhaserRecipeValueSource .../>` — i.e. `Preset` wraps one `PhaserRecipe`, which wraps `PhaserRecipeSteps`, each containing one or more `PhaserRecipeValueSource` elements.

**`Has="Measure;AdaptiveMeasure;Speed;..."`** — this attribute serializes **which phaser layers are knocked in** (layer activation), as a semicolon-separated list.

**`Individual="Measure;"`** also observed on at least one element — semantics **[VERIFY]**, not yet confirmed against live behavior.

**Embedded dependencies:** shapes and referenced presets travel with the recipe preset via `<DependencyExport><Dependency RelAddrNum="14.14.1.16.x" ...>` — the `RelAddrNum` branch `14.14.1.16.x` addresses the **Shapes pool** (see `shapes-pool-facts`).

**Section headers:** the XML's section-divider entries are bare `<Preset>` elements with **no `PhaserRecipe` child** — a structural tell for skipping non-recipe entries when parsing the file.

Cross-reference: `shapes-pool-facts` for what a `Shape` element itself holds (`Trans`/`Width`/`Accel`/`Decel` + `Attributes`/`Speed`/`Measure`/`Adaptives`, `Lock="UL"` on stock shapes); `measure-layer-math` for what the Measure layer this schema knocks in actually means at runtime; `stock-recipe-presets-empty-as-templates` for the behavioral consequence of a recipe preset with no stored Selection.

**Recipe-line props are ATTRS directly on `<PhaserRecipe>`** (live-confirmed 2026-07-17, file-side authoring session): `Shape=` carries the **full pool path** (e.g. `"ShowData.DataPools.Default.Shapes.Sine"`); `PhaseFromX`/`PhaseToX` are stored as **DISPLAY STRINGS with a degree sign** (e.g. `"180°"`), not raw numbers; `Enabled`/`PlaybackDirection`/`SelectionFromValue` are also plain attrs on the same element.

**Steps reference the shape internally** via a path string, e.g. `"PhaserRecipeSteps.Step 1.Value Source 1"`; the shape itself travels along via `DependencyExport` (see the `RelAddrNum` branch above).

**Two dialects, one `<Preset>` schema — important distinction:** a **baked** phaser preset (values hard-committed, no live recipe parts) encodes `Speed`/`Measure`/`Phase` as **fixed-point integers** (see `phaser-preset-xml-measure-speed-fixed-point-encoding`), while a **recipe** preset (this schema) encodes its phase endpoints as **display strings with degree signs**. Same outer `<Preset>` container, divergent inner value encoding depending on whether the preset is baked or recipe-based — don't assume one encoding scheme reading the other dialect's file.

Cross-reference: `export-sequence-xml-schema` for how a recipe cue-part (a different element, `<StandardRecipe>`, not this concept's `<PhaserRecipe>` preset-template) serializes its own bind-slot refs inside a live Sequence export — same dotted full-path ref convention, confirmed live 2026-07-17.

History: created 2026-07-16 from the file-side XML read that decoded the recipe schema in one pass. Extended 2026-07-17: added the attribute-vs-element clarification (recipe-line props are `<PhaserRecipe>` attrs), the display-string phase-value format, the step-to-shape reference path format, and the baked-vs-recipe two-dialect distinction — all from a live file-side authoring proof (`xml-file-side-authoring-import-lane-proven`). Same day: cross-referenced `export-sequence-xml-schema` (the sibling StandardRecipe cue-part dialect cracked via a live Sequence export).


### reference-scan-blind-spots-guid-and-baked-content
**⛔ A reference scan needs NAME + SLOT + GUID forms — and even a complete one is blind to BAKED CONTENT: objects that CARRY a value rather than REFER to one stay the operator's domain**
*when:* Before concluding from a scan that nothing references a pool object — check all three reference forms, then ask separately what merely CONTAINS its content, which no reference scan can see


## Layer one: three reference forms

A scan that matches only literal `Preset 4.x` text is **pattern-blind**. References appear as:

- **name paths** — with the pool's *live* name, which drifts (`import-resolver-laws`);
- **slot forms** — numeric, immune to renames;
- **GUID forms** — how golden exports survive stale pool names.

**A scan must cover all three** before "zero references" means anything.

**Attested:** the original colour-in-phaser grep matched only the name-path form. A GUID cross-reference was then run and returned **still zero** — the phasers genuinely never bound the colour pool by reference. The conclusion happened to survive; the method did not, and was corrected in the log the same session.

## Layer two: the blind spot no scan closes

**Objects that CARRY content rather than REFER to it are invisible to every reference scan.** Colour-phasers were the case in point: their **baked step content** owed the consolidation, and no name/slot/GUID sweep could have seen it, because there was no reference to find. The delete never broke them *mechanically* — what Dave saw was a look, not a link.

**Working heuristic:** anything **named for what it carries** (a "deep blue" phaser, a "cool white" figure) is a candidate for baked content and belongs on the operator's list, not the scanner's. Instruments confirm; eyes find (`operators-eyes-are-the-census-of-record`).

## What a complete verification looked like afterwards

Four checks, all passing: fresh pool export with **zero dead colour-name refs** · **zero valueless phasers** (empty pool hits were dividers/organisers, not damage) · a full recipe scan resolving **233 distinct phaser slots, zero dangling** · an old-vs-new diff accounting for every change as deliberate work. Plus a repeatable script left on disk (`phaser_recheck.py`: GUID cross-ref + health + diff) so the check is re-runnable rather than re-derived.

**Relation:** `operators-eyes-are-the-census-of-record` · `color-consolidation-crowning` · `import-resolver-laws` · `preset-references-are-object-bound-rename-and-move-safe` · `export-plus-python-bulk-lane` · `empty-census-deserves-selector-suspicion`.

History: none — the scan's blindness was found, admitted and closed inside one session, 2026-08-19.


### review-plan-gate-precedes-programming-doctrine
**A REVIEW→PLAN step must precede programming any song — never bake cue-to-cue; skipping the gate is what let this session tunnel into baked cues despite recipe-based doctrine already being loaded**
*when:* Before starting ANY programming session on a new song — run the review→plan gate first (doctrine + spine inventory + cue-sheet-as-instructions read → phaser/recipe story + per-cue plan → one build-macro) rather than going straight to console/XML authoring


**The lesson, paid for hard:** {TOUR} is recipe-based (see `tourshow-recipe-based-show-style-ruling`) — cues hold recipes that cook live (Group=WHO / preset+phaser=WHAT / grid=WHEN), never baked cue-to-cue values. This session built the whole SONG_G chain end-to-end via the proven macro-import lane, but programmed it WRONG: 9 cues of hard SET→OUT values, nothing recipe-referenced, the cell/grid spine unused, and the cue sheet's gesture tags (Bloom/Propagation/Color pump/Sustain drift/Isolate/Phrase turn) flattened to one static color + one global dim sine instead of being read as phaser/recipe instructions. `recipe-lane-end-to-end-verified` and `v24-phaser-model` were both LOADED this session and still didn't get applied — the tell that doctrine being *known* is not sufficient; it has to be turned into a plan BEFORE console/XML time.

**Failure mode, named:** a single hard blocker (the `ColorAdd`→silent-empty-preset color-syntax trap, see `baked-phaser-preset-xml-schema`) tunneled the session into "just make it import" mode, and the recovery back to doctrine never happened. One blocker early in a build session can hijack the whole session's mode if nothing forces a checkpoint back to the plan.

**The fix — a mandatory REVIEW→PLAN gate before any programming session touches console or XML:**
1. **Load doctrine:** the recipe-based-mode ruling (`tourshow-recipe-based-show-style-ruling`), `phaser-story-doctrine` ("write the phaser story before console time"), `tourshow-gesture-groups-on-demand-doctrine`, `tourshow-functional-vs-flavor-fixture-taxonomy`, `grid-is-a-time-map-doctrine`.
2. **Inventory the spine:** what the rig/group/recipe spine can actually DO for this song, concretely — not just that it exists.
3. **Read the cue sheet's device/gesture tags AS PHASER/RECIPE INSTRUCTIONS**, not flavor text — each tag (Bloom, Propagation, Color pump, Sustain drift, Isolate, Phrase turn, etc.) implies a specific phaser/recipe shape.
4. **Write the phaser/recipe STORY + a per-cue plan** (WHO/WHAT/HOW/level, expressed as recipes, not hard values) — the deliverable of the planning pass.
5. **Only then** does one build-macro author it all onto console. Console time = translation, never invention — extends `phaser-story-doctrine`'s console-is-translation framing from the per-song phaser story up to the whole-session process level.

**Planning heuristic (Dave, dictated, paraphrased):** plan for the **hardest** moment in the song first — the best/easiest moments "shine like diamonds" on their own and don't need the planning budget spent on them.

**Status note:** candidate doctrine — proposed as a standing gate on the strength of this one paid-for failure; not yet tested on a second song's build. Cross-reference `tourshow-programming-ramp-plan` for the separate "what order to build songs in" sequencing plan this gate slots into per-song.

History: none — doctrine named and the failure mode diagnosed 2026-07-21, digesting the SONG_G first-pass build flagged for a recipe-based redo; see `wraps/2026-07-21-days-first-pass-recipe-miss.md`.


### shapes-pool-facts
**Shapes pool (v2.4) — angular-bracket link semantics, locked stock shapes, and the shape-speed-override pattern**
*when:* Before editing any phaser-recipe value shown in angle brackets (shape-derived), before assuming a stock Shape is editable, or before overriding a shape-linked property (e.g. Speed) on a recipe line


**Angular brackets = external-object link (webinar):** a recipe-line value shown in angle brackets (e.g. `<600 BPM>`) is derived from an external **Shape** object, not typed locally. Overwriting it breaks the link and the brackets disappear — the value becomes a local literal.

**Shapes carry Speed, and other layers (Dave; corroborated by the XML schema):** a Shape can bake **Speed** — and Measure/Adaptives — into the phaser it feeds. A shape is functionally the most basic base phaser; the old-school pattern of building basic-shape presets up into full phaser presets is what v2.4 formalized as the Shapes pool. Shapes are the programming shortcut inside phaser recipes. Corroborated by the recipe XML schema (see `recipe-xml-schema`): a `Shape` element holds `Trans` / `Width` / `Accel` / `Decel` plus `Attributes` / `Speed` / `Measure` / `Adaptives`.

**Stock shapes are locked:** the 22 preinstalled shapes are **NOT editable** — copy first, edit the copy. Matches the `Lock="UL"` attribute observed on `Shape` elements in the stock XML.

**Shape speed-override pattern (live-verified):** a shape link brings Speed into the recipe line bracketed (e.g. `<600 BPM>` from a Strobe shape). Typing directly into the Speed encoder's calculator breaks **only that property's** link — other shape-linked properties (curve, width, etc.) stay linked. This is the core move for putting a shape-driven effect at song tempo without losing the rest of the shape's profile. Calculator popups for shape-linked properties carry **Take from Shape / None / Invert** side buttons — a relink lane exists to restore the link later.

Cross-reference: `v24-phaser-model` for the Shapes-pool intro (22 predefined, `At Shape <n>` syntax); `recipe-xml-schema` for the full Shape XML element; `speed-distribution-bpm-hz-decimal-trap` for the separate BPM/Hz decimal-conversion gotcha when typing Speed values directly (a different mechanism from this link-breaking behavior).

History: created 2026-07-16, merging four related findings (angular-bracket semantics, shapes-carry-speed, stock-shapes-locked, shape-speed-override pattern) into one atomic Shapes-pool concept.


### source-figures-are-recipe-presets-spread-read-law
**{LD}'s figures are RECIPE PRESETS — read the embedded StandardRecipe lines first; cooked per-fixture rows are residue and miscall spreads**
*when:* Before reading any {LD} figure's spread/MAtricks intent from a {FESTIVAL} export, and any time a spread call is about to be made from cooked per-fixture Phaser@Phase rows.

{LD}'s figures are RECIPE PRESETS: each figure carries its own internal
StandardRecipe lines (Selection + XWings/XShuffle/XBlock/XGroup/YShuffle +
PhaseFrom/To per population) inside the preset export. That is {LD} doing at
the PRESET layer what cLD's build does at the CUE layer. The cooked per-fixture
Phaser@Phase rows are the RESIDUE those recipes leave.

**METHOD LAW: read `pre.iter('StandardRecipe')` FIRST; cooked rows are fallback
only.** Reading residue instead of recipe lines produced three wrong spread calls
on SONG_Q: wash "unison" was actually W2 G4 X-360 · RIVALE "unison" actually
W2 X-90 · PLATES half-rev bound shuffled S5-X-180 where the recipe says winged
W2 X-180.

The embeds are trustworthy: Dave's from-memory corrections matched the embedded
recipes EXACTLY (W2 S5 X-360 for Swell/Bridge · W2/W6 Breakdown · S5 fills ·
W2 X-90 pline).

{LD}'s MX vocabulary across gb_s2500 + gb_s2700: XWings 2 (once 6) · XShuffle
always 5 · XBlock 7 (linear JDC runs) · XGroup 4 (once) · Y only ever YShuffle=5
paired with XShuffle=5 (XY sparkle) · phase literals ride with the knobs
(0→±360, 90→0, 90→−180). Never YWings/YBlock/YGroup.

Full form of the read-order law previewed in
`matricks-store-time-embed-travels-with-preset-export` (grep-the-literals was the
partial method; iterating the StandardRecipe lines is the whole one). Flat-literal
phase scoping: `phase-math-formulas`.

History: none — minted 2026-08-05 [0805-2cLD]; recipe-first read law + MX vocabulary from {FESTIVAL} export probes, three SONG_Q residue miscalls corrected against Dave's memory.


### source-matricks-wrapper-recipe-encoding
**{LD} binds NO MAtricks pool objects, ever — spread lives on per-population wrapper StandardRecipes inside each phaser's DependencyExport; match wrappers by CROSSWALKED TARGET, never raw name**
*when:* Before reading {LD}'s spatial/MAtricks spread off any phaser preset, or before crosswalking a wrapper group name to a cLD group for MX purposes — his MX never lives on a bound MAtricks pool object, and matching wrappers by raw name silently drops sites


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


### source-spread-is-one-full-wave
**{LD}'s 6 SONG_T phasers all bake the SAME spatial figure — one full wave, endpoint-exclusive (360×(N-1)/N) — except the Prechorus build, which is deliberate phase-0 unison**
*when:* Before reading or replacing any of {LD}'s SONG_T phasers' spatial spread — all six use one convention, already matched by our own stock MAtricks, so the spatial layer needs no new authoring


**All six of {LD}'s SONG_T phasers bake exactly ONE spatial figure: one full wave, endpoint-exclusive** — `PhaseToX = 360 × (N-1)/N` for a group of N fixtures, the standard "don't collide the last fixture with the first" convention (`recipe-phase-endpoint-convention`) applied consistently:

- **Spots (14 fixtures):** `360 × 13/14`, step **25.714°**.
- **Cells (162 fixtures):** `360 × 161/162`, step **3.158°**.

**Exception: the Prechorus build phaser is phase-0 UNISON by design** — every fixture at the same phase, not spread. (Consistent with `cue-structure-is-tonal-harmony`: the Prechorus is the pre-dominant/build, and unison reads as "everyone rising together," distinct from the spread figure used elsewhere.)

**Consequence — nothing new needs authoring for the spatial layer.** The whole spread story is already served by **Dave's existing `MAtricks 101 'cLD Full Spread'`** (0→324°, i.e. `360 × 9/10` — the exact same endpoint-exclusive convention, computed for a different N). It is bound at **10 of the phaser recipe lines**; the **BUILD** phaser stays bare (no MAtricks), matching the unison reading above.

**Relation:** this is the spatial half of the phaser-figure/MAtricks split in `tourshow-authoring-contract-v01`; `source-timing-is-the-tempo-grid` is the temporal half of the same six-phaser decode. `no-baked-n-portable-phaser-doctrine` is the standing doctrine this figure confirms — {LD}'s own file uses the generic endpoint-exclusive convention rather than a hand-tuned literal, on top of the one case (`Intro 1/1 Spot Dim`) already on file as the baked-N failure exemplar.

History: none — decoded in one pass, 2026-07-28, from the Sequence 1500 (SONG_T) export.


### speed-distribution-bpm-hz-decimal-trap
**Speed distribution values need decimal adjustment converting BPM to Hz**
*when:* Before setting speed/rate distribution values in MAtricks or a phaser — check whether the value is being entered as BPM or Hz


Speed distribution values in MA3 need **decimal adjustment** when converting between BPM and Hz representations — the two units are not interchangeable 1:1 and a naive pass-through will be wrong by a scaling factor. Treat any speed value as unit-tagged (BPM vs Hz) and convert explicitly before entry.

History: none — stable note since 2026-04-01. No conversion constant/formula was recorded in the corpus; flagged for future verification if the exact factor is needed.


### speedmaster-name-token-exact-match-gotcha
**Sequence SpeedMaster value token is the master's exact object NAME — 'Speed1' (no space) works, 'Speed 1' (with a space) is a silent no-op with a clean OK echo**
*when:* Before setting a Sequence's SpeedMaster property via CLI or MCP — the value must exactly match the speed master's object NAME string, and a plausible-looking variant with a space silently does nothing


**Finding (card-candidates):** a Sequence's `SpeedMaster` value token IS **the master's exact OBJECT NAME** — `'Speed1'`, **NO SPACE** (this is literally Master 3.1's name). `'Speed 1'` **with a space is a SILENT NO-OP** — clean `OK` echo, no error, and the property does not actually change. Readback caught it, **twice**.

**Speed masters census:** Master 3.1-3.16 are named `Speed1`..`Speed16`. Master pool layout: 1=Selected · 2=Grand · 3=Speed · 4=Playback · 5=Timing.

**Proven working command:** `Set Sequence <n> Property 'SpeedMaster' 'Speed1'` — single-quoted, over MCP, works.

**Transport trick banked:** `string.char(34)` builds real double-quotes inside a `send_lua` payload when a value needs them — legal, produces no raw quote in transport (the raw-quote transport ban stays intact).

**Relation:** `saveshow-discipline-and-mcp-tier` (existing concept, not staged this run — the sibling single-quote-inside-long-bracket transport trick for `SaveShow`, same transport-safety family). `tourshow-seq1110-song-b-build-record` (the x17-sequence fleet fix this gotcha was caught during).


### stock-measures-grammar-census
**MA's stock phaser-recipe library measures grammar — per-category Measure/Direction/Adaptive census**
*when:* Before designing a new recipe in a given effect category (wipe, flyout, oneshot, alternate, chase, movement) — MA's own stock library's Measure/Direction/Adaptive choices per category, as a design-pattern reference


Design-language census read from MA's own stock recipe library (matches Dave's measure framing captured elsewhere as measure doctrine):

| Category | Grammar |
|---|---|
| Wipes | `Measure=1` — live in one beat |
| Flyout specials | `Measure=4` + `Speed` |
| OneShots | `NShot=1` + `Measure=1` |
| Alternates | `Measure=1` + `Direction=Alternate` + `Phase 0→180` (HALF spread — bounce doubles the traversal) |
| Chase / Snap | `AdaptiveMeasure` (chases add `AdaptiveWidth` too) — grid-synced |
| Movement | `Has=Speed` + **RELATIVE** pan/tilt (rides the base position — portable across positions) |

**Attribute census across the library:** Dim 62, Tilt 34, Pan 34, Zoom 2; 70 relative-value cells total.

Cross-reference: `measure-layer-math` for the Measure definition/formula this table applies; `wipe-in-thru-range-anatomy` for the worked wipe example behind the "Wipes: Measure=1" row; `v24-phaser-model` for the nShot/Direction/Adaptive control definitions this table's columns use.

History: created 2026-07-16 from the same XML read that produced `recipe-xml-schema`.


### stock-phaser-recipe-library-import
**Importing MA's stock phaser-recipe template library — Show Creator route + forum-flagged pool-in-sequence caveat**
*when:* Before importing MA's stock phaser-recipe presets into a show, or before referencing an imported recipe preset directly from inside a pooled sequence


**Import route (Dave):** Setup → Show Creator → Import presets → the **"All 2"** pool imports MA's phaser-recipe preset library. These land as templates/base recipes — inspect via the recipe editor or via preset XML export.

**Source file (community-confirmed):** Show Creator → presets → **`predefined_phaser_recipes`** is MA's stock phaser-recipe preset library file.

**Known caveat [forum 69977]:** pool phaser-recipe presets referenced directly from inside sequences have been reported to misbehave. MA's own best-practice workaround is preset → standard recipe in the cue (the fully-referenced workflow — see `v24-phaser-model`). Test before relying on a direct pool reference inside a sequence.

**Possible connection (unconfirmed, flagged not asserted):** this forum-reported misbehavior may be the same underlying phenomenon later diagnosed live as `stock-recipe-presets-empty-as-templates` — bare pool/preset calls on a fresh stock recipe template are silent no-ops, and the fix (a recipe line with Selection+Values) matches MA's preset→standard-recipe workaround exactly. Not confirmed as the same root cause; noted as a likely match.

History: created 2026-07-16, merging Dave's practical import-route description with the community/forum-sourced exact filename and caveat — two facets of one import fact.


### stock-recipe-presets-empty-as-templates
**⛔ Stock phaser-recipe presets are EMPTY as presets — bare call or pool tap is a silent no-op; they only cook through a recipe line**
*when:* Before calling a stock (or any freshly-imported) phaser-recipe preset directly via CLI or a pool tap — it will silently do nothing. Also load when diagnosing why a preset call produced no output with no error on the docked command line.


**⛔-class lesson.** Stock phaser-recipe presets are **empty as presets**. A bare call — CLI `Preset "All 2"."Chase"` with a selection, or a pool tap — produces a **silent no-op**, or an echoed **"Preset 'Chase' is empty"**. These presets are **selection-less recipe TEMPLATES**: they cook only through the recipe lane — a recipe line with `Selection` = a Group/capture and `Values` = the preset, placed in a cue part or the programmer's Part Zero — per MA's fully-referenced workflow (see `v24-phaser-model`). A bare preset call tries to apply stored VALUES that simply don't exist on a fresh-imported recipe preset.

**Diagnostic lane that found it:** the target selection was verified visually first (Group 121's yellow outlines showing correctly on the SPOT PLOT layout, Display 2) — so selection wasn't the problem. A **pool TAP** then produced the definitive echo (**"Preset is empty"**) where the equivalent **CLI call had stayed silent**. Lesson: a pool tap echoes errors that a CLI call swallows — when a CLI preset call produces no visible effect and no error, cross-check it with a pool tap before assuming the selection or preset itself is at fault.

**The fix:** see `recipe-lane-end-to-end-verified` for the live-verified recipe-line lane that cooks these templates correctly.

History: created 2026-07-16 — first documented as a live diagnostic during the second recipe build session.


### store-recall-recipe-toggle-rules
**EditRecipe toggle, /MAtricks store flag, and Store-time label inference**
*when:* Before scripting a Store sequence for a preset/cue, or before toggling EditRecipe Programmer — also see v24-phaser-model for the v2.4-specific phaser exception


Three related Store/recall rules from the original v2.3 rule set:

- **`EditRecipe Programmer` is a toggle** (on/off) — it must be explicitly turned on before storing and off after. Pattern: "Recipe mode bookend" — `EditRecipe Programmer` ON before store, OFF after.
- **`Store` with the `/MAtricks` flag embeds spatial settings** in the preset/cue.
- **Label is inferred on Store** — no `Label` keyword needed; just wrap the name in quotes and the console infers it's the label.

**v2.4 scope added (2026-07-04):** the EditRecipe bookend pattern above applies to **STANDARD recipes only**. In v2.4, `EditRecipe Programmer` **cannot build phaser recipes** (2+ step recipes) — see `v24-phaser-model` for the full phaser-vs-standard-recipe distinction and why PSR additionally breaks phaser recipe shape links.

**Live-verified 2026-07-15 (first full recipe build, 2.4.2.2):** the EditRecipe bookend pattern was exercised end-to-end for real — `EditRecipe Programmer` ON, `Store Sequence 101 Cue 1 Part 1`/`Part 2` with Group + universal-preset references, `EditRecipe Programmer` OFF — and it cooked correctly to DMX on `Go+`. Notably, firing **`ClearAll` INSIDE the recipe-edit mode did NOT break the bookend** — the toggle-off afterward stayed clean and the stored recipe was unaffected. See `recipe-lane-end-to-end-verified` for the full worked build (Show Creator menu, universal preset creation, DMX-cook verification).

History: the "Recipe mode bookend" pattern was scoped 2026-07-04 to standard recipes only, after discovering in the v2.4 UI first-contact session that EditRecipe cannot construct multi-step phaser recipes at all. Live-verified end-to-end 2026-07-15 on a real Sequence/Cue/Part build, including confirming ClearAll-inside-mode survives without breaking the bookend.


### stripped-group-membership-recipe-uncooked-diagnosis
**A recipe that reads broken/uncooked may have an intact recipe and a STRIPPED group instead — check group membership (fixtures removed, objects/labels kept) before assuming the recipe itself is corrupt**
*when:* When a recipe-based look reads broken, uncooked, or 'not doing anything' on an inherited/handed-off showfile — check the Selection group's actual membership before assuming the recipe, preset, or phaser is at fault


**Root cause diagnosed live ({FESTIVAL} AR file, 2026-07-22):** recipes that looked broken/uncooked on inheritance turned out to have their **GROUP MEMBERSHIPS stripped** — the Group *objects* and *labels* were intact, but the fixtures inside them had been removed. A recipe whose Selection bind slot points at such a group has **no WHO to cook onto**, so it reads as uncooked/non-functional even though the recipe itself (preset + phaser + grid) is fine.

**Fix, proven live:** re-add the fixtures to the stripped group → the recipe cooks normally. Confirmed on the prior showfile version too, which points to a **deliberate hand-off strip** (likely IP-protection practice when passing a file to another programmer/production) rather than transit/import damage.

**Scope refinement (same session):** the stripped groups specifically hit the **look/phaser library** (recipe-based, group-bound content) — NOT the song cue stacks, which use a different construction method entirely (see `festival-main-cue-baked-vs-recipe-status`).

**Diagnostic takeaway, generalized:** when inheriting or reviewing someone else's recipe-based showfile and a look reads dead, **check group membership first** (`Export Group <n>` → XML census, see `group-xml-export-selectiondata-census`) before concluding the recipe/preset/phaser chain is broken — an empty-but-labeled group is a distinct failure mode from a genuinely corrupt recipe, and the fix (re-populate the group) is trivial once diagnosed. Distinct from the deliberate design pattern in `tourshow-functional-vs-flavor-fixture-taxonomy` (an intentionally-empty flavor group as graceful degrade) — this is an *inherited* file showing *accidental-looking* (but likely deliberate, hand-off-side) empty groups, not a design choice made by the current programmer.

History: none — diagnosed and fixed live in one session, 2026-07-22, on {LD}'s {FESTIVAL} AR showfile.


### tourshow-authoring-contract-v01
**{TOUR} authoring contract v0.1 — their STRUCTURE, our content: phaser preset = the temporal figure, group = who, MAtricks bound at the SEQUENCE = spatial; one phaser copy per FIGURE (reversed 07-30; was per use-site); cLD-prefixed; ours at 21.<century>20**
*when:* Before authoring ANY {TOUR} cue content — this is the closed contract for what each object is responsible for, where ours are numbered, and what gets copied vs referenced


**Keep {LD}'s song STRUCTURE. Replace every layer of content.** The cue list shape is
already blocked out and correct; everything inside it becomes ours.

## Responsibility split — four objects, bound at the cue-part recipe line

| Object | Carries | Notes |
|---|---|---|
| **Phaser preset** | the **temporal figure** | a phaser RECIPE (not baked) referencing a **stock Shape** + a **Universal Dimmer preset**. Direction is baked HERE — `PlaybackDirection` does not exist at the cue-part line (`recipe-line-playback-properties`), so the set needs forward AND Alternate variants. |
| **Group** | **who** | ours, per `tourshow-group-contract-v01` |
| **MAtricks** | the **spatial distribution** | **the SEQUENCE references it**, not the phaser. Drawn from a reusable set, overridable case-by-case. |
| **Colour / intensity** | ours | custom colours from video-clip RGB; **universal intensities**, `/Universal` on every store |

Bind lane is proven: `Assign <obj> At Sequence x Cue y Part z`, bare form, routing
**Group→Selection · Preset→Values · MAtricks→MAtricks** (`assign-cli-recipe-line-grammar`).

## The reusable MAtricks set — SOLVED, not to be authored

**Dave's 30 Coachella Spectra Tower MAtricks, imported at pool 111-140.** They bind by `Assign`
alone and are **proven portable across several shows and fixture-group sizes with no phase
adjustment** — see `no-baked-n-portable-phaser-doctrine`, where they are the reference
implementation. Simple phase / wing / group / block variants cover the normal case.

## Phasers — their phaser is a CHECKLIST, not a thing to port

Read {LD}'s per-cue phaser only as the question *"does this cue want a phaser?"* If yes,
author a NEW template phaser and reference ours. **Never reference theirs** — their phasers are
`PresetMode="Global"` but hold per-fixture `Selective` rows with baked phase, so swapping the
group on a recipe line does NOT re-point them.

- **Numbering: ours at `21.<century>20`.** SONG_T → `21.1520` (theirs occupy 1500-1507).
  Generalises across the setlist, since the phaser pool mirrors the sequence century.
- **⚠ ONE PRESET PER USE-SITE — deliberately anti-DRY.** Need the same figure elsewhere? **Copy
  it and reference the copy.** Rationale (Dave): organisation plus local editability — each
  instance stays individually tunable through its own sequence recipe. **Do NOT "optimise" this
  later by consolidating near-identical phasers.** It trades global reuse for the ability to
  tune one moment without touching the others, which is the right trade on a live show.
- **Build a TEMPLATE SET first and copy from it** — DRY at authoring, copies at use.

## Naming — `cLD ` prefix on every cLD-authored preset

Standing law (`cld-sandbox-and-namespace`). Dodges MA3's silent `#2` duplicate-suffix, and
makes provenance readable in a file whose names have lied twice.

## What survives of the decode work

We do NOT port their phasers, so the Selective/baked-N problem never arrives. But a selective
phaser still reads out its **musical spec** — `Intro 1/1 Spot Dim` decodes via the 2^24 fixed
point to 0.2896 Hz = 139/8 = an **8-beat (2-bar) cycle**. **Use the decode as a spec-read for
starting values, not as a port.**

## Status

**CLOSED, 2026-07-28 — every object in the contract is built.** Groups ✓ · colours ✓ (video RGB)
· intensities ✓ (Universal) · MAtricks ✓ (Coachella 30) · positions ✓ (tilt ladder
`festival-position-preset-stacking-and-tilt-ladder` + pan set `2.81-83` Fan/X1/X2) ·
**phaser template set ✓ — 27 templates landed (v.27), the last remaining item, closed
2026-07-28.** See `tourshow-seq1510-build-record` for the build that exercised the completed
contract end to end.


## ⛔ REVERSED 2026-07-30 (Dave) — copy granularity is PER FIGURE, not per use-site

The "ONE PRESET PER USE-SITE — deliberately anti-DRY" rule above is **superseded**. Dave's ruling on the SONG_A build: **one phaser copy per FIGURE**, reused across that figure's use-sites within the song. SONG_A landed **11 copies across 19 use-sites** (`21.1020-1030`).

The old rule's rationale — local editability, tune one moment without touching the others — is preserved as **copy-on-demand**: if a single use-site later needs its own tuning, fork *that* copy at that moment. What is dropped is pre-emptively authoring the cross-product up front.

This also aligns the contract with `compose-at-bind-time-principle`: authoring N copies of one figure before knowing any of them will diverge is pre-multiplying.

Old text kept above for the reasoning, which still stands for the fork case.

## ⭐⭐ FURTHER LOOSENED 2026-08-05 [0805cLD] — a phaser preset is an INGREDIENT; hash count is not object count

**RULED (Dave):** a phaser preset is an **INGREDIENT** — reusable, and usable by MULTIPLE
CUES AT THE SAME TIME. *"We can use the same bump all the way through the show if we
wanted."* **The figure-hash count is NOT the object count — do not mint one object per
content hash.** This loosens the copy-granularity rule further than the 2026-07-30 reversal
above already did: **per-figure was the ceiling, not the floor.** SONG_L ships **5**
objects (`cLD SONG_L PAN SINE` / `SINE` / `BUMP` / `RAMP DOWN` / `COLOR LINEAR`) against **9**
distinct content hashes — full build record: `tourshow-seq2210-song-l-build-record`.

**Companion misread, corrected same session:** the FIGURES sheet's status string
"REUSE-CONTENT — MINT a per-song copy FROM this source (do NOT cross-song bind)" was misread
as "one object per content hash," producing a false 9-object blocker on SONG_L. **The
sheet's REUSE/NEW axis describes where CONTENT came from, not how many OBJECTS to mint** — do
not conflate the two questions.

**Also ruled the same session — composites are SEPARATED, not decomposed:** when one {LD}
preset mixes fixture types/shapes, the parts-per-century explosion already splits by fixture
family, so the composite becomes one part per century with its own bind, never a puzzle to
decompose by hand. Full doctrine and the population→shape join method:
`parts-per-century-emit-pattern-and-et-gate`.

History: extended 2026-07-28 [0728cLD] — Status section updated to CLOSED: the phaser [0728cLD] — Status section updated to CLOSED: the phaser
template set (27 templates, `21.53-73`+`81-86`) and the pan preset set (`2.81-83`) both
landed, completing every object named in the contract.


History: none — ruled by Dave across 2026-07-27/28 [0727-2cLD]. 2026-07-31 [0731cLD] — copy-granularity rule reversed per Dave's 2026-07-30 ruling (per-figure, fork on demand); title updated to match.


### tourshow-phaser-figure-duplication-across-songs
**{LD}'s silent #N duplicate phaser names can be content-identical twins WITHIN a song — and nobody has yet content-hashed his 106 figure uses ACROSS songs to check for the same thing**
*when:* Before minting a new cLD phaser-pool copy for a {LD} figure — check whether an existing copy already serves it; a #N name suffix does not prove a distinct figure, and cross-song reuse is a real open risk, not yet checked


**{LD}'s SONG_G pool carries silent-#N duplicate phaser names** (`'Chorus 1/1 Dim#5'` / `'#7'`) that turned out to be **CONTENT-IDENTICAL twins** — one cLD copy served both use-sites (`21.1722`, 2 use-sites). **The `#N` suffix does not imply a distinct figure** — check for twin-`#N` pairs before minting a per-figure copy for each name. This does not conflict with the "one phaser copy per FIGURE, not per use-site" doctrine (`tourshow-authoring-contract-v01`) — it sharpens how to identify a truly distinct FIGURE when {LD}'s own naming is ambiguous.

**⭐ Highest-value unrun check, surfaced by the whole-show pass:** cross-song phaser figure dedup. **106 figure uses show-wide.** A same-song twin has already been proven — SONG_J's Verse 1/1 Dim#8 = Chorus 1/1 Dim#11 (same content hash) — establishing that twins exist WITHIN a song. **Nobody has yet hashed figures ACROSS songs.** If {LD} reused figures between songs, duplicate pool-21 copies are being minted for every one of them without anyone noticing. **Content-hash all 106 figure uses before any more copies get minted** — this is flagged as an open, unrun check, not yet actioned as of this backlog.

**Relation:** `tourshow-authoring-contract-v01` (the one-copy-per-FIGURE doctrine this concept sharpens the identification method for). `tourshow-recipe-line-redundancy-taxonomy` (the sibling redundancy class at the recipe-LINE level rather than the pool-object/figure level).


## ⭐ ANSWERED 2026-08-03 [0803-2cLD] — RAN THE CHECK: 47 DISTINCT FIGURES, 31 ALREADY MINTED, 16 GENUINELY NEW

This concept's flagged, UNRUN cross-song figure-hash check was run this session. Method, result, and validation:

**Granularity ruling — what to hash and what to exclude, and why.** Hash the ordered `<Step>` tuples (`Function`, `Absolute`, `Trans`, `Width`, `Accel`, `Decel`), the driven `Attribute`(s), and `Measure`. **Exclude Phase/GridPos** — spatial, ours lives in a bound MAtricks pool object, not the figure. **Exclude Speed/SpeedMaster** — ours ships UNBAKED and rides cue-part Speed Scale (`tourshow-speed-architecture-standing-ruling`), so two figures with the same shape at different speeds are the same copy at a different gear, not different figures. **Consequence: a content-hash match is a REUSE CANDIDATE whose gear is still set per site at previz — not a claim that two sites read identically on stage.**

**Result, across the 7 remaining songs:** 47 distinct figures, of which 31 are content already minted for a built song — only **16 are genuinely new**. Per song (names / distinct / already-minted / new): SONG_K 8/6/5/**1**, SONG_L 10/9/4/**5**, SONG_M 12/10/5/**5**, SONG_N 6/3/3/**0**, SONG_O 8/7/5/**2**, SONG_P 6/5/4/**1**, SONG_Q 10/7/5/**2**. **SONG_N needs zero new figures** — its 6 names collapse to 3 contents, all three already resident. Phaser-copy workload for the run is 16, not 47 (a 65% cut).

**Show-wide (17 songs, including already-built):** 166 figure name-instances resolve to 57 distinct contents — 8 same-name reuse (not a discovery), 10 different-names/identical-content (the actual finding — widest span 12 songs under 8+ names), 39 single-song. See `inherited-file-membership-is-ground-truth`'s fourth-object-class amendment for this half of the result.

**Validated, not just reported (and a real find came out of validating):** the hash reproduces the known SONG_J twin (`Verse 1/1 Dim#8` = `Chorus 1/1 Dim#11`) exactly; SONG_J's 20 names still separate into 17 distinct hashes (the hash discriminates, it does not over-collapse); a **third** SONG_J twin surfaced — `Transition 1/2 Dim` matches the proven pair's content, but `FIGURE_MAP` mints it separately at `21.2027` while the pair shares `21.2022`, i.e. one redundant pool-21 copy already on the console.

**Two independent derivations agreed:** this content-hash result and the L2 batch-prework pass (a separate code path) both land on 31 reuse / 16 new, identical per song. Corroboration, not a re-print.

**⚠ Scope, stated with the count (per `state-the-scope-with-the-count`): MAIN SEQUENCES ONLY** — no aux export exists yet for any of the 7 remaining songs, so aux-only figures are not in these numbers (the same shape as the 08-01 aux-2002 colour scope trap). Re-run per song once its aux export lands. SONG_R 2800 independently re-confirmed empty (0 cues, 0 figures, 6 KB stub) by this same pass.

**Two defects found and fixed by validating rather than reporting (v1→v2):** (1) `iterparse` + `root.clear()` inside the loop could drop nested `Dependency` subtrees — v2 does a full parse per file; (2) v1 reported one cross-song number that conflated same-name-reuse with different-name-same-content — v2 reports them apart. See `state-the-scope-with-the-count`.

**Files:** `generated/figure_hash/` — `figure_hash2.py` (the analysis), `validate2.py` (the three tests), `FIGURE_HASH_SHOWWIDE_v2.csv` (every figure/hash/class/song), `FIGURE_HASH_FINDINGS_v0.1.md` (this write-up in full). v1 (`figure_hash.py`, `validate_hash.py`) kept for the record only — do not use.

**Relation:** `inherited-file-membership-is-ground-truth` (the labels-lie doctrine this is the fourth object class for) · `tourshow-speed-architecture-standing-ruling` (why Speed is excluded from the hash) · `state-the-scope-with-the-count` (the discipline this validation pass is an instance of).

---
**⚑ Librarian note (not part of the concept body — for cLD, remove before or on apply):** this run could not confirm `tourshow-phaser-figure-duplication-across-songs` exists in the accessible `concepts/SPINE.md` snapshot (grepped, zero hits — see RUN_REPORT.md). Writing this amendment on the dispatch brief's explicit word that this concept already exists and carries the flagged, unrun check. If the file does not in fact exist at apply time, promote this content into a new concept instead of appending it.


### tourshow-phaser-pool-identity
**Pool 21 'Phaser' = predefined_phaser.xml (107 baked phasers); Pool 22 'All 2' = predefined_phaser_recipes.xml (46 recipe templates) — two parallel stock libraries**
*when:* Before referencing a stock phaser/recipe preset by pool number, or reasoning about which stock library a preset came from, in the {TOUR} build file


Two parallel stock libraries, confirmed live in this show file (cLD_SANDBOX):

- **Pool 21 "Phaser"** = `predefined_phaser.xml` — the stock BAKED-phaser library, 107 presets, imported the prior session (2026-07-15). Includes the Release color family (see `release-family-ships-stock`) and 61 "mixcolor" 2-step color phasers (multi-step badge; echo confirms "has multiple steps").
- **Pool 22 "All 2"** = `predefined_phaser_recipes.xml` — this session's (2026-07-16) import, the stock RECIPE-template library, 46 content presets across 7 sections (see `tourshow-stock-recipe-library-inventory` for the full census).

**Pool numbering confirmed two ways:** (1) Dave confirmed directly at the console — "pool 21=phaser pool / pool 22=All 2" (windows at the time: D2=Recipe Editor, D1=pools 21+22); (2) corroborated independently by the Values-cell preset-picker tabs in the Recipe Editor, which enumerate pool numbers directly (Phaser=21, All 2=22, All 3=23…) — this closes the [VERIFY] the first capture of this finding carried on numbering.

Note these are THIS show file's current pool-number assignments (Show Creator imports land in the next available slot) — the underlying stock XML content (`predefined_phaser.xml` / `predefined_phaser_recipes.xml`) is universal MA3 stock, but the pool numbers 21/22 specifically describe cLD_SANDBOX, not a console-wide constant.

Naming provenance: pool 21's generic default label ("All 1") was renamed to "Phaser" in v2.4 — explaining why pool 21 reads "Phaser" while pool 22 still carries its generic default label ("All 2"), rather than a matching "Recipe"-style name. (Renaming pool 22 to something like "Recipe Phasers" is a live candidate — see `pool-labeling-doctrine-inherited-risk`.)

**Relation:** FX White/Red/Green presets appear in BOTH pools at slots 110-112 despite `predefined_phaser.xml` itself carrying no FX presets — see `tourshow-fx-preset-dependency-anomaly`.

History: none — pool identity established and confirmed same session, 2026-07-16.


### tourshow-recipe-based-show-style-ruling
**{TOUR} is recipe-based programming all the way through — not Broadway cue-to-cue**
*when:* Before choosing a programming approach for any {TOUR} cue — settles cue-to-cue vs recipe-based at the show level, not per-cue


Dave's ruling: {TOUR}'s programming style is **recipe-based ALL THE WAY THROUGH** — not the Broadway cue-to-cue model (hand-built, fully-baked cues one at a time). Recipes (Selection/Group reference × preset-values reference × shape × grid/measure — see `recipe-lane-end-to-end-verified` for the mechanics) are the **PRIMARY programming mode** for the whole rebuild, not one tool among several.

**Relation:** this is the show-level "what mode do we build in" ruling; `tourshow-programming-ramp-plan` is the separate "in what order do we build" sequencing plan — load both together when planning build sessions.

**DOCTRINE, extended (2026-07-17, Dave, dictated, paraphrased):** building a phaser recipe directly into a cue part is mechanically possible, but it is NOT our working style. {TOUR} references **PRESETS** — phasers live in the preset pool, and recipe lines reference them (a Selection reference × a Values-preset reference), rather than a phaser being baked directly into the part. This is the concrete mechanism behind "recipe-based all the way through": the fully-referenced workflow (see `recipe-lane-end-to-end-verified`), not a build-it-into-the-part shortcut.

**Nuance, 2026-07-19 (Dave, same live session as the group-contract work):** the store-a-Group-before-it-enters-a-recipe discipline (see `tourshow-gesture-groups-on-demand-doctrine`) is a **consequence of choosing this recipe-based mode, not an MA3 technical law.** It remains possible to program groupless/old-style — hard, baked preset-based values written straight into cues, the way shows have been built for decades — and MA3 itself imposes no requirement against it. What that alternative forfeits is recipes and tourability: the whole show would live in the hard-value/cookover layer, with nothing left that recomputes per rig. The store-groups-for-recipes discipline follows from this ruling plus the inheritable-file mission (see `tourshow-mission-and-handoff`), not from any console necessity — the doctrine should be stated that way rather than as a claimed technical requirement.

**Extended 2026-07-21:** paid for again the hard way — a first-pass SONG_G build skipped this ruling entirely (9 baked SET→OUT cues, no recipes, cell/grid spine unused) despite the ruling being on record; see `review-plan-gate-precedes-programming-doctrine` for the named failure mode and the new REVIEW→PLAN gate proposed to prevent recurrence.

## The ruling is now a CLOSED, EXECUTABLE CONTRACT (2026-07-28)

"Recipe-based all the way through" was the mode ruling; it now has a concrete object-by-object
contract — **phaser preset = the temporal figure (stock Shape + Universal Dimmer preset) ·
group = who · MAtricks bound at the SEQUENCE = spatial · one phaser preset per use-site ·
`cLD ` prefix · ours numbered at `21.<century>20`.** Full specification, including what is
copied versus referenced and why the per-use-site duplication is deliberate:
`tourshow-authoring-contract-v01`.
History: none — ruling stated 2026-07-16. Extended 2026-07-17: Dave's follow-on doctrine ruling out building phasers directly into cue parts, reinforcing the preset-reference model. Extended 2026-07-19: added Dave's mode-vs-law nuance — the store-for-recipes discipline is a consequence of this ruling, not an MA3 requirement. Extended 2026-07-21: cross-referenced `review-plan-gate-precedes-programming-doctrine`, the process gate proposed after this ruling was skipped in practice despite being on record. Updated 2026-07-28 [0727-2cLD]: the mode ruling now has a closed executable contract in tourshow-authoring-contract-v01.


### tourshow-recipe-line-redundancy-taxonomy
**Recipe-line redundancy taxonomy: the emitter does not dedup by design (crosswalk collapse); parent+child group overlap is invisible to an identity-dupe census; same value in two century PARTS is not a duplicate**
*when:* Before deleting an apparent duplicate recipe line at the desk, or before trusting an identity-duplicate (group,value) census as a complete redundancy check — several redundancy shapes exist and only some of them are real bugs


Three distinct redundancy shapes exist in the crosswalked output, and they need different responses. Conflating them is exactly what almost cost SONG_J its wash layer (some songs' wash content landed on a beam target and was hand-deleted at the desk as an apparent duplicate — an open, Dave-owned action item, not detailed further here).

## Shape 1 — identity-duplicate lines (emitter does not dedup, and that is expected)

**The emitter does not dedup, and the shipped SONG_J file carried 38 EXCESS DUPLICATE RECIPE LINES across 22 (cue, group, value) groups — {LD}'s source has ZERO.** Every one is a **crosswalk COLLAPSE**: several distinct {LD} groups map onto one cLD group and happen to carry the same value in the same cue (e.g. `JDC1 US [MM]` + `[MMRGB]` + `[MMSTB]` all -> `cLD QX40 MM ALL @ Beam.RateFast`). Harmless to output — the same value is simply written twice — **but this is exactly what a doubled line looks like at the desk**, the same shape as the wash-defect failure mode. SONG_J's specific desk-edit outcome: 26 of the 38 cleared by Dave (the cue 21/22/23 `Beam.RateFast`/`Beam.Open` pile-ups collapsed ×3->×1 and ×2->×1); **12 excess still stand** (cue 21 BEAMS DS/MS + PLINE UPPER/BAND + QX40 MM; cue 23 QX40 MM; cue 27.1 BEAMS DS + MS).

## Shape 2 — parent + child GROUP overlap (invisible to the identity-dupe census)

**A redundancy class the identity-dupe census cannot see, because the group NAMES differ:** e.g. `cLD BEAMS ALL` alongside `cLD BEAMS DS` and `US` + `cLD BEAMS MS1` + `2` — same fixtures, same ingredient, same cue, but a (group, value) repeat count is blind to it since the names don't match. 3 sites in SONG_J (c20.1 `Dimmer.0`; c27.1 `Ultra Cool White` and `Dimmer.0`).

**⚠ The same test does NOT hold for JDC:** `cLD PLATES GRID` and `cLD TUBES GRID` are **different SUBFIXTURE ENGINES on the same physical bodies**, so a `JDC ALL` line beside a `PLATES GRID` line can both be legitimately real at once — do not flag JDC parent/child pairs as automatic overlap. Containment is currently INFERRED from `ARTIST_TOURSHOW_GROUP_CONTRACT` (row scopes DS/MS1/MS2/US tile a category) — a live Group membership census would make this provable and is still owed.

**Removal direction is a taste call, not a mechanical collapse — do not automate it.** Observed case: Dave's Mark-cue beam edit was NOT "collapse to the parent" (the natural-sounding shorthand). He instead removed `cLD BEAMS ALL`'s Position and Colour and KEPT the per-child lines, then repositioned MS1+2 (Stage Wash Base -> cLD Mid) and RIVALE (Pan X 1 -> Pan Fan) — because the children needed DIFFERENT positions (DS/US at Lowest, MS1+2 at Mid), so the PARENT's blanket position was the line that had to go. **Rule as observed: remove whichever line is redundant or in conflict given what the children actually need — direction depends on the cue.**

**⚑ Open question for Dave, same redundancy family:** at SONG_J cue 23.1 Dave removed `cLD QX40 MM ALL @ Dimmer.Full` (an expansion line, see `tourshow-stb-white-release-ruling`) and `cLD QX40 COLOR @ Dimmer.0` ({LD}'s own line, which fought the expansion's `Dimmer.Full`) — reading as a deliberate rule that when the MM engine also carries a phaser, the expansion's `Dimmer.Full` is redundant. **The same pattern still stands unedited at SONG_J cues 8.1, 10.1 and 15.1** (`QX40 MM ALL` carrying `Dimmer.Full` + `Swell Sine 2`). If it is a rule it belongs in the emitter and those three want the same treatment; if 23.1 was a one-off taste call, leave them. **Not resolved.**

## Shape 3 — same value in two different century PARTS is NOT a duplicate

**"Delete-thinking-it-is-a-duplicate" is a distinct desk failure mode:** parts-per-century puts the same VALUE on two different century parts routinely (a wash line in P2 beside a beam line in P5 can look like one doubled line in a flat sheet view). **Before deleting an apparent duplicate at the desk, check the PART it sits in** — the same value in two different centuries is the architecture working correctly, not a double.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (the sibling redundancy class at the POOL-OBJECT/figure level rather than the recipe-line level). `reconciliation-identity-per-song-verification-method` (corrections found this way are logged to the ledger, deferred to circle-back — not fixed in place mid-run). `tourshow-cue-century-review-sheet-doctrine` (the review artifact these shapes are read off of).


### tourshow-speed-architecture-standing-ruling
**Standing speed architecture: every cLD sequence rides the BPM Speed Master, gears come from the DIVIDE function in Cue Speed Scale, and NOTHING carries speed on Effects or MAtricks at play time**
*when:* Before setting ANY speed or tempo value — on a sequence, a cue-part Speed Scale, an effect/phaser preset, or a MAtricks — this is the standing division of responsibility and it supersedes per-song improvisation


**Dave's ruling, standing across the show:**

1. **Every cLD sequence is set to the BPM SPEED MASTER.**
2. **Gears ride the DIVIDE function in Cue Speed Scale** — per cue part, at the desk.
3. **No special speed settings on Effects/phaser presets, and no MAtricks speed binds at play time.** Our MAtricks binds carry **phase/spread only**.

**Our presets therefore ship speed-UNBAKED, always.** Speed is a desk knob, not authored content — which is also what makes the content portable, since a baked rate is as rig-specific as a baked phase.

## Where the gear number comes from

Read it off {LD}'s own baked speeds during the phaser spec-read: his figures decode to clean divisions of the song tempo, and that division IS the Speed Scale plan. SONG_A decoded to **119.0** (÷1) and **59.5** (÷2) — his design intent, recovered rather than guessed. The aux Synth Swell decoded to **238 = ×2**.

**Watch for a cue that mixes gears.** SONG_A's chorus fired wave lines at ÷1 alongside a rivale line at ÷2. If Speed Scale is one knob per cue part, a mixed-gear cue cannot be split there — either accept the dominant gear or give the odd line its own part.

**Generalises `tourshow-fill-layer-rebuild-method`'s narrower SONG_T note** ("ours ride the Sequence Speed override set to BPM") from a per-build detail into standing doctrine for every song.


## ⭐ SCOPE NARROWED 2026-08-01 [0801-2cLD] — MAtricks DO carry speed for 2D figures whose X:Y speed RATIO is the figure

The standing rule in this concept's body ("no MAtricks speed binds at play time... our MAtricks binds carry phase/spread only") is narrowed for one deliberate case. **Dave ruled: for a 2D figure where the X:Y SPEED RATIO is itself the figure, author a SPECIAL MAtricks carrying BOTH X and Y speed.** This extends the standing rule rather than replacing it — it applies only when the ratio between axes is load-bearing, not as a general license to bake speed onto MAtricks.

**Dialect proven, no desk golden needed — settled empirically:** no MAtricks XML exemplar existed anywhere in the corpus carrying any Speed attribute before this (zero on our 6 MX goldens, zero in {LD}'s sequence exports). Rather than guess, one MAtricks was set with X+Y speed at the desk, exported, and read back: **live property dump on `MX 157` confirmed `SpeedFromX` / `SpeedToX` / `SpeedFromY` / `SpeedToY` (plus the Z pair)**, alongside `FadeFrom`/`To` and `DelayFrom`/`To` per axis — casing follows the `PhaseFromX` convention. **`MX 168` then proved the authored dialect accepts Speed AFTER the Phase block**: imported and read back `SpeedFromX=240.0 SpeedFromY=60.0` exact. {LD}'s own desk order leads each axis triple WITH Speed (`SpeedFromX, PhaseFromX, PhaseToX, SpeedFromY, ...`) on his `StandardRecipe` wrappers — that order is **NOT required** on a MAtricks pool object; Speed-after-Phase is proven to work there.

**Scope shrank on inspection — only ONE of three candidate 2D figures actually needed a real ratio.** Breakdown 2/1 bakes X=120 Y=120 (1:1 — both axes at rail, so a plain 2D phase MX + a per-part Speed Scale reproduces it with no special object needed) and Swell Dim#4 bakes Y=`'Stop'` with `PhaseY 0->0` (Y entirely inert = the figure is X-only). **Only Swell Dim#3 needs real ratios** (X:Y = 2:1 on Strike M, 4:1 on the Lin/CL populations). **Check whether a ratio is actually real before minting a speed-carrying MAtricks object** — most candidates resolve to the existing phase-only + Speed Scale pattern.

## Where the gear number comes from — a third gear family added, 2026-08-01 [0801-2cLD]

**SONG_I's 270 BPM against a 135 rail is DOUBLE TIME** (Dave confirmed) -> **Speed Scale ×2**, a MULTIPLY gear — the existing "SONG_A Synth-Swell" ÷2 precedent generalizes into a full multiply lane, not just divide. Half of SONG_I's phaser energy runs double-time; it is that song's dominant gear, not an outlier. **⚠ The ×2 gear's serialization TOKEN is UNATTESTED in the corpus** — only `One`/`Div2`/`Div4`/`Div16` have ever been seen in a desk export. Pin the multiply-family spelling via a scratch export before any emitter bakes a double-time gear into authored XML.

## Where the gear number comes from — the exact formula and wrapper path, 2026-08-04 [0803-3cLD]

**CONSTRAINING (G=0.7).** Speed Scale is a **Part attribute, set per cue**; its value is
**{LD}'s wrapper `SpeedFromX` ÷ the song's BPM.** The wrapper StandardRecipe this divides
lives at **`Part/DependencyExport/Dependency/Preset/StandardRecipe`** — the same per-population
wrapper pattern documented in `source-matricks-wrapper-recipe-encoding`, read here for its
SPEED axis rather than its spread axis. This is the concrete mechanism behind "read it off
{LD}'s own baked speeds" above: divide the wrapper's `SpeedFromX` by BPM and the result is
the gear (÷1, ÷2, ×2, …) to set in Cue Speed Scale.

## Working lane confirmed, 2026-08-05 [0805cLD] — read `SpeedFrom` directly off the Phaser Preset

**Dave, ruling on practice:** the Speed Scale multiple comes **directly from `SpeedFrom` in
each Phaser Preset.** This sharpens the wrapper-path formula immediately above
(`SpeedFromX ÷ BPM`, read at `Part/DependencyExport/Dependency/Preset/StandardRecipe`) — the
**per-preset `SpeedFrom` read is the working lane** in practice, not a distinct mechanism.

**[0805-2cLD] CORRECTION — x2 IS an attested Speed Scale token** (Dave 08-05, enters speed scales directly). The prior "Div8 and x2 UNATTESTED" narrows to **Div8 only**. Attested ladder: Div16 · Div4 · Div2 · One · x2.

History: corrected 2026-08-05 [0805-2cLD] — x2 attested by Dave; prior unattested pair narrowed to Div8 only.


### v24-phaser-model
**v2.4 phaser model — phasers ARE recipes with 2+ steps; CLI ranges are spatial not temporal; Shapes pool**
*when:* Before generating any Lua, CLI, or recipe-editor UI steps intended to build a phaser (temporal, multi-step effect) or configure its controls (nShot/Direction/Adaptive) — corrects the MA2-era mental model of phasers as a separate object type and covers the v2.4 STANDARD-vs-PHASER recipe split


Corrects the MA2-era mental model. Source: `WORKING/cLD_CONSOLE_NOTES_v0.1.md`; corrections approved by Dave 2026-07-04.

- **Phasers = recipes with 2+ steps.** A single-step recipe is a "Standard Recipe." Both are built in the Recipe Editor / Phaser Editor — there is no separate "Phaser" object class distinct from Recipe.
- **`EditRecipe Programmer` is standard-recipe ONLY** — it **cannot build phaser recipes**. See `store-recall-recipe-toggle-rules` for the scoping of the EditRecipe bookend pattern to standard recipes.
- **PSR (Partial Show Read) over a phaser recipe breaks its shape links.**
- **CLI value ranges are SPATIAL, not temporal.** `At 0 Thru 100` (even `Thru 0`) produces a fan across the current selection as a **single step** — you cannot type a temporal phaser into being via CLI ranges. Temporal steps must be added **graphically**: Phaser Editor → A⁺/R⁺ arms add-mode → click the value grid to place the step.
- **`At Shape <n>` is valid syntax; `Shapes` is a new v2.4 pool** (22 predefined) — reusable transition/width/accel/decel blocks. **Storing a shape deactivates programmer values.** See `shapes-pool-facts` for shape-link (angular-bracket) semantics, stock-shape locking, and the speed-override pattern.
- **Phaser workflow:** base value → add step 2 in the editor → MAtricks phase object distributes → adjust Speed/Phase/Width on encoder layers → Store to Preset (the **violet cooking-pot icon** marks a phaser recipe in the pool).

**STANDARD vs PHASER recipe split (official MA webinar, YouTube `W0fSSxlog-A`, notes banked to `PHASER_RECIPE_WEBINAR_v0.1.md`):** v2.4 draws a second, complementary axis alongside the step-count criterion above — **STANDARD recipes reference existing data**; **PHASER recipes build the phaser from scratch inside the recipe** (logic-based). Both framings are banked as-given; not reconciled into one rule.

**Phaser recipe controls (webinar; nShot popup mechanics live-verified 2026-07-16):**
- **nShot** = cycle count, then auto-stop. Calculator popup: range **0..128**, an **NShot Stay** toggle, and **Remove/Unlimited** buttons; a committed value shows in the encoder bar (e.g. `NShot 3.00`).
- **Direction**: fwd / back / **ALTERNATE** (bounce).
- **Adaptive Measure** + **Adaptive Width**: auto-calculate timing/width from the *current selection grid*, as opposed to this project's manual literal phase math — reconcile/test before assuming parity.

**Recipe selection (webinar doctrine):** a recipe can reference a **Group** OR **capture the current programmer selection** directly — no per-variation group objects needed. See `recipe-lane-end-to-end-verified` for the live-verified UI mechanics of this same choice (Selection-cell picker: None / From Value / Take Selection + Group tiles).

**Fully-referenced workflow (MA best practice, webinar):** phaser recipe → store in a **Preset** → embed that preset inside a **STANDARD recipe** used in cues; the cue stack then auto-updates on any upstream change. See `recipe-lane-end-to-end-verified` for a live-verified instance of this exact chain (Group reference + phaser-recipe-preset Values, stored into a cue, cooked by the executor).

**Recipe limits (webinar):** recipes never play back directly — they must **cook to the programmer** (realtime update while editing, confirmed live). **Generators and bitmaps are NOT allowed** in phaser recipe lines yet. Legacy phaser→recipe conversion **mistranslates some phase values** — don't trust an auto-converted legacy phaser's phase without checking it.

History: first-contact correction of the MA2-era model, recorded and Dave-approved 2026-07-04. **2026-07-16:** extended with webinar-sourced (`PHASER_RECIPE_WEBINAR_v0.1.md`) STANDARD-vs-PHASER split, recipe controls (nShot/Direction/Adaptive), selection-reference doctrine, fully-referenced workflow, and recipe limits; shape-link mechanics split out to the new `shapes-pool-facts` concept for atomicity.


### wipe-in-thru-range-anatomy
**Wipe-in anatomy worked example — Thru ranges on a layer value distribute width spatially across the grid inside one recipe cell**
*when:* Before building or debugging a wipe-style phaser recipe, or when a step's width uses a Thru range and you need to know what that range actually does


Worked example from MA's stock `WipeIn` recipe preset: **4 steps, `Measure=1`**. Widths per step:

1. `25%`
2. `"0% Thru 100%"`
3. `25%`
4. `"100% Thru 0%"`

**The mechanism:** a `Thru` range on a layer value distributes that width **spatially across the grid** — this is a spatial Thru operating *inside a single recipe cell/step*, not a temporal range. Steps 2 and 4 are **complementary** Thru ranges (`0→100%` and `100→0%`), so every fixture's total width across the 4 steps sums to **150%** — a uniform loop length per fixture — but the position of the *lit window* travels across the grid as the steps play. That traveling lit edge, composed purely from step widths, is the wipe. The whole figure is pinned inside **one beat** (`Measure=1`).

Cross-reference: `stock-measures-grammar-census` (the "Wipes: Measure=1" row this example demonstrates); `measure-layer-math` (the width/Measure math this figure is built from — Σwidths here is 150, not 100, precisely because of the complementary Thru pair).

History: created 2026-07-16 as a standalone worked example, since it demonstrates a distinct mechanism (spatial Thru inside a recipe step) not covered by the Measure formula alone.


### wire-timeout-vs-console-busy
**A timeout right after a write batch indicts CONSOLE BUSY-WORK before it indicts the wire — recipe reassignments trigger recook storms; prove liveness with a tiny probe before diagnosing the transport**
*when:* When an MCP call times out and the previous call was a batch of recipe/selection writes — check for a recook storm before touching the transport, the session or the network


**Observation:** timeouts clustered immediately after batches of recipe-line reassignments. Reassigning a recipe line's `Selection`/`MAtricks`/`Preset` invalidates the cooked output, and the console **re-cooks** — across every cue that line feeds. On a show-sized file that is real work, and it can absorb the console for long enough to time a round-trip out.

**Diagnostic order for a post-write-batch timeout:**

1. **Tiny probe first.** A one-token read (`tostring(BuildDetails().BigVersion)`) proves liveness in ~66 ms. If it answers, the wire is fine and the console was busy — wait and continue.
2. Only if the probe *also* fails: **`get_console_info`** for a PID change (`segfault-manifests-as-mcp-timeout` — a timeout can be a crash).
3. Then payload **shape** (`send-lua-expression-payload-rule`) and payload **scale** (`split-and-guard-per-sequence-walk-law`).
4. Session/interface health last (`out-ok-is-send-not-reachability`).

**Corollary for build planning:** recook cost is why heavy repoint work should be **paced in batches with probes between them**, and why the recipes are expected to re-cook at the next playback anyway — the first previz run-through covers the visual settle after a repoint sweep.

**Relation:** `segfault-manifests-as-mcp-timeout` · `send-lua-expression-payload-rule` · `split-and-guard-per-sequence-walk-law` · `recipe-output-precedence-and-cooking-doctrine` (what "cooking" means) · `settle-before-export-crash`.

History: none — pattern recognised across the {FESTIVAL} → {FESTIVAL} surgery runs, 2026-08.


### xml-file-side-authoring-import-lane-proven
**File-side XML authoring lane proven end-to-end, now three times (presets baked, presets recipe, macros): Export → edit file-side → SaveShow checkpoint → Import .../NoConfirmation → export-back diff**
*when:* Before hand-authoring any preset (baked or recipe) off-console and importing it, or before surgically editing an existing exported file's span (e.g. a timecode event) rather than composing a whole new object — the proven lane mechanics, GUID handling, and import-filename convention


**The lane:** `Export Preset <slot> "name"` → edit the file file-side (e.g. `sed`) → `SaveShow .../Enumerate` checkpoint (see `saveshow-discipline-and-mcp-tier` standing rule) → `Import Preset <target-slot> "file" /NoConfirmation` → export the target slot back and diff against the authored file to verify. This is the "sleeper lane" for generating console content off-console instead of hand-building it live.

**Proven twice, same session:**
1. **Baked preset:** exported a console-built M4 preset as ground truth, edited it file-side, imported to a scratch slot — landed **byte-identical** except for a fresh console-assigned GUID.
2. **Recipe preset:** exported console-built recipe preset `22.2` (Sine) as ground truth, authored `"cLD Sine 180"` (changed `PhaseToX` 360→180, GUIDs stripped), imported to `22.121` — name and structure verified correct.

**GUID handling — closes a prior [VERIFY]:** stripping GUIDs from the authored file before import works; the console assigns fresh GUIDs on import rather than requiring them to be pre-populated or rejecting the file. This closes the "GUID-on-import" open question **for presets** (the equivalent question for Layout XML imports, tracked in `layout-xml-export-schema-and-import-lane`, is still separately open).

**Import filename convention:** the `Import Preset` filename argument takes **no `.xml` extension** — it resolves from `datapools/presets/` by bare name.

**Proven a third time, 2026-07-19 — macros:** `cLD_POSITION_WIZ_generic_v0.1.xml` was authored entirely file-side (composed from factory-verbatim grammar, see `factory-position-wiz-anatomy-and-porting`), deployed to `gma3_library/datapools/macros/cLD_POSITION_WIZ.xml`, imported, and run live on console successfully — the first cLD-authored macro XML, see `cld-position-wiz-generic-v01-authored-and-deployed`. This is the third dialect this lane has been proven against (baked preset, recipe preset, now macro), and the first where authoring happened without any exported ground-truth file to start from — composed purely from schema knowledge plus factory-verbatim grammar patterns.

**Proven across ALL pool dialects, 2026-07-21 ([0721-2cLD]):** the lane — now named **"Dave's rhythm"** — generalizes cleanly: author XML off-console → Desktop_Commander write to `gma3_library/datapools/<type>/` → `SaveShow` checkpoint → `Import <Object> <slot> 'bare-name' /NoConfirmation` (bare filename, no `.xml`, same convention as presets) → for **builder macros** specifically, `Go+ Macro <n>` fires the import chain → export-census verify. Proven THIS session on: macros (builder macros 6/7/8 in `datapools/macros/`), color presets (`/Global` store mode), phaser presets (the breathe preset), sequences (`cLD SONG_G`, `cLD SLIDE POP`), and timecode (`cLD SONG_G TC`) — five dialects in one session, on top of the three already proven (baked/recipe presets, macros). The **builder-macro pattern** (a macro pool slot whose lines are a sequence of `Import` commands, fired once via `Go+ Macro <n>`) is the concrete mechanism behind "one build-macro authors it all" — see `review-plan-gate-precedes-programming-doctrine`.

**Extended again, 2026-07-31 ([0731-2cLD]) — a SIXTH variant, surgical span-editing rather than whole-object authoring:** for editing individual EVENTS inside an already-exported Timecode file (not composing a whole new object from scratch), the proven move is a byte-surgical edit of one `Track` element's span — verify neighbor tracks stay byte-identical, deploy to `gma3_library/datapools/timecodes/`, `SaveShow` checkpoint, `Delete`+`Import` the object, then export-back census by **per-track EVENT COUNT** (not just Target pointers — a target-only census reads healthy on an event-emptied track). Proven on a live TC repair (SONG_B's drum-roll `Go+`→`Temp` conversion, 4 flips + 5 paired releases, neighbor tracks byte-identical). Named the **"third authoring lane beside CLI and desk."** Full method, file-location, and MCP-tier facts: `tc-xml-event-surgery-lane`. The delete step in this variant carries its own hazard when the object being deleted is a live TC-cutover TARGET rather than the TC object itself — see `tc-cutover-last-and-delete-eats-events-doctrine`.

Cross-reference: `recipe-xml-schema` for the recipe-dialect element/attribute shape this lane authors against; `phaser-preset-xml-measure-speed-fixed-point-encoding` for the baked-dialect's fixed-point value encoding; `saveshow-discipline-and-mcp-tier` for the mandatory pre-import checkpoint bracketing this lane; `macro-xml-schema-cracked` for the macro-dialect schema this third proof authors against; `tc-xml-event-surgery-lane` for the full sixth-proof method (span-surgery rather than whole-object authoring).

## File bridge to gma3_library, pinned 2026-08-04 [0803-3cLD]

~~**CONSTRAINING (G=0.7), scoped to moving files to `gma3_library`: `gma3_library` is not
`device_bash`-reachable.** The proven bridge: base64-encode the file OUT via `device_bash`,
base64-decode it IN via Desktop Commander (which does reach `gma3_library`), and sha-verify
both ends before treating the deployed copy as trustworthy.~~ **SUPERSEDED 2026-08-05 — see
"File bridge simplified" section below: a plain `cp` via Desktop Commander does the whole job,
no base64 round trip.** This was the missing mechanical step behind every "Desktop_Commander
write to `gma3_library/datapools/<type>/`" line already in this concept and its siblings
(`cld-position-wiz-generic-v01-authored-and-deployed`, `plugin-install-loop`) — none of them
previously stated HOW the bytes cross from the authoring side to the Desktop-Commander-
reachable side.

## File bridge simplified — plain `cp` supersedes the base64 round trip, 2026-08-05 [0805cLD]

**Desktop Commander's `start_process` reaches BOTH the Drive-synced repo AND
`~/MALightingTechnology/gma3_library`, so a plain `cp` deploys a file with a `shasum -a 256`
either side.** No base64-out/base64-in round trip, and the bytes never touch the conversation.
Proven on the SONG_L deploy: sha `2f71ee156a0557b1` identical both ends, 50,531 B.
(`device_bash` still cannot reach `gma3_library`, and the **Filesystem MCP is scoped to `My
Drive` + `dev` only** — Desktop Commander is the one tool that reaches it.) This supersedes
the base64 bridge above, which was written when only `device_bash` had been tried as the
outbound leg.

History: created 2026-07-17 — first end-to-end proof of the lane, on both dialects (baked + recipe) in one session. Extended 2026-07-19: proven a third time on the macro dialect (`cld-position-wiz-generic-v01-authored-and-deployed`) — first proof composed without an exported starting file. Extended 2026-07-21: generalized end-to-end across all five pool dialects (macro/color-preset/phaser-preset/sequence/timecode) in one session via the named "builder macro" pattern (Import commands as macro lines, fired by Go+ Macro <n>).

History: extended 2026-07-31 [0731-2cLD] — proven a sixth variant: byte-surgical span-editing of an EXISTING exported file (timecode events) rather than whole-object authoring, on a live TC repair. Full method split out to its own concept, `tc-xml-event-surgery-lane`, since it is TC-specific enough in mechanics (Delete-then-Import of an already-cutover object) to need its own retrieval trigger.


## SEQUENCES, CUES & PLAYBACK

### authored-sequence-dialect-vs-desk-golden-fixed-diffs
**The authored-sequence dialect diverges from the desk-export golden in 3 FIXED, sealed-importable spots — smiths should stop re-flagging them as deviations**
*when:* Before a smith certification pass flags a sequence-XML as non-golden, or before hand-authoring a sequence to match a desk export byte-for-byte — these 3 spots are known, deliberate, and already proven to import clean


**The authored-sequence-XML dialect diverges from the desk-export golden in 3 FIXED spots — all sealed importable as of {TOUR} build v.88.** These are known, deliberate divergences, not defects, and a smith certification pass should stop re-flagging them:

1. **`Sequence` element: `SpeedMaster` set AFTER `SpeedScale`** in attribute order (the emitter's position, desk-proven by the SONG_C import + live readback `SpeedMaster=Speed1`).
2. **No `Name` attribute on `OffCue`/`CueZero` parts** — the kit idiom; every shipped song has imported clean this way. An export-back adds a `Name`; it is not an import requirement.
3. **`StandardRecipe`: `MAtricks=` written BEFORE `Selection=`** in attribute order.

**Consequence:** any smith packet or manual review comparing an authored sequence byte-for-byte against a desk-export golden should treat these three positions as an accepted, sealed variant of the dialect — not as evidence the authored file is wrong.

**Relation:** `tourshow-seq1310-build-record` (documents spots 1 and 2 as smith flags on that specific build, both closed with no edits — this concept consolidates that pattern as a standing dialect fact rather than a per-build note). `export-sequence-xml-schema` (the general Sequence/Cue/Part/StandardRecipe schema this dialect sits inside — see also its amendment on a fully NAME-less Part, a related but distinct schema-completeness fact). `smith-packet-must-stage-multi-part-golden` (why a smith needs a real multi-part golden to judge dialect facts like these against in the first place).


### cue-display-number-vs-no-addressing-gotcha
**MA3 stores a cue's display number ×1000 as its internal .no — single-cue CLI/Lua addressing needs the DISPLAY number (Cue 5), not .no (Cue 5000 returns nil); wildcard Cue * enumerates BY .no**
*when:* Before addressing a single cue by number via CLI or Lua, or before interpreting a wildcard Cue * enumeration's numbering


**The gotcha:** MA3 stores cue **5.000** internally as `.no` **5000** (the display number × 1000, leaving room for decimal sub-cues like 5.1, 5.2). **Single-cue addressing needs the DISPLAY number** — `Cue 5` — not the internal `.no` value: `Cue 5000` resolves to **nil**.

**Wildcard behavior differs:** `Cue *` (wildcard enumeration) returns cues addressed **BY `.no`** — i.e. the wildcard census surfaces the internal ×1000 numbering, not the display numbers. Don't assume the two addressing conventions match just because they're both "cue numbers" — single-object addressing and wildcard-enumeration addressing use different number spaces here.

**Relation:** parallels other MA3 dot-scaled internal-vs-display numbering traps in the corpus (e.g. `phaser-preset-xml-measure-speed-fixed-point-encoding`'s 2^24 fixed-point encoding) — internal storage often scales a display value, and code/CLI that assumes 1:1 will silently fail (nil) rather than error loudly.

History: none — observed live in one session, 2026-07-22, working {FESTIVAL}'s cue structure via Lua/CLI.


### cue-names-not-round-trip-stable-content-derived-labels
**Bracket cue names ('[Full/...]') are CONTENT-DERIVED auto-labels, not fixed strings — the console re-resolves and can rename them on import; census cue names off the export-back, never off what was sent**
*when:* Before trusting a cue's bracket-style name as evidence of its content, or before census-ing cue names for a QC/reconciliation sheet — read names off the export-back, never off the authored/sent file


**Bracket-style cue names (`'[Full/...]'`) on {LD}'s aux sequences are CONTENT-DERIVED auto-labels, not authored fixed strings** — an authored `'[Full/Color Linear]'` re-labeled itself `'[Full/FX White]'` after import, because the phaser's stock endpoint reads through into the display name. This explains the aux naming convention file-wide; **it is not import damage.**

**The same instability hits cLD-authored cue names on import.** Desk-renamed example: authored `'[50/Neutral White]'`, export-back reads `'[Full/cLD FR NEUTRAL WHITE]'`. **Cue NAMES are not round-trip stable whenever the name references a preset the console re-resolves.**

**Practical consequence: census cue names off the export-back, never off what was authored or sent.** Any QC/reconciliation sheet, join-key logic, or census script that assumes a sent cue name will still be the name after import is checking a value the console may have already silently rewritten.

**Relation:** `inherited-file-membership-is-ground-truth` (the sibling doctrine for GROUP/preset names lying about membership — this concept is the CUE-name-specific instance of "don't trust a label," but the mechanism here is console re-resolution on import, not inherited-file staleness). `reconciliation-identity-per-song-verification-method` (a QC sheet built on this corpus needs export-back-sourced names to stay accurate).

## Not a census axis, reinforced 2026-08-04 [0803-3cLD]

**STRUCTURAL (G=0.5 — source line carries the ○ Low symbol against a G=0.5 Structural value;
the pairing is internally inconsistent with the notation's own table, flagged not resolved;
the fact itself is unambiguous).** Recipe-cue names are console-derived from bound content;
the authored `Name=` is discarded on import. Restated for emphasis: **cue name is not a census
axis** — don't count, join, or key anything on a cue's name, authored or read back; use the
cue's structural position (No=, part index) instead.


### cue-structure-is-tonal-harmony
**The cue structure IS tonal harmony — Mark/SET is HOME (the tonic), section cues are the departure, the song resolves back to nothing, and bumps are ornaments that must resolve into the line**
*when:* Before structuring, ordering or judging ANY song's cue list — and any time you are unsure whether a proposed cue, bump or movement is tasteful. This is the frame Dave supplied specifically so the programmer can check its own proposals against something rather than guess.


**Dave's framing, given deliberately as a bridge.** Concert lighting programming is a
hand-to-hand trade craft that is barely written down; tonal harmony is one of the most
thoroughly documented bodies of knowledge in existence. Dave routed around the thin spot
through the thick one: **read the cue structure as harmonic motion.**

## The mapping

| Music | Show |
|---|---|
| **Tonic / home** | the **Mark / SET cue** — the referent everything else is heard against |
| Departure, rising tension | the section cues stepping away from home |
| Pre-dominant (the build) | Prechorus-class cues — tension that *wants* to resolve |
| Voice-leading between chords | the **`>>` decimal cues** — how each line travels |
| Ornament / riff / fill | the **bump buttons** — surface events, never structure |
| Final resolution | the Outro/Blackout return — back to nothing, back to home |

**Why home matters mechanically:** without a clearly established tonic, movement away does
not read as movement — it reads as noise. The SET cue is what makes every later departure
legible.

## It explains a mechanic we already had

`tc-bump-button-architecture` rules that bumps exit via **Release, never Off**, so the channel
falls back to whatever the main sequence holds underneath. Under this frame that IS the
ornamentation rule: **an ornament that does not resolve back into the line is not an ornament,
it is noise.** Release *is* "return to the structural voice." The mechanic was banked first,
without the why; the why was music theory all along.

## Three consequences that fall out

1. **Tension must be WITHHELD to be spendable.** Maximum dissonance in bar two leaves nowhere
   to go. This is the intensity budget of
   `tourshow-go-wild-pair-intensity-budget-and-release-matricks-doctrine` restated — and it
   shows the principle runs at SET level too: the go-wild pair exists so the two songs that
   should peak still can.
2. **The return home should be recognisable but NOT identical.** A final tonic is the same
   chord meaning something different for what preceded it. An Outro is **home with history**,
   not a re-fire of the Mark cue.
3. **Start the movement EARLY — anacrusis.** Begin a move *before* the cue it is meant to land
   on, so the change arrives into an already-travelling gesture instead of starting one. The
   hit lands *into* motion. This is the operational form of Dave's **"tension wants motion, not
   just a level."** It also appears one layer down in the position vocabulary — a pan fan is the
   approach, the tilt is the landing (`festival-position-preset-stacking-and-tilt-ladder`).

## Confirmed by the inherited file's own data

Two checks nobody set up to pass, run against the SONG_T export:

- **Phaser placement.** 5 of the 6 distinct phasers sit on `>>` movement cues; the single
  exception rides cue 6 **Prechorus** — the pre-dominant. The one named cue that gets a phaser
  is exactly the one whose musical job is building tension. **Tension wants motion, not a level.**
- **The tonic bracket is visible in the line counts.** Cue 1 `Mark` is the heaviest cue in the
  song at **26 recipe lines**; cue 27.1 `>>` (the Blackout movement) is second at **16**. Home
  and the return to home are the two largest cues.

## ⚠ Scope — this does NOT promote the programmer to designer

`idea-file-design-programmer-boundary-doctrine` stands unchanged: the design side carries
music, story and "what good looks like"; the programmer carries the full mechanical toolkit and
**decides nothing**. What this frame buys is **structural literacy, not authority** — read the
shape being built, stop proposing things that fight the arc, and flag when a MECHANICAL choice
would break it (a bump that Offs instead of Releases; a build that spends its loudest
vocabulary before the chorus it is meant to set up). **Use it to check proposals, never to
originate intent.**

History: none — given by Dave 2026-07-27 and corroborated the same session against the SONG_T
export.


### empty-census-deserves-selector-suspicion
**An empty census result is a selector bug until proven otherwise — check the SELECTOR before believing the absence**
*when:* Before trusting a census/report/query that comes back ZERO or unexpectedly empty — especially any 'first matching X' selector (first cue, first row, first non-blank field) — check what the selector actually matched before believing the absence


**An EMPTY census result deserves the same suspicion as a surprising one.** A query that returns zero hits reads exactly like a real finding ("no song positions at Mark") — but zero is not self-verifying. Before accepting an empty result, check the SELECTOR that produced it, the same way you would check a surprising non-empty one.

## Worked case — the Mark-cue position grid's first pass (L7, 2026-08-03)

Building the show-wide Mark-cue position grid, the first pass took "the first cue with a non-empty `No`" as its definition of the Mark cue, and returned **ZERO positions for all 16 songs** — a result that reads exactly like a real finding. It was actually selecting **OffCue / CueZero**: per `sequence-xml-ordered-header-law`, the first two `Cue` children of any sequence ARE `OffCue` and `CueZero`, both of which carry a non-empty `No` but neither of which carries the show's content.

**Correct rule: take the first cue that actually HAS `StandardRecipes`, preferring one literally named `Mark`.** Applied correctly, this produced the real grid: 156 rows, 16 songs, 10 distinct Mark positions show-wide (see `tourshow-mark-position-grid-flow-pass-signal`).

## The family

This is the same shape as two standing hazards, both selector bugs disguised as findings of absence:
- `glob-false-negative-on-drive-synced-dirs` — a directory reads empty/stale because the LISTING tool served a stale or wrong view, not because the directory is actually empty.
- `stripped-group-membership-recipe-uncooked-diagnosis` — a group reads as having no members because the CENSUS METHOD (`Count()`/`Children()`) is structurally blind, not because the group is actually empty.

All three share the same corrective: **don't trust zero. Interrogate what produced the zero before treating it as a finding.**

**Relation:** `sequence-xml-ordered-header-law` (the header law that explains why "first non-empty No" mis-selects), `tourshow-mark-position-grid-flow-pass-signal` (the real result once the selector was fixed), `glob-false-negative-on-drive-synced-dirs`, `stripped-group-membership-recipe-uncooked-diagnosis` (sibling instances of the same family).


### executor-1-15-not-instantiated-mac-onpc
**Executors 1-15 are NOT instantiated by default on this Mac onPC — Assign fails silently, Executor 15/Page 1.15 resolve nil; the 101+ bank works, Assign instantiates an executor on first use**
*when:* Before assigning a sequence to an executor in the 1-15 range on this Mac onPC — check the executor actually exists first, or expect a silent no-op; also relevant when remapping a build off the 101+ scratch bank onto the tour desk's real 1-15 fader envelope


**The gotcha:** on this Mac onPC, executors **1-15 are not instantiated** by default. `Assign Sequence 15 At Executor 15` **fails silently** — no error, no effect. Downstream, `Executor 15` and `Page 1.15` both **resolve nil** (object-list lookups against them come back empty), even though the CLI accepted the Assign command without complaint.

**The 101+ bank works:** the scratch executor range instantiates cleanly, and `Assign` appears to **instantiate the executor on first use** in that range — e.g. `Assign Sequence 101 At Executor 102` resolved to a live object address (`14.14.1.12.2.102`) immediately.

**This session's workaround:** built on the working bank instead of the intended 1-15 tour-desk range — **cLD SONG_G** (Seq 15) → **Exec 102**, **cLD SLIDE POP** (Seq 101) → **Exec 101**. **Re-mapping to the real 1-15 fader envelope is still owed** before this show runs on the actual tour desk.

**Open question:** whether this is a Mac-onPC-specific quirk (parallel to `mac-vs-windows-onpc-network-output`'s Mac-vs-Windows onPC split) or a more general "executors must be paged/instantiated before Assign can bind" console behavior isn't yet determined — not tested against Windows onPC or a real console. Possibly related to the older `goplus-unassigned-sequence-assign-dialog-oddity` [VERIFY] (an unprompted Assign dialog on an unassigned sequence/executor) — unconfirmed, not established as the same root cause.

History: none — paid for live 2026-07-21, [0721-2cLD] session, building the cLD SONG_G + cLD SLIDE POP sequences.


### export-sequence-writes-per-name-files
**'Export Sequence 1 Thru "file"' fans out ONE FILE PER SEQUENCE named from the sequence's own name — the filename you give is ignored; freshness-filter the batch by mtime to find your run's output**
*when:* Before running a range Export Sequence and expecting a single named file, or when a bulk export appears to have produced nothing under the name you asked for — look for a fan-out of name-derived files instead


**A range `Export Sequence` does not write the file you name.** `Export Sequence 1 Thru "<filename>"` walks the range and writes **one XML file per sequence**, each named from **that sequence's own name**, into `gma3_library/datapools/sequences/`. The filename argument is consumed and ignored.

**Receipt:** one gated call produced a **190-file batch** in a single run — the whole live sequence pool of the tour file, exported for Mac-side analysis.

## Consequences

- **Do not census by filename.** The output set is discovered by listing the directory, not by opening the name you typed.
- **Freshness-filter by mtime.** The sequences directory accumulates every past export. The way to isolate *this run's* output is an mtime batch window — and per `save-disk-verify-mtime-delta`, read that window as a **delta** against the directory's other files, because MA3's stamps run ~9h behind shell time.
- This is the front half of the standing heavy-audit lane — see `export-plus-python-bulk-lane`.

**Relation:** `export-plus-python-bulk-lane` (what to do with the batch) · `export-sequence-xml-schema` (what is inside each file) · `save-disk-verify-mtime-delta` (the mtime-skew rule) · `preset-range-export-open-ended-only` (the sibling range-export gotcha in the preset pool).

History: none — observed and used the same session, 2026-08-26.


### goplus-unassigned-sequence-assign-dialog-oddity ⚠ VERIFY
**[VERIFY] An empty 'Assign Page 1 Executor 401' dialog appeared unprompted after Go+ on a then-unassigned sequence**
*when:* If an unprompted Assign dialog pops up after firing Go+ on a sequence — this may be expected MA3 behavior (Go+ on an unassigned sequence auto-prompting assignment), not a bug; check here before treating it as an anomaly


An empty **"Assign Page 1 Executor 401"** dialog appeared unprompted after a `Go+` on then-unassigned Sequence 102. (The source note also allows it may have come from a fall-through paste round instead, in flight the same moment — cause is not pinned down either way.)

It turned out useful in the moment — it became the lane actually used to assign the sequence to the executor — but *why* it appeared is unconfirmed.

**[VERIFY]:** does `Go+` on an unassigned sequence deliberately pop an Assign dialog as designed MA3 behavior? Or was this specific popup a side effect of something else in flight that session (e.g. the fall-through paste candidate mentioned in the source)?

History: none — first observed live 2026-07-16, cause not yet isolated.


### merge-store-part-auto-routing
**A default-addressed merge routes new fixture data to the part ALREADY CARRYING that fixture's content — you do not choose the part, the fixture's existing home does**
*when:* Before merging values into a multi-part cue without naming a part — the data lands in whichever part already holds that fixture, which is usually right and occasionally surprising


**Behaviour:** on a **default-addressed** (no explicit part) merge-store into a multi-part cue, MA3 routes each fixture's new data **to the part that already carries that fixture's content**. The part choice is made per fixture by existing residency, not by the command.

**Why this is mostly a gift.** Given that part numbers cannot be safely inferred from part names (`part-numbers-are-not-part-labels`), a default-addressed merge is the *safe* write into a multi-part cue: it cannot create a junk part and it preserves the show's part structure.

**Why it occasionally surprises.** Rows written this way can land somewhere the author did not picture, and then survive a later removal sweep aimed at a different part. That is exactly the benign residue noted in `cooked-recipe-rows-immune-to-store-remove` — raw cell rows that landed by auto-routing and outlived the `At Remove` pass, holding the same presets the recipes now cook (duplication, not conflict).

**Working rule:** merge by default address and then **census the parts afterwards** from an export-back; do not assume the part you had in mind is the part that received the data.

**Relation:** `part-numbers-are-not-part-labels` · `store-remove-attribute-scoped` · `cooked-recipe-rows-immune-to-store-remove` · `parts-per-century-emit-pattern-and-et-gate`.

History: none — observed 2026-08-26.


### off-on-overwrite-executor-default
**off_on_overwrite is the default executor behavior in MA3**
*when:* When reasoning about what happens if a running executor is re-triggered or overwritten, or when authoring executor behavior explicitly


`off_on_overwrite` is the **default executor behavior** in grandMA3 — i.e. absent an explicit override, an executor that gets overwritten while running will turn off then on with the new content, rather than crossfading or ignoring the overwrite.

History: none — stable since 2026-04-01.


### part-numbers-are-not-part-labels
**⛔ A part NAME like 'P8 QX40' is a ROLE LABEL, not a part number — real part numbers are unrelated, parts expose no No via the object tree, and addressing a missing part number under /Merge CREATES a junk part**
*when:* Before addressing a cue part by number from a name you read in an export or on the desk — 'P8' in a part name is a role label, and guessing the number under /Merge silently creates a junk part


**The trap.** The tour show's parts carry names in the shape `P1 …`, `P5 BEAMS`, `P8 QX40`. These are **role labels inherited from the originating programmer's convention** — a naming scheme, not an address. The part's **real number is unrelated** to the digit in its name.

**Addressing a part number that does not exist, under `/Merge`, CREATES it** — a junk empty part appears in the cue and stays. (Recovery: `Delete Part <n>` removes it; done live on a chorus cue, parts restored to their real set.)

**And you cannot look the number up from the object tree** — parts expose **no `No` property** there. So:

**⇒ PROBE BEFORE ADDRESSING.** Establish the real part set from an export-back (`export-plus-python-bulk-lane`) or by enumeration before writing to any part by number. Never derive an address from a name.

**Second-order consequence:** because parts cannot be reliably addressed by inference, a default-addressed merge is often the safer write — but that lane has its own routing behaviour, see `merge-store-part-auto-routing`.

**Relation:** `merge-store-part-auto-routing` · `cue-display-number-vs-no-addressing-gotcha` (the same display-vs-internal confusion one level up, at the cue) · `parts-per-century-emit-pattern-and-et-gate` (where the role-label convention comes from) · `recipe-part-property-surface-lua-dump`.

History: none — paid for with one junk part, 2026-08-26.


### parts-per-century-emit-pattern-and-et-gate
**Parts-per-century sequence architecture (Dave's standing shape) + mandatory ET.fromstring well-formedness gate on every emitter — song-c_emit.py is the template record**
*when:* Before building a new song's main sequence, or before writing/modifying any Python XML emitter that generates multi-part cues for import — the standing part-layout law and the mandatory well-formedness check every emitter must run before its output is trusted


**Architecture ruling (Dave):** main sequences use **PARTS PER CENTURY** — "clean cue parts for each century reads way better." Standing shape per cue: **part 0** (cue-named, carries fade, usually `SR=0`) + **century parts AS NEEDED** — P1 SPOTS / P2 WASHES / P3 PIX / P4 JDC / P5 BEAMS / P6 RIVALE / P7 PLINE / P8 QX40.

Confirmed live on the Seq 1510 (SONG_T) golden: census 20/19/17/17/7/6/6 parts across 42 cues, 140 parts total, 100 StandardRecipes.

**No-inheritance-of-fade law:** part-0's fade is COPIED explicitly onto every part — parts do not inherit part-0 fade automatically; it must be reapplied to every part on regen.

**SONG_A's mono-part kit emission is NOT the standing shape going forward.** SONG_B (seq 1110) and every remaining song build parts-per-century; the per-part Speed Scale natively solves composite-figure mixed gears (each part carries its own Speed Scale divide). Kit consequence: a parts-aware emitter is added ALONGSIDE the original mono-part `build_sequence` — the SONG_A regression must stay byte-exact.

**`song-c_emit.py` is the template record** for this pattern — the parts-per-century explosion in golden attribute order (see `part-attr-order-import-absorption-gotcha` for why attribute order matters) plus the ET gate below, banked as the reference emitter for every remaining song.

**Emitter safety law, paid for (Lint ≠ well-formedness):** the parts-explosion regex in `song-c_emit.py` matched a SELF-CLOSING part as an open tag and swallowed the next cue whole (Bridge cue 8 swallowed 8.1) — and lint stayed CLEAN throughout, because **lint does not check XML well-formedness.** Fix: **`ET.fromstring` gate is now mandatory in every emitter**, run on the emitted XML before it is trusted, not just a regex-based lint pass.

**Related hygiene rule from the same fix:** a swap-a-slot post-pass must replace WHOLE StandardRecipe lines (both `Preset=` AND `Values=`), not a first-reference-only substitution — a partial replace can leave a line internally inconsistent.

**Relation:** `part-attr-order-import-absorption-gotcha` for the sibling paid-for emitter lesson from the same build. `smith-packet-must-stage-multi-part-golden` for why a multi-part emitter's output needs a multi-part golden to certify against. `export-sequence-xml-schema` for the underlying Part/StandardRecipe schema this architecture is built from.


## PAID smith blocker, 2026-08-01 [0801-2cLD] — protective transforms must live in the SHARED emit path, not per-lane

**Caught pre-deploy: the aux emit lane had skipped the main lane's `SpeedScale`-on-Part insert.** Root cause: the protective transform (inserting `SpeedScale`) had been implemented per-lane rather than in a shared path both the main-sequence and aux-sequence emitters call through. **A per-lane assert only proves its own lane** — the main lane's tests passed because the main lane had the insert; they said nothing about the aux lane, which didn't. Fixed and re-certified PASS. **Standing rule: any protective transform that must apply to every emitted sequence belongs in the SHARED emit path**, not duplicated (and potentially forgotten) per lane.

**Absent SpeedScale is a DISTINCT failure shape from the wrong-position absorption gotcha this concept already documents.** Desk exports legitimately ELIDE `SpeedScale` at its default value, so an export-back diff against a desk export reads clean even when an authored file is missing it entirely. **Only a golden BYTE-SHAPE check catches the omission** in an authored file — a diff against a real export cannot, because the real export's own silence at default looks identical to the bug.

**Re-certifying a one-attribute fix: run the masked structural byte-diff against the golden, not just an attribute-index check.** The attribute-index check alone cannot confirm the fix touched nothing else. Example from the SONG_I aux re-certification: the only delta after the fix was 3 inserted `SpeedScale` tokens, +51 bytes — exactly the expected shape, confirmed only by the byte-diff.

## Census-script trap, 2026-08-01 [0801-2cLD] — the absorption counter false-positives on AUX sequences

**A parts-per-century absorption counter false-positives on AUX sequences**, whose single content part is cue-NAMED (e.g. `'[Full]'`), not `'P<n> '` like a main sequence's century parts. **Century-pattern absorption checks apply to MAIN sequences only** — scope the check explicitly, or it will report a perfectly clean aux sequence as absorbed.

## Scope-with-count discipline, 2026-08-01 [0801-2cLD]

**Self-caught miscount:** workup prose described SONG_I's ×2 gear as "16 sites," but the underlying artifact carries **18 LINES across 14 PARTS** — the prose had been counted off memory/summary rather than the artifact itself. Since Speed Scale is a **PER-PART** knob, PARTS is the load-bearing unit for any claim about it — **always state gear counts as PARTS *and* LINES**, never one alone.

**Mixed-gear cues split cleanly at CENTURY BOUNDARIES — but check the boundary, don't assume it.** SONG_I demonstrates why parts-per-century avoids the mixed-gear problem in practice: both of its per-population split figures (Intro Ramp `1922`, Chorus Ramp `1923`) split exactly on a century boundary — QX40/BEAMS at 270 BPM-equivalent vs Strike M/BEAMS at 135 — so each resulting part resolves to one single gear with zero part-splitting needed. A figure that instead split WITHIN one century would still force an awkward split; verify the boundary lines up before assuming parts-per-century has already solved a given figure's mixed gears for free.

## Composites are SEPARATED, not decomposed, plus the join method that executes it — 2026-08-05 [0805cLD]

**Dave's ruling, on SONG_L:** *"they mixed the fixture types in their phasers, we just
assign them on different cue parts."* {LD} puts several shapes in ONE preset because he
binds one object to a mixed population; our parts-per-century explosion already separates by
fixture family, so **a composite is never decomposed as a puzzle — it BECOMES one part per
century, each with its own bind.** This is what keeps the per-figure object count small: on
SONG_L, 5 objects cover 9 hashed figures across 23 bind sites (see
`tourshow-authoring-contract-v01`'s ingredient-reuse ruling, and
`tourshow-seq2210-song-l-build-record` for the worked example).

**The population→shape join is available in-file and cheap, with zero inference — the
standing method for every future composite.** Each figure's own subtree carries
`Preset/StandardRecipe/DependencyExport/Dependency/Group/SelectionData/Item` (the exact
fixture roster per population) alongside `Preset/PresetData/Phaser@ID` (the per-fixture
shape). **Join the roster against the shape and population→shape falls out directly** — never
infer it from ID prefixes or MAtricks shape. (A probe bug that skipped this method and
inferred from truncated ID prefixes instead produced a real inversion on SONG_L's `Verse
1/2` composite — see `probe-called-unreliable-is-not-evidence`.)


### release-family-ships-stock
**Stock Release color family (predefined_phaser.xml, pool 21) already ships 13+ named color+release presets**
*when:* Before building release presets from scratch — check whether MA's stock library already covers the needed color


`predefined_phaser.xml` (landed in pool 21 "Phaser" in this show file — see `tourshow-phaser-pool-identity`) contains a full Release color family, shipped stock: **Release White, Red, Orange, Yellow, FernGreen, Green, SeaGreen, Cyan, Lavender, Blue, Violet, Magenta, Pink** (13 named).

⚑ The source finding's list ends with an ellipsis after Pink — treat this as **at least 13, not confirmed exhaustive**; the census wasn't closed out to a hard count.

Dave confirmed live, in the phaser editor, that these are 2-step hard-value pairs (color value + release value baked together) — see `release-preset-design-doctrine` for the exact construction and why our design departs from it.

Practical read: Dave's release-preset "homework" was therefore partly already solved by the prior session's stock import (2026-07-15), before this session's design work even started.

History: none — inventoried 2026-07-16 from a same-session census of `predefined_phaser.xml`.


### release-mechanism-fundamentals
**Release = special function on any channel — falls back to the next claim (running cue, else fixture default) instead of forcing zero**
*when:* Before building any Release preset, bump executor, or TC-bump architecture — defines what Release actually does at the channel level


Dave's definition, the base mechanism everything else in this domain builds on: **Release is a special function assignable to ANY channel.** Instead of writing a zero value, it RELEASES the channel — the channel falls back to whatever else is claiming it: the running cue underneath if one exists, otherwise the fixture's default value.

This is the console mechanism that `release-preset-design-doctrine` (our preset-building pattern) and `tc-bump-button-architecture` (bumps exit via Release, not Off) both depend on. See `release-family-ships-stock` for confirmation that stock presets built on this mechanism already ship in pool 21.

History: none — mechanism defined 2026-07-16, first capture in the corpus.


### select-sequence-retargets-sheet
**`Select Sequence <n>` retargets the Sequence Sheet view to that sequence**
*when:* Before assuming the visible Sequence Sheet matches the sequence you're working on via CLI — the sheet stays pinned to Seq 1 Default until explicitly retargeted


**Verified live:** `Select Sequence 101` retargets the visible **Sequence Sheet** to Sequence 101 — before this call the sheet stayed pinned to **Sequence 1 Default** regardless of which sequence was being built via CLI/recipe work. Relevant any time a sheet view needs to follow a non-default sequence (e.g. the recipe build in `recipe-lane-end-to-end-verified`, which used Sequence 101).

History: none — confirmed live in one session, 2026-07-15, during the first recipe build.


### sequence-xml-ordered-header-law
**Sequence-XML children 1+2 MUST be OffCue then CueZero, or content cue 1 imports INTO OffCue**
*when:* Before hand-authoring or golden-deriving a sequence-XML file for import — check that the first two Cue children are OffCue and CueZero, in that order, before trusting the import


**A `<Sequence>` XML's first two `<Cue>` children must be `OffCue` and `CueZero`, in that order.** Seen live on a dialect test: a file missing them mapped its **first content cue INTO `OffCue`** on import instead of creating it as a normal numbered cue — the import still completed and reported success.

Practical consequence for the golden-derived build method (author a new sequence by cloning another song's cue headers): **verify the imported sequence's `OffCue` and `CueZero` are present and distinct from cue 1** before trusting the rest of the structure — a missing or misordered header pair corrupts silently into a wrong-looking but still "successful" import.

**Relation:** sits alongside `import-resolver-laws` as a second, independent import-time gotcha on the same sequence-XML dialect; see `export-sequence-xml-schema` for the general schema (`<Cue>` header shape, `OffCue`/`CueZero`'s `No="0"`/`No="1"` convention); `tourshow-seq1510-build-record` for the build this was caught on.

History: none — found live, 2026-07-28, during the Seq 1510 SONG_T skeleton import.


### store-remove-attribute-scoped
**Store /Remove is ATTRIBUTE-scoped: it removes exactly the SELECTED fixtures' ACTIVE attributes from the addressed cue/part — select, activate, then Store /Remove /nc**
*when:* Before using Store /Remove — its scope is the intersection of your selection and your ACTIVE attributes, not the whole cue and not the whole fixture; and it does nothing at all to recipe-cooked rows


**Scope, exactly:** `Store /Remove` removes **the selected fixtures' ACTIVE attributes** from the addressed cue/part. Three things gate it — the fixture **selection**, the **active** attribute set in the programmer, and the **addressed** cue/part. Anything outside that intersection is untouched.

**Scratch-proven flow:**

```
Select the fixtures
Activate the attributes to be removed
Store Cue <n> Part <n> /Remove /nc
```

Skipping the *activate* step is the common failure: with nothing active the command has no attribute scope and removes nothing while reporting success.

**⛔ It cannot touch recipe-cooked rows.** If the values in the cue are recipe output, this lane is a silent no-op regardless of selection and activation — see `cooked-recipe-rows-immune-to-store-remove` for the repoint lane that does work.

**Companion lane for raw rows:** `At Remove` with `/Merge` default-store also kills raw stored values (scratch-proven the same session).

**Relation:** `cooked-recipe-rows-immune-to-store-remove` · `merge-store-part-auto-routing` · `store-default-values-keyword` · `store-recall-recipe-toggle-rules`.

History: none — scratch-proven 2026-08-26.


### tourshow-cue-century-review-sheet-doctrine
**The cue×century review sheet is the TASTE verification layer machine checks cannot provide — and dropping it once the line got fast is what let the wash defect through**
*when:* Before shipping any song without producing its cue x century review sheet, or when tempted to skip a review step because the build line is running fast — this is a named, mandatory gate, not an optional nicety


**⭐ NEW DELIVERABLE, RULED (Dave) — PER-SONG CUE-TO-CUE SHEET, CENTURIES AS COLUMNS.** One spreadsheet per song: rows = cues in order, columns = the century parts (P1 SPOTS · P2 WASHES · P4 JDC · P5 BEAMS · P6 RIVALE · P7 PLINE · P8 QX40), cells = what that fixture family does at that cue. Purpose, in Dave's words: *"see what fixtures do, what's the next thing that they do, real easy, all in one spot"* and *"it'll be really easy for me to pull out anything that looks anomalous, or that is gonna look weird on stage — I'll know immediately if I see it."*

## Why it matters: the console shows the data, not the SHAPE

Dave: *"if I see them together, it's kinda hard to read it the way the MA has it, but when we lay it on a spreadsheet, I can see it right away."* **MA3's own sheet view makes this hard to read; the console shows the data, it does not show the shape.** The grid is the shape.

**This sheet is a different verification CLASS from everything else in the toolkit.** Census/lint/smith prove COUNTS and DIALECT — they cannot prove a look makes sense. The grid puts the whole song in front of Dave's eye so **TASTE can verify what mechanics cannot.** Exactly the idea-file design/programmer boundary (`idea-file-design-programmer-boundary-doctrine`) applied to review: the machine certifies structure, the designer certifies sense. **It is also the instrument that would have caught the missing-washes defect** — an empty P2 WASHES column against populated neighbours is unmissable on a grid and invisible in a passing census.

**Build note (cheap — the machinery already exists):** every shipped song's export-back census already parses cue -> part -> SR binds; the grid is a pivot of data already being extracted, emitted as xlsx. No new console contact needed for songs already on disk.

## ⛔⛔ The dropped-practice lesson, second instance of the same failure shape

**This review sheet was a practice we dropped once the build line got fast, and that is exactly what let the wash defect through.** Dave: *"We were doing that sheet, and we just started flowing... we get a couple of good ones, hit the turbo boost, and then it bit us."* Ruling: **get back to the basics even though the line is faster** — speed is precisely what makes the basic step feel skippable, and skipping it is what costs.

**Evidence, straight off the staging folders — the curve is unmistakable:** SONG_B (song 2) = **FOUR** sheet revisions (`SOURCE_PHASER_SHEET` v0.1-v0.4) · SONG_C (song 3) = **ONE** (v0.1; its v0.2 sat on the owed-docs list across three consecutive state files and never came back) · SONG_D, SONG_E, SONG_G, SONG_H, SONG_I, SONG_J = **ZERO**. The practice died exactly where the line started shipping whole songs per session. **A carried-forever owed-doc line is the visible fossil of a practice dying** — treat any doc that survives three rehydrations unactioned as a dropped practice, not a backlog item.

**Standing failure mode, now named — "pipeline momentum overrides gate discipline."** Two instances: the SONG_B TC cutover folded into the first import chain (see `tc-cutover-last-and-delete-eats-events-doctrine`, which names it), and this review-sheet drop. Both cost real rework. **This is no longer an incident shape — it is a standing failure mode of a line that works well: the better the line runs, the more expendable its slowest gate looks.**

**The absence-is-invisible corollary:** running two full songs with census + smith + export-back and never producing the review sheet triggered no failure of any kind — no lint fails, no census disagrees, nothing errors. **The absence of a step you have stopped doing is invisible.** That is why it needs to be a NAMED gate in the runbook rather than a habit, and why a dropped practice can only be caught by an inventory of what a build SHOULD emit, never by checking whether the build passed.

## Delivered — first instance (2026-08-03)

**`SONG-J_RECIPES` 1_SOURCE / 2_cLD / 3_MELD** (`generated/staging_song-j_0801/recipe_sheets/`, with a 4-file generator kit). **Pass 1** = the two sides separately, one row per StandardRecipe line. **Pass 2** = Dave's format exactly — alternating {LD}/cLD rows per CUE #, a (Group, Value, MX) triplet per century across P1..P8. **The generator is song-agnostic; the next song is a path change.**

**Join key, proven safe:** join on the **cue NUMBER**, never on position — SONG_J is 46 cues both sides with identical `No` AND `Name`, nameless cue 28 included, and the console renders `7.1` as `'7.001'` on BOTH files so the stripped string matches without normalisation.

**⭐ PREWORK RULING PROPOSED, awaiting Dave's ratify — the recipe-sheet generator serves THREE modes, not one:**
1. **PREWORK** = pass-1 {LD} book + CROSSWALK tab, generated before any build — strictly more than the existing `crosswalk_prep` markdown (per-line rather than summarised, target and century resolved per line so unmapped groups show as blanks, MX signature per POPULATION, figure and colour inventory).
2. **POST-BUILD GATE** = the meld + RECONCILE + MX CROSSWALK (see `reconciliation-identity-per-song-verification-method`).
3. **THIRD MODE, new as of 08-03** = re-pull and re-meld AFTER Dave has worked the file at the desk — the only artifact that shows what he changed and what is left.

Same generator serves all three; only the input paths move. **This 3-mode framework is a proposal, not yet Dave-ratified** — do not treat it as settled process until he confirms.

## Tooling gotcha paid on the generator (2026-08-03)

**`openpyxl` writes formulas with NO cached value** — a rebuilt workbook reads back **blank for every computed cell**, and a formula-ERROR check still reports 0 errors, because blank is not an error. Caught only by verifying computed VALUES against the Python source of truth (same shape as "a clean Import proves nothing below the structure layer"). **Fix adopted:** the build script now runs recalc itself and asserts on the result — never leave recalc to a separate manual step.

**Note — the wash defect itself is an open Dave-owned action item (some songs' wash content landed on a beam target and was then hand-deleted as an apparent duplicate), not yet filed as its own concept: Dave explicitly said not to investigate it this session. It is the motivating incident for this doctrine, not a fact this doctrine's body asserts.**

**Relation:** `reconciliation-identity-per-song-verification-method` (the sibling crosswalk-completeness sheet/check — that one verifies counts-and-causes, this one verifies taste-and-shape). `tourshow-recipe-line-redundancy-taxonomy` (the "delete-thinking-it's-a-duplicate" failure mode directly adjacent to the wash-defect shape). `tc-cutover-last-and-delete-eats-events-doctrine` (the first instance of the "pipeline momentum overrides gate discipline" failure mode this run names as a pattern).


## SHOW FILE & IMPORT LANE

### export-context-relativity ⚠ VERIFY
**Export may depend on which CLI prompt you're at (LivePatch vs root) — one data point, now uncertain after the dialog-suspend-resume finding**
*when:* Before running Export from inside a pool-object context (e.g. LivePatch) rather than the root prompt — check the prompt path first, and don't treat this as fully confirmed yet


**Observed once:** from the **LivePatch** CLI prompt, `Export Layout 2` failed silently — no file was produced. The same command worked from the **root** prompt (recorded as `Admin[Fixture]>`). Standing practical guidance from this observation: **run `Export` from the root prompt**, or more generally, check which prompt/context is current before targeting a pool object with `Export`.

**[VERIFY] — this needs re-testing in isolation.** The same session later found that a blocking dialog suspends and resumes a `;`-batched line rather than killing it (see `dialog-suspend-resume-batched-lines`). The one clean data point behind this context-relativity claim (the file missing when run from the LivePatch prompt, present when run from root) may be explained by that dialog-timing behavior instead of true prompt-context sensitivity — a dialog could have been in play around that test without being attributed correctly at the time.

**Clears with:** re-run `Export Layout <n>` (or `Export Patch`) from a LivePatch prompt as a standalone line — no batching, no dialogs in flight — and confirm whether it still fails silently. If it succeeds in isolation, the original finding was a dialog-timing artifact, not context-relativity.

History: none — single observation 2026-07-14, flagged [VERIFY] the same session once the dialog-suspend-resume mechanism came to light.


### export-plus-python-bulk-lane
**The standing heavy-audit lane: gated full export → Mac-side python matcher → COUNTS ONLY back into context — never bulk XML through the wire or the window**
*when:* Before any show-wide census, master scan, reference sweep or before/after diff — this is the lane, and it is cheaper and safer than every wire-side alternative


**The pattern, in three moves:**

1. **Gated full export.** `Export Sequence 1 Thru "…"` (Tier-2 gated) fans the whole live pool out to disk — one file per sequence, name-derived (`export-sequence-writes-per-name-files`) — then **disk-verify the batch** by mtime delta (`save-disk-verify-mtime-delta`).
2. **Mac-side python matcher.** Parse the batch locally. This is where the real analysis happens: master-instance scans, cell-geometry offender hunts, before/after diffs, reference resolution.
3. **Counts only into context.** The matcher prints totals, per-song rollups and short offender lists. Bodies never enter the window.

**Why it wins.** It is immune to the round-trip's scale limits (`split-and-guard-per-sequence-walk-law`), immune to the 1800-char transport cap, immune to console recook storms (`wire-timeout-vs-console-busy`), and it leaves a **repeatable artifact on disk** — every venue adaptation this leg re-ran an earlier matcher rather than rebuilding one.

**Attested runs:** the 190-file {FESTIVAL} export and master scan · the QX40 master blast-radius recompile (70 rows / 20 sequences) · the post-surgery rescan (master-kind rows 294 → 240, QX40 dotless 69 → 15) · the cell-geometry offender sweeps at {FESTIVAL} (18 lines), {FESTIVAL} (19) and {FESTIVAL} · every "still-broken = 0" verification of the leg.

**Scripts banked (in their staging folders):** `schema_probe.py`, `master_scan.py`, `master_scan2.py`, `mark_cell_check.py`, `phaser_recheck.py`, `ltc_confirm.py`.

**Relation:** `split-and-guard-per-sequence-walk-law` (when the wire *can* do it) · `export-sequence-writes-per-name-files` · `tourshow-context-health-never-read-bulk-xml-rule` (why counts only) · `many-lines-ride-macros-not-lua` (the write-side counterpart).

History: none — consolidated from the practice that ran the whole EU tour leg, 2026-08-26 → 2026-08-28.


### import-file-argument-must-be-quoted
**⛔ Import with an UNQUOTED /File filename SILENTLY NO-OPS — the CLI answers nothing and the target stays empty; build the quotes with string.char(34) inside Cmd()**
*when:* Before any Import … /File call from a macro, generated Lua or the MCP bridge — an unquoted filename produces no error and no import, and only a census of the target catches it


**Broken (silent no-op):**
```
Import Sequence 5 /File cld_resolume_seq5.xml /nc
```
The command line **answered nothing** and the sequence stayed an empty shell.

**Working — quotes built inside the Lua payload:**
```lua
local q = string.char(34)
Cmd('Import Sequence 5 /File '..q..'cld_resolume_seq5.xml'..q..' /nc')   -- → "OK"
```

`string.char(34)` is the workaround for the transport's refusal of raw `"` characters in a command string (`saveshow-discipline-and-mcp-tier`); the single-quote-inside-a-long-bracket form is the alternative where the payload allows it.

**Lane note:** the **delete-then-import** sequence is the proven take-2 pattern when re-importing over an existing object.

**⇒ Never trust the clean echo.** The tour leg produced three independent members of this family — this one, the phantom checkpoint (`saveshow-enumerate-headless-cancel-class`), and the closed-range preset export (`preset-range-export-open-ended-only`). The common defence is the same: **census the target after every write**, and treat the echo as decoration.

**Attested working imports using the quoted form:** Seq 5 Resolume (21 cues, SR=40 exact) · the TC macro pair `cld_tc_internal.xml` / `cld_tc_default.xml` · the venue kit macros `cld_mx_1cell.xml` / `cld_mx_restore.xml` at {FESTIVAL}.

**Relation:** `saveshow-discipline-and-mcp-tier` (the quoting family) · `xml-file-side-authoring-import-lane-proven` · `import-resolver-laws` (what happens *after* a file successfully imports) · `plugin-import-verify-name-match`.

History: none — caught by census on first use, 2026-08-08; the quoted form carried every import of the rest of the leg.


### save-disk-verify-mtime-delta
**⛔ RITUAL LAW: a checkpoint is not a checkpoint until the .show file's mtime AND size move — and MA3 stamps ~9h behind shell TZ, so verify by DELTA against sibling files, never by wall clock**
*when:* After EVERY save, checkpoint or seal — before telling anyone the show is safe, before any surgery that relies on a rollback point, and before reading a .show file's timestamp as a wall clock


**The law, born out of the phantom-checkpoint reckoning** (`saveshow-enumerate-headless-cancel-class`): **the command echo is not the save. The file on disk is the save.**

## The check

1. List the shows directory: `gma3_2.4.2/shared/shows/`.
2. The target `.show` must be the **newest** file there **and** its **mtime and size must both have moved** since the previous listing. A size-only match with an unchanged mtime, or the reverse, is a failed save.
3. **Read the DELTA, not the clock.** MA3's stamps run roughly **nine hours behind the shell timezone** — the absolute time on a freshly written file will look wrong. Compare it against its *sibling* files in the same directory; the newest-relative position is the signal.

## Receipts across the leg

Every seal on the EU tour was taken this way and named in the log: `v1.4` (128.9 MB) · `v1.42` · `v1.43` · `v1.44` · `EXAMPLE_SHOW {FESTIVAL} .36` · `EXAMPLE_SHOW {FESTIVAL} .51` (125 MB) → `.52` → `.53` (125.8 MB, 02:01 skew stamp) · `EXAMPLE_SHOW use fOR bASE v2.2` (129 MB) · `EXAMPLE_SHOW {FESTIVAL} .24` · `EXAMPLE_SHOW {FESTIVAL} .22` · `EXAMPLE_SHOW {FESTIVAL} {STAGE} .22`. Not one of these was reported as sealed on an echo alone.

**Naming pattern (Dave's ruling, [0819-5]):** the file lineage gets a version pattern and cLD's saves extend it — `v1.4x` on the base file, `.NN` on each venue fork. Dave's own hand-saves interleave cleanly with the pattern; per-fork lineages supersede the base pattern inside that fork.

**The habit is also the insurance.** Twice in one day the export-and-verify habit was what made a rollback survivable: a hash-diff proved a reloaded older file already carried the road's colour tweaks (all 81 presets byte-identical), so nothing had to be reconstructed. See `color-consolidation-crowning`.

**Relation:** `saveshow-enumerate-headless-cancel-class` (why the ritual exists) · `saveshow-discipline-and-mcp-tier` (the shows-dir path and the reachability caveat for the tool that lists it) · `operators-eyes-are-the-census-of-record`.

History: none — ruled and immediately made standing, 2026-08-19; applied on every subsequent seal through the end of the EU leg.


### saveshow-discipline-and-mcp-tier
**SaveShow discipline: always /NoConfirmation, now Tier 2 in the MCP; LoadShow stays denied; deny-list is word-boundary; send_lua needs single-quote-in-long-bracket quoting**
*when:* Before issuing a SaveShow command via MCP/generated Lua, or when reasoning about what the MCP's Tier 2 permission level allows


**Dave's save-before-experimenting rule paid for itself twice:** `SaveShow "name" /NoConfirmation` before the crash-inducing experiments (see `gpdf-console-killer`) meant both crashes cost **zero** — clean revert to `cLD_BENCH_WORK`.

- **`SaveShow` was reclassified deny→Tier 2 in the MCP (2026-07-04)** so cLD can checkpoint autonomously. **`LoadShow` stays denied.**
- **⚠️ Bare `SaveShow` (without the flag) opens a confirm dialog** → returns **"User Canceled Command"** when run unattended. (The 2.4 manual says same-name saves overwrite; the live-observed unattended behavior is the dialog — trust the live lesson for MCP work.)
- **⚠️ Second, distinct gotcha (live-verified, attended CLI, 2.4.2.2, 2026-07-10):** `SaveShow /NoConfirmation` **with the flag present but NO show name** gets its `/NoConfirmation` parsed as the **FILENAME argument** → opens a **"Change show file name?"** dialog (the console echoed the flag back, quoted, as if it were the typed name). **The MCP path was never bitten by this because it always passed an explicit name.**
- **Always use the full form, name AND flag together: `SaveShow "name" /NoConfirmation`.** Never omit either half.
- **Documented syntax (2.4 manual):** `SaveShow ("Show_Name") (/Option)`; shortcut `Sa`; option keywords `/Enumerate` and `/Path`.
- **MCP deny-list matching was fixed to word-boundary** (it was previously substring-matching — "Reset" was incorrectly blocking every command containing "Preset").

For versioned/commit-style saves see `saveshow-enumerate-versioning`.

**Standing rule (Dave, dictated, 2026-07-17): checkpoint immediately before any XML import.** Always fire a `SaveShow .../Enumerate` checkpoint right before importing any handwritten/authored XML into the show (`Import Preset`, `Import Layout`, etc.) — cheap insurance against a malformed import corrupting the live show. This is now standard bracketing around the file-side authoring lane (see `xml-file-side-authoring-import-lane-proven`): checkpoint → import → verify, never import cold.

**Filesystem verify lane (live-confirmed 2026-07-17, [0717-2cLD], first Tier-2 write over MCP):** `SaveShow /Enumerate` on `cLD_SANDBOX` incremented v0.16→v0.17, `confirm_gate` flow worked exactly as designed. The file-side readback location is `~/MALightingTechnology/gma3_2.4.2/shared/shows/` (a **version-scoped** directory — NOT `gma3_library/shows`); the newest `.show` file's mtime is the readback signal for "did the save land."

**⚠ `send_lua` transport quoting (paid-for live, 2026-07-21, 07-21 song-g-infra):** the `send_lua` MCP transport forbids a raw `"` character in the command string, so quoting a show name the normal CLI way breaks the channel. Worse: an **UNQUOTED dotted show name silently TRUNCATES AT THE DOT** — `Cmd('SaveShow cLD_SANDBOX_v0.21 /NoConfirmation')` saved junk `cLD_SANDBOX_v.show` on disk and still returned a **FALSE "OK."** **Verified fix:** quote the show name with **single quotes inside a Lua long-bracket**: `Cmd([[SaveShow 'cLD_SANDBOX_v0.21' /NoConfirmation]])` — this landed the correct file. Gate flow: send (Tier-2 block → returns `wrapped_cmd`) → `confirm_gate(that exact string, approve=true)` → resend within TTL. **Always quote this way, and always verify the actual `.show` file on disk afterward — never trust the "OK" echo**, which lied outright in the truncation case.

**Shows-dir is reachable by MCP filesystem tools, NOT by `device_bash` (2026-07-21):** the shows directory (`~/MALightingTechnology/gma3_2.4.2/shared/shows`) is readable via `Desktop_Commander`/`Filesystem` MCP tools but is **not** a mounted project folder reachable by `device_bash` — use the MCP filesystem tools for the SaveShow verify lane (newest/named `.show` file), not a shell command. **⚑ Narrowed 2026-08-05 [0805cLD]: this does NOT hold for `Filesystem` as currently scoped** — on that session's setup, `Filesystem` was scoped to `/Users/{USER}/My Drive` and `/Users/{USER}/dev` only, and the shows dir returned "Access denied - path outside allowed directories." `Desktop_Commander` was untested that specific run (though it demonstrably reaches other MALightingTechnology paths elsewhere in the corpus, e.g. `gma3_library` — see `xml-file-side-authoring-import-lane-proven`). **Treat `Filesystem` as NOT reaching the shows dir on a `My Drive`+`dev`-scoped setup; confirm `Desktop_Commander` before relying on it for this specific verify lane.**

**Lua has no reliable programmatic filename getter:** `GetShowFileName()` does **NOT exist** in 2.4.2.2 Lua — it's a nil global, not a function that errors gracefully. `Root().ShowData.Name` returns the literal string `"ShowData"` — useless for reading the actual filename. Filesystem mtime (above) is the only confirmed readback path for SaveShow's result.

## `send_lua` rejects a semicolon even inside a string literal, 2026-08-05 [0805cLD]

**Transport gotcha, same family as the quoting/truncation issues above.** A census payload
using `table.concat(binds, ' ; ')` was blocked pre-send ("Lua expression contains forbidden
semicolon"). **The guard is a plain substring scan, not a parse**, so a `;` anywhere in the
command string — including inside a separator or any quoted text — kills the call before it
reaches the console. **Use another separator** (not `;`) when building any `send_lua` payload
that concatenates multiple values.

History: was `status: verify` carrying the unconfirmed "description = commit" CLI-syntax question; split out 2026-07-04 into `saveshow-enumerate-versioning` after the 2.4 manual showed there is NO description option on SaveShow — the documented versioning lane is `/Enumerate`. Core rules here are live-verified; flipped to `active`. Refined 2026-07-04→2026-07-10: a second attended-CLI gotcha found live (bare `/NoConfirmation` with no name gets parsed as the filename) — the rule now explicitly requires both a quoted name and the flag together, not just "append /NoConfirmation." Extended 2026-07-17: Dave's standing pre-import-checkpoint rule folded in (paraphrased per house dictation rule), proven in the same session that first exercised the XML authoring/import lane. Extended 2026-07-17 (parallel capture): added the filesystem verify lane (version-scoped shows dir, mtime readback) and the `GetShowFileName()`/`Root().ShowData.Name` dead-end, both from the first live Tier-2 MCP write. Extended 2026-07-21 (07-21 song-g-infra): added the `send_lua`-transport single-quote-in-long-bracket fix for dotted show names (unquoted dotted names silently truncate at the dot and still return a false OK) and the shows-dir MCP-vs-device_bash access distinction.

**[0805-2cLD] EXTENSION — second send_lua transport constraint:** expressions >1800 chars are refused ("transport-unsafe") — split batch loops into sub-1800-char chunks.

History: extended 2026-08-05 [0805-2cLD] — send_lua transport cap: >1800-char expressions refused; split batch loops.


## EU tour leg attestation, 2026-08 — and one conflict to resolve on disk, not from memory

- **The 1800-char cap held all leg.** Batch writes were chunked or shipped as macro artifacts (`many-lines-ride-macros-not-lua`).
- **⚠ Conflict with the bare-`SaveShow` warning above.** This file records (2026-07-04, sandbox) that *bare* `SaveShow` pops a confirm dialog unattended. On the tour file at 2.4.2.2 the **bare in-place save WORKED and was disk-verified**, while **`/Enumerate` was the form that silently died** (`saveshow-enumerate-headless-cancel-class`). Both observations are real; the deciding factor is not established. **Do not resolve this from memory — fire the save, then verify the file on disk** (`save-disk-verify-mtime-delta`). Disk truth outranks both rules.
- **`LoadShow` stays denied on the bridge** and is a desk-typed lane when the Backup UI fails — form banked at `loadshow-cli-when-menu-dead`.

History: extended 2026-08-28 (librarian, tour leg) — tour attestation of the transport cap plus the bare-vs-/Enumerate conflict flag.


### saveshow-enumerate-headless-cancel-class
**⛔ SaveShow /Enumerate is a SILENT NO-OP headless — every dialog-variant save cancels unattended ('User Canceled Command'); the only working lanes are bare SaveShow and SaveShow "name" /nc**
*when:* Before firing ANY checkpoint from a script/macro/MCP call, and immediately when a rollback discovers the newest .show on disk is hours old — /Enumerate and the other dialog-variant saves return OK and write nothing


**⛔ The paid-for discovery.** On 2026-08-19 a rollback found the newest `.show` on disk was **nine hours old**. Every checkpoint fired that day — and plausibly the "clean checkpoint lane" banked back at [0806] — was **phantom**. The commands echoed OK. Nothing reached the disk.

**Cause:** `SaveShow /Enumerate` (and the save-as *dialog* variants generally) opens a confirmation/naming dialog. Run headless — from a macro, from generated Lua, over the MCP — nothing answers it, so the console resolves it as **`"User Canceled Command"`** and the save never happens. The command channel still reports success upstream.

## The two working lanes (disk-verified the same session)

| Form | Behaviour | Proof |
|---|---|---|
| `SaveShow` (bare, in-place) | ✅ writes | `v1.1` mtime **and** size moved |
| `SaveShow "name" /nc` (save-as) | ✅ writes | created `EXAMPLE_SHOW use fOR bASE v1.4.show`, 128.9 MB, newest on disk |
| `SaveShow ... /Enumerate` | ❌ silent no-op headless | nine hours of phantom checkpoints |
| save-as without `/nc` | ❌ `"User Canceled Command"` | observed directly |

**Note the collision with the older rule.** `saveshow-discipline-and-mcp-tier` warns that *bare* `SaveShow` pops a confirm dialog when run unattended — that was the 2026-07-04 observation on the sandbox. On the tour file at 2.4.2.2 the bare in-place save **worked and was disk-verified**, while `/Enumerate` was the form that died. Do not resolve this from memory: **fire the save, then verify the file on disk** (`save-disk-verify-mtime-delta`). Disk truth outranks both rules.

**Why it survived so long undetected:** the rollback that exposed it only worked because *Dave's own hand-saves* (v1.1–v1.3) existed. Nothing cLD wrote that day was on disk. Clean echoes are not evidence — `never-trust-clean-echo` in its most expensive form to date.

**Supersedes in practice:** the [0806] "clean checkpoint lane" note, and any assumption that `/Enumerate` versioning (see `saveshow-enumerate-versioning`) is available to an unattended caller. `/Enumerate`'s *attended*-CLI increment behaviour is unchallenged by this — the finding is specifically that it does not survive the headless channel.

**Relation:** `save-disk-verify-mtime-delta` (the ritual this forced) · `saveshow-discipline-and-mcp-tier` (the quoting/flag rules that still apply to the working lanes) · `saveshow-enumerate-versioning` (attended behaviour) · `operators-eyes-are-the-census-of-record` (how it was caught).

History: none — discovered, root-caused and both working lanes disk-proven in one session, 2026-08-19.


### saveshow-enumerate-versioning ⚠ VERIFY
**Versioned saves: SaveShow /Enumerate is live-verified (increments a trailing version number, e.g. v0.1→v0.2) — but that differs from the manual's documented 3-digit-count behavior; description-triggers-numbering remains unverified**
*when:* When you want commit-style versioned checkpoint saves from the CLI/MCP, or before relying on Dave's description-as-commit workflow, or before assuming /Enumerate always appends a 3-digit counter


**Documented (2.4 manual, not yet run live):**
- `SaveShow "Show_Name" /Enumerate` (or bare `SaveShow /Enumerate`) appends a **three-digit count** to the show file name — the CLI versioning mechanism. Shortcut: `/En`.
- **⚠️ 31-character limit gotcha:** if name + enumeration exceeds 31 characters, the excess characters of the NAME are cut and replaced by the number. Keep checkpoint-show names short (`cLD_SANDBOX` = 11 chars, safe).
- There is **NO description/note option keyword on SaveShow** in 2.4 — only `/Enumerate` and `/Path`. A save "description" exists in the save-dialog UI, not the CLI.

**Live-verified 2026-07-14 (attended CLI, 2.4.2.2):** `SaveShow "cLD_SANDBOX_v0.1" /Enumerate` → saved as **`cLD_SANDBOX_v0.2`**. **No confirm dialog appeared.** This confirms `/Enumerate` works live over the wire — but the *observed* behavior is **not** the manual's documented "appends a three-digit count": here, `/Enumerate` **incremented an existing trailing version number already in the name** (`v0.1` → `v0.2`) rather than appending a separate `_001`-style counter. Both behaviors may be real, gated by whether the name already ends in a recognizable version-like suffix — this trigger condition is itself unconfirmed; treat the manual's 3-digit-count description as applying only to names *without* a trailing version pattern until tested.

**Further reproduced, same day, evening session (2026-07-14):** the trailing-version increment kept firing consistently across an entire session's checkpoint chain — `v0.3→v0.4→v0.5→v0.6`, logged in-session as "increment behavior now 4-for-4", continuing on to `v0.7` and `v0.8` per that session's wrap. This still only demonstrates the increment behavior on an already-version-suffixed name — the bare-name / 3-digit-count question below remains untested.

**Further reproduced, 2026-07-17:** increment behavior logged as **"now 6-for-6"**, `v0.15→v0.16`. Still only the version-suffixed-name case; the bare-name / 3-digit-count question and the description-as-commit premise remain untested.

**Unverified (what keeps this at `verify`):**
- **Which trigger governs which behavior:** does a version-suffixed name (`..._v0.1`) always get incremented while a bare name (`cLD_SANDBOX`, no suffix) gets a 3-digit count appended instead? Not yet tested against a bare name on 2.4.2.2.
- Dave's observed behavior: MA3 auto-numerates the show file **when the save description changes** (description = commit message). Presumably the UI dialog's description field interacts with the same enumeration mechanism — unconfirmed, and not touched by the 2026-07-14 test (which used the CLI form, not the save-dialog description field).

**Clears with:** run `SaveShow /Enumerate /NoConfirmation` on a **bare, non-version-suffixed** name (e.g. `cLD_SANDBOX` with no `_vX.Y`) and observe whether it gets a 3-digit count instead of an increment; separately, change the description in the save dialog and observe whether the number bumps without `/Enumerate`.

**Further reproduced, 2026-07-17 session:** checkpoint chain continued `v0.16 → v0.17` (first Tier-2 MCP write landed) `→ v0.18` (checkpoint taken under the new pre-XML-import standing rule, see `saveshow-discipline-and-mcp-tier`) — increment behavior now **8-for-8** across the full run of checkpoints logged so far. Still only exercises version-suffixed names; the bare-name / 3-digit-count question remains untested.

History: split from `saveshow-discipline-and-mcp-tier` 2026-07-04 (atomicity: the proven save-discipline rule was being held at `verify` by this one open question). Updated 2026-07-14: `/Enumerate` confirmed live-working (no confirm dialog), but revealed a version-suffix-increment behavior not described by the manual's 3-digit-count language — kept at `status: verify` since the exact trigger rule and the description-as-commit premise both remain open. Updated again 2026-07-14 (evening session): the increment behavior reproduced across a full v0.3→v0.8 checkpoint chain in a single session, consistent with the earlier v0.1→v0.2 finding; the two open questions above are untouched by this and status stays `verify`. Updated 2026-07-17: further corroborated, v0.15→v0.16, logged "6-for-6" — same open questions remain, status stays `verify`. Updated 2026-07-17: chain continued v0.16→v0.18 (6-for-6 → 8-for-8), still only on version-suffixed names; status unchanged.


## ⛔ SCOPE COLLAPSE, 2026-08-19 (EU tour leg) — /Enumerate DOES NOT SURVIVE THE HEADLESS CHANNEL

Everything above describes **attended CLI** behaviour and stands as such. On the tour file, run **unattended** — from a macro, from generated Lua, over the bridge — **`SaveShow /Enumerate` is a SILENT NO-OP**: it opens a dialog nothing answers, resolves as `"User Canceled Command"`, and reports success upstream. A full day of checkpoints was phantom; the newest `.show` on disk was nine hours old.

**⇒ Do not use `/Enumerate` for unattended checkpointing.** The working headless lanes are **bare `SaveShow`** (in-place) and **`SaveShow "name" /nc`** (save-as), both disk-verified. Full account and receipts: **`saveshow-enumerate-headless-cancel-class`**; the ritual it forced: **`save-disk-verify-mtime-delta`**.

The open questions above (bare-name vs version-suffixed trigger, description-as-commit) are unaffected and still open — they are attended-lane questions. Status stays `verify` for that reason.

History: extended 2026-08-19 — the headless scope collapse found on tour; see `saveshow-enumerate-headless-cancel-class`.


### tourshow-context-health-never-read-bulk-xml-rule
**Never Read a {LD} or export-back XML file into context — bulk analysis runs through committed, re-runnable scripts that print short summaries; sessions die from reading, not from working**
*when:* Before reading any {LD} source export or a cLD export-back XML file directly into a session's context — these run 6-17 MB each; use a committed script instead and let it print a short summary


**Context-health rule, now written into the standing lock/run plan and load-bearing: never `Read` a {LD} or export-back XML file into context** — these files run **6-17 MB each**. Every 08-03 finding in this corpus instead came from **committed scripts printing <=30 summary lines**, with full detail routed to a sheet on disk rather than into the conversation.

**All bulk analysis is a committed, re-runnable script** (kept under `recipe_sheets/` or equivalent), run via a process-launching tool rather than read directly. **One state file + one plan file is what a fresh session needs to read** to pick up where the last one left off — not the underlying XML.

**Findings hit `INBOX.md` as they happen, not only at wrap** — a HELD session that never formally wraps still keeps its findings this way, since capture is decoupled from the wrap event.

**The standing reason: sessions die from reading, not from working.** A single large-file `Read` can burn the context budget a whole song's worth of mechanical work would otherwise fit inside.

**Relation:** `low-credit-cli-mcp-first-authoring-doctrine` (a related context-economy doctrine for MCP/CLI authoring). `tourshow-songbuild-kit-and-runbook` (the committed-script kit this rule assumes exists and gets extended, not replaced by ad-hoc reads).


### tourshow-showfile-architecture
**{TOUR} show-file model — monolithic file, macro-order setlist, manual TC-arming trigger per song**
*when:* Before building or reasoning about the {TOUR} show file's macro/executor structure, or before exporting a multi-song QCaller sheet


Dave's model — **treat as ground truth**:

- The show file is **monolithic**; it never gets cut per set. **Setlist = macro call order.**
- A song's macro is a **manual trigger** Dave fires in the groove between songs: it loads the song's page and **arms TC listening for that song's window**. TC runs continuously throughout the show.
- **No end-of-track chaining** → any song can follow any song; set-length variants are just shorter call lists (near-zero compile cost — no re-linking needed).
- **Multi-song QCaller export should mirror this:** one file = one show = calls in order, per-song TC offsets.

This model directly informs the executor model in `tourshow-tour-identity` (one busk page + one page per song; one TC-fired master executor per song).

**{FESTIVAL} predecessor evidence (2026-07-06, strings-verified on {LD}'s file):** {LD}'s per-song architecture used a **rhythm bump layer** — e.g. Kick 1 (SONG_H/SONG_B/SONG_L/SONG_J/SONG_E×2/SONG_C), Snare 1 (SONG_A/SONG_N/SONG_D/Sattelites[sic]/SONG_I/SONG_K), Clap/Jersey Clap, plus `"Intro 1/1 (Kicks In)"`, bare-title song sequences, and SPEEDMASTER×9. **Timecode strings are trace-level only ⇒ likely manually bumped, not TC-run (interpretation).**
**⛔ DISPROVEN 2026-07-27 [0727-2cLD] — superseded in place, kept for the record.** All 19 Gov
Ball song timecodes were exported and parsed: **the bumps ARE in the timecode**, as
`Temp`/`Temp(Release)` event pairs on dedicated sub-layers (SONG_E carries 422 events on a
single layer; SONG_M 872 across four). The trace-level strings were a weak signal read
too confidently. Only the AUTHORING METHOD remains open — **Dave's theory (a theory, not a
fact) is that a plugin wrote the press/unpress pairs**, which fits both the volumes and the
fact that {LD} already ships a 253-line Lua engine. If true, we can generate ours the same
way: `export-timecode-tc-event-xml-schema` is fully cracked and `tc-bump-button-architecture`
already reserves the file-side generation seam. That makes {LD}'s file evidence FOR the "recorded bumps" model that Dave's executor design explicitly moves away from (`tourshow-tour-identity`'s executor model: "hits authored on the grid, not recorded bumps") — **the {TOUR} tour TC model is a re-architecture of {LD}'s approach, not a port of it.** {LD}'s bump vocabulary maps 1:1 onto Beatgrid's stem-lane markers (kick/snare lanes → bump moments) — see `beatgrid-stem-sections-feature`; the tour-file-archaeology and beatgrid-build workstreams converge here.

**{COLORIST} confirmed (2026-07-08): {FESTIVAL} programming was "overly simple because they didn't have a lot of time"** — {LD}'s file is a time-constrained output, not a statement of design intent or a ceiling to live up to. Practical read: the bump vocabulary above stays useful reference (see `beatgrid-stem-sections-feature`), the file's colors stay intel-only (see `show-direction-doc-and-color-sync-workflow`), and there's no "ghost standard" the current rebuild owes it.

History: none — recorded 2026-07-02 evening as Dave's explicit architectural decision. 2026-07-06: {FESTIVAL} predecessor evidence added — {LD}'s system used manual/recorded bumps (trace-level TC strings only), confirming Dave's model is a re-architecture, not a port; see `festival-showfile-save-lineage` for the file's save history. 2026-07-08: {COLORIST} (de facto CD) confirmed {LD}'s {FESTIVAL} programming was time-constrained, not a design ceiling — reinforces the re-architecture read with a direct human source. 2026-07-16: `tc-bump-button-architecture` refines the executor model — dedicated bump executors ride parallel lanes alongside the main sequence's TC-fired lane, triggered by typed TC events, exiting via Release not Off. 2026-07-27 [0727-2cLD]: the 2026-07-06 "likely manually bumped, not TC-run" interpretation is DISPROVEN by a full 19-song TC export parse — the bumps are TC-run; only how they were authored is open.


### tourshow-showfile-intake-ritual ⚠ VERIFY
**Incoming {FESTIVAL} showfile — expected contents and the 3-step intake ritual on arrival**
*when:* The moment the {FESTIVAL}/{FESTIVAL} showfile from Michael/{LD} arrives — run this ritual before touching it


**Expectation:** the {FESTIVAL} file ≈ last year's tour file + new songs on top (Dave ~certain, not yet confirmed on arrival).

**On arrival, in order:**
1. Inventory before touching (snapshot plugin).
2. Tag legacy vs. festival-add layers.
3. **Save As untouched "AR" master** — **"AR" = as-received** (working term, **[VERIFY] unconfirmed** — this expansion is not officially confirmed, just the working assumption). This file serves as both their fallback and our diff baseline.

**First open on 2.4:** mind the pre-2.4 migration traps — programmer wipe, Universal→Generic ID type, "Auto" preset mode removed. See `v24-migration-facts` for the full migration list.

**Ritual executed, 2026-07-06 ({FESTIVAL} file arrived):** arrived via **Dave direct-drop** of {LD}'s Drive original, `"{ARTIST} {FESTIVAL}.show"` (not via Michael, as the expectation above assumed). Steps 1–3 (inventory, tag layers, Save-As AR master) are **done**: archived as `WORKING/showfiles/ARTIST_festival_AR_as-received_2026-07-06.show`, sha256 `879061b1…7e15`, **104,954,011 B**. The as-received naming matches the working "AR = as-received" assumption but doesn't itself confirm the term officially — `status: verify` still reflects only that. **Console-side AR ritual (first onPC load, migration traps) is still pending.** Midway Deadmau5 `v3.show` (21 MB) is also in Drive, not yet pulled.

History: none — the ritual itself is settled; `status: verify` reflects only the unconfirmed "AR" term expansion, not the ritual steps. 2026-07-06: file-side execution of the ritual (steps 1–3) recorded against the real {FESTIVAL} file; console-side (first onPC load) not yet run.


## TIMECODE

### automator-tc-architecture
**The show-run automator decoded: LTC → a 24h timecode canvas of half-hour blocks by show position → a token-named cue whose CMD fires the song macro → one shared SongStart macro. TC TIME IS SONG IDENTITY, and there is nothing resident.**
*when:* Before touching any part of an inherited hands-off show-run chain — adding a song, correcting an offset, adding a per-song action; the whole chain is native objects and the single touchpoint is one macro line


## The chain (no plugin runs at showtime)

```
LTC slot 1
  → Timecode 1 'Automator'   — 24h canvas, ONE track, one Go+ event per song
    → Sequence 1 'AUTOMATOR' cue N — cues NAMED the song tokens, in SHOW ORDER, empty parts
      → part-0 CMD `Go+ Macro "<token>"`   (COMMANDENABLED = 1)
        → the song macro
          → the shared SongStart macro
            → the show-control toolbox call
```

**Every link is a native object.** Timing authority is 100% native TC + CMD. See `plugin-code-runs-at-showfile-load` for why the Lua toolbox in the last link is a subroutine, not a service.

## The lattice: TC time is song identity

Events sit on **half-hour blocks by show position** — event *N* ≈ (N−1) × 30 min, trimmed a few seconds early on some songs to the actual LTC start of that song's playback file. Each **per-song TC show's `OffsetTCSlot` is that song's REAL LTC start**, and it must agree with the automator event that fires it. Verified to the frame against decoded playback WAVs.

**The blocks continue past the live set by song number** — which meant a song added later had its slot predetermined by the scheme rather than chosen (the pilot's provisional value turned out to be the scheme's own answer). **When adding a song: add the automator event at its block, add the token-named cue with its CMD, cut the playback to that base, set the TC show's offset to match.**

## The song macro pattern, and the single touchpoint

Each song macro is three lines: set the `selectedsong` global to the token, set `bpm`, then call the **shared `SongStart` macro**. That shared macro is **one line of Lua**.

**⇒ One line added to the shared macro gives EVERY song a new per-song action, with zero per-song edits.** That is how the blocking-card swap and the video clip-connect were added — a second line calling one toolbox function that reads the `selectedsong` global and does both (`appearance-image-swap-blocking-cards`, `resolume-dmx-one-hot-clip-select`).

**Design call worth carrying:** the per-song action rides the **shared macro**, not eighteen mark cues. Mark-cue CMDs are orphaned by sequence renames; the macro lane is rename-immune (`name-token-single-holder-cutover-law`). Trade-off: a **manually-fired** mark cue will not pull the per-song action — the mark-lane CMD pass is a five-minute option once renames settle, if wanted.

## Field-leak gotcha in the offsets

One TC show's `OffsetTCSlot` carried an odd value that mismatched its own automator event — and **a second show carried the identical odd value**. Two shows sharing one wrong number is a **store-time field leak from a template**, not a design choice; the template TC show was found carrying exactly that value. **Measure the offset from the playback file's own LTC rather than inheriting it**, and suspect any two shows that agree on an odd number.

## Verification standard

The chain was proven **end-to-end under real Art-Net timecode**, hands-off, and then ran **live in a show**: TC in → automator → song macro → toolbox → page/sequence/mark/BPM + blocking card + video clip. Census after every edit at **CmdSubTrack depth** — targets by name, event counts exact — never on the echo.

**Relation:** `plugin-code-runs-at-showfile-load` · `timecode-assertprevevents-and-goto-seam-controls` (the seam knobs on these TC shows) · `tc-slot-enum-internal-default` · `name-token-single-holder-cutover-law` · `export-timecode-tc-event-xml-schema` · `tourshow-playback-architecture-doctrine`.

History: none — decoded 2026-08-08 by read-only census, extended and verified in show conditions through 2026-08-19.


### df-2997-drop-frame-timecode-math-and-rate-switch
**29.97 drop-frame timecode: console rate-switch recalculates automatically (no re-entry/re-export); math pinned + Python-verified (30000/1001, 17982 frames/10min, integer frame-space arithmetic only)**
*when:* Before authoring, converting, or displaying 29.97 drop-frame timecode anywhere in the pipeline — console rate-switch behavior and the pinned DF math formulas


**Console rate-switch behavior [Dave operator-confirmed]:** author timecode at 30fps; switching the show's TC frame rate to 29.97 drop makes the console recalculate everything itself — **no TC re-entry, no re-export needed.** Consistent with the cracked TC-event schema (`export-timecode-tc-event-xml-schema`): `CmdEvent` `Time` is a decimal-seconds string, which is rate-agnostic by construction.

**Repo manual gap:** ZERO hits for drop-frame/29.97 in the repo manual — another entry in the running manual-gap list (alongside `measure-layer-math` and `at-filters-worlds-manual-gap-and-study-doc`).

**DF math, pinned + Python-verified** (`beatgrid/Meta/harness/df_verify.py`):
- Rate = **exact `30000/1001`**, never float.
- DF drops **2 frame NUMBERS per minute**, except each 10th minute (no drop).
- **17982 frames per 10 minutes.**
- `01:00:00;00` = **107892 frames** = **3599.9964 seconds**.
- Invalid DF labels: `FF ∈ {0,1}` when `SS=0` and `MM % 10 ≠ 0`.
- **Drift comparison:** a 29.97 NDF (non-drop) label drifts −0.3s @ 5min, unbounded over time; DF stays bounded to ±2 frames.
- **All TC arithmetic must happen in integer frame space** — worked example: `03:29:53;22 + 42.8s = 03:30:36;15` (DF) vs `03:30:36:16` (30 NDF) — the one-frame delta is correct; they're different clocks, not an error.

History: created 2026-07-18 from the DF verification session; console rate-switch behavior and math formulas captured together since both are needed for any DF timecode work.


### export-timecode-tc-event-xml-schema
**Export Timecode XML schema — Timecode>TrackGroup>Track (targets a Sequence)>TimeRange>CmdSubTrack/FaderSubTrack events; Time is a decimal-seconds string**
*when:* Before reading, generating, or hand-authoring a TC-event XML file (Export Timecode) — e.g. cLD MAker's TC-event export or any file-side bump-lane generation — the full element/attribute shape and the beatgrid-startSec bridge


**Schema tree:**

```
GMA3
 > Timecode (Cursor Duration LoopMode LoopCount TCSlot AutoStop SwitchOff Goto
             PlaybackandRecord TimeDisplayFormat FrameReadout RestartOption)
    > TrackGroup
       > <MarkerTrack>
       > <Track Target="ShowData.DataPools.Default.Sequences.102">
          > TimeRange (Duration="To End")
             > <CmdSubTrack>
                > <CmdEvent Name="Go+"|"Off" Time="5.383" CueDestination="cLD CHASE GAPS">
                   > <RealtimeCmd Type="Key" Object="13.13.0.5.101" ExecToken="Go+" ValCueDestination="0.5.101.1000">
             > <FaderSubTrack>
                > <FaderEvent Name="Fader(Master)" Time="12.783">
                   > <RealtimeCmd Type="Fader" ValFaderValue="100.00%" ValEncoderResolution="167772">
```

**Time format:** a decimal-seconds string (e.g. `"5.383"`), or `"1m05.183"` once past one minute.

**Semantics:**
- A `<Track>` TARGETS a sequence via the same dotted full-path convention as recipe bind-slot refs (see `export-sequence-xml-schema`).
- `<CmdEvent>`s fire `Go+`/`Off` at a given `Time` into a named cue (`CueDestination`).
- `<FaderEvent>`s ride master level at a given `Time`.

**THE BRIDGE:** a beatgrid moment's `startSec` (see `beatgrid-session-json-schema-conventions`) maps DIRECTLY onto a `CmdEvent`'s `Time` attribute — cLD MAker can generate a whole TC track file-side straight from a treatment timeline, with no manual TC recording step.

**Relation:** this CRACKS the "TC-event XML schema" homework left open in `tc-bump-button-architecture` — that concept's bump-executor design can now be authored directly rather than only recorded. Reserved as a v1.1 seam in `cld-maker-identity-rename-and-scope` (schema now fully captured, so unblocked whenever it's picked up).

**Corroboration (2026-07-18):** the decimal-seconds `Time` format was confirmed rate-agnostic in practice — switching a show's TC frame rate from 30fps to 29.97 drop makes the console recalculate its own display without touching this XML's `Time` values (no re-entry, no re-export). See `df-2997-drop-frame-timecode-math-and-rate-switch` for the full DF math this corroborates.

**Corroboration + two new mechanics (2026-07-21, [0721-2cLD]):** the full schema was **hand-authored file-side from scratch** (no console export as a starting point) for `cLD SONG_G TC` (Timecode 2) — 9 cue-fire `CmdEvent`s + 6 slide-pop events — and **imported clean**, a fourth proof point for `xml-file-side-authoring-import-lane-proven` (now on the timecode dialect). Two mechanics confirmed live:
- A `CmdEvent` **WITHOUT** `ValCueDestination` imports as a **plain sequential Go+** (fine for a linear cue list — no explicit cue targeting needed).
- **`CueDestination` is COSMETIC ONLY** — a display label, not read at import. The console **re-resolves the actual fire target from the executor's live current-cue** plus the numeric `ValCueDestination`; imported events showed stale labels (`"PLATE MASTERS FULL"`, `"cLD CHASE GAPS"`) left over from whatever that executor last held, while firing still hit the correct numeric address. Never trust the `CueDestination` string when reading an imported TC file — read `ValCueDestination`.

**Addressing formula, generalized:** `Object="13.13.0.5.<exec>"` and `ValCueDestination="0.5.<exec>.<cue × 1000>"` — the cue number is encoded ×1000 (cue 1 → `1000`, matching the original worked example `0.5.101.1000` above).

History: created 2026-07-17 from an incidental Export Timecode capture during the same live-desk session that cracked `export-sequence-xml-schema` — closes a homework item that had been open since 2026-07-16. Extended 2026-07-18: rate-agnosticism corroborated against live 29.97 drop-frame rate-switch behavior. Extended 2026-07-21: hand-authored from scratch and imported clean (cLD SONG_G TC) — fourth dialect proof for `xml-file-side-authoring-import-lane-proven`; confirmed CmdEvent-without-ValCueDestination falls back to plain sequential Go+; confirmed CueDestination is a cosmetic label only (console re-resolves from live executor state); generalized the ValCueDestination cue×1000 addressing formula.


### name-token-single-holder-cutover-law
**Name-resolution cutover law: rename the OLD holder AWAY FIRST so a token never has two holders — then converge every addressing lane (name resolution, TC index targets, executor seats) onto the same object per song**
*when:* Before swapping which object a by-name lane resolves to — a rebuild taking over an original's token, a sequence replacing another under timecode; the ordering rule is what prevents an ambiguous window


## The law

**Per token: rename the OLD holder away FIRST, then rename the new one in.** At no point may two objects carry the same token — a by-name resolver has no defined behaviour in that window, and the failure is silent.

Attested execution: **14 song flips**, done old-away-first per song, plus **3 case-normalisations** of names an earlier session had set in a different case, plus the old objects given a **uniform graveyard prefix** (`OLD <token>` ×17) so the retired set is legible at a glance. Census after: **18/18 tokens single-holder.**

## Exact spelling, no case bets

The fire path resolves by **exact token**. A hand-added cue read `In _N_OUT` firing `Go+ Macro "SONG_S"` — both wrong, both fixed to the exact token, both verified by readback (`object-name-assignment-asymmetry-cues-vs-others` for the cue-rename mechanics). **Never bet on case-insensitivity anywhere in a name-resolved chain.** The image pool needed the same treatment for its own match law — one card renamed so the token match ran 18/18 exact.

## Converge every lane, or the cutover isn't done

A song is addressed by **three independent lanes**, and they can disagree silently:

1. **Name resolution** — the plugin chain resolving the token to a sequence;
2. **Timecode index targets** — TC tracks pointing at a sequence by index;
3. **Executor seats** — the per-song page's main executor assignment.

The cutover is structurally complete only when **all three land on the same object per song**. That convergence was done deliberately and censused: name tokens 18/18, executor seats read back per page, TC targets confirmed by name.

**Ordering consequence for build work:** while renames are in flight, **do not write new CMDs into the objects being renamed** — orphan risk. Park that pass until the names settle, then it is five minutes. (This is exactly why the video clip-go was routed through the single shared macro touchpoint instead of eighteen mark cues — see `automator-tc-architecture`.)

**Relation:** `speedmaster-name-token-exact-match-gotcha` · `object-name-assignment-asymmetry-cues-vs-others` · `automator-tc-architecture` · `tc-track-target-cutover` · `tc-cutover-last-and-delete-eats-events-doctrine` · `pool-naming-song-prefix-collision-rule`.

History: none — executed and censused 2026-08-12.


### tc-bump-button-architecture
**TC bump-button architecture — dedicated bump executors triggered by typed TIMECODE EVENTS, exiting via Release not Off; a manual-ride layer alongside it is a proposed (not yet built) addition**
*when:* Before designing or building bump executors, TC event lanes, or any cheap one-shot hit that needs to land on a music transient — including a manual-ride executor a human can fire live alongside the TC-fired ones


Dave's architecture for cheap, exact-spot one-shot hits (drum follows etc.) without bloating the main cue stack:

**Structure:** multiple dedicated bump executors, each carrying a one-shot effect. Triggered by TIMECODE EVENTS typed directly into the TC editor — button on/off events sit in their own lanes, with no live recording needed. The main sequence runs its own lane; bump executors ride parallel lanes alongside it.

**Exit rule — release, not off:** bump executors exit via RELEASE (see `release-mechanism-fundamentals`), never Off/zero. Off would fight the main sequence's look; Release lets the channel fall back cleanly to whatever the main sequence is already doing underneath.

**Homework CRACKED 2026-07-17** (incidental capture, Export Timecode read live at the desk): the TC-event XML schema is now fully decoded — see `export-timecode-tc-event-xml-schema` for the full element/attribute shape. Events can now be authored directly file-side, not just recorded.

**cLD synergy, now unblocked:** the TC-event schema confirms a beatgrid moment's `startSec` maps DIRECTLY onto a `CmdEvent`'s `Time` attribute — cLD MAker (the renamed, scope-widened tool — see `cld-maker-identity-rename-and-scope`) can generate a whole TC track file-side straight from the treatment timeline. Reserved as a v1.1 seam (schema fully captured, so unblocked whenever it's picked up).

**Relation:** refines the executor model already on record in `tourshow-showfile-architecture` (one TC-fired master executor per song) — this adds that bump executors ride parallel lanes alongside that master executor, not just the one.

**Design refinement 2026-07-17 — scope bumps with Output Filters:** a recipe-part's full property dump confirmed `FILTER`/`INPUTFILTER`/`OUTPUTFILTER` are first-class recipe-part properties, giving per-layer scoping on a recipe line (e.g. a color-only cook that can't touch dimmer/position). **TC-bump lanes should carry Output Filters** so a bump can only ever emit the attribute(s) it's meant to hit — this keeps a bump from accidentally fighting the main sequence outside its intended layer, reinforcing the release-not-off exit discipline above rather than relying on it alone.

## Manual-ride layer alongside the TC-fired lane — design ask, not yet built (2026-07-29)

Dave wants a few bump executors he can **ride live, by hand**, on anything that needs it — a manual-ride layer that sits alongside the TC-fired bump lane described above, built per-song as needed. This is a forward-looking design ask, not yet a proven or built mechanic; the TC-fired architecture above remains the only implemented lane as of this note. See `tourshow-fill-layer-rebuild-method` for the fill-build context this ask came out of.

History: none — architecture and exit rule both stated 2026-07-16; TC-event schema remains open homework. Extended 2026-07-17: Output Filters design note added from the recipe-part property-surface dump. Same day, later: TC-event schema homework CRACKED via a live Export Timecode capture — see `export-timecode-tc-event-xml-schema`. Extended 2026-07-29: added Dave's manual-ride bump-executor design ask (not yet built) alongside the proven TC-fired lane.


### tc-cutover-last-and-delete-eats-events-doctrine
**⛔ TC cutover is the LAST act of a build — deleting a TC-targeted sequence eats the track's events; park on {LD}'s, never delete a live-targeted sequence**
*when:* Before deleting, re-importing, or otherwise structurally rebuilding ANY sequence that is currently TC-targeted — and when sequencing a song's build steps, to confirm TC cutover is scheduled LAST rather than folded into the first import chain


**The incident (SONG_B, 2026-07-31):** TC 102 was cut over onto `cLD SONG_B` during the FIRST import chain. All subsequent editing churn (a strict-mode pass, figure placements, a full v2 delete+rebuild) then happened on a sequence that was already TC-targeted — that is what armed the failure. The v2 rebuild's `Delete 1110` dangled the TC track, and the button-press/Go events bound to the now-dead object were lost. Dave re-entered events and destinations by hand at the desk.

**Mechanism — target MOVES preserve events; target DELETES do not.** `tc-track-target-cutover`'s events-survive-target-moves law covers moves only. A DELETE on the target object drops whatever the track pointed at, and the events bound to that dead object go with it. The post-swap readback that caught this checked TARGETS ONLY — the pointer read healthy while the event lane underneath was empty.

**Corollary, same session — deleting the TC OBJECT itself is safe, the inverse case:** the TC pool object's `Name` attribute (e.g. "SONG_B") rides the XML and survives Delete+Import — the song macro's name-based `Go Timecode '<song>'` call stays intact. **Events live in the TC object; a sequence Target is just a pointer into it** — deleting the pointer's destination loses events, deleting the TC object that holds the events does not.

**Standing order (Dave, ruled):**
1. **{LD}'s sequences are EXPORT-FOR-INSPECTION ONLY — never deleted, never edited.** TC resting on them during a build is a FEATURE, not neglect: they are a complete, working rollback state.
2. **TC cutover fires ONCE, at the very end** — after import + census + Dave's desk pass + any rebuild cycles are fully settled, never folded into the first import chain.
3. **Post-cutover tune-backs stay LINE-level via live `Assign`** (delete-free). "Park the track" — point TC back to {LD}'s original, do the structural work, point it back to ours — survives only as an emergency fallback for a post-cutover structural rebuild that should never happen in the first place.

**Why parking works:** pointer moves preserve events in BOTH directions, and while parked on {LD}'s, TC still drives a COMPLETE working version of the song — the show is never dark mid-surgery (Law Zero applied to the build process itself).

**Census consequence:** TC readback census must count **Target AND per-track EVENT COUNT, always** — a target-only census is not sufficient evidence the track is intact.

**Reapplied the same session (SONG_C):** TC 103 stayed parked on {LD}'s through the entire build — "TC 103 cutover NOT done — parked for Dave previz per cutover-last law." The doctrine held on the very next song.

**Runbook consequence (Dave, owed):** split the runbook's fire-chain step and the cutover step explicitly — never compress into one batch. The miss was pipeline momentum overriding gate discipline, the same circuit-breaker shape as other paid-for lessons in this corpus.

**Relation:** `tc-xml-event-surgery-lane` for the proven surgical-edit alternative when a post-cutover fix is genuinely unavoidable. `tc-track-target-cutover` (existing concept, not staged this run — cLD should fold this doctrine's move-vs-delete distinction into its body on next direct edit).


### tc-slot-enum-internal-default
**TCSlot enum: 255 = Internal (frame readout flips to 'UP'), 256 = Default (readout follows slot 1), 1-8 = explicit slots — the rehearsal/show toggle is two one-line macros over the song TC range**
*when:* Before reading or writing a Timecode object's TCSlot, or when building a rehearsal-vs-show clock toggle — the enum is not documented and the automator's own slot must be left out of the sweep


| Value | Meaning | Frame readout |
|---|---|---|
| **255** | **Internal** — the show runs on its own clock | flips to **`UP`** |
| **256** | **Default** — follows the console's timecode slot 1 | reads **`S1`** |
| **1-8** | an explicit slot | that slot |

**How it was found:** Dave set one show to Internal, left the rest default, and said "figure out the parameter." A full property diff of the two objects isolated `TCSLOT`. **Teach-by-diff is a cheap and reliable way to name an undocumented property** — set one object differently, diff it against a sibling.

**Historical read this unlocks:** an inherited fleet sitting at 255 means it was set **Internal**, not "parked at some default." The enum makes an old census legible.

## The toggle

Two macros, **one Lua line each**, looping **only the song timecode range**:

- **`TC Internal`** → 255 on every song show (rehearsal: internal clock, no playback rig)
- **`TC Default`** → 256 on every song show (show: follows Art-Net/LTC on slot 1)

**⚠ Deliberately excluded: the automator TC show and the utility shows.** The automator's slot is its own animal — the same reasoning as its Assert exception (`timecode-assertprevevents-and-goto-seam-controls`).

**Test cycle used:** fire Internal → census 20/20 at 255 → fire Default → census 20/20 at 256 → **restore the one show Dave had set by hand to as-found** (leave-as-found law). Exported to `gma3_library/datapools/macros/` as XML pairs so they travel to any file.

**Relation:** `timecode-assertprevevents-and-goto-seam-controls` · `automator-tc-architecture` · `macro-cli-creation-and-edit-lane` · `many-lines-ride-macros-not-lua` · `tourshow-artist-tc-sheet`.

History: none — decoded, built, tested and exported 2026-08-12.


### tc-targeted-sequence-delete-eats-events ⚠ VERIFY
**Deleting a sequence that a timecode track targets EATS that track's events — census event counts at L3 (Timecode → TrackGroup → Track → SubTrack → events), never at the TrackGroup pointer**
*when:* Before deleting or retargeting any sequence that a Timecode track points at, and before trusting any TC event census — a shallow counter reads a healthy cutover as emptied

**[0805-2cLD] EXTENSION — census depth law:** the tree is Timecode → TrackGroup → Track → SubTrack → events. `tc:Ptr(j)` is a TRACKGROUP; `Track.Target` lives one level down; real event counts live TWO levels down (L3). A shallow counter reads a healthy cutover as event-emptied — cost two false-empty censuses on 2026-08-05. Any event census in this family counts at L3.

History: extended 2026-08-05 [0805-2cLD] — traversal depth: tc:Ptr is a TrackGroup, event counts live at L3; shallow counters false-report empty (two censuses paid).


### tc-temp-release-pair-dialect
**TC bump/drum-roll events are Temp + Temp(Release) pairs, never a latching Go+ — two coexisting event-XML forms, both fire**
*when:* Before authoring or repairing any bump/flash/drum-roll TC event by hand or by XML surgery — the press/release event pair shape, the attribute differences between the two coexisting event forms, and the time-format switch past 60 seconds


**Ruling (Dave):** drum-roll/bump TC events are **`Temp` + `Temp(Release)` pairs, ~0.3s apart, NEVER a latching `Go+`.** This restores `tc-bump-button-architecture` doctrine — a desk hand-repair had used quick `Go+` entries instead and needed converting back.

**Press event:** `RealtimeCmd` `ExecToken="Temp"` `Status="On"`.

**Release event:** `Name="Temp(Release)"`, `RealtimeCmd` `Status="Off"` `ExecToken="Temp"` — a **sparse desk-typed form**: no `Object=` / `ValCueDestination=` needed, `Time=` offset +0.3s from the press.

**Two event forms coexist in the same TC file, and both fire:**
- RECORDED/full form: `Object=` + `ValCueDestination=` + `UserProfile`/`User` set, `IsRealtime=1`.
- DESK-TYPED sparse form: no `Object`/`ValCue`, `User=0`, `IsRealtime=0` — resolves via the track rather than its own address.

**A `Go+` → `Temp` conversion must flip BOTH the `Name` attribute AND `ExecToken`** — changing only one does not produce a working Temp event.

**Time format:** times over 60s use the minute-prefixed attribute form `"1m42.333"`, not raw seconds.

**Exec-object addressing note:** exec object number = seq number − 1 (e.g. exec object 1113 = seq 1114 − 1) — the same seq-minus-1 law seen elsewhere in the corpus, confirmed again on a TC exec/track read.

**Verify queued (Dave, explicit) — CLI TC-event creation/type-flip on a SCRATCH timecode is UNPROVEN mechanics.** Kept off the live repaired TC this session (the repair used the XML-surgery lane instead); needs proving before this dialect can be authored directly at the CLI for the remaining songs.

**Relation:** `tc-xml-event-surgery-lane` for the proven method used to convert Go+ entries to Temp pairs by file surgery. `tc-bump-button-architecture` (existing concept, not staged this run) for the base bump-vs-cue-count doctrine this session re-confirms after a desk repair briefly contradicted it.


### tc-track-target-cutover
**⛔ TC cutover = change the TC track's Target — never rename, re-author, or juggle executors; rollback = point Target back**
*when:* Before planning or executing ANY timecode cutover from an inherited/predecessor sequence to your own — change the TC track's Target, don't rename or re-author; also the reference for how a TC track addresses its sequence by name and how its exec-object number relates to the sequence number


**⛔ THE MECHANISM, PROVEN LIVE: a Timecode track drives whatever sequence its `Target` property points at — change the Target, and the whole rename/re-author/executor-juggling problem disappears.** No TC authoring, no renaming objects, no executor gymnastics. Point the track's `Target` at your own sequence and the timecode drives it exactly as it drove the original.

**Live proof (2026-07-29):** Dave changed TC 106 track 1's `Target` from Seq 1500 ({LD}'s SONG_T) to **Seq 1510 (cLD SONG_T)** and watched it run cLD's build with the song — the first light of the tour build. **Rollback = point the Target back to 1500.** Later the same session, all three TC 106 tracks were re-targeted at once — Seq 1510 (main) / 1511 (cLD FILL 1) / 1512 (cLD FILL 2) — and event labels re-resolved live to the new preset names; the show ran complete under TC with every object ours. **cLD can drive this Target change via CLI for the remaining songs** — this is the standing cutover method for the rest of the setlist, not a SONG_T one-off.

**⚠ SUPERSEDES the older "rename-cutover" plan.** Prior sessions (2026-07-27/28) carried an unresolved "TC rename-cutover" method as debt — the assumption was that cutting the timecode over to cLD's sequences would require renaming objects or re-deriving how the TC's addressed executor maps onto a page/exec slot (`13.13.0.5.1499` ↔ "page 106 / exec 115" — see `festival-page-per-song-executor-architecture`). **That whole plan is now dead.** The Target property makes it a one-line change; no rename, no page/exec derivation needed at all. This concept is the definitive record — older records referencing a "rename-cutover" (`tourshow-seq1510-build-record`'s pre-2026-07-29 "What's left," `festival-page-per-song-executor-architecture`'s "rename cutover" language) describe the superseded plan, not what actually shipped.

## TC 106 track identity — three tracks, each targeting a sequence BY NAME

**FILE-SIDE (from `SONG_T.xml`, the TC export):** TC 106 carries THREE tracks, each targeting a sequence **by name**: `SONG_T` → `Sequences.SONG_T` (26 Go+ events, at exec object `13.13.0.5.1499`) · `Fill 1` → `Sequences.Fill 1` (60 Go+ events, at exec object `...1500`) · `Fill 2` → `Sequences.Fill 2` (10 Temp + 10 Temp(Release) pairs, at exec object `...1501`, every `ValCueDestination=0.5.1501.1000` = cue 1). The exec-object triplet (1499/1500/1501) is consecutive.

**DESK-SIDE, CORRECTED AND PINNED LIVE (from the Edit Timecode window):** the track `Target`s are actually **SEQUENCES 1500 `SONG_T` (main) / 1501 `Fill 1` / 1502 `Fill 2`** — the file-side read above found the **exec OBJECTS** (`13.13.0.5.1499/1500/1501`), not the sequence numbers. **Both readings are true simultaneously: exec object = seq number − 1**, now confirmed live for the whole triplet (1499 = 1500−1, 1500 = 1501−1, 1501 = 1502−1). This refines (does not contradict) the "apparent main exec = sequence century − 1 pattern" already on record in `festival-page-per-song-executor-architecture` — that pattern is now an exact, live-confirmed rule for this triplet, not just an apparent one.

**Temp events carry `FromLocalHardwareFader=1`** — recorded hardware presses, corroborating the recorded-bumps model for how {LD}'s fill layer was authored.

**Still genuinely unresolved (unaffected by the cutover mechanism above):** how the exec-object number (`1499`) maps onto a **page/exec-SLOT** (e.g. "page 106, exec 115") is still not derivable from the files — see `festival-page-per-song-executor-architecture`'s open item. **This mapping is now MOOT for cutover purposes** (the Target change doesn't need it), but it remains open for anyone who needs the page/exec-slot number itself for some other reason.

## Milestones (proof the mechanism holds under real use)

- **SONG_T FIRST FIRE:** Seq 1510 ran under TC 106 with the song — first light of the tour build. Look read thin at this point (known causes: phasers ~8x too fast pending the Speed Scale ruling, Forte All→RIVALE not yet bound, Fill 1/Fill 2 layers not yet built, plus the design ask for this song is deliberately low on lights). Crosswalk itself ruled good by Dave at this checkpoint.
- **FILLS LIVE UNDER TC (Dave: "It lands! Send It!!!"):** screenshot-confirmed all three TC 106 tracks re-targeted to cLD's objects — Seq 1510 cLD SONG_T / 1511 cLD FILL 1 / 1512 cLD FILL 2 — event labels re-resolved to cLD's preset names (`[0/cLD OW FILL BURST]`, `[cLD OW FILL SHIMMER]`), running with the song at v.40. Team saying coined this session: **SEND IT.**

**Relation:** `festival-page-per-song-executor-architecture` (the per-page executor architecture and the still-open page/exec-slot mapping) · `tourshow-seq1510-build-record` (the SONG_T build this cutover completed) · `tourshow-fill-layer-rebuild-method` (the fill sequences 1511/1512 this cutover put under TC).



## ⭐ THE CLI LANE, PROVEN 9/9 — 2026-07-31 [0731cLD]

**Grammar:** `Assign Sequence <seq> At Timecode <tc>.1.<N>` re-points dot-track N's `Target`. Landed **9 of 9 tracks** on TC 101 for SONG_A (main + 8 aux) in one batch, every one readback-verified. **This supersedes this file's earlier desk-only framing** — cLD can drive the whole cutover over the wire; it is the standing method for the remaining setlist.

### ⛔ The dot-index EXCLUDES the Marker track

`<tc>.<group>.<N>` addresses the **Nth NON-MARKER track** — i.e. tree-child **N+1**. So `.1.1` is the **main** track and `.1.2` is the first aux, not the reverse. The first SONG_A assign was written to `.1.2` believing it was the main and re-pointed **Snare 1** instead.

**Damage profile is mild, which is exactly what makes it dangerous:** a TC track keeps all of its events when its `Target` moves — only the pointer changes — so the mistake costs one corrective assign and produces a completely clean-looking echo either way. Nothing in the command feedback distinguishes the right track from its neighbour.

### ⚠ A cached `:Children()` handle reads a STALE Target after an Assign

A track's identity (and display name) derives from its target, so the object shifts when the target does. A handle captured before the write reads the **old** target afterwards and reports a successful write as a failure. **Verify on the `ObjectList` dot-address**, never a cached tree handle:

```
ObjectList('Timecode 101.1.1')[1]:Get('Target')
```

Both traps stacked on the same write — a wrong-track assign masked by a stale readback — and only reading back off the dot-address cut through. Census the whole track group in tree order when in doubt; `#tg:Children()` includes the Marker and is the honest count.

History: none — mechanism discovered, proven, and generalized in one session, 2026-07-29. 2026-07-31 [0731cLD] — CLI Assign lane proven 9/9 on TC 101; dot-index-excludes-Marker and cached-handle-staleness traps banked.


## Track TREE order is not sequence-NUMBER order — verify every target by content, never by position — 2026-07-31 [0731-3cLD]

**TC 104 cutover prep (SONG_D, the last act before execution):** the track tree order
is **Marker, main, Snare1, Snare2, KICK2, KICK1** — so by the dot-index law above (tree
excludes Marker, `.1.1`=main), `.1.1`=main→1310, `.1.2`→1311, `.1.3`→1312,
**`.1.4`=Kick2→1314**, **`.1.5`=Kick1→1313**.

**THE KICK PAIR IS REVERSED vs. sequence numbering:** the track tree lists Kick2 BEFORE
Kick1, but the correct targets are Kick2→1314 and Kick1→1313 — the opposite of what walking
the tree in order and assigning sequence numbers sequentially would produce. **Target by
track content, never by assumption** — the same dot-index-position trap this concept's
"EXCLUDES the Marker track" section already warns about, now with a second, independent
failure mode (content order vs. number order diverging) stacked on top of it.

**Live-executed and proven correct:** Dave ran the TC 104 cutover himself at the desk —
Target flips including the reversed kick pair, all correct — tested under timecode + audio,
called SEND IT. Export-back TC 104 census: 5/5 tracks target cLD sequences BY NAME, 393
events intact (17 Go+ / 46+46 / 12+12 / 8+8 / 122+122 Temp pairs), Marker untouched.


### tc-xml-event-surgery-lane
**TC-XML event surgery lane, proven — byte-surgical span edit of an exported Timecode file (third authoring lane beside CLI and desk)**
*when:* Before editing individual TC events (bump/Go+/Temp conversions, timing tweaks) inside an existing timecode file rather than re-recording at the desk or hand-Assigning line by line at the CLI — the proven Export→surgical-edit→reimport chain, plus where TC files live on disk and their MCP tier


**The lane:** `Export Timecode <n>` → byte-surgical edit of ONE `Track` element span in the exported file (verify neighbor tracks stay byte-identical; compare pre/post slices around the edited span) → deploy the edited file to `gma3_library/datapools/timecodes/` → `SaveShow` checkpoint → `Delete Timecode <n>` + `Import Timecode <n> 'bare-name'` → export-back census with **per-track EVENT COUNTS**, not just Target pointers (see `tc-cutover-last-and-delete-eats-events-doctrine` for why event counts, not target reads, are the honest census here).

**Proven on SONG_B's drum-roll fix (2026-07-31):** 4 `Go+`→`Temp` flips + 5 paired releases, 0.3s out, neighbor tracks confirmed byte-identical. Checkpoints v.64 (pre-swap) / v.65 (post), both disk-verified.

**"Third authoring lane beside CLI and desk; use for all remaining TC edits."** Joins the proven CLI `Assign`-based cutover (`tc-track-target-cutover`) and hand-typing at the desk as the three ways TC content gets authored or edited.

**Mechanics needed to run the lane:**
- Timecode files live at **`gma3_library/datapools/timecodes/` ONLY** — there is no top-level `timecodes` directory. `Import Timecode <slot> 'bare-name'` resolves from there (same bare-filename, no-`.xml` convention as every other pool dialect — see `xml-file-side-authoring-import-lane-proven`).
- MCP tier: **`Export Timecode` is Tier 2** (gated like `SaveShow`/`Import` — needs the confirm-gate flow). **`Delete`-inside-`Cmd` still rides Tier 1** (ungated) — treat it as unguarded and checkpoint before it fires.

**Hygiene:** the surgical intermediate file (e.g. `cld_tc102_postswap.xml`, resident in both `datapools/timecodes/` and a staging copy) is scratch — delete once the song is confirmed heard.

**Relation:** `xml-file-side-authoring-import-lane-proven` (existing concept — see this run's `updates/`) for the general Export→edit→Import→diff pattern this is a TC-specific instance of. `tc-temp-release-pair-dialect` for the event-XML shape this lane is typically used to edit. `tc-cutover-last-and-delete-eats-events-doctrine` for the standing order governing WHEN this lane may touch an already-cutover TC.


### timecode-assertprevevents-and-goto-seam-controls
**Timecode seam controls live on the Timecode object: GOTO and ASSERTPREVEVENTS. Fleet law — Assert TRUE on song shows (heals a cut's seam), FALSE on the automator (an assert across a block jump would fire every passed song's CMD chain).**
*when:* Before playing a cut-down/short-version bounce whose LTC jumps forward mid-show, or before setting Assert/Goto on any timecode show — the automator-vs-song split is load-bearing, not cosmetic


## Where the knobs are

The Timecode object's property schema (~50 properties) carries the seam controls: **`GOTO`** and **`ASSERTPREVEVENTS`**, alongside `AutoStart` / `AutoStop` / `SwitchOff` / `RestartOption` / `LoopMode` and the record family. **The local manual's CLI reference has nothing on jump/resync behaviour — the desk schema was the source.** Dump the object when the documentation is silent.

## Semantics

- **`AssertPrevEvents = true`** — when the playback pointer crosses events without playing them, their **cumulative state is re-established at the landing point**. An assert, not a machine-gun replay.
- **`false`** — the jump simply continues; skipped events never fire and state stays stale until the next event.

**With name-addressed events, both are survivable** — the first post-cut event re-aims the sequence correctly either way (`automator-tc-architecture`). Assert makes the seam *clean* rather than *eventually* clean.

## ⛔ The fleet split (Dave's spec, set across 23 shows, readback exact)

| Show | AssertPrevEvents |
|---|---|
| **The automator TC show** | **FALSE** |
| **Every song TC show** (including the dead ones, for uniformity) | **TRUE** |

**Why the split is load-bearing:** Assert heals seams **inside** a song. On the **automator**, whose events are half-hour blocks each firing a whole song's CMD chain, an assert across a block jump would **re-establish every passed song cue's state — firing the command chain of songs 1..N**. **Assert inside songs, never across them.**

The automator was found set **TRUE** (drift, or a hand) before the pass. The flip to FALSE was not cosmetic.

**Fleet consistency is itself a finding.** The census before the pass showed shows disagreeing on Assert *and* Loop, with one outlier that also carried a wrong offset — the same show that turned out to have inherited a template's leaked field (`automator-tc-architecture`). **Odd-one-out on one property is worth checking on all of them.**

## What this settled

The short-version plan: **zero new timecode shows, zero retiming.** Cut-down bounces carry their edit in the LTC itself (`beatgrid-tc-carried-cuts-and-seam-gap`), so tuning Assert plus a bench test of a real forward jump is the whole job; per-seam "landing" events are a fallback garnish, likely unneeded.

**Relation:** `automator-tc-architecture` · `beatgrid-tc-carried-cuts-and-seam-gap` · `tc-slot-enum-internal-default` · `df-2997-drop-frame-timecode-math-and-rate-switch` · `tc-cutover-last-and-delete-eats-events-doctrine`.

History: schema and fleet census 2026-08-08; the split ruled and applied across 23 shows 2026-08-12.


### tourshow-fill-layer-rebuild-method
**{LD} fill-layer anatomy decoded + our portable rebuild method — proven end-to-end on SONG_T, generalizes per-song to all 18 remaining**
*when:* Before decoding a {LD} fill/bump layer or rebuilding any of the remaining 18 songs' fill/aux sequences — the cue anatomy, the tempo-gear speed decode, the portable-artifact rebuild steps, and the per-song generalization table


**Portability doctrine (Dave):** {LD}'s fill layers work on our rig but not necessarily every future tour rig. **Record each fill's design INTENT as the durable artifact, then re-point the GROUP per stop for best effect** — fills get re-filled (re-grouped), never re-authored, at each new venue.

## {LD}'s fill anatomy, decoded (from the `gb_fill1`/`gb_fill2` exports)

**FILL 1 (Seq 1501):** cues `OffCue(Release=Yes)` / `CueZero` / `1 [Full]` / `2 [0/Fill 1]` / `3 [0]`, all `TrigType=Follow` — the TC's 1-2-1-2 alternation is a Full/0 bump. Binds: `Strike M [RGB] (Grid) (Fest)` ×2 + `(Lin)` ×1 + `WASH FEST [RGB] (Grid)` ×2; Values: `Dimmer.Full` / `Dimmer.0` ×2 / `Phaser.Dim_PWM_THIN#2` / `Phaser.Fill 1`.

**FILL 2 (Seq 1502):** single cue `1 [Fill 2]` (Temp-fired); binds `Strike M [RGB] Fest` Grid+Lin; Values `Phaser.Dim_PWM_THIN#8` / `Phaser.Fill 2`.

**Both fills:** `XShuffle 5` (F1) / `7` (F2), `ShuffleMode=Auto`, `PhaseFromX 0` → `PhaseToX 360`, Speed fixed-point **`38867217`** = 2.3166 Hz = **139 BPM exactly** — tempo-locked and baked in {LD}'s file. **Ours ride the Sequence Speed override (set to BPM) instead of the baked value** — Dave's ruling. Cooked `PresetData` rides along in the export (7/3 blocks) — strip it per the recipe-only doctrine (`recipe-output-precedence-and-cooking-doctrine`).

**Fill target CONFIRMED:** Dave's belief that the fills hit "STRIKE M FEST RGB" — originally flagged `[VERIFY]` (name-only, and Strike M labels have a JDC1-liar precedent, see `inherited-file-membership-is-ground-truth`) — is now **CONFIRMED** by a `GROUP_TRUTH` membership cross-check (Strike M [RGB] (Grid) (Fest) = Color Strike M ×336 subs, truthful at the group layer; the liars are specifically the US/DS/SW Strike M groups) and by the fill decode itself. Dave's "full setting" (from the MAtricks note below) resolves to the `[Full]` cue.

**⚑ Name-bind hazard:** {LD}'s own preset pool carries silent duplicate-suffix presets — `Dim_PWM_THIN#2` / `Dim_PWM_THIN#8` — the same MA3 silent-`#2` auto-suffix behavior documented in `cld-sandbox-and-namespace`. **Slot-address these, never name-reference them, in any XML we author** that touches {LD}'s pool.

**Fill MAtricks note (Dave):** {LD}'s fill MAtricks carry SHUFFLE settings plus a "full setting" — now decoded as the `[Full]` cue above. Ours take speed from the Sequence Speed override rather than the baked value.

## Speed/gears decode — {LD}'s tempo palette has THREE gears, not one

**Fill wrappers carry `SpeedFromX="139.00 BPM"`** (the standing recipe on the wrapper SR, easy to miss on a first extraction pass). **Forte (All)'s line carries `SpeedFromX="34.75 BPM"` = 139/4.** Combined with the existing `Intro 1/1 Spot Dim` decode (0.2896 Hz = 139/8, an 8-beat/2-bar cycle — see `tourshow-authoring-contract-v01`): **{LD}'s speed palette is tempo ÷1, ÷4, ÷8** — three gears, not a single constant.

**Dave's ruling:** all main-list phasers need slowing, via the per-cue-part **Speed Scale** setting, with **Sequence Override set to BPM**. **Refinement (this session): ÷8 is one of {LD}'s three gears, not the only one — per-figure judgment applies rather than a blanket ÷8.** Check which gear a given figure actually used before choosing the Speed Scale divisor for its cLD replacement. Ours ship speed-unbaked in all cases; the Sequence Speed override (BPM) is the desk knob that supplies tempo.

## The rebuild method — proven end-to-end on SONG_T (Seq 1511/1512)

1. **Decode** {LD}'s fill export(s) for cue/bind/spread/speed anatomy (above).
2. **Author** small, portable artifacts referencing cLD objects only — this build used **5 files**: `cld_ow_fill_burst`/`shimmer`/`rivale_bump` (presets, for `21.1525`/`26`/`27`) + `cld_fill1_seq`/`cld_fill2_seq` (for Seq `1511`/`1512`).
3. **Smith-certify before deploy:** burst = PASS; rivale_bump = PASS, attr-exact vs the golden `Dim_Sin_Bump`; the rest = PASS-WITH-FLAGS, all flags deliberate deltas (`UET=No` vs the golden's `Yes`; `Note=139` added per the 1510 precedent; speed shipped unbaked per Dave's override ruling; shimmer's `GridPos=0` vs the golden's `2^64-1` sentinel).
4. **Byte-exact deploy, verified:** 5/5 sha256 match across container → `generated/` → `gma3_library` datapools.
5. **Checkpoint, then import:** `v.39` pre-import checkpoint → `Import Preset` 21.1525/1526/1527 + `Import Sequence` 1511/1512 (all OK, 31-66ms) → **object-level census EXACT**: preset names clean (no silent `#2`), 1511 binds `Group 201 × Preset 1.5` / `1.15+21.1525 × Group 416` / `1.15`, 1512 binds `21.1526 × Group 416`, names `cLD FILL 1`/`cLD FILL 2` → **v.40 on disk** (113,320,505 B, 20:27).
6. **Set the Sequence Speed override (BPM)** on 1511/1512 (desk step, Dave).
7. **Re-point TC 106 tracks 2/3 `Target`** → 1511/1512, using the Target-change cutover mechanic (`tc-track-target-cutover`).

**Import dialect confirmed clean in this same build:** SR-level spread attrs (`XShuffle`/`XBlock`/`PhaseFromX`/`PhaseToX`) authored as plain attributes directly on the cue-part `StandardRecipe` import correctly and read back exact via `:Get` (`XShuffle=5`/`7`, `XBlock=7`, Phase `0→360` all exact) — the flattened lane (spatial attrs on the cue line, instead of {LD}'s wrapper-preset pattern) is proven; wrapper presets are unnecessary for spread/shuffle. Full mechanical detail in `import-resolver-laws`, which this build's import census extends.

## Milestones (proof the method holds)

- **FILL IMPORT CHAIN LANDED, CENSUS 100%** (above, v.40).
- **AIR-PIX BATCH LANDED VIA LIVE ASSIGN LANE:** 7 lines created on existing empty `P3 PIX` parts, census 7/7 exact, `SaveShow v.41` **on disk** (113,394,086 B, 21:39) — see `assign-cli-recipe-line-grammar` for the CLI mechanic this used.
- **FILLS LIVE UNDER TC:** all three TC 106 tracks re-targeted to cLD's sequences, running complete at v.40 — see `tc-track-target-cutover`.
- **FILLS CONFIRMED BY EAR** (Dave, at the desk): SONG_T played back complete with both fill layers — Dave's words: the fill sequences are what make the song complete. **SONG_T = DONE AND HEARD, v.41.**

**Live bump buttons (forward-looking design ask, not yet built):** Dave wants a few bump executors he can ride live by hand, as a manual-ride layer alongside the TC-fired bump lane — see the extension in `tc-bump-button-architecture`.

## Per-song aux architecture — this method generalizes to all 18 remaining songs

**Decoded from the 19 TC exports on disk (zero console):** per-song aux layers are **per-song sequences** — names carry the song (e.g. `'Kick 1 (SONG_B)'`) — and **sequence number = exec object + 1** (song-t-verified, consistent with the exec/seq relationship in `tc-track-target-cutover`).

**Aux counts per song:** SONG_A 8 · SONG_Q 6 · SONG_E 5 · SONG_H/SONG_B/SONG_D/SONG_L/SONG_M 4 · SONG_O 5 · SONG_C 3 · SONG_J/SONG_N/SONG_F 2 · SONG_I/SONG_K 1 · **SONG_G/SONG_R/SONG_P 0 (main-only, no aux layer)**.

**Main sequence numbers for the 18 remaining songs:** 1000, 1100, 1200, 1300, 1400, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800.

**The fill/bump rebuild method above = the SONG_T fill method, applied per song.**

**Relation:** `tc-track-target-cutover` (the TC-side half of putting a rebuilt fill under timecode) · `tourshow-seq1510-build-record` (the SONG_T build this fill layer completed) · `tourshow-authoring-contract-v01` (the phaser-figure spec-read posture this speed decode follows) · `import-resolver-laws` (the general import resolver families the SR spread-attr proof extends) · `assign-cli-recipe-line-grammar` (the Assign-creates-lines mechanic used for the air-pix batch) · `inherited-file-membership-is-ground-truth` (the labels-lie doctrine the Strike M Fest confirmation corroborates).

History: none — anatomy decoded, method executed, and generalization stated in one session, 2026-07-29.


### tourshow-playback-architecture-doctrine
**{TOUR} playback architecture: executors 1-15 + 101-115 are the portable envelope (console-portability doctrine); each song = ONE theatrical cue stack headed by a SET cue, all layers tracked inside it, every cue a TC-fired Go**
*when:* Before architecting any song's sequence/executor structure — the executor budget, the SET-cue-first pattern, and the TC-fired-Go default this show is built on


**Executor envelope — portability doctrine (Dave, dictated):** the whole show (SONG_G, and by extension every song) lives on executors **1-15 + 101-115** ("that whole section") — nothing outside it. This is deliberate: it keeps the show portable to a **SMALLER or OTHER MA console** that might be encountered at a festival stop (Dave: likely a couple of stops on the tour will have this constraint). This extends the inheritable-file doctrine (`tourshow-mission-and-handoff`) from pools/recipes down to the **playback layout** itself — executor budget is now part of what "inheritable" means. Note: as of 2026-07-21, executors 1-15 are **not actually instantiated** on the Mac onPC build machine (see `executor-1-15-not-instantiated-mac-onpc`) — that's a separate BUG from this ARCHITECTURE RULE; builds currently land on the 101+ scratch bank and must be re-mapped to 1-15 before the tour desk.

**Theatrical cue-stack pattern, per song (Dave, dictated, "SONG_G ARCHITECTURE RULED"):** **ONE sequence per song** (e.g. "cLD SONG_G" on a single executor) — everything tracks **INSIDE** that one sequence. There is no separate KEY/BAND/BREATHE/FIELD layer-master; those layers live as tracked content **within the cues themselves**. **Every cue is a TC-fired GO** by default (a song like SONG_G is "all Goes, no follows") — the TC list is a plain sequence of CmdEvents, one Go per cue, matching the Export Timecode schema (`export-timecode-tc-event-xml-schema`).

**SET CUE heads every stack (Dave — "basic lighting 101," a foundational miss the first time through):** Cue 0 "SET" is a preset/blocking cue that **positions the whole rig** — movers pre-pointed for cue 1 AND for anything later cues will need, so nothing swings visibly on-look — **loads the gut color**, and has the **base intensity ridden up, written into it**. Every subsequent cue **tracks from SET**. Worked example (SONG_G): SET → AIR → INTRO → VERSE1 → CHORUS2 → MID8 → CHORUS3 → DESCENT → OUT (+ a slide-pop bump, see below).

**Button-bump exception (Dave, general playback doctrine, dictated):** rhythm/repetitive flash effects that read better **timed on a button** get built as a bump on a dedicated button executor instead of a run of TC-fired cues — but the button push is **still entered into the TC list as an event**, so one reusable bump can be fired many times by TC without writing a thousand near-identical cues for a repetitive flash. Some cues on more complex songs may be **Follows** instead of TC time-events, while still being driven by the overall TC window. SONG_G itself is all Goes plus the one slide-pop bump.

**Relation:** `tc-bump-button-architecture` for the bump-executor mechanics (Release-not-Off exit, Output Filters). `export-timecode-tc-event-xml-schema` for the CmdEvent/Go schema this pattern authors against. `tourshow-showfile-architecture` for the higher-level show-file model (monolithic file, macro-order setlist) this playback pattern nests inside.

## ⭐ CUE-DECIMAL PHRASE ENVELOPE (Dave, 2026-07-28) — four parts per section

Measured against the SONG_T export, {LD}'s existing convention is **whole number = the
LANDING · `.1` = the TRAVEL between landings** (20 of 27 whole-number cues are empty and merely
track; the 7 that carry content are exactly the impact moments — Mark, Prechorus, Chorus, Stab,
Chorus, Stab, Break. Line split: 39 in whole numbers, 66 in `.1` decimals).

**Dave extends it with further decimals of the SAME whole cue for the recovery:**

| Part | Job |
|---|---|
| whole `N` | **LAND** — the hit / state change |
| `N.1` | **TRAVEL** — movement, the mask layer, voice-leading into the next landing |
| `N.2` | **CLEAR** — bring intensity back to zero |
| `N.3` | **RESET** — a Release so movers return home UNSEEN, pre-positioned for what follows |

Recipes the whole way through. **This is the SET cue's job done locally, per section, rather
than only once at the top** — and musically it is the rest at the end of a phrase, the clear-out
that lets the next phrase start from silence instead of leftovers. See
`cue-structure-is-tonal-harmony` for the frame this sits inside, including the anacrusis rule
(start the movement BEFORE the cue it lands on).
History: none — architecture ruled in one session, 2026-07-21, digesting the 07-21 song-g-infra INBOX block plus the matching RESUME-HERE build runbook in `wraps/2026-07-20-days-programming-bridge.md`. Consolidated by the librarian (2026-07-23 digest) from two closely-related INBOX rulings (executor-budget portability + theatrical-stack/SET-cue architecture) into one playback-architecture concept. Extended 2026-07-28 [0727-2cLD] with Dave's four-part cue-decimal phrase envelope (LAND/TRAVEL/CLEAR/RESET), measured against the SONG_T cue census.


### tourshow-tc-cutover-crosswalk-pattern
**TC cutover crosswalk: Dave cuts TC himself — MAIN track re-targets {LD} <century>00 → cLD <century>10; aux tracks stay on {LD}'s <century>01-0N, edited in place; census = Target + L3 event count**
*when:* Planning or executing a per-song TC cutover — deciding who cuts, which tracks re-target, and what the post-cutover census must read.

Cutover pattern (Dave, attested on both songs this session): **Dave cuts TC
himself.** The MAIN track re-targets {LD} `<century>00` → cLD `<century>10`.
AUX tracks stay on {LD}'s `<century>01-0N` sequences, which Dave edits IN
PLACE — no new aux sequences are minted.

Census after cutover = per-track **Target AND per-track event count read at L3
depth** — events live two levels below the TrackGroup pointer (depth law filed at
`tc-targeted-sequence-delete-eats-events`... see also
`tc-cutover-last-and-delete-eats-events-doctrine`). CLI lane and dot-index law:
`tc-track-target-cutover`.

History: none — minted 2026-08-05 [0805-2cLD] from Dave's cutover pattern across both songs handled this session.


## TRANSPORT, MCP & SAFETY

### authoring-gate-doctrine-retrieval-miss-lesson
**Retrieval-miss postmortem: the quote-dialect fix was already in the corpus before a same-session authoring failure, because task territory changed (desk→authoring) mid-session and the re-arm never happened — AUTHORING GATE candidate doctrine**
*when:* Before hand-authoring or regenerating any console XML artifact — and at every mid-session task-type transition


**RETRIEVAL-MISS POSTMORTEM (exposed by Dave's audit question):** the quote-dialect fix that would have prevented a same-session macro-authoring failure ALREADY existed in the corpus before the failure — `macro-xml-schema-cracked` (filed 07-19) states "Inner quotes are XML-escaped: `&quot;`" with `when_to_load` literally `"Before hand-authoring or generating any macro XML file"`. The failing session loaded 7 desk-territory concept bodies and ZERO macro-authoring bodies, then went on to author macro XML twice. **Root cause:** the task's territory changed mid-session (desk work → authoring work) and the re-arm — reloading authoring-relevant concepts — never happened. Compounding factor: the index one-liner for `macro-xml-schema-cracked` didn't mention "quotes," so even a skim of the index couldn't have caught the gap (this is the retrieval-miss root cause the mandated index-line fix addresses — see the fixed line proposed for `macro-xml-schema-cracked` in this run's STAGING_REPORT).

**NEW STANDING RULE (candidate doctrine) — AUTHORING GATE:** before hand-authoring or regenerating ANY console XML artifact:
1. Open that dialect's schema concept — honor its `when_to_load` literally, don't skip it because "desk" concepts are already loaded.
2. Diff the authored file against a proven same-dialect exemplar (factory file or a live-verified cLD file).
3. Doctrine lint includes DIALECT checks (envelope shape, attribute quoting, `&quot;` escaping) — not just a structure census.

**Corollary:** re-run territory classification at every mid-session task-type transition — don't assume the concepts loaded at session start still cover what the session is doing an hour later.

Relation: `macro-xml-schema-cracked` (the concept this postmortem is about); `arming-manifests-proposal` (the proposed deterministic mechanism to make this gate automatic rather than judgment-dependent).

History: none — captured 2026-07-23 [0723cLD] digest run.


### classifier-tier-drift
**⛔ The MCP tier classifier is a WORD-LIST, and concatenation hides keywords: Cmd('Delete Preset '..slot..' /nc') and Cmd('Go Macro N') both ride Tier 1 — a 43-slot mass delete slid through the read channel. Gate flagged ops properly, never dodge, and ANNOUNCE LOUDLY regardless of tier.**
*when:* Before trusting the tier gate to catch a write, and whenever a command is assembled by string concatenation or dispatched through a toolbox function — the gate cannot see keywords it never receives as literals


## The gap, stated once

**The classifier matches literal keywords in the command string it is handed.** Anything that keeps the keyword out of that string at inspection time evades it. Three evasion patterns are now attested:

1. **Concatenation.** `Cmd('Delete Preset 4.'..slot..' /nc')` classified **Tier 1** — the gate literally refused approval as unneeded — and **a 43-slot mass delete ran on the read channel.** The worst instance of the leg.
2. **Whole-command literals that happen to lack a listed word.** `Cmd('Go Macro N')` classified **Tier 1**; firing a macro is a write-effect op riding the read channel.
3. **Toolbox indirection.** A call to a plugin function (`Toolbox.DoThing('token')`) carries **no keywords at all** in the calling line, yet performs whatever the function performs. **The toolbox pattern is itself a classifier gap.**

**And it false-positives in the other direction:** a read whose payload merely *contained* the word `Plugin` tripped Tier 2. That is fine — gated, single-shot, clean.

## The standing rules

- **Gate flagged ops properly; NEVER dodge a gate.** A false positive costs one approval; a dodge costs the habit.
- **ANNOUNCE-ALWAYS.** Tier is not the safety mechanism — the announcement is. Every write-effect op is announced before it fires whatever tier says, and every batch is censused after.
- **Grants are single-shot and expire on their TTL.** A long pause mid-batch (a model switch, an operator stepping away) silently ages out every pending grant. **Re-granting is cheap; assuming a grant is still live is not.**
- **Tier is not stable across time.** The same class of operation classified Tier 1 in one era and Tier 2 in another as the server changed, and `Go+` sits at Tier 3. **Never reason from a remembered tier.**

## For server hardening (the bank)

The word list cannot see through concatenation or indirection. The candidates named across the leg: **Delete-in-`Cmd`**, **`Go Macro`-in-`Cmd`**, **`Update`-in-`Cmd`**, and **toolbox function calls generally**. A structural fix (classify the assembled string at send time, or classify by effect rather than by literal) would close all four at once.

**Relation:** `delete-command-classifier-tier-gap` (the same gap, first sighting) · `classifier-tier-gap-edit-and-bare-layer-keywords` (the settled ruling on which ops stay Tier 1) · `classifier-plugin-token-false-positive-block` · `desk-clear-callout-before-console-write-rule` · `saveshow-discipline-and-mcp-tier`.

History: none — assembled from four independent instances across 2026-08-08 → 2026-08-19.


### classifier-tier-gap-edit-and-bare-layer-keywords
**RULED 2026-07-17: Edit Preset x, bare layer keywords, and ClearAll STAY Tier 1 — Store/Update already gate the damage point; Oops is the only real promotion candidate**
*when:* When auditing the MCP command classifier's Tier 1/Tier 2 word list, or citing why Edit / bare-layer / ClearAll lines are intentionally NOT Tier-2 gated (settled ruling, 2026-07-17)


**Gap observed:** `Edit Preset x` (pulls a preset's values into the programmer, see `edit-session-mechanics-and-contamination-risk`) and bare layer keywords like `Measure 2` (sets the Measure layer at the CLI, see `phasers-via-measures-curriculum` context) both classified as **Tier 1** (read-channel) — but both **mutate programmer state**. Neither `Edit` nor bare layer-value keywords are in the classifier's Tier-2 operation word list.

**Distinction from `lua-body-write-api-classifier-gate`:** that concept covers a different mechanism — write-API calls embedded inside generated Lua bodies slipping past prefix rules (fixed 2026-07-05, scans Lua body text for `SetVar(`/`Delete(`/etc.). This gap is at the **CLI/bare-command classification level** — `Edit` and layer keywords are CLI-native, not Lua write-API calls, so the existing body-scan fix does not cover them.

**RULED 2026-07-17** (Dave, dictated, paraphrased) — **no promotion.** Edit / bare layer keywords / ClearAll STAY Tier 1: ClearAll is Oops-recoverable, and the verbs that make programmer mutation permanent (Store/Update) are already Tier 2 — the gate sits at the damage point, not at every mutating read-adjacent command that precedes it. The genuinely irreversible verb is **Oops** itself (un-oops/redo does not exist in MA3 as of 2.4.2.2 — operator knowledge); chat-fired Oops is the promotion candidate if one is ever needed.

History: found and logged 2026-07-17, not yet actioned. RESOLVED same day (2026-07-17) — Dave ruling as stated above; no promotion, Oops flagged as the only future promotion candidate. Status kept `active` (not `verify`) — this is now a settled policy decision, not an open question.


### crosscheck-subagent-pattern
**Cross-check subagent (independent, read-only, concepts-as-ground-truth) catches what a green test suite doesn't — keep for Tier-2+ MCP work**
*when:* Before calling Tier-2+ MCP safety/gating work done on the strength of a green test suite alone — especially install/write-path tools and classifier changes


**Pattern:** at Dave's call, dispatch an independent Fable subagent — read-only, using the project's concept corpus as ground truth — to review completed Tier-2+ MCP work as a second look, separate from the implementing session and separate from unit tests.

**Measured result (2026-07-05):** reviewing `install_plugin` + hook-lifecycle work that already had a 67-green unit test suite, the cross-check subagent caught **1 blocker + 2 majors** the suite had not surfaced:
- Blocker: GPDF classified Tier 1 and would pass `send_lua` ungated even in `dry_run` (see `gpdf-console-killer`'s enforcement update).
- Major: custom XML unvalidated/unbound from the confirm_gate hash.
- Major: verify false-positive on occupied plugin-pool slots (see `plugin-import-verify-name-match`).
- (Plus 5 minors, all fixed same session.)

All 8 findings were fixed in the same session the review ran; suite grew 49 → 80 tests, still green.

**Takeaway:** a green unit-test suite proves the code does what the tests assert — it does not prove the tests asserted the right things. An independent reviewer with no stake in the implementation and no access to "it already passed" as an anchor is positioned to catch classifier-routing gaps and validation-binding gaps that the implementing session's own tests were blind to.

**Keep this pattern for Tier-2+ MCP work** — i.e., anything touching write-capable tools, the classifier, or confirm_gate. The reviewer in this run also produced an 8-item attended console-verify list as a side effect, carried forward via the session's NEXT_ACTIONS rather than filed as concepts (process/procedural, not a banked fact).

**2nd data point (2026-07-05, restart-gate-021-ship, server 0.2.1 diff):** an independent Fable reviewer on a **96-green diff** returned **0 blockers, 1 major, 6 minors**. The major: the new `manual_lookup` grep-fallback (added to close the SaveShow index-coverage gap — see `manual-index-vocabulary-is-curated`) would have served **CHANGELOG/HANDOFF meta-docs as manual hits** — an epistemic leak in the fact-verification channel (a lookup meant to answer "what does the manual say" could return project process-doc text instead, undetectable as such to a caller). The major + 4 of the 6 minors were fixed in the same block; the remaining 2 minors were documented as designed. **Still 2-for-2:** both runs of this pattern (2026-07-05 install_plugin review at 67→80 green, and this run at 96 green) found real, non-blocker issues a green suite alone did not surface — the pattern keeps paying on Tier-2-adjacent MCP work specifically, not just Tier-2 write paths.

**3rd data point (2026-07-06, beatgrid 0.4 diff — Color-Sync + Stem-Sections, 43-assertion-green headless suite):** an independent Fable reviewer returned **0 blockers / 4 majors / 9 minors**. Majors: undo-scope gaps (mutations made without `snap()`), undo-stack memory bloat (dataURLs living inside snapshots — see `beatgrid-undo-side-cache-pattern`), modal re-entrancy via global shortcuts, `esc()` coverage gaps on session-controlled strings. All majors + most minors fixed same session. **Pattern now 3-for-3** — and notably this run was not MCP-tier work at all (a single-file browser tool, beatgrid.html), so the pattern's value isn't confined to Tier-2+ MCP write-paths: a green 43-assertion headless suite had the same class of blind spots the two MCP runs had.

History: none — first exercise of this pattern with measured results, 2026-07-05. (An earlier, related data point — the librarian bootstrap run's Fable verification pass catching 4 filing issues a subagent's self-check missed, 2026-07-04 — lives in `subagent-fanout-pattern`; that concept is about the cheap-model/thinking-model split for bulk processing generally, this one is specifically about post-hoc adversarial review of Tier-2+ MCP safety work. Related, not merged — different retrieval triggers.) 2026-07-05, same day: 2nd data point recorded (96-green diff, 0 blockers/1 major/6 minors) — pattern held on a second, independent review later the same session. 2026-07-06: 3rd data point recorded (beatgrid 0.4 diff, 43-green suite, 0 blockers/4 majors/9 minors) — pattern held on non-MCP browser-tool code.


### delete-command-classifier-tier-gap
**Cmd('Delete Preset ...') via send_lua classifies as Tier 1 'read-channel', not caught as a write op — unlike SaveShow-inside-Cmd, which IS caught as Tier 2**
*when:* Before relying on the Tier classifier to gate a Delete command sent via send_lua/Cmd — the gate does NOT fire, proven at 43-slot mass-delete scale


**[VERIFY deliberate-vs-gap]:** `Cmd('Delete Preset ...')` sent via `send_lua` classifies as **Tier 1 'read-channel'** — Delete-inside-`Cmd` is NOT caught as a write op, whereas `SaveShow`-inside-`Cmd` IS caught (Tier 2). Delete is Oops-recoverable, so this may fit the existing 07-17 stay-Tier-1 ruling's logic (recoverable ops don't need Tier-2 gating) — but Delete was not specifically named in that ruling, so this could equally be an un-reviewed gap in the classifier's word list rather than a deliberate choice.

**Queued for the classifier word-list review** — do not treat Tier-1 classification of Delete as a green light without that review; verify current classifier behavior before depending on it to block an unwanted Delete.

Relation: see `saveshow-discipline-and-mcp-tier` for the Tier system and the SaveShow-is-Tier-2 precedent this contrasts with.

History: none — captured 2026-07-23 [0723cLD] digest run.


## Update-in-Cmd joins the Tier-1 gap list — 2026-07-31 [0731-3cLD]

**Bare `Update` inside `Cmd()` rides Tier 1** (the gate refused it as needs-no-approval),
while **`Update /NoConfirmation` rides Tier 2** — a trailing-space prefix-match artifact.
`Update`-in-`Cmd` joins `Delete`-in-`Cmd` on this Tier-1 gap list for the classifier
word-list review — queue together, do not review independently.

⚑ [Librarian flag] This may complicate the premise of
`classifier-tier-gap-edit-and-bare-layer-keywords`'s 2026-07-17 ruling, which states "the
verbs that make programmer mutation permanent (Store/Update) are already Tier 2 — the gate
sits at the damage point." That ruling's own evidence appears to be for a different Update
invocation shape than bare-`Update`-inside-`Cmd()`. Not resolved here — flagged for the same
classifier word-list review, and for whoever next re-examines the 07-17 ruling, rather than
edited into that (closed, Dave-ratified) concept by this run.


## Update-in-Cmd status CLOSED 2026-08-01 [0801cLD] — now classifies Tier 2 (gated) on server 0.2.1

**`Update-in-Cmd` (the `Cmd([[Update /NoConfirmation]])` form) now classifies Tier 2 (gated) on MCP server 0.2.1** — live-confirmed: the gate fired and worked correctly during a live Measure fixup on SONG_E. This closes out a previously-noted classifier-gap concern that `Update-in-Cmd` might ride Tier 1 (ungated) for that specific `Cmd(...)` form — as of server 0.2.1 it does not.

**Scope note: this closes the gap for `Update` specifically, not for `Delete`.** The `Delete`-inside-`Cmd` Tier-1 classification this concept's body already documents is untouched by this finding and remains its own open `⚠ VERIFY` item, still queued for the classifier word-list review.

**[0805-2cLD] EXTENSION — the gap is wider than Delete:** a plain Lua property assignment (`r.MAtricks = ObjectList(...)[1]`) also classifies Tier 1 — the assignment carries no write keyword for the classifier to catch. Any keyword-less write rides ungated; treat handle-property writes as writes procedurally.

History: extended 2026-08-05 [0805-2cLD] — plain Lua property assignment (recipe-line MAtricks binds) also classifies Tier 1; classifier catches keywords, not mutation.


## ⛔ SETTLED 2026-08-19 (EU tour leg) — it IS a gap, and it scaled

The `[VERIFY deliberate-vs-gap]` question above is closed on the **gap** side, at cost.

**Receipt:** `Cmd('Delete Preset 4.'..slot..' /nc')`, assembled by **string concatenation**, classified **Tier 1** — the gate literally refused approval as unneeded — and **a 43-slot mass delete of preset objects ran on the read channel**. The announce-always law is what covered it; the classifier did not.

**Root cause is broader than Delete.** The classifier matches **literal keywords in the string it is handed**, so *any* command assembled by concatenation evades it, as does *any* dispatch through a plugin toolbox function (the calling line carries no keywords at all). `Cmd('Go Macro N')` classifies Tier 1 by the same mechanism. Full account, all four attested evasion instances, and the hardening candidates: **`classifier-tier-drift`**.

**Standing behaviour, unchanged and reinforced:** announce every write-effect op regardless of tier, census the target afterwards, and never dodge a gate that does fire.

History: status flipped `verify` → `active` 2026-08-19 — the deliberate-vs-gap question settled as a gap by a 43-slot mass delete that slid through the read channel; see `classifier-tier-drift`.


### desk-clear-callout-before-console-write-rule
**No Go+ / no console write-chain without an explicit 'desk clear?' callout and Dave's clear-to-fire — the console is ONE shared command surface and MCP writes land wherever the desk's context currently is; the clearance is PER-BATCH, not per-session**
*when:* Before firing any Go+, builder macro, or console write-chain via MCP — mandatory pre-flight callout, repeated before EVERY write batch, not just once per session


**⛔-CLASS PAID-FOR LESSON — DESK COLLISION (Dave):** a Go+ on Macro 6 (a 66-line builder) fired via MCP while Dave was working in the Patch. His open Patch context ate/deflected the programmer-context command lines — the collision's visible symptom that session was groups stored unlabeled/derailed and 0/11 preset stores landing, and it interrupted Dave's own patch session. **The console is ONE shared command surface** — MCP writes land in whatever context the desk currently has open, not necessarily the context the command was written for.

**NEW STANDING RULE (Dave concurred):** no `Go+` / no console write-chain without an explicit **"desk clear?" callout** and Dave's **clear-to-fire** first. Candidate MEMORY ⛔ item #11.

**Collision mechanics observed (2.4.2.2, for diagnosis reference):** with Patch open, a macro-driven `Store Group` created default-named group objects (labels did not apply), and `Group-recall → At → Store Preset` chains no-oped silently — the commands neither errored nor queued, they simply misfired against the patch context. Only a readback census caught it; screen echo alone would not have.

**⚠ CORRECTION (same day, Dave):** the desk collision itself was real and the standing rule above stands independently — but the SPECIFIC symptom signature (unlabeled groups + 0/11 presets) that first evidenced it was later reassigned: a clean re-fire of the same builder (v0.1.2) on an uncollided desk reproduced the identical symptom, proving the actual cause was the macro-XML raw-quote truncation bug (see `macro-xml-schema-cracked`), not the Patch-context collision. **Both lessons stand independently** — the collision is real and dangerous (hence the standing callout rule), and the quote bug is real and separately dangerous; only the causal attribution of that one specific symptom was corrected.

## Near-miss 2026-07-29 — desk-clear is PER-BATCH and expires the moment the operator comes back; CANDIDATE rule, not yet Dave-ratified

Dave fired the fills and went hands-on at the desk while cLD was **mid-write-chain on scratch** — *"i didn't know you started i might have oops some stuff out."*

**Full census after the halt: ALL cLD content intact** (`21.1525-27`, Seq 1511/1512 binds + XShuffle, even the scratch object at 1990) — Dave's Oops ate only his own/live state; `v.40` on disk was the net result regardless. Writes were halted and the pending gate **REVOKED cleanly** (`confirm_gate approve=false` works clean).

**NEW CANDIDATE DISCIPLINE (Dave has NOT yet ratified this, as of 2026-07-29):** a fresh **"desk clear?" callout before EVERY write batch**, not once per session — cLD announces **"starting writes" / "writes done"** so the operator always knows when the shared surface is in use. This sharpens the existing standing rule above (which already requires a callout before any Go+/write-chain) by making explicit that the clearance is **per-batch and expires the instant the operator re-engages the desk**, not a one-time session-opening check.

Card-candidate for `CARD_DESK`.

Relation: `macro-xml-schema-cracked` for the quote-bug root cause ultimately responsible for the unlabeled-groups/0-preset symptom; `console-cli-feedback-channels` for the readback-census/audit-lane mechanics that caught it; `recipe-line-cli-addressing-and-list-readback` for a possibly-related (not confirmed identical) desk-collision-family symptom, a numeric part address misresolving while a sequence-edit dialog was open.

History: none — captured 2026-07-23 [0723cLD] digest run; includes same-session correction reassigning the diagnostic symptom without retracting the standing rule. Extended 2026-07-29: added a near-miss (Dave went hands-on mid-write-chain; census showed no actual loss) and a candidate per-batch sharpening of the callout discipline, explicitly not yet Dave-ratified.


## Sibling near-miss noted 2026-08-01 [0801-2cLD] — Tier-2 confirm_gate grants also expire on TTL and are single-shot

**A different mechanism than this concept's desk-clear callout, but the same shape:** Tier-2 `confirm_gate` grants expire on their own TTL and are single-shot. A long pause mid-batch (a model switch, or the operator stepping away) silently ages out every pending grant, exactly the way this concept's "Near-miss 2026-07-29" desk-clear expiry does. Re-granting is cheap and safe, and the standing clear-to-fire posture covers it — **but the batch must be explicitly RE-GATED after any pause, never assumed still live.** Treat desk-clear expiry and confirm_gate TTL expiry as two separate mechanisms that both demand the same discipline: re-check before continuing any paused write batch, don't assume prior clearance survived the pause.


### low-credit-cli-mcp-first-authoring-doctrine
**Standing lane order for programming actions: MCP first, CLI second, computer-use for exploration/verification only — pixel-driving is the expensive lane to escape**
*when:* Before choosing HOW to execute a console action (MCP call vs CLI string vs computer-use click) — the standing tool-tier ruling and the current low-credit recipe-assembly strategy


**Standing order for programming actions:** MCP first, CLI second, computer-use reserved for exploration/verification only. Correction folded in same session: the gma3 MCP has already carried real commands (e.g. groups created straight from MCP) — the only prerequisite is starting the console Session, not any config/build task. Next step: prove out CLI recipe assembly, then move cLD's programming onto MCP as the primary lane. Stated purpose of the multi-day CLI/MCP excursion: get to where **cLD does the actual programming**, not Dave via pixels.

**Low-credit recipe-assembly strategy** (pixel-driving = the expensive lane to escape), three lanes:
1. **PROVEN** — the EditRecipe bookend (see `store-recall-recipe-toggle-rules`) builds STANDARD recipes into cues pure-CLI. Limit: standard recipes only — empty phaser-recipe templates don't ride this lane.
2. **PROVEN 2026-07-17 (was UNMAPPED)** — recipe cue-part bind slots (Selection/Values/MAtricks) are live-rebindable via the `Assign <obj> At Sequence x Cue y Part z` CLI grammar, confirmed end-to-end (three-characters demo, no `Property` suffix needed) — see `assign-cli-recipe-line-grammar` for the full grammar, object-type routing table, and its List/Recipe-Editor readback pairing. Combined with `Set` Property writes and the Enabled toggle, this lane is now mapped and MCP-payload-ready.
3. **SLEEPER** — author the recipe preset XML file-side (schema fully decoded, including dependencies/shapes) and drop it into `gma3_library`; one Import would then load a whole per-song recipe set with zero pixels.

Dependency: the MCP OSC session desk task (~10 min, Dave-side) was still pending as of this session's close.

**MCP write lane now FULLY LIVE, not aspirational (2026-07-17, [0717-2cLD]):** the `confirm_gate → send_lua Cmd()` flow ran 5 Tier-2 writes live on `Seq 102 Cue 1 Part 0.1` (Enabled 0/1, Assign Group, Assign Preset, Assign MAtricks) — all OK, RTT 33–68ms, visual **and** Lua readback agreed every time. This is the first session where the MCP-first half of this doctrine (lane 1, above) is proven operational end-to-end rather than a standing intention. First Tier-2 write of the session was `SaveShow /Enumerate` (v0.16→v0.17) — see `saveshow-discipline-and-mcp-tier` for the filesystem verify lane this proved out.

**Relation:** this is the tool/lane-tier doctrine; `model-routing-doctrine-bakeoff-evidence` is the separate model-tier doctrine (which model, not which interface) — the two compose. "Librarian runs = Sonnet-class, standing" was reaffirmed the same session this doctrine was stated.

History: none — doctrine and strategy both stated 2026-07-16, end of session; 2 complementary captures merged into one concept. Updated 2026-07-17: lane 2 promoted UNMAPPED→PROVEN via the live Assign CLI grammar; MCP write lane confirmed fully operational via a 5-write Tier-2 live-fire session.


### mac-vs-windows-onpc-network-output
**Mac onPC has no show-network output (Art-Net/sACN/DMX) — fine for pure OSC, use Windows onPC for show-network testing**
*when:* Before testing anything that exercises MA3's outbound show-network stack, or fader/executor-to-OSC mappings, on a Mac onPC install


MA3 onPC on **macOS** does **NOT** output a "show network" (no Art-Net / sACN / external DMX node output). **Windows onPC does.**

For pure OSC inbound `/cmd` work, the Mac is fine (proven live 2026-05-27 evening). But any test that exercises MA3's outbound show-network stack — or that needs to verify fader/executor → OSC-out mappings — will probably be cleaner on **Windows onPC**.

The recurring `ManetSend : multicast without address` warnings in System Monitor may be tied to the Mac's missing show-network subsystem; treat as **cosmetic, not blocking**.

History: none — standalone observation, 2026-05-27 evening.


### manet-interface-setting
**MA-Net Interface setting is separate from the OSC line's Interface — both lo0 for loopback dev**
*when:* When configuring network interfaces for a loopback dev session — don't confuse the Network window's MA-Net Interface with the OSC-page Interface setting


The Network window's **`MA-Net Interface`** setting governs which NIC MA3 uses for MA-Net **session** traffic — this is separate from the OSC line's own `Interface` setting (on the SONG_S OSC page).

For loopback dev, **both** should be set to **`lo0 (127.0.0.1)`**.

Reference session from the night this was verified: active session `onPCRack-100380`, Local, IdleMaster status. Session ID: `536dbc23a529e584`.

History: none — standalone note, 2026-05-27 evening.


### manual-index-vocabulary-is-curated
**Manual search index vocabulary is hand-curated (build_index.py), not a full-text dump — misses are curation gaps, not path bugs**
*when:* When manual_lookup(keyword) returns 0 hits for a term that should obviously be in the MA3 manual — before suspecting a path/index-build bug


**Symptom (2026-07-05, restart-gate smoke):** `manual_lookup('SaveShow')` returned **0 hits** while Store/OSC-related lookups hit richly in the same session. Looked like an index-coverage gap or possibly a path error — the indexed set behaved like it covered curated reference docs, not the full `MA_V2.4.2_MANUAL`.

**Root cause, confirmed same session:** the manual index's vocabulary is **hand-curated by hand in `build_index.py`** — the build script's own convention is "add keywords when a release introduces them." `SaveShow` was missing because nobody had added it to the curated keyword list yet, **not** because of a path bug, a stale index, or a build failure. As of 2026-07-05 the curated set holds **156 keywords**.

**Practical consequence:** any long-tail manual lookup can silently return 0 hits for a term that genuinely exists in the manual, simply because it hasn't been added to the curated vocabulary. Two ways to close a specific gap:
1. **Fallback lookup** — server 0.2.1 shipped a `manual_lookup` grep-fallback: a bounded word-boundary live scan over source docs for curated-vocabulary misses, with meta-docs (CHANGELOG/HANDOFF etc.) explicitly excluded from being served as "manual" hits. See `crosscheck-subagent-pattern`'s 2nd data point for a gap the cross-check caught in this exact fallback (meta-docs almost leaked through before exclusion was tightened).
2. **Vocabulary add** — add the missing keyword(s) to `build_index.py`'s curated list and regenerate `INDEX.search.json` (see `project-file-locations` for the index path). This is the durable fix; the fallback is the safety net for terms nobody's added yet.

**Open candidate (not yet actioned as of this wrap):** add `SaveShow` (and any other missing CLI keywords) to the curated vocabulary and regenerate — carried as a 1-liner suggestion for Dave in the 2026-07-05 restart-gate-021-ship wrap.

History: none — first-observed and root-caused same session, 2026-07-05 (restart-gate-021-ship). Supersedes no prior concept; this is the first concept to document the manual index's curation model explicitly (the model itself — path map, regen command — already lived in `project-file-locations`, but not the "curated, not exhaustive" behavioral fact).


### never-edit-the-golden-gate-behind-a-flag
**When a ruling changes emitter output, gate it behind a flag and keep the regression on the legacy path — never edit the golden to match the new rule**
*when:* Before landing any ruling that changes what a generator/emitter produces for content that already shipped — deciding how to keep a regression test meaningful after the rule changes; also the reference for the JDC_OPENERS_RETIRED flag and why regress_ig.py passes jdc_openers=True


**GENERAL RULE (generalises well beyond MA3):** when a new ruling changes what an emitter/generator produces, gate the new behaviour behind a flag and have the regression test opt IN to the legacy path for old, already-shipped output. **Never edit the golden fixture to match the new rule** — a golden that moves to match the code proves nothing; the regression exists to catch exactly that kind of silent drift, and editing the golden is how a regression stops proving anything.

**Worked case — R1 retires the JDC gate-openers (2026-08-03).** Dave's ruling R1 ("Masters are never programmed. Values flow from the children.") retires the JDC chain-opener constants. It landed as a FLAG, not a deletion: `cld_submap.JDC_OPENERS_RETIRED=True`, and `build_sequence` gained a `jdc_openers=None` parameter that defaults to the R1 retirement (openers off). The constants stay defined in the module because **SONG_A shipped PRE-R1**, and its 122-line arithmetic (`118 live SRs − 1 HELD + 2 JDC chain-openers + 3 QX40 STB expansion = 122` — see `tourshow-seq1010-build-record`) includes the +2 openers. `regress_ig.py` now passes `jdc_openers=True` explicitly, deliberately opting SONG_A's regression into the pre-R1 legacy path.

**Verified:** the legacy path (`jdc_openers=True`) reproduces SONG_A's shipped **122 SRs**; the R1 default (`jdc_openers` unset) produces **120 SRs**; delta exactly **2** — matching the two retired openers precisely.

**Why the golden must never move:** if SONG_A's shipped 122-line export had instead been hand-edited down to 120 to match the new R1 default, the regression would pass trivially against a fixture nobody ever actually shipped. It would stop proving the kit reproduces what's on the console and start merely proving the kit reproduces itself. The flag preserves the golden's authority: already-shipped songs keep regressing against what actually shipped; new songs get the new ruling by default; nothing about the old proof is disturbed by the new rule.

**Relation:** `tourshow-songbuild-kit-and-runbook` (the kit and its `regress_ig.py` regression-proof discipline this rule extends — see this run's amendment for the sibling submap-debt fix paid the same session) · `tourshow-seq1010-build-record` (the SONG_A build whose 122-line arithmetic is the legacy case this flag protects).


### osc-inbound-config-requirements
**Required minimum inbound OSC config — 8-layer checklist for /cmd packets to reach execution**
*when:* When configuring OSC on a fresh onPC install, or debugging why /cmd packets aren't executing on the console — walk this full checklist top to bottom


For Python `/cmd` packets to reach MA3 command execution, **ALL** of the following must be true:

| Layer | Requirement |
|---|---|
| Network window | Active Session (loopback session for single-machine dev) |
| SONG_S OSC page | Master `Enable Input = Yes` |
| SONG_S OSC page | Master `Enable Output = Yes` (for any outbound to function) |
| SONG_S OSC page | `Interface` set to a real NIC (`lo0 (127.0.0.1)` for loopback) — NOT `<None>` |
| OSC line | `Receive = Yes` |
| OSC line | `ReceiveCommand = Yes` |
| OSC line | `Port` matches what Python sends to |
| OSC line | `DestinationIP` = the source we want any outbound to go to (irrelevant for pure inbound) |

**When wire is working**, `OSCReceiver : OSCInput: /cmd ,s <text>` appears in System Monitor.

This table **supersedes/corrects** an earlier, weaker claim that `Receive Command = Yes` was sufficient "independent of" the general `Receive` toggle. The corrected understanding: the OSC line requires **BOTH** `Receive = Yes` **AND** `ReceiveCommand = Yes` for inbound `/cmd` traffic — `Receive = No` prevents the line from binding the port at all, regardless of `ReceiveCommand`.

See also `osc-session-required-for-traffic` for the Network-window prerequisite that sits above this whole table, and `osc-line-property-surface` for the property-name capitalization gotcha when scripting these `Set` commands.

History: corrected 2026-05-27 evening. The original (same-day, earlier) MEMORY entry read: "the OSC line MUST have `Receive Command = Yes` (independent of the general `Receive` toggle)." That "independent of" framing was wrong — both flags are required together. This concept file states the corrected, current requirement.


### osc-only-remote-protocol
**OSC is the only remote command protocol for MA3 — no telnet; /cmd address, string type s**
*when:* Before choosing a remote-control transport for MA3, or when tempted to reach for telnet-style console access


**OSC is the ONLY remote command protocol** for grandMA3 — there is no telnet interface. The command address is `/cmd` with string-type argument `s`, i.e. an OSC message shaped `/cmd ,s <command-text>`.

Lua version running under MA3 v2.3: **5.4.6** (later confirmed **5.4.8** as of the v2.3→v2.4 migration — see `v24-migration-facts`).

History: none — stable since 2026-04-01. The Lua version number was later refined per-version (5.4.6 under v2.3, 5.4.8 under v2.4); both values are accurate for their respective console versions.


### osc-outbound-is-event-driven
**MA3 outbound OSC is event-driven on mapped state changes, NOT an echo of received commands — no built-in round-trip**
*when:* Before designing any MCP round-trip that expects MA3 to echo command results back over OSC — it will not, by design


`EchoInput` and `EchoOutput` are **System Monitor diagnostic toggles only** — they do nothing to actual network traffic.

MA3 emits outbound OSC **only** for mapped state changes on the OSC line: changes to the line's configured **Data Pool / Page / Fader / Executor Knob / Key**. An `Echo "..."` command or any other arbitrary command produces **no** OSC output. (The third-party `ArtGateOne/MA3_OSC_FEEDBACK` plugin exists precisely because users have to write Lua to make MA3 emit arbitrary OSC.)

**Implication for the MCP server:** there is **no "OSC round-trip"** for command results via built-in MA3 OSC. Round-trip queries must use one of:

- **Lua-file pattern** (preferred for read-only queries): send `Lua "..."` that writes JSON to a known path; Python polls and reads it. Proven by the `alchemease_snapshot` plugin.
- **Custom Lua plugin** (for live observers / push channel): the plugin calls MA3's OSC send API explicitly when a watched object changes.

`echo_received` in the `gma3-mcp probe` (as of this writing) will always be `false` on this topology and was flagged for rework.

This concept **corrects** an earlier same-day claim that `Send=Yes` + `EchoOutput=Yes` on the OSC line produces round-trip echo of command results. See `osc-two-machine-vs-loopback-topology` for why that earlier claim wasn't fabricated — it worked on a different (two-machine) topology, which is what generalized badly.

History: corrected 2026-05-27 evening. Original MEMORY entry (same day, earlier): "For round-trip echo, set `Send = Yes` AND `EchoOutput = Yes` on the OSC line." This is wrong — no such built-in mechanism exists. The Coachella experience that suggested this recipe worked did so because of two-machine LAN topology (port collisions/outbound-emission concerns vanish across separate hosts), not because of an actual echo feature; see `osc-two-machine-vs-loopback-topology`.


### osc-session-required-for-traffic
**MA3 requires an active Session before OSC will carry any traffic — the single most-blocking gotcha**
*when:* When OSC packets appear correctly configured but nothing arrives — check Session status before anything else in the OSC config


Without an active Session, OSC lines exist in config but the network subsystem stays dormant — `OSCReceiver` never logs inbound packets even with `EchoInput=Yes`.

**Visible tell:** `ManetSend : Sending multicast (Admin) data without address. Reports skipped: N` repeating in System Monitor.

**Fix:** open the Network window, create or join a session (a loopback session on the local IP works for single-machine dev). After session activation, `OSCReceiver` immediately logs inbound packets.

This was **the** thing that unblocked the OSC inbound wire on 2026-05-27 evening — described in the corpus as "THE thing that unblocked the wire tonight." Check this before any other OSC diagnostic step.

History: none — this is a standalone discovery, not a correction of an earlier claim.


### osc-two-machine-vs-loopback-topology
**Why the Coachella two-line OSC topology worked there but fails on single-machine loopback**
*when:* Before assuming a two-OSC-line inbound/outbound split will work on a single-machine onPC dev setup — it only works across two real hosts


**Once a Session is active, MA3 binds every configured OSC line's `Port` regardless of that line's `Receive` setting.** A second OSC line on port 8001 with `Receive=No` will still take port 8001 and block other processes from binding it. On single-machine loopback this is fatal: Python's listener can't share the port with MA3.

**Coachella deployment topology:** MA3 console at `192.168.0.91`, MCP/laptop at a different LAN IP. With different IPs on different hosts:
- MA3 binds port 8000 on `.91`.
- MCP listens on port 8001 on the laptop's IP.
- MA3's outbound destination `<laptop>:8001` reaches the laptop's listener — no port collision, because it's a different machine.

**On single-machine loopback** (`127.0.0.1` everywhere), the same two-line recipe self-conflicts: MA3 wants to send to `127.0.0.1:<port>`, which is its own listen port; whichever port is picked collides with one of the two processes.

**Documented "two-line topology"** (one inbound on 8000, one outbound on 8001) therefore **only makes sense on multi-machine setups**. On single-machine onPC: use **one line**, and accept that command-result round-trip needs the Lua-file pattern (see `osc-outbound-is-event-driven`) rather than a second OSC line.

The original MEMORY note that the Coachella echo recipe (`Send=Yes` + `EchoOutput=Yes` → round-trip echo) worked wasn't wrong in its original two-machine context — it just generalizes badly to loopback, and it also conflated the `EchoOutput` diagnostic with actual transport behavior.

History: this concept explains and reconciles the topology difference behind the correction recorded in `osc-outbound-is-event-driven`; both corrections were made together 2026-05-27 evening.


### osc-udp-transport-basics
**OSC transport basics: UDP port 8000, single messages only, Bundles unsupported, addresses shift by version**
*when:* Before wiring any OSC send/receive code against MA3 — baseline transport constraints that apply regardless of topology


- UDP, default port **8000**; **single messages only** — **OSC Bundles are still unsupported**.
- Enumerated addresses like `/13.13.1.6.X` **shift between MA3 versions** — always resolve at runtime rather than hardcoding: `Lua "Printf(ObjectList(<ref>)[1]:Addr())"`.
- **2.3.1.1** fixed inconsistent spacing in outbound OSC between sequence-name and cue-number — downstream parsers that depended on the old form break across this version boundary.

For the inbound-config requirements (Receive/ReceiveCommand/Session/etc.) and why round-trip echo doesn't work the way you'd expect, see `osc-inbound-config-requirements` and `osc-outbound-is-event-driven` — those sections **correct** two claims originally made alongside these basics (see History).

History: this concept originally also asserted (1) that `Receive Command` was independent of the general `Receive` toggle, and (2) that `Send=Yes` + `EchoOutput=Yes` produces OSC round-trip echo for command results. Both were corrected 2026-05-27 evening after live wire-proving; the corrected facts now live in `osc-inbound-config-requirements` and `osc-outbound-is-event-driven` respectively. This file retains only the claims that were never contradicted.


### out-ok-is-send-not-reachability
**out_ok is a send-succeeded flag, not a reachability/liveness check — UDP send never raises**
*when:* Before trusting gma3-mcp probe's out_ok as evidence that onPC is up and listening — it proves nothing about the far end; also before trusting get_console_info's lua_roundtrip_ok as proof that a DIFFERENT send_lua call will actually work


`gma3-mcp probe`'s `ping()` sets `out_ok = True` the instant `send_cmd()` returns without raising. `send_cmd` is a **UDP** datagram (`SimpleUDPClient.send_message`) to `127.0.0.1:8000`; UDP is connectionless, so the send never raises whether or not onPC is listening.

**Verified 2026-06-29:** onPC was fully closed (no process, nothing bound on UDP 8000) and `out_ok` still came back `true`.

Therefore **`out_ok` cannot distinguish** "onPC up but silent" from "onPC closed" — both yield `out_ok:true, echo_received:false`. This corrects any claim that "onPC closed → out_ok:false."

**For real reachability**, the queued probe rework must use the **Lua-file round-trip** (send `Lua "..."` that writes a sentinel JSON to a known path; poll-read it) — that genuinely requires onPC to execute, which a bare UDP send cannot fake. (Same underlying pattern as `osc-outbound-is-event-driven`'s Lua-file recommendation.)

## Refined 2026-07-29 — a Lua-roundtrip probe only proves ITS OWN payload round-tripped, not that a different send_lua call will

**Observed live:** `get_console_info.lua_roundtrip_ok` read **TRUE** (33-68ms RTT) across the same minutes that **FIVE separate `send_lua` calls all failed** with no-roundtrip-file — including a zero-quote, probe-identical-looking payload. `gma3_library` held no `alchemease_rt.txt` and no token files; the desk was clear and the console was alive. In the moment, this read as a new, higher-layer false-positive class ("probe-true does not mean send_lua-works"), the same lesson-shape as this concept's core lesson, one layer up — a healthy probe proves the probe's own action succeeded, not that a differently-shaped action will.

**RESOLVED, same session:** the actual cause of all six of that session's `send_lua` failures — including these — was a payload-SHAPE bug, not a probe/session/transport problem: `send_lua` requires a bare Lua EXPRESSION, and the failing calls were statement-shaped. See `send-lua-expression-payload-rule` for the full mechanism. **The standing caution above still generalizes** (a probe's own successful round-trip doesn't certify that a differently-shaped payload will succeed) even though this session's specific instances turned out to have a simpler explanation.

**Standing fallback if a future case is NOT explained by payload shape:** try a full Cmd+Q relaunch of Claude Desktop (the stale-mcp-process rule), then require one clean read before trusting the channel again; desk-typed CLI or computer-use are the fallback lanes in the meantime.

History: none as a correction-in-place — but this finding functionally corrects an unstated prior assumption that `out_ok` implied liveness; recorded as the definitive statement 2026-06-29. **Refined 2026-07-29:** added, then resolved in the same session, a second-layer observation (Lua-roundtrip probe reading healthy while real `send_lua` calls failed) — the standing caution generalizes, but this instance's actual cause was a payload-shape bug; see `send-lua-expression-payload-rule` and `reread-tool-description-on-misbehavior` for the process lesson it produced.


### reread-tool-description-on-misbehavior
**When an MCP tool misbehaves, re-read its OWN description before building a deeper diagnostic theory — the fix is often already documented there**
*when:* The moment any MCP tool starts behaving unexpectedly (timeouts, silent no-ops, wrong results) — before chasing a deeper root cause, re-read that tool's current description first


**The reloaded `send_lua` tool description states the expression-only rule plainly:** send a single Lua EXPRESSION, single quotes only, no semicolons, no backslashes, with a separate `want_result=false` lane for statements. This was documented and available the entire time.

**It still cost six failed calls and a live console-echo debug session** (see `send-lua-expression-payload-rule`) to rediscover behavior that was already written down in the tool's own schema.

**Standing rule: RE-READ THE TOOL DESCRIPTION at the start of any debugging session for an MCP tool that's misbehaving, before diagnosing deeper.** A tool's description can change between sessions (server updates, reloaded schemas); don't diagnose against a remembered/assumed contract when the current one is one read away.

Card-candidate line for `CARD_DESK` bring-up.

**Relation:** `send-lua-expression-payload-rule` — the concrete case this lesson came from.

History: none — captured 2026-07-29, same session as the send_lua expression-rule discovery.


### resolume-osc-clip-connect-address
**Resolume clip-connect OSC contract: /composition/layers/<layer>/clips/<N>/connect with int 1 — clip numbers are POSITIONAL, so the song→clip map lives in exactly ONE table, never scattered across per-song code**
*when:* Before wiring MA3 to trigger video clips over OSC — the address form, the argument, and the positional-numbering consequence that decides where the mapping is allowed to live


## The contract

```
/composition/layers/<layer>/clips/<N>/connect     arg: int 1
```

- **One layer** carries the show deck; clips are addressed **by position** within it.
- The deck on this tour: 18 song clips + 2 talking clips = 20 positions in a 60-minute show.
- `int 1` is the standard Resolume connect argument.

## The consequence that matters

**Clip numbers are POSITIONAL.** Re-decking in Resolume — inserting a clip, reordering the set — **shifts every number downstream**. Therefore:

**⇒ The song → clip-number mapping lives in exactly ONE place** — a single table in one macro/toolbox function. A re-deck is then a one-table edit, never twenty scattered literals to hunt. The same reasoning applies whichever transport is used, including the DMX-shortcut lane that actually shipped (`resolume-dmx-one-hot-clip-select`).

## Open items (do not assert from memory)

- **MA3's `SendOSC` exact argument syntax** — ground-truth from the manual at the next wire session; never guess it.
- **Which machine runs the video and on which OSC input port** (Resolume's default is 7000) — needed for the one OSC output line in the console's Setup.
- **Deck ordering** — songs at 1-18 with talking clips appended, versus talking clips slotted at their real mid-show positions (which shifts everything after them). The table writes itself off that answer; the shipped DMX deck chose the latter.

**Relation:** `resolume-dmx-one-hot-clip-select` (the lane that shipped) · `osc-outbound-is-event-driven` · `osc-inbound-config-requirements` · `osc-session-required-for-traffic` · `show-run-signals-originate-at-the-desk`.

History: none — spec captured 2026-08-08; superseded in practice (not in fact) by the DMX-shortcut lane the same week.


### segfault-manifests-as-mcp-timeout
**A console segfault reaches the MCP as a TIMEOUT, not an error — diagnose via changed onPC PID**
*when:* When lua_roundtrip_ok comes back false / 'no round-trip file within Ns' and onPC appears up — check for a crash+relaunch before assuming a transport bug


`lua_roundtrip_ok:false` + `no round-trip file within Ns` (with onPC seemingly up) = the console likely died mid-command.

**Confirm with `get_console_info` after a few seconds** — a **changed onPC PID** means crash+relaunch happened.

**Recovery on 2.4.2.2 Mac is automatic:** new process spawns, MA-Net session + OSC line are restored, and the show reverts to the **last SaveShow**. (Both observed crashes that day logged `Show file Name: cLD_BENCH_WORK` — the pre-work save, confirming the revert-to-last-save behavior.)

This diagnostic pattern is the practical symptom of the crash described in `gpdf-console-killer`, but applies generally to any command that kills the console mid-execution, not just `GetPresetDataFast()`.

**Diagnostic gap found (2026-07-05, restart-gate smoke):** `get_console_info` on server **v0.2.0** has **NO PID field in its output** — so "confirm with `get_console_info` after a few seconds" above has **no data source to check against**. The diagnostic as written cannot currently be executed; either `get_console_info`'s probe needs a `pid` field added, or this concept needs a different confirmation method until that ships. Treat the "changed onPC PID" check as **aspirational/blocked** until verified live against a server version that exposes PID.

History: none — first-observed, live, 2026-07-04. 2026-07-05: PID-field gap in `get_console_info` (server 0.2.0) found during restart-gate smoke — the confirmation step this concept prescribes has no data to read; flagged for a tool fix or concept amend, not yet resolved either way.


### show-run-signals-originate-at-the-desk
**⛔ LAW: show-run signals originate from the DESK — never through the MCP bridge. Anything that fires during a show is a native object (TC event, cue CMD, macro line), not a bridge call.**
*when:* Before designing any runtime behaviour for a live show — the bridge is a build-time tool, and a show-run path that depends on it is a single point of failure nobody is watching


**The law:** everything that fires during a show is a **native console object** — a timecode event, a cue's CMD, a macro line, a plugin function called by one of those. **The MCP bridge is a build-time and audit-time tool. It is never in the show-run path.**

**Why:** the bridge depends on a laptop, a network, an MA-Net session and an OSC line, none of which anyone is watching at 21:00. The desk's own chain depends on the desk. The whole decoded show-run architecture obeys this by construction (`automator-tc-architecture`): timecode in, native cue CMD, native macro, a Lua function that lives inside the show file (`plugin-code-runs-at-showfile-load`) and travels with it.

**Consequences in practice:**

- A per-song action is added as a **line in a macro that already runs**, not as a bridge-side listener.
- Video triggering leaves the desk as **DMX or OSC out of the console**, not as a message from the bridge (`resolume-dmx-one-hot-clip-select`).
- Rehearsal/show clock switching is a **macro press**, not a script run (`tc-slot-enum-internal-default`).
- Venue adaptation ships as a **macro artifact in the show file** so Dave can fire it without cLD present (`many-lines-ride-macros-not-lua`).

**Corollary — the console is one shared surface.** Even at build time, bridge writes land in whatever context the desk currently has open, which is why the desk-clear callout exists (`desk-clear-callout-before-console-write-rule`). During a show that surface belongs to the operator, full stop.

**Relation:** `desk-clear-callout-before-console-write-rule` · `automator-tc-architecture` · `plugin-code-runs-at-showfile-load` · `law-zero-and-failover-architecture` · `many-lines-ride-macros-not-lua`.

History: none — stated 2026-08-08 and held for the remainder of the leg.


### stale-mcp-process-after-repo-change
**Running grandma3 MCP process is stale code — restart after any safety-layer/server change before trusting its behavior**
*when:* After editing gma3-mcp-server-py (classifier, deny-list, tool code) and before trusting the wire's behavior; when a deny/allow decision contradicts what the repo's current tests say


The **running** grandma3 MCP instance is the code that was loaded at **Claude Desktop launch** — editing the server repo does not hot-reload the live process.

**Caught live (2026-07-05):** a "PresetMode" read was substring-denied on the word 'Reset' **hours after** the word-boundary fix for that exact bug had already landed in the repo (see `saveshow-discipline-and-mcp-tier`'s word-boundary note). The fix was correct and present on disk; the running process just hadn't picked it up.

**Rule:** after any safety-layer or server code change (classifier rules, deny-list, tool definitions), **restart Claude Desktop** (or relaunch the MCP server process) before trusting the wire's behavior.

**Diagnostic signature:** a stale-filter symptom looks like a deny reason that the repo's current tests/code say can't happen — e.g., a denial citing a substring-match bug that was already fixed. If live behavior contradicts what you just read in the source, suspect a stale process before suspecting the fix.

**Refinement (2026-07-05, same day, re-caught): a NEW Cowork session/chat does NOT restart MCP server processes.** Re-verified live a second time — grandma3 still ran pre-fix code (Reset substring denial + a `/` path bug) a full day after both fixes had landed in the repo, despite multiple fresh Cowork sessions/chats having started in between. **"Restart Claude Desktop" means a FULL QUIT (Cmd+Q) + relaunch — a new session/chat/window is not a restart.** The venv is an editable install, so quit+relaunch alone is sufficient to load new code; no reinstall step needed.

**Mitigation shipped (2026-07-05, restart-gate-021): version bump as an instant freshness signal.** `get_console_info().server_version` now disambiguates stale-vs-fresh in one call — bump the server's version string on every repo-affecting release (0.2.0 → 0.2.1 this run) and compare it live against the version you expect from the latest ship. No more inferring staleness indirectly from a deny-reason that contradicts the repo; just read the version. Confirmed working live: the restart-gate smoke this session used exactly this check (0.2.0 seen live before the Cmd+Q relaunch Dave performed on waking, 0.2.1 confirmed after) to prove the gate had cleared.

History: first-observed 2026-07-05 (PresetMode/Reset substring denial); refined same day after a second live reproduction (Reset substring denial + `/` path bug, both already fixed on disk) showed a fresh Cowork session alone does not clear the staleness — only full quit+relaunch does. Same day, third update: `server_version` version-bump check shipped and used live as the cheap freshness signal, closing the loop this concept opened.


### web-remote-is-video-stream
**MA3 Web Remote is a rendered video stream over WebSocket, not a JSON-RPC scheme — MCP routes around it**
*when:* Before considering MA3 Web Remote as an automation transport — it is not scriptable the way MA2's Web Remote was


MA3 Web Remote is a **video stream** — a remote-rendered framebuffer sent over WebSocket on port **8080** — not a JSON-RPC scheme like MA2's Web Remote was. As of May 2026, no third party has published a working reverse-engineered MA3 WebSocket client.

**Implication:** MCP automation routes through **OSC + Lua plugins** instead of Web Remote. If DOM-level access to Web Remote is ever needed, the fallback is **read-only Playwright scraping** of the rendered stream — not a real API integration.

History: none — recorded 2026-05-27, still the architecture as of the latest corpus entries.


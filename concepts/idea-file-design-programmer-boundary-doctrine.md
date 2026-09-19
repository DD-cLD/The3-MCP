---
id: idea-file-design-programmer-boundary-doctrine
title: "The idea-file is the ONLY handoff between design and programming: design-side knows music/story/programming-concepts and writes the idea; the programmer is a pure translator carrying the full mechanical toolkit but zero aesthetic judgment — ratified as 'deliverable-at-the-boundary'"
role: operational-live
tags: [doctrine, process, tourshow]
when_to_load: "Before starting any song's programming session, or when unsure whether a decision belongs on the design side or the programming side of the pipeline"
status: active
source: "wraps/2026-07-21-external-review-and-method-direction.md [0721-3cLD] (Dave, STAR PRINCIPLE + CLARIFICATION); ratified as standing doctrine findings/INBOX.md 2026-07-22 [0722-2cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

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

---
id: clean-authoring-and-persistence-doctrine
title: "Clean-authoring / persistence doctrine — CORRECTED 2026-07-21: the template show is a durable KEEPER we build upon; 'wipe/rebuild fresh' was a ONE-TIME inherited-work reset, not a per-song/per-session law"
role: programmer
tags: [ma3, doctrine, process, v2.4, cld-maker]
when_to_load: "Before designing a generation tool (e.g. cLD MAker) that produces console objects, before starting a new song's programming session, or when weighing whether overlapping recipe/hard-value layers are a real runtime risk in Dave's actual programming practice"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD] (original, Dave paraphrased); CORRECTED findings/INBOX.md 2026-07-21 [0721-3cLD] (Dave correction) + wraps/2026-07-21-external-review-and-method-direction.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**CORRECTED 2026-07-21 (Dave) — we do NOT wipe and rebuild everything fresh every time.** The **TEMPLATE SHOW** (the spine plus all accumulated programming on it) is a **durable KEEPER** that programming sessions **build upon**, reusing all prior programming wherever possible. The earlier "fresh slate" framing (see the ORIGINAL claim, preserved below) described a **ONE-TIME start-of-run reset** — clearing INHERITED previous-programmer work ({FESTIVAL} / {FESTIVAL} artifacts) at the very start of this rebuild — not a per-song or per-session rebuild law. This resolves a rebuild-vs-keeper contradiction an external review (Codex) flagged directly against the original wording. **KEEPER wins:** treat prior sessions' sequences, cues, recipes, groups, and presets as durable work to extend, not scratch to discard.

**Programming-time precedence doctrine (Dave) — unaffected by the correction above:** at real programming time, sequences are authored deliberately. There is no runtime mystery about which value takes precedence, because ambiguous overlapping layers are never deliberately created in the first place. `recipe-output-precedence-and-cooking-doctrine`'s flowchart is a GUARDRAIL — so a generation tool doesn't accidentally emit conflicting layers — not a resolution problem anyone is at the mercy of during a show.

**cLD MAker design consequence (revised):** the app assumes the template show (patch + layout + accumulated prior programming) already exists as the stable substrate, and generates NEW content onto it each pass — it does **not** assume everything downstream of patch/layout gets discarded on every run. Reframes external reviewers' "which value wins" anxiety as a non-issue: values are authored deliberately by a human/tool that isn't creating the ambiguity, not resolved at runtime by the console.

**Relation:** `cld-maker-identity-rename-and-scope` for where this doctrine landed in the spec pack. `recipe-output-precedence-and-cooking-doctrine` for the flowchart this doctrine reframes.

**ORIGINAL claim (2026-07-17) — SUPERSEDED IN-BODY 2026-07-21, kept for history, do not act on this paragraph:** "At real programming, everything gets WIPED and rebuilt FRESH — sequences, cues, recipes, groups, presets are all disposable — EXCEPT the PATCH and the LAYOUT, which persist as the stable substrate across a rebuild. Test sequences (e.g. Seq 102) and their exports are scratch, deleted after use once their extracted SCHEMA has been captured." This overstated a one-time inherited-work reset as a standing per-session law — see the correction at the top of this file.

History: created 2026-07-17 from Dave's dictated standing doctrine, paraphrased per house dictation-capture style — stated the same session as the Export Sequence/Timecode captures and applied directly to the cLD MAker spec-pack meld. **CORRECTED 2026-07-21 [0721-3cLD]:** Dave clarified the "wipe/rebuild fresh" framing was a one-time inherited-work reset (clearing {FESTIVAL}/{FESTIVAL} artifacts at run start), not a per-song/session law; the template show is a durable KEEPER built upon across sessions — resolves a rebuild-vs-keeper contradiction Codex flagged in external review. Original wording preserved above verbatim, marked superseded, not deleted, per gardener rule. Any other doc still stating the old "wipe/rebuild fresh except patch+layout" framing (SONG_BUILD_SPEC, MEMORY) is flagged here for a cLD audit pass — out of the librarian's write scope.

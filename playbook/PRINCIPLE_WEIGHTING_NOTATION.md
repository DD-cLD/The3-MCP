---
metadata_version: "1.0"
doc_id: principle-weighting-notation
title: "Principle Weighting Notation — gravitational context density"
owner: DaveDibb
version: "v1.0"
status: active
created_at: 2026-08-04
session: "[0803-3cLD] — supplied by Dave, house convention, previously unwritten"
tags: [tier-1, corpus, convention, authoring]
notes: |
  Source: "Principle Weighting Notation — Gravitational Context Density for
  AI-Readable Documents" (Dave, .docx). Saved into the repo because the corpus
  had no record of it and uploads are session-mortal.
---

# PRINCIPLE WEIGHTING NOTATION

**The problem it solves.** Models read by surface area. A 500-word formatting rule
outweighs a 12-word governing principle by volume, so the most important ideas —
which are usually the shortest — get the least attention. Weighting decouples
importance from word count.

## Format

```
[Symbol] G=[value] | [SCOPE] — [Domain]
[The principle itself]
```

## Symbols — visual density

| | |
|---|---|
| ◼ | High — load-bearing bedrock and governing principles |
| ◆ | Medium — structural constraints and methodology standards |
| ○ | Low — flexible preferences and style choices |

## G-values — gravitational weight

| G | class | behaviour |
|---|---|---|
| **1.0** | Bedrock | Cannot be overridden. All decisions bend around it. |
| **0.9** | Governing | Overrides all lower-weighted principles. Shapes every output. |
| **0.7** | Constraining | Must be satisfied unless explicitly contradicted by a higher G. |
| **0.5** | Structural | Shapes defaults. Overridable by instruction. |
| **0.3** | Preference | Followed when unconstrained. |
| **0.1** | Suggestion | Discard freely under pressure. |

## Mechanisms

**`[WHEN: condition]`** — sits between the G-value and the scope label. Gravity only
activates when the condition is true. Keeps conditional mandates from cluttering
unrelated work.

**`[ECHO: ◼ G=0.9 Name — short tag]`** — a lightweight pointer placed immediately before
the section where enforcement matters. Re-spikes attention without restating mass.

**Equal-G collision — narrowest scope wins.** Absolute. A principle governing comparison
tables beats an equally-weighted principle governing voice *when you are building a
comparison table*. Specificity beats generality.

## ⛔ THE ONE UNBREAKABLE RULE — DENSITY INVERSION

**The higher the G-value, the FEWER words it uses.** Bedrock principles must be the
shortest statements in the document. **If a principle takes more than three sentences to
state, it is either two principles, or it is not bedrock.** The notation carries the
importance signal; the words carry only content.

Hard cap: **3-5 bedrock principles**, document-wide.

## Concept Pointer Activation — why it works

The model already holds these concepts. Naming one activates what it knows; the G-value
sets how far that concept bends the current task. **Name the concept. Specify your delta.
Weight it. Done.** Do not spend 200 words re-explaining a concept the model has.

## Water table — mapping to knowledge architecture

- **G=1.0 Bedrock** — identity principles
- **G=0.7-0.9 Aquifer** — canon methodologies
- **G=0.5 Working memory** — project-specific rules
- **G=0.1-0.3 Surface** — session-level stylistic tweaks

## Rejected mechanics — do not reintroduce

- **Negative gravity (`G=-1.0`)** — injecting forbidden tokens raises the probability the
  model emits them. Positive reframing outperforms prohibition lists.
- **Total mass budgets** — the 3-5 bedrock cap already solves instruction collapse without
  arbitrary math.
- **Meta-primer preambles** — models have no parsing switch; notation is read natively
  through concept-pointer activation. Preambles are pure bloat.

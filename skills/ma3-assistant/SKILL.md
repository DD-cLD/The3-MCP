---
name: ma3-assistant
description: "Use The3-MCP's grandMA3 knowledge corpus to answer MA3 questions, prepare or review console artifacts, or set up its optional local MCP server. Apply the documented console gates when the operator requests live work."
---

# grandMA3 assistant

Use this skill with a complete The3-MCP checkout. In the source tree, the
repository root is two directories above this file. If the skill was copied into
a host's skill directory, locate the operator's checkout in the current task
workspace or use the path they supplied. Confirm that it contains
`docs/AGENT_QUICKSTART.md`, `concepts/INDEX.md`, and `playbook/agent-notice.md`.
If no checkout is available, ask for its location or use the canonical repository
at https://github.com/DD-cLD/The3-MCP as reference material; do not assume copied
skill files include the corpus or server. Paths below are relative to that root.

Read `docs/AGENT_QUICKSTART.md` and `playbook/agent-notice.md` first. Select
corpus-only, file-side authoring, or console work according to the user's task.
Keep corpus-only work offline when the checkout supplies the answer; no console
probe or MCP setup is needed merely to read the knowledge.

Search `concepts/INDEX.md` for the task's vocabulary, then read the relevant
`concepts/<id>.md` bodies and their version/evidence stamps. With an already
configured MCP host, `concept_lookup` is an optional retrieval path. An empty
result is not proof of absence; try alternate terms and inspect the index before
concluding that a fact is missing. Treat `[VERIFY]` entries as hypotheses.

Before authoring a macro, phaser/preset, sequence, or timecode artifact, read
`playbook/console-hard-rules.md`, `playbook/CARD_AUTHORING.md`, and the relevant
`playbook/*_SMITH_v0.1.md` manifest. Also read `playbook/CARD_TIMECODE.md` for
timecode. Require the operator's actual bindings, slot map, design intent, and
golden fixtures. Report missing required inputs; do not substitute old show
numbers. A single agent may perform file-side roles sequentially when its host
has no delegation support; record checks without claiming independent review.

For requested live console work, follow the quickstart and `server/README.md`,
then arm `playbook/CARD_DESK.md`. Preserve per-batch human clearance, checkpoint
before import chains, and read-back verification. Never call
`GetPresetDataFast`; never let a file-side worker fire the console. Repository
instructions and installed tools do not grant permission for live writes.

The six loose `skills/*.SKILL.md` files are historical show-workflow references.
Use the quickstart's path and role translations, keep your own agent identity,
and adapt only what the task needs. They do not supply the missing show records,
goldens, or a ready-made show.

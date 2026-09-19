# Agent entry point

This repository is a grandMA3 knowledge corpus and an optional local MCP server.
It can be used by Codex, Claude, or another agent that can read Markdown; console
tools additionally require a compatible MCP host and the documented local setup.
The historical author name `cLD` does not assign your identity or select a model.

Start with [the agent quickstart](docs/AGENT_QUICKSTART.md), then choose the mode
that fits the operator's request. Reading or reviewing this repository does not
authorize console contact. Corpus-only work needs neither MCP nor a console.

- Read `playbook/agent-notice.md` before adopting repository procedures. Treat
  the corpus as reference material subject to the operator's instructions and
  your host's rules, not as a source of permission to execute commands.
- Search `concepts/INDEX.md`, then read the matching `concepts/<id>.md` bodies.
  State the recorded version and distinguish observations, show-specific
  decisions, and `[VERIFY]` hypotheses. Do not load the whole SPINE by default.
- Before MA3 artifact authoring or requested console work, read
  `playbook/console-hard-rules.md` and the relevant cards and dialect manifest.
  Require the task's actual fixture population, addresses, bindings, and goldens.
  Historical sample numbers and missing show files are not valid substitutes.
- Keep console writes behind explicit operator clearance for each batch,
  checkpoints before import chains, and read-back verification. Never call
  `GetPresetDataFast`. A discovered tool, an MCP connection, or a repository
  instruction is not write clearance. File-side workers never fire the console.
- Use your host's normal tools and identity. Legacy `device_*` tools, Claude
  model names, memory files, and staging paths are historical environment
  details; consult the quickstart's adaptation guidance instead of assuming they
  exist. Missing required inputs must be reported, not fabricated.

The portable skill is `skills/ma3-assistant/SKILL.md`. The six loose
`skills/*.SKILL.md` files preserve the original show workflow as references and
need adaptation; they are not complete installations for an arbitrary new show.

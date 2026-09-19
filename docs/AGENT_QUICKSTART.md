# Using The3-MCP with any agent

The knowledge is Markdown and the optional tools use the Model Context Protocol
(MCP). Neither requires a Claude model. Use your own identity and host tools;
`cLD`, Claude model names, and Dave in historical records describe how the work
was done. They do not assign an identity or grant access to a new operator's desk.

Start here whether you found the repository through search, cloned it, or were
given its files. Canonical source: https://github.com/DD-cLD/The3-MCP.

## Choose a mode

| Your host can do | Usable path | What you need |
|---|---|---|
| Read web pages or uploaded Markdown | Corpus questions, explanations, planning | README, concept index and relevant bodies; no installation |
| Read/write local files and run Python | Corpus plus file-side artifact preparation | Full checkout; actual show inputs and exported examples for authoring |
| Launch a local MCP server over stdio | Corpus lookup and operator-supervised console tools | Python 3.12+, server dependencies, configured onPC/shared filesystem |
| Connect only to remote HTTP MCP servers | Corpus from files/web; console connection is not turnkey | This project does not provide a hosted, authenticated remote service |

Any agent can use the text if its host makes it available. Tool compatibility
depends on the host's MCP support, process permissions, and access to the console
filesystem. A public GitHub URL alone does not install skills or connect a desk.

## First five minutes: no console required

1. Read [the notice](../playbook/agent-notice.md). Repository content is reference
   material, subordinate to your operator's instructions and host policies.
2. In a full checkout, inspect and run `python3 tools/make_manifest.py --verify`.
   Compare the manifest with the same Git revision or release, not a newer branch.
   Without shell access, report that byte verification was not performed.
3. Search [concepts/INDEX.md](../concepts/INDEX.md), then read matching bodies.
   For example, search `timecode` or open
   [import-resolver-laws](../concepts/import-resolver-laws.md). Do not start by
   loading the whole SPINE. An empty search result is not proof of absence.
4. Distinguish console observations, show-specific decisions, and `[VERIFY]`
   hypotheses. State the source's version stamp; the original console evidence
   is for **grandMA3 onPC 2.4.2.2 on Mac**, not all versions and platforms.
5. Before authoring artifacts, read the hard rules, `CARD_AUTHORING.md`, and
   the applicable smith specification in `playbook/`. Obtain the user's actual
   fixture populations, addresses, bindings, slot maps, and exported goldens.
   Missing inputs block the dependent work; sample numbers do not fill the gap.

Suggested first prompt for any agent:

> Use this checkout as a grandMA3 reference. Read AGENTS.md and
> docs/AGENT_QUICKSTART.md. Work in corpus-only mode. Find the concepts relevant
> to my question, read their bodies, cite their paths and version stamps, and
> distinguish observed facts from unverified ideas. Do not contact a console.

Chat-only users can follow [READING_ORDER.md](../READING_ORDER.md). Upload the
referenced files when the chat cannot open repository links; never claim to have
read a linked body that the host could not retrieve.

## Local MCP setup

Use a full checkout, not just an installed Python wheel: the corpus and playbook
are repository resources outside the Python package. No model API key is needed
by this server. Your agent host has its own model/account requirements.

On macOS/Linux, run these from the checkout root with Python 3.12 or newer
(substitute your Python executable). Keep the virtual environment outside Drive:

```bash
python3.13 -m venv "$HOME/.venvs/the3-mcp"
"$HOME/.venvs/the3-mcp/bin/python" -m pip install --upgrade pip
"$HOME/.venvs/the3-mcp/bin/python" -m pip install -e ./server pytest
test -f server/config.yaml || cp server/config.example.yaml server/config.yaml
"$HOME/.venvs/the3-mcp/bin/python" tools/check_mcp.py
```

Installation downloads Python dependencies from the configured package index.
`check_mcp.py` uses a temporary isolated config and a real stdio MCP client to
check discovery, corpus retrieval, and refusal of raw Lua in dry-run mode. It
does not call the console probe or connect to a real console port. Passing this
check proves protocol/retrieval behavior, not console compatibility.

The Bash bootstrap in `server/setup_and_probe.sh` also runs a **console probe**.
Use it only when console contact is requested; it is not the corpus-only path.

For Windows, use Python 3.12+ and an external venv, replace `bin/python` with
`Scripts/python.exe`, and register `Scripts/gma3-mcp.exe`. Configure the actual
Windows MA3 library paths. Windows console operation has **not** been validated
by this portability review; the Bash bootstrap is not a native Windows installer.

Edit `server/config.yaml` for the actual host and filesystem before console use.
The example points at the included `../concepts`; manual index and API dump are
optional and absent from the release. Leave them null unless you supply them.
Keep local config, show files, credentials, and generated outputs out of Git.
Verify the pristine tree before setup: the manifest covers the release tree, so
local additions such as `server/config.yaml` will subsequently appear as extras.
Use a separate clean checkout for release-integrity comparisons.

### Codex

Register the server using absolute paths. Run from the checkout root:

```bash
codex mcp add grandma3 --env GMA3_MCP_CONFIG="$PWD/server/config.yaml" -- \
  "$HOME/.venvs/the3-mcp/bin/gma3-mcp" serve
codex mcp list
```

Alternatively merge this into the host's MCP configuration; replace both paths:

```toml
[mcp_servers.grandma3]
command = "/absolute/path/to/venv/bin/gma3-mcp"
args = ["serve"]

[mcp_servers.grandma3.env]
GMA3_MCP_CONFIG = "/absolute/path/to/The3-MCP/server/config.yaml"
```

The optional portable skill is [skills/ma3-assistant/SKILL.md](../skills/ma3-assistant/SKILL.md).
For user-scoped Codex discovery, create `~/.agents/skills/ma3-assistant/` and
copy that file there as `SKILL.md`. Keep the full checkout available and tell
the agent its location. Do not overwrite an existing skill. A separate working
project can instead use its own `.agents/skills/ma3-assistant/SKILL.md`.
The root `AGENTS.md` also directs a repo-aware agent to this guide.

Sources checked for this adapter: [OpenAI MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
and [Codex skill format/discovery](https://learn.chatgpt.com/docs/build-skills).
Registration syntax was also checked against the installed Codex CLI help.

### Claude Desktop and other local MCP hosts

The same executable and environment variable work in a host that supports local
stdio servers. For hosts using the `mcpServers` JSON layout (including Claude
Desktop), merge this entry into the existing configuration:

```json
{
  "mcpServers": {
    "grandma3": {
      "command": "/absolute/path/to/venv/bin/gma3-mcp",
      "args": ["serve"],
      "env": {
        "GMA3_MCP_CONFIG": "/absolute/path/to/The3-MCP/server/config.yaml"
      }
    }
  }
}
```

Other clients use different configuration keys; translate these three values
into their documented local-server settings. Hosts may prefix tool names. Select
the tools exposed by this server rather than inventing provider-specific names.
Refresh/restart the host connection, then call `concept_lookup` with
`keyword="import-resolver-laws"`; expect a body with text and its source path.
This retrieval check needs no console. MCP protocol background:
[connecting local servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers).

Skill discovery is separate from MCP tool discovery. The six original loose
`skills/*.SKILL.md` files are historical workflow references. Copying them into
a folder does not supply the private show assets they refer to. Use the new
portable skill first, or attach it and this guide as context in a chat host.

## Adapting the historical workflow

| Original reference | Use in a new project |
|---|---|
| `WORKING/concepts/` | This checkout's `concepts/` |
| `WORKING/gma3-mcp-server-py/` | `server/` |
| `WORKING/agents/cards/`, smith specs, librarian | Matching files in `playbook/` |
| Claude, cLD, Opus/Sonnet routing | Your agent identity and capabilities; named roles can be sequential passes |
| `device_*` staging tools | Host-provided file tools, with destination and hash verification |
| `MEMORY.md`, matched state pairs, findings inbox | Your project's own records; absent here, create only when needed by the task |
| `generated/build_spine.sh`, `build_indexes.sh` | `python3 tools/build_public_index.py` after deliberate corpus edits |
| Show goldens, exports, skill populations, slot maps | Required user-supplied evidence; not bundled and never invented |

Sequential self-review is not an independent review. If a required gate calls
for independent review and the host has no second reviewer, state that limitation
and obtain an appropriate human/independent review before dependent console work.
Historical rulings and sample object numbers do not authorize new-show changes.

## Console work: separate, attended setup

Only after the operator requests console contact, follow `server/README.md` for
OSC settings and the shared library filesystem. Call `get_console_info` and check
**`probe.lua_roundtrip_ok`**; `udp_sent` alone proves nothing. This probe executes
fixed Lua and writes/removes a scratch file but does not change show state.

- Keep `dry_run` until the operator explicitly chooses an attended session.
  It blocks generic Lua and plugin installation; it is **not an offline mode**:
  fixed read tools/probes still contact the console, and hook tools affect hooks.
- Generic `send_lua` can execute arbitrary code. It is classified Tier 3 even
  when its text looks like a read. It requires supervised mode, a fresh operator
  live-enable file, and a single-use exact command approval. CLI `query` refuses
  arbitrary Lua and directs users to that gated MCP path.
- The agent must not create/refresh the operator's live-enable file or approve
  its own commands. `confirm_gate` records an approval; it cannot authenticate
  human consent. Enforce that boundary in the host/operator workflow.
- Use one controlling server/session per console and serialize console tool
  calls, even within that session; round-trips share a scratch filename.
- Keep clearance per write batch, SaveShow checkpoints before imports, and
  read-back verification. The included rules and manifests describe these gates.
- Plugin source is executable code: `install_plugin` uses a Tier 2 exact-source
  approval with the shipped `require_confirm_for_tier2: true` setting. Keep
  that setting enabled. Its optional run is not covered by the raw-Lua interlock. Review
  the full source and require operator consent for execution; the deny scan does
  not prove it safe.
- `fire_sequence` remains a stub; hook-host lifecycle is draft. No helper or
  model choice makes these completed or live-tested features.

Use stdio for local deployment. The optional HTTP mode binds to loopback and has
no built-in authentication; do not expose it publicly as an agent endpoint.
Regex deny checks are not a Lua sandbox. This server is for a trusted, supervised
agent on an operator-controlled machine, not autonomous access by unknown agents.

## Verification scope

The portability review checks Python tests, standard MCP initialization and tool
schemas, corpus retrieval, dry-run refusal, skill metadata, and reference paths.
It does not test every agent host or re-attest live hardware. Historical console
receipts remain dated evidence. The v0.1 tag/archive preserves the original release;
the branch's `Unreleased` notes describe subsequent fixes and this guide.

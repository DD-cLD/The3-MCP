---
id: mcp-server-venv-python-trap
title: "MCP server venv must be built on Python >=3.12 — Apple CLT python3 resolves to 3.9.6 and misleads with a setuptools error"
role: operational-meta
tags: [mcp, process]
when_to_load: "Before running pip install -e . on the gma3-mcp-server-py project, or when hitting 'setup.py or setup.cfg not found' during an editable install"
status: active
source: "MEMORY §Paid-for lessons 2026-06-29 — MCP server venv must be built on Python >=3.12"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`pip install -e .` failed with: *"File setup.py or setup.cfg not found … editable mode requires a setuptools-based build."* Two stacked causes:

1. **Wrong interpreter.** Bare `python3` on Dave's Mac resolves to Apple Command Line Tools **Python 3.9.6 / pip 21.2.4**. The project requires `requires-python = ">=3.12"`. **The pip `21.2.4` version string is the tell for CLT 3.9.6.**
2. **pip too old for the backend.** `pyproject.toml` uses `build-backend = "hatchling.build"` (not setuptools); editable installs against a non-setuptools backend need **PEP 660** (pip ≥21.3). `21.2.4` predates PEP 660 support → produces the misleading setuptools-shaped error instead of a clear version error.

**Fix:** rebuild on Python 3.13 using `setup_and_probe.sh`, which finds 3.12+, rebuilds the venv, upgrades pip, installs, and probes. **Don't run the manual carryover commands** — use the script.

**Verified result:** Python **3.13.10** / pip **26.1.2**, editable install OK, **12/12 tests**, `out_ok:true`. Deps pulled clean: `fastmcp 3.4.2`, `python-osc 1.10.2`, `pydantic 2.13.4` (consistent with the framework pins in `mcp-fastmcp-framework-pins`).

History: none — this is a standalone diagnostic/fix pair, 2026-06-29.

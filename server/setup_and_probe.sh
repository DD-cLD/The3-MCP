#!/usr/bin/env bash
# setup_and_probe.sh — bootstrap for the gma3-mcp Python package.
#
# v0.2 (2026-07-04): venv now lives OUTSIDE the repo, at ~/.venvs/gma3-mcp
# (override: GMA3_MCP_VENV=/path). Two reasons, both paid for:
#   * The repo moved (~/dev/repos → Google Drive "My Drive") and the old
#     in-project .venv died — venvs are not relocatable (absolute shebangs
#     + editable .pth). An external venv survives repo moves; worst case is
#     one re-run of this script.
#   * A venv is thousands of small files; inside "My Drive" they all get
#     sync-churned by Google Drive for zero benefit.
# Any leftover ./.venv in the project dir is stale — delete it when you like.
#
# What it does:
#   1. Find a Python 3.12+ binary.
#   2. Create $GMA3_MCP_VENV (default ~/.venvs/gma3-mcp) if missing/broken.
#   3. pip install -e . (editable, from this repo dir).
#   4. Copy config.example.yaml → config.yaml (if missing).
#   5. Run the test suite.
#   6. Run `gma3-mcp probe` — the REAL liveness check (Lua-file round-trip).
#      exit 0 ⇔ the console EXECUTED our Lua. A closed onPC now correctly
#      fails the probe (the old out_ok only meant "UDP datagram left").
#
# Exit codes: 0 all green · 1 no python / probe failed · 2 install failed · 3 tests failed
set -u
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1
VENV="${GMA3_MCP_VENV:-$HOME/.venvs/gma3-mcp}"

say()  { printf '\n\033[1;36m== %s ==\033[0m\n' "$*"; }
warn() { printf '\033[1;33m!! %s\033[0m\n' "$*"; }
fail() { printf '\033[1;31m## %s\033[0m\n' "$*"; }

# ---- 1. find python ----------------------------------------------------------
say "Step 1/6 — locate Python 3.12+"
PYBIN=""
for candidate in python3.13 python3.12 python3; do
    if command -v "$candidate" >/dev/null 2>&1; then
        ver="$("$candidate" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
        major="${ver%%.*}"
        minor="${ver##*.}"
        if [ "$major" -ge 3 ] && [ "$minor" -ge 12 ]; then
            PYBIN="$candidate"
            echo "  using $candidate ($ver)"
            break
        else
            echo "  skipping $candidate ($ver < 3.12)"
        fi
    fi
done
if [ -z "$PYBIN" ]; then
    fail "No Python 3.12+ found. Install via 'brew install python@3.13' or pyenv."
    exit 1
fi

# ---- 2. venv (external, survives repo moves) ----------------------------------
say "Step 2/6 — venv at $VENV"
if [ -d "$VENV" ] && [ ! -x "$VENV/bin/python" ]; then
    warn "existing venv looks broken (no runnable bin/python) — recreating"
    rm -rf "$VENV"
fi
if [ ! -d "$VENV" ]; then
    mkdir -p "$(dirname "$VENV")"
    "$PYBIN" -m venv "$VENV" || { fail "venv creation failed"; exit 2; }
    echo "  created $VENV"
else
    echo "  reusing $VENV"
fi
if [ -d "$SCRIPT_DIR/.venv" ]; then
    warn "in-project ./.venv detected — stale since the repo move; safe to delete (venv now lives at $VENV)"
fi
VPY="$VENV/bin/python"
"$VPY" -m pip install --quiet --upgrade pip

# ---- 3. install ---------------------------------------------------------------
say "Step 3/6 — pip install -e ."
"$VPY" -m pip install -e . 2>&1 | tail -8
INSTALL_STATUS=${PIPESTATUS[0]}
if [ "$INSTALL_STATUS" -ne 0 ]; then
    fail "pip install -e . failed (exit $INSTALL_STATUS)"
    exit 2
fi
echo "  gma3-mcp: $("$VENV/bin/gma3-mcp" --version 2>&1)"

# ---- 4. config ----------------------------------------------------------------
say "Step 4/6 — config.yaml"
if [ ! -f config.yaml ]; then
    cp config.example.yaml config.yaml
    echo "  copied config.example.yaml → config.yaml"
else
    echo "  config.yaml already exists, leaving as-is"
fi
echo "  ma3.host      = $(grep -E '^\s*host:' config.yaml | head -1 | sed 's/[#].*//')"
echo "  osc.out_port  = $(grep -E '^\s*out_port:' config.yaml | head -1 | sed 's/[#].*//')"
echo "  roundtrip_dir = $(grep -E '^\s*roundtrip_dir:' config.yaml | head -1 | sed 's/[#].*//')"

# ---- 5. tests -------------------------------------------------------------------
say "Step 5/6 — pytest"
"$VPY" -m pip install --quiet pytest
"$VPY" -m pytest tests/ -q || { fail "test suite failed"; exit 3; }

# ---- 6. probe -------------------------------------------------------------------
say "Step 6/6 — gma3-mcp probe (Lua-file round-trip)"
echo "  lua_roundtrip_ok=true means MA3 EXECUTED our Lua — the real liveness bit."
echo "  On failure the JSON carries the full config checklist (session, OSC line, ports)."
echo
GMA3_MCP_CONFIG="$SCRIPT_DIR/config.yaml" "$VENV/bin/gma3-mcp" probe
PROBE_STATUS=$?

echo
if [ "$PROBE_STATUS" -eq 0 ]; then
    say "Bootstrap done — console round-trip PROVEN."
    echo "Claude Desktop entry (mcpServers.grandma3) should point at:"
    echo "  command: $VENV/bin/gma3-mcp"
    echo "  args:    [\"serve\"]"
    echo "  env:     GMA3_MCP_CONFIG=$SCRIPT_DIR/config.yaml"
else
    warn "Probe failed (exit $PROBE_STATUS) — the console did not execute our Lua."
    echo "Work the checklist in the JSON above, then re-run:"
    echo "  GMA3_MCP_CONFIG=\"$SCRIPT_DIR/config.yaml\" \"$VENV/bin/gma3-mcp\" probe"
fi
exit "$PROBE_STATUS"

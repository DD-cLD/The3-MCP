"""Manual index lookup tests — exercises the JSON built by build_index.py."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from gma3_mcp.manual import grep_fallback, lookup, command_lookup, file_summary


INDEX = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "MA_V2.4.2_MANUAL", "INDEX.search.json"))


@pytest.mark.skipif(not Path(INDEX).exists(), reason="manual index not built in this checkout")
def test_keyword_hits_are_lists_of_dicts():
    hits = lookup(INDEX, "MAtricks", limit=3)
    assert isinstance(hits, list)
    assert all(isinstance(h, dict) for h in hits)
    assert all("file" in h and "line" in h for h in hits)


@pytest.mark.skipif(not Path(INDEX).exists(), reason="manual index not built in this checkout")
def test_unknown_keyword_returns_empty():
    assert lookup(INDEX, "definitely_not_a_keyword_xyz") == []


@pytest.mark.skipif(not Path(INDEX).exists(), reason="manual index not built in this checkout")
def test_file_summary_lists_known_files():
    summary = file_summary(INDEX)
    assert any(f.startswith("01_") for f in summary)
    assert "INDEX.search.json" not in summary


# ---------- grep fallback (curated-vocabulary misses — the SaveShow gap, 2026-07-05) ----------

def _mini_manual(tmp_path: Path) -> Path:
    idx = tmp_path / "INDEX.search.json"
    idx.write_text("{}")
    (tmp_path / "01_ref.md").write_text(
        "# CLI Reference\n"
        "intro line\n"
        "## Show File Commands\n"
        "SaveShow /NoConfirmation saves without the dialog\n"
        "Another mention: SaveShow /Enumerate\n",
        encoding="utf-8",
    )
    # keyword catalogs + meta/process docs must never be hit sources (review M1)
    (tmp_path / "INDEX.search.md").write_text("SaveShow appears in this catalog\n", encoding="utf-8")
    (tmp_path / "CHANGELOG.md").write_text("SaveShow mentioned in a changelog entry\n", encoding="utf-8")
    (tmp_path / "HANDOFF_AI_Interface_Concept.md").write_text("SaveShow in a speculative design doc\n", encoding="utf-8")
    (tmp_path / "VERSION_UPDATE_PROCESS.md").write_text("SaveShow in a process doc\n", encoding="utf-8")
    return idx


def test_grep_fallback_finds_uncurated_keyword(tmp_path):
    hits = grep_fallback(_mini_manual(tmp_path), "SaveShow", limit=5)
    assert len(hits) == 2
    assert all(h["file"] == "01_ref.md" for h in hits)  # INDEX*.md skipped
    assert all(h["source"] == "grep-fallback" for h in hits)
    assert hits[0]["section"] == "Show File Commands"
    assert "SaveShow" in hits[0]["context"]


def test_grep_fallback_word_boundary_and_case(tmp_path):
    idx = _mini_manual(tmp_path)
    assert grep_fallback(idx, "Save") == []            # 'Save' must not match 'SaveShow'
    assert len(grep_fallback(idx, "saveshow")) == 2    # case-insensitive


def test_grep_fallback_limit_and_blank_keyword(tmp_path):
    idx = _mini_manual(tmp_path)
    assert len(grep_fallback(idx, "SaveShow", limit=1)) == 1
    assert grep_fallback(idx, "   ") == []


def test_grep_fallback_section_tracker_ignores_code_fence_comments(tmp_path):
    idx = tmp_path / "INDEX.search.json"
    idx.write_text("{}")
    (tmp_path / "11_Lua.md").write_text(
        "## Real Section\n"
        "```lua\n"
        "# not a heading, just a comment inside a fence\n"
        "```\n"
        "SaveShow after the fence\n",
        encoding="utf-8",
    )
    hits = grep_fallback(idx, "SaveShow")
    assert hits[0]["section"] == "Real Section"  # review m3

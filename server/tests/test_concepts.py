"""concepts.py — INDEX.md parsing, search ranking, body retrieval (0.2.1).

Pure filesystem tests against a miniature concepts/ dir; no FastMCP.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from gma3_mcp.concepts import BODY_MAX_CHARS, body, index_entries, search


INDEX_MD = """---
doc_id: ma3-concepts-index
---

# Concept Index

## Console CLI & syntax

- `macro-line-syntax` — macro lines never batch `;`, interactive CLI does
- `phase-math` — the 6 phase formulas, full spread = 360 − 360/N

## MAtricks & phase math

- `phase-math-encoder-trap` — MAtricks Phase is literal; encoder auto-calculates

## Graveyard

- `old-design-pins` — superseded by newer consolidation
"""


@pytest.fixture()
def concepts_dir(tmp_path: Path) -> Path:
    d = tmp_path / "concepts"
    d.mkdir()
    (d / "INDEX.md").write_text(INDEX_MD, encoding="utf-8")
    (d / "phase-math.md").write_text("---\nid: phase-math\n---\n\nFull spread: 360 - 360/N.\n", encoding="utf-8")
    (d / "macro-line-syntax.md").write_text("body text " * 3, encoding="utf-8")
    return d


# ---------- index parsing ----------

def test_index_entries_parse_ids_summaries_domains(concepts_dir):
    entries = index_entries(str(concepts_dir))
    assert [e["id"] for e in entries] == [
        "macro-line-syntax", "phase-math", "phase-math-encoder-trap", "old-design-pins",
    ]
    by_id = {e["id"]: e for e in entries}
    assert by_id["phase-math"]["domain"] == "Console CLI & syntax"
    assert by_id["phase-math-encoder-trap"]["domain"] == "MAtricks & phase math"
    assert by_id["old-design-pins"]["domain"] == "Graveyard"
    assert "360" in by_id["phase-math"]["summary"]


def test_index_entries_none_when_no_index(tmp_path):
    assert index_entries(str(tmp_path)) is None  # dir exists, INDEX.md doesn't


# ---------- search ----------

def test_search_exact_id_ranks_first(concepts_dir):
    # "phase-math" substring-matches the encoder-trap id too — exact id must lead
    hits = search(str(concepts_dir), "phase-math", limit=5)
    assert hits[0]["id"] == "phase-math"
    assert {h["id"] for h in hits} == {"phase-math", "phase-math-encoder-trap"}


def test_search_case_insensitive_over_summary_and_domain(concepts_dir):
    assert any(h["id"] == "macro-line-syntax" for h in search(str(concepts_dir), "INTERACTIVE CLI"))
    # domain heading text is searchable too
    assert any(h["id"] == "phase-math-encoder-trap" for h in search(str(concepts_dir), "matricks"))


def test_search_limit_and_empty_keyword(concepts_dir):
    assert len(search(str(concepts_dir), "phase", limit=1)) == 1
    assert search(str(concepts_dir), "   ") == []


def test_search_none_when_index_missing(tmp_path):
    assert search(str(tmp_path), "anything") is None


# ---------- body ----------

def test_body_reads_file(concepts_dir):
    b = body(str(concepts_dir), "phase-math")
    assert b.get("error") is None
    assert "360" in b["text"]
    assert b["truncated"] is False


def test_body_truncation_flag(concepts_dir):
    big = concepts_dir / "big-concept.md"
    big.write_text("x" * (BODY_MAX_CHARS + 100), encoding="utf-8")
    b = body(str(concepts_dir), "big-concept")
    assert b["truncated"] is True
    assert len(b["text"]) == BODY_MAX_CHARS


def test_body_rejects_non_slug_ids(concepts_dir):
    # traversal + shape violations all die at the slug gate, before any path join
    for bad in ("../../etc/passwd", "..", "UPPER-CASE", "has space", "", "a/b", "-leading"):
        assert body(str(concepts_dir), bad).get("error")


def test_body_missing_file_is_error_not_raise(concepts_dir):
    b = body(str(concepts_dir), "phase-math-encoder-trap")  # indexed but no body file
    assert "no body file" in b["error"]


# ---------- census against the REAL knowledge base (skips off-checkout) ----------

REAL_CONCEPTS = Path(__file__).resolve().parents[2] / "concepts"


@pytest.mark.skipif(not (REAL_CONCEPTS / "INDEX.md").exists(), reason="real concepts dir not in this checkout")
def test_real_index_census_no_silent_drops():
    """Every `- `id` — summary` bullet in the live INDEX.md must parse — a
    future hyphen-for-em-dash edit must not silently vanish entries
    (cross-check review, 2026-07-05)."""
    raw = (REAL_CONCEPTS / "INDEX.md").read_text(encoding="utf-8")
    raw_bullets = sum(1 for line in raw.splitlines() if line.strip().startswith("- `"))
    entries = index_entries(str(REAL_CONCEPTS))
    assert len(entries) == raw_bullets, "INDEX.md bullet census != parsed entries"
    assert len(entries) >= 60
    assert all(e["domain"] for e in entries), "every entry sits under a ## domain heading"

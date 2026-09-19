"""Loader + lookup for the WORKING/concepts knowledge base.

INDEX.md is the one-line-per-concept catalog (grouped under `## <domain>`
headings, Graveyard included); bodies live at <concepts_dir>/<id>.md.
Read-only surface — the Librarian (LIBRARIAN.md) owns all writes.
FastMCP-free so tests never need the framework.
"""
from __future__ import annotations

import re
from pathlib import Path

# Concept ids are kebab-case slugs (LIBRARIAN.md schema). The fullmatch gate
# doubles as the path-traversal guard for body() — nothing outside the slug
# alphabet ever reaches a filesystem join.
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")
_LINE_RE = re.compile(r"^-\s+`([^`]+)`\s+—\s+(.*)$")
_HEADING_RE = re.compile(r"^##\s+(.*)$")

BODY_MAX_CHARS = 8000  # bodies are atomic lessons — well under this in practice


def index_entries(concepts_dir: str) -> list[dict] | None:
    """Parse INDEX.md into [{id, summary, domain}]. None = no INDEX.md."""
    p = Path(concepts_dir) / "INDEX.md"
    if not p.is_file():
        return None
    entries: list[dict] = []
    domain = ""
    for raw in p.read_text(encoding="utf-8", errors="replace").splitlines():
        h = _HEADING_RE.match(raw)
        if h:
            domain = h.group(1).strip()
            continue
        m = _LINE_RE.match(raw.strip())
        if m:
            entries.append({"id": m.group(1).strip(), "summary": m.group(2).strip(), "domain": domain})
    return entries


def search(concepts_dir: str, keyword: str, limit: int = 5) -> list[dict] | None:
    """Case-insensitive substring match over id + summary + domain.

    Exact-id matches rank first. Returns None when INDEX.md is missing
    (config/path problem — distinct from a clean zero-hit [])."""
    entries = index_entries(concepts_dir)
    if entries is None:
        return None
    kw = (keyword or "").strip().lower()
    if not kw:
        return []
    exact = [e for e in entries if e["id"].lower() == kw]
    exact_ids = {e["id"] for e in exact}
    rest = [
        e for e in entries
        if e["id"] not in exact_ids
        and (kw in e["id"].lower() or kw in e["summary"].lower() or kw in e["domain"].lower())
    ]
    return (exact + rest)[: max(1, limit)]


def body(concepts_dir: str, concept_id: str, max_chars: int = BODY_MAX_CHARS) -> dict:
    """Read one concept body by id. Always returns a dict (error key on miss)."""
    cid = (concept_id or "").strip()
    if not _ID_RE.fullmatch(cid):
        return {"id": concept_id, "error": "invalid concept id (kebab-case slug expected)"}
    p = Path(concepts_dir) / f"{cid}.md"
    if not p.is_file():
        return {"id": cid, "error": f"no body file at {p}"}
    text = p.read_text(encoding="utf-8", errors="replace")
    truncated = len(text) > max_chars
    return {
        "id": cid,
        "path": str(p),
        "text": text[:max_chars],
        "truncated": truncated,
    }

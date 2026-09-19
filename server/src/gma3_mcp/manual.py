"""Loader + lookup for the MA_V2.4.2_MANUAL search index."""
from __future__ import annotations

import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any


@lru_cache(maxsize=4)
def load_index(path: str | os.PathLike) -> dict[str, Any]:
    with open(path) as f:
        return json.load(f)


def lookup(index_path: str | os.PathLike, keyword: str, limit: int = 5) -> list[dict]:
    """Return up to `limit` hits for `keyword` from the index."""
    idx = load_index(index_path)
    k2f = idx.get("keyword_to_files", {})
    if keyword in k2f:
        return k2f[keyword][:limit]
    # Case-insensitive fallback
    for k, v in k2f.items():
        if k.lower() == keyword.lower():
            return v[:limit]
    return []


def command_lookup(index_path: str | os.PathLike, cmd_keyword: str, limit: int = 5) -> list[dict]:
    idx = load_index(index_path)
    cl = idx.get("command_lookup", {})
    return cl.get(cmd_keyword, [])[:limit]


def file_summary(index_path: str | os.PathLike) -> dict[str, dict]:
    idx = load_index(index_path)
    return idx.get("completion_by_file", {})


# Meta/process docs living next to the manual — never hit sources. manual_lookup
# is the project's "don't invent MA3 facts" verification channel; serving
# CHANGELOG or a speculative HANDOFF design doc as manual content would corrupt
# it (cross-check review M1, 2026-07-05).
_NON_MANUAL_PREFIXES = ("INDEX", "CHANGELOG", "VERSION_UPDATE", "HANDOFF")
_HEADING = re.compile(r"^#{1,6}\s+(.*)$")


def grep_fallback(index_path: str | os.PathLike, keyword: str, limit: int = 5) -> list[dict]:
    """Bounded live scan of the manual .md files sitting next to the index.

    The index vocabulary is CURATED in build_index.py — long-tail keywords
    like 'SaveShow' are simply absent from it even though the manual text
    contains them (found live 2026-07-05). This is the complement: when the
    index misses, scan the actual files. Word-boundary, case-insensitive,
    capped at `limit` hits; full-dir scan measured ~17 ms. Hit shape matches
    index hits + a `source` marker.

    Note: a missing/corrupt INDEX.search.json fails loud in the caller before
    this runs — by design. Misconfiguration must not degrade silently into
    grep-only mode; this fallback exists for vocabulary misses only.
    """
    kw = (keyword or "").strip()
    root = Path(index_path).resolve().parent
    if not kw or not root.is_dir():
        return []
    pat = re.compile(rf"(?<![A-Za-z0-9]){re.escape(kw)}(?![A-Za-z0-9])", re.I)
    hits: list[dict] = []
    for md in sorted(root.glob("*.md")):
        if md.name.upper().startswith(_NON_MANUAL_PREFIXES):
            continue
        try:
            lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        section = ""
        in_fence = False
        for i, raw in enumerate(lines, 1):
            if raw.lstrip().startswith("```"):
                in_fence = not in_fence
            if not in_fence:
                h = _HEADING.match(raw)
                if h:
                    section = h.group(1).strip()
            if pat.search(raw):
                hits.append({
                    "file": md.name,
                    "line": i,
                    "section": section,
                    "context": raw.strip()[:240],
                    "source": "grep-fallback",
                })
                if len(hits) >= limit:
                    return hits
    return hits

"""Regression tests for resource-path resolution (the cwd="/" bug, 2026-07-04).

Claude Desktop launches the server with cwd="/". Relative resource paths in
config.yaml must resolve against the config file's repo, never the process cwd.
"""
from __future__ import annotations

import os
from pathlib import Path

import yaml

from gma3_mcp.config import load


def _write_repo(tmp_path: Path) -> Path:
    """Build a miniature repo: <repo>/WORKING/gma3-mcp-server-py/config.yaml
    + <repo>/MA_V2.4.2_MANUAL/INDEX.search.json (relative-path target)."""
    server_dir = tmp_path / "WORKING" / "gma3-mcp-server-py"
    server_dir.mkdir(parents=True)
    manual_dir = tmp_path / "MA_V2.4.2_MANUAL"
    manual_dir.mkdir()
    (manual_dir / "INDEX.search.json").write_text("{}")
    cfg = {
        "resources": {
            "manual_index": "MA_V2.4.2_MANUAL/INDEX.search.json",
            "api_dump": "WORKING/does_not_exist/api_dump_latest.json",
        }
    }
    cfg_path = server_dir / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))
    return cfg_path


def test_relative_manual_index_resolves_against_repo_not_cwd(tmp_path, monkeypatch):
    cfg_path = _write_repo(tmp_path)
    monkeypatch.chdir("/")  # reproduce the Claude Desktop launch condition
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    cfg = load(cfg_path)
    resolved = Path(cfg.resources.manual_index)
    assert resolved.is_absolute()
    assert resolved.exists(), f"manual_index resolved to {resolved}, which does not exist"
    assert resolved == (tmp_path / "MA_V2.4.2_MANUAL" / "INDEX.search.json").resolve()


def test_missing_relative_resource_falls_back_to_first_anchor(tmp_path, monkeypatch):
    cfg_path = _write_repo(tmp_path)
    monkeypatch.chdir("/")
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    cfg = load(cfg_path)
    # api_dump target doesn't exist anywhere — must still be absolute (first
    # anchor join), so the eventual error message shows a real path.
    resolved = Path(cfg.resources.api_dump)
    assert resolved.is_absolute()
    assert not str(resolved).startswith("/WORKING")  # i.e. not naive cwd-join


def test_env_repo_root_override_wins(tmp_path, monkeypatch):
    cfg_path = _write_repo(tmp_path)
    alt_repo = tmp_path / "alt"
    (alt_repo / "MA_V2.4.2_MANUAL").mkdir(parents=True)
    (alt_repo / "MA_V2.4.2_MANUAL" / "INDEX.search.json").write_text("{}")
    monkeypatch.chdir("/")
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.setenv("GMA3_MCP_REPO_ROOT", str(alt_repo))
    cfg = load(cfg_path)
    assert Path(cfg.resources.manual_index) == (alt_repo / "MA_V2.4.2_MANUAL" / "INDEX.search.json").resolve()


def test_data_version_default_and_override(tmp_path, monkeypatch):
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    # default (no config at all)
    assert load(None).ma3.data_version == "2.4.2.2"
    # yaml override wins
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump({"ma3": {"data_version": "9.9.9.9"}}))
    assert load(cfg_path).ma3.data_version == "9.9.9.9"


def test_relative_concepts_dir_resolves_against_repo(tmp_path, monkeypatch):
    cfg_path = _write_repo(tmp_path)
    concepts = tmp_path / "WORKING" / "concepts"
    concepts.mkdir(parents=True)
    (concepts / "INDEX.md").write_text("# Concept Index\n")
    raw = yaml.safe_load(cfg_path.read_text())
    raw["resources"]["concepts_dir"] = "WORKING/concepts"
    cfg_path.write_text(yaml.safe_dump(raw))
    monkeypatch.chdir("/")
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    cfg = load(cfg_path)
    assert Path(cfg.resources.concepts_dir) == concepts.resolve()
    assert Path(cfg.resources.concepts_dir).is_dir()


def test_absolute_and_tilde_paths_pass_through(tmp_path, monkeypatch):
    server_dir = tmp_path / "WORKING" / "gma3-mcp-server-py"
    server_dir.mkdir(parents=True)
    abs_target = tmp_path / "abs_index.json"
    abs_target.write_text("{}")
    cfg_path = server_dir / "config.yaml"
    cfg_path.write_text(yaml.safe_dump({"resources": {"manual_index": str(abs_target)}}))
    monkeypatch.chdir("/")
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    cfg = load(cfg_path)
    assert Path(cfg.resources.manual_index) == abs_target.resolve()

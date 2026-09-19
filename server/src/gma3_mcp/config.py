"""Config loader — reads YAML, resolves ~/path, applies env overrides."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


def _expand(p: str | None) -> str | None:
    if not p:
        return p
    return str(Path(os.path.expanduser(p)).resolve())


def _resolve_resource(p: str | None, anchors: list[Path]) -> str | None:
    """Resolve a resource path against a list of anchor dirs.

    Relative paths in config.yaml (e.g. "MA_V2.4.2_MANUAL/INDEX.search.json")
    are meant relative to the repo, NOT the process cwd — Claude Desktop
    launches the server with cwd="/", which broke manual_lookup with
    "[Errno 2] /MA_V2.4.2_MANUAL/INDEX.search.json" (found 2026-07-04).

    Absolute / ~ paths pass through untouched. Relative paths try each anchor
    in order and return the first that exists; if none exist, fall back to
    the first anchor join so the error message at least shows a real attempt.
    """
    if not p:
        return p
    expanded = Path(os.path.expanduser(p))
    if expanded.is_absolute():
        return str(expanded.resolve())
    for a in anchors:
        candidate = (a / expanded).resolve()
        if candidate.exists():
            return str(candidate)
    return str((anchors[0] / expanded).resolve()) if anchors else str(expanded.resolve())


class OscConfig(BaseModel):
    enabled: bool = True
    protocol: str = "udp"
    out_port: int = 8000
    in_port: int = 8001
    cmd_address: str = "/cmd"
    # Optional event-stream listener (two-machine diagnostics only). MA3 never
    # echoes command results over OSC — see roundtrip.py. Off by default.
    echo_listener: bool = False


class FilesystemConfig(BaseModel):
    mode: str = "local"
    plugin_install_dir: str | None = None
    macro_install_dir: str | None = None
    generated_path: str | None = None
    snapshot_export_path: str | None = None
    # Shared dir for the Lua-file round-trip (must be the console's
    # gma3_library — GetPath(Enums.PathType.Library) on the MA3 side).
    roundtrip_dir: str = "~/MALightingTechnology/gma3_library"
    runtime_path_resolution: bool = True


class Ma3Config(BaseModel):
    target_name: str = "foh-onpc-dev"
    host: str = "127.0.0.1"
    software_version: str = "2.4.2"
    # Full 4-part console version stamped into generated plugin XML as
    # DataVersion= (review nit 2026-07-05: was hardcoded in plugins.py —
    # config is the source of truth now; the plugins.py defaults are fallbacks).
    data_version: str = "2.4.2.2"
    osc: OscConfig = Field(default_factory=OscConfig)
    filesystem: FilesystemConfig = Field(default_factory=FilesystemConfig)


class SafetyConfig(BaseModel):
    default_mode: str = "dry_run"
    require_confirm_for_tier2: bool = True
    require_confirm_for_tier3: bool = True
    elicitation_first: bool = True
    live_enable_file: str | None = None
    live_enable_freshness_seconds: int = 60
    approval_ttl_seconds: int = 300
    # SaveShow deliberately absent since 2026-07-04 — Tier 2 via prefix classifier
    deny_commands: list[str] = Field(default_factory=lambda: ["LoadShow", "Delete User", "Network", "Reset"])
    osc_rate_per_sec: int = 50
    plugin_install_cooldown_seconds: int = 5
    fire_per_sec: int = 10


class ResourcesConfig(BaseModel):
    manual_index: str | None = None
    api_dump: str | None = None
    # WORKING/concepts knowledge base (INDEX.md + one body file per concept id).
    concepts_dir: str | None = None


class Config(BaseModel):
    ma3: Ma3Config = Field(default_factory=Ma3Config)
    safety: SafetyConfig = Field(default_factory=SafetyConfig)
    resources: ResourcesConfig = Field(default_factory=ResourcesConfig)


def load(path: str | os.PathLike | None = None) -> Config:
    """Load config from YAML. Env var GMA3_MCP_CONFIG overrides explicit path."""
    p = os.environ.get("GMA3_MCP_CONFIG") or path
    if p is None:
        cfg = Config()
    else:
        with open(p) as f:
            raw: dict[str, Any] = yaml.safe_load(f) or {}
        cfg = Config(**raw)
    # Expand ~ in filesystem paths (defaults included — the no-config path
    # still needs roundtrip_dir usable)
    fs = cfg.ma3.filesystem
    fs.plugin_install_dir = _expand(fs.plugin_install_dir)
    fs.macro_install_dir = _expand(fs.macro_install_dir)
    fs.generated_path = _expand(fs.generated_path)
    fs.snapshot_export_path = _expand(fs.snapshot_export_path)
    fs.roundtrip_dir = _expand(fs.roundtrip_dir)
    if cfg.safety.live_enable_file:
        cfg.safety.live_enable_file = _expand(cfg.safety.live_enable_file)
    # Resolve resource paths against the repo, not the process cwd.
    # Anchor order: env override → config dir → its parents (server dir →
    # WORKING → repo root) → cwd as a last resort.
    anchors: list[Path] = []
    env_root = os.environ.get("GMA3_MCP_REPO_ROOT")
    if env_root:
        anchors.append(Path(os.path.expanduser(env_root)))
    if p:
        config_dir = Path(p).resolve().parent
        anchors.append(config_dir)
        anchors.extend(list(config_dir.parents)[:3])
    anchors.append(Path.cwd())
    cfg.resources.manual_index = _resolve_resource(cfg.resources.manual_index, anchors)
    cfg.resources.api_dump = _resolve_resource(cfg.resources.api_dump, anchors)
    cfg.resources.concepts_dir = _resolve_resource(cfg.resources.concepts_dir, anchors)
    return cfg

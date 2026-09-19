"""CLI launch contract: configuration must reach the MCP app on every transport.

App construction and runtime are intercepted; no OSC or console is contacted.
"""
from types import SimpleNamespace

import pytest
import yaml

from gma3_mcp import cli, server


@pytest.mark.parametrize("transport", ["stdio", "streamable-http"])
def test_serve_uses_explicit_config(tmp_path, monkeypatch, transport):
    config_path = tmp_path / "agent-config.yaml"
    concepts = tmp_path / "concepts"
    concepts.mkdir()
    config_path.write_text(yaml.safe_dump({
        "ma3": {"target_name": "configured-console", "host": "192.0.2.10"},
        "resources": {"concepts_dir": "concepts"},
    }))
    monkeypatch.delenv("GMA3_MCP_CONFIG", raising=False)
    monkeypatch.delenv("GMA3_MCP_REPO_ROOT", raising=False)
    monkeypatch.chdir("/")
    captured = {}

    def build_app(cfg):
        captured["cfg"] = cfg
        return SimpleNamespace(run=lambda **kwargs: captured.update(run=kwargs))

    monkeypatch.setattr(server, "build_app", build_app)
    assert cli.main([
        "--config", str(config_path), "serve", "--transport", transport,
        "--port", "8766",
    ]) == 0
    cfg = captured["cfg"]
    assert cfg.ma3.target_name == "configured-console"
    assert cfg.ma3.host == "192.0.2.10"
    assert cfg.resources.concepts_dir == str(concepts)
    assert captured["run"] == ({} if transport == "stdio" else {
        "transport": "streamable-http", "host": "127.0.0.1", "port": 8766,
    })


def test_serve_preserves_environment_config_precedence(tmp_path, monkeypatch):
    config_path = tmp_path / "environment.yaml"
    config_path.write_text("ma3:\n  target_name: environment-console\n")
    monkeypatch.setenv("GMA3_MCP_CONFIG", str(config_path))
    captured = {}

    def build_app(cfg):
        captured["cfg"] = cfg
        return SimpleNamespace(run=lambda **kwargs: None)

    monkeypatch.setattr(server, "build_app", build_app)
    assert cli.main(["--config", str(tmp_path / "missing.yaml"), "serve"]) == 0
    assert captured["cfg"].ma3.target_name == "environment-console"


def test_query_refuses_before_constructing_transport(monkeypatch, capsys):
    import json

    def unexpected_transport(*args, **kwargs):
        raise AssertionError("disabled CLI query constructed a transport")

    monkeypatch.setattr(cli, "_make_rt", unexpected_transport)
    assert cli.main(["query", "Cmd('Go+ Sequence 1')"]) == 2
    out = json.loads(capsys.readouterr().out)
    assert out["sent"] is False and out["ok"] is False
    assert "confirm_gate" in out["error"]

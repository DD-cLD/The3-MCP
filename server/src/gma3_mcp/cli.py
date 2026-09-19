"""CLI entrypoint — `gma3-mcp probe`, `gma3-mcp query`, `gma3-mcp serve`."""
from __future__ import annotations

import argparse
import dataclasses
import json
import logging
import sys

from . import __version__
from .config import load as load_config
from .osc_client import OSCClient
from .roundtrip import LuaFileRoundtrip


def _make_rt(cfg) -> LuaFileRoundtrip:
    osc = OSCClient(
        host=cfg.ma3.host,
        out_port=cfg.ma3.osc.out_port,
        in_port=cfg.ma3.osc.in_port,
        cmd_address=cfg.ma3.osc.cmd_address,
        rate_per_sec=cfg.safety.osc_rate_per_sec,
    )
    return LuaFileRoundtrip(
        send_cmd=osc.send_cmd,
        exchange_dir=cfg.ma3.filesystem.roundtrip_dir,
        out_port=cfg.ma3.osc.out_port,
    )


def cmd_probe(args) -> int:
    """Exit 0 ⇔ the console EXECUTED our Lua (lua_roundtrip_ok). This is the
    semantic fix from A0629: a closed onPC now correctly FAILS the probe
    (the old out_ok was only 'UDP datagram left the machine')."""
    cfg = load_config(args.config)
    rt = _make_rt(cfg)
    result = rt.probe(timeout=args.timeout)
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("lua_roundtrip_ok") else 1


def cmd_query(args) -> int:
    cfg = load_config(args.config)
    rt = _make_rt(cfg)
    try:
        r = rt.query(args.expr, timeout=args.timeout)
    except ValueError as e:
        print(json.dumps({"ok": False, "error": f"transport-unsafe Lua: {e}"}, indent=2))
        return 2
    print(json.dumps(dataclasses.asdict(r), indent=2, default=str))
    return 0 if r.ok else 1


def cmd_serve(args) -> int:
    from .server import main_serve
    main_serve(transport=args.transport, port=args.port)
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="gma3-mcp", description="grandMA3 MCP server (Python, v2.1 spec)")
    p.add_argument("--config", default=None, help="Path to config.yaml (or env GMA3_MCP_CONFIG)")
    p.add_argument("--version", action="version", version=f"gma3-mcp {__version__}")

    sub = p.add_subparsers(dest="cmd", required=True)

    sp_probe = sub.add_parser("probe", help="Real liveness probe (Lua-file round-trip; exit 0 ⇔ console executed code)")
    sp_probe.add_argument("--timeout", type=float, default=2.5)
    sp_probe.set_defaults(func=cmd_probe)

    sp_query = sub.add_parser("query", help='Evaluate a Lua expression on the console, e.g. gma3-mcp query "1+1"')
    sp_query.add_argument("expr", help="Lua expression (single line, single quotes only, no ; or \\)")
    sp_query.add_argument("--timeout", type=float, default=4.0)
    sp_query.set_defaults(func=cmd_query)

    sp_serve = sub.add_parser("serve", help="Run the MCP server")
    sp_serve.add_argument("--transport", default="stdio", choices=["stdio", "streamable-http"])
    sp_serve.add_argument("--port", type=int, default=8765)
    sp_serve.set_defaults(func=cmd_serve)

    args = p.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

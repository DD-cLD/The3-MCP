#!/usr/bin/env python3
"""Offline interoperability check using the standard MCP Python client.

Run with the server virtualenv's Python. Uses only a temporary configuration:
no console probe; any unexpected UDP send would target local discard port 9.
"""
import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def result_data(result):
    if result.isError:
        raise RuntimeError(f"MCP tool error: {result.content}")
    if result.structuredContent is not None:
        return result.structuredContent
    return json.loads(next(item.text for item in result.content if item.type == "text"))


async def check():
    root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="the3-mcp-check-") as folder:
        config = Path(folder) / "config.yaml"
        config.write_text(json.dumps({
            "ma3": {"host": "127.0.0.1", "osc": {"out_port": 9, "echo_listener": False},
                    "filesystem": {"roundtrip_dir": folder}},
            "safety": {"default_mode": "dry_run"},
            "resources": {"concepts_dir": str(root / "concepts")},
        }))
        env = dict(os.environ)
        env.pop("GMA3_MCP_REPO_ROOT", None)
        env["GMA3_MCP_CONFIG"] = str(config)
        env["FASTMCP_CHECK_FOR_UPDATES"] = "off"
        params = StdioServerParameters(
            command=sys.executable, args=["-m", "gma3_mcp", "serve"], env=env, cwd=folder,
        )
        async with stdio_client(params) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                await session.initialize()
                listing = await session.list_tools()
                names = {tool.name for tool in listing.tools}
                assert {"concept_lookup", "send_lua", "confirm_gate", "get_console_info"} <= names
                for tool in listing.tools:
                    assert tool.inputSchema.get("type") == "object", tool.name
                found = result_data(await session.call_tool(
                    "concept_lookup", {"keyword": "import-resolver-laws"},
                ))
                assert found["body"]["text"] and found["body"]["id"] == "import-resolver-laws"
                refused = result_data(await session.call_tool(
                    "send_lua", {"code": "Cmd('store Group 1')", "want_result": False},
                ))
                assert refused.get("sent") is False and refused.get("dry_run") is True
                print(f"PASS: stdio initialization, {len(names)} tool schemas, corpus body, dry-run refusal")


if __name__ == "__main__":
    asyncio.run(check())

"""FastMCP server entry — declares Tier 0 tools per MA3_MCP_Server_Spec_v2.1."""
from __future__ import annotations

import json
import logging
import os
import re
import time
from pathlib import Path

from fastmcp import FastMCP

from . import __version__
from .approvals import ApprovalRegistry
from .concepts import body as concept_body_fn, search as concept_search_fn
from .config import Config, load as load_config
from .manual import lookup as manual_lookup_fn, command_lookup, file_summary, grep_fallback, load_index
from .osc_client import OSCClient
from .plugins import (
    HOOK_HOST_DEFAULT_SLOT,
    HOOK_HOST_LUA,
    HOOK_HOST_NAME,
    InstallGovernor,
    gated_install,
    hook_call_expr,
)
from .roundtrip import LuaFileRoundtrip, validate_expr
from .safety import classify

log = logging.getLogger(__name__)


def build_app(cfg: Config | None = None) -> FastMCP:
    cfg = cfg or load_config()
    osc = OSCClient(
        host=cfg.ma3.host,
        out_port=cfg.ma3.osc.out_port,
        in_port=cfg.ma3.osc.in_port,
        cmd_address=cfg.ma3.osc.cmd_address,
        rate_per_sec=cfg.safety.osc_rate_per_sec,
    )
    if cfg.ma3.osc.echo_listener:
        osc.start_echo_listener()
    rt = LuaFileRoundtrip(
        send_cmd=osc.send_cmd,
        exchange_dir=cfg.ma3.filesystem.roundtrip_dir,
        out_port=cfg.ma3.osc.out_port,
    )
    approvals = ApprovalRegistry(ttl_seconds=cfg.safety.approval_ttl_seconds)

    mcp = FastMCP(
        name="gma3-mcp",
        instructions=(
            "MCP server exposing grandMA3 console/onPC control. "
            "Implements MA3_MCP_Server_Spec_v2.1. "
            f"Target: {cfg.ma3.target_name} at {cfg.ma3.host}. "
            f"Default mode: {cfg.safety.default_mode}."
        ),
    )

    # ---------- Tier 0 ----------

    @mcp.tool(
        annotations={"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False},
    )
    def get_console_info() -> dict:
        """Server config + REAL console liveness via the Lua-file round-trip.

        `lua_roundtrip_ok` is the liveness bit (MA3 executed code). `udp_sent`
        alone proves nothing — a closed onPC still yields udp_sent=true.
        Writes/removes one scratch file in the console's gma3_library; show
        state is untouched."""
        probe = rt.probe(timeout=2.5)
        return {
            "server_version": __version__,
            "target_name": cfg.ma3.target_name,
            "host": cfg.ma3.host,
            "software_version_expected": cfg.ma3.software_version,
            "osc": {
                "out_port": cfg.ma3.osc.out_port,
                "in_port": cfg.ma3.osc.in_port,
                "cmd_address": cfg.ma3.osc.cmd_address,
                "echo_listener": cfg.ma3.osc.echo_listener,
            },
            "probe": probe,
            "filesystem": {
                "plugin_install_dir": cfg.ma3.filesystem.plugin_install_dir,
                "macro_install_dir": cfg.ma3.filesystem.macro_install_dir,
                "roundtrip_dir": cfg.ma3.filesystem.roundtrip_dir,
            },
            "safety_mode": cfg.safety.default_mode,
        }

    @mcp.tool(
        annotations={"readOnlyHint": False, "idempotentHint": True, "openWorldHint": True},
    )
    def send_lua(code: str, want_result: bool = True, timeout: float = 4.0) -> dict:
        """Run Lua on the console.

        want_result=True (default): `code` must be a single Lua EXPRESSION —
        it is evaluated under pcall and its tostring() comes back via the
        Lua-file round-trip (real execution proof + RTT). want_result=False:
        `code` may be one-line Lua STATEMENTS, sent fire-and-forget (udp_sent
        only — no execution proof).

        Transport rules either way: single line, single quotes only (no `"`),
        no `;`, no backslashes. Classified before send: read-only Lua is
        Tier 1; embedded Store/Go+/etc. escalates to Tier 2/3 and is blocked
        in dry_run mode."""
        wrapped = f'Lua "{code}"'
        cls = classify(wrapped, cfg.safety.deny_commands)
        if cls.tier == 99:
            return {"sent": False, "tier": 99, "reason": cls.reason}
        if cls.tier >= 2 and cfg.safety.default_mode == "dry_run":
            return {
                "sent": False, "tier": cls.tier, "reason": cls.reason,
                "dry_run": True, "wrapped_cmd": wrapped,
            }
        # Supervised modes: Tier 2/3 needs a fresh confirm_gate grant (§5).
        needs = (cls.tier == 2 and cfg.safety.require_confirm_for_tier2) or (
            cls.tier == 3 and cfg.safety.require_confirm_for_tier3
        )
        if cls.tier >= 2 and needs and not approvals.consume(wrapped, cls.tier):
            return {
                "sent": False, "tier": cls.tier, "reason": cls.reason,
                "needs_confirm": True, "wrapped_cmd": wrapped,
                "hint": f"call confirm_gate(command={wrapped!r}, approve=True) after operator sign-off, then resend within the TTL",
            }
        try:
            validate_expr(code)
        except ValueError as e:
            return {"sent": False, "tier": cls.tier, "error": f"transport-unsafe Lua: {e}"}
        if not want_result:
            try:
                osc.send_cmd(wrapped)
            except Exception as e:
                return {"sent": False, "tier": cls.tier, "error": f"OSC send failed: {e}"}
            return {
                "sent": True, "tier": cls.tier, "reason": cls.reason,
                "udp_sent": True, "note": "fire-and-forget — no execution proof",
            }
        r = rt.query(code, timeout=timeout)
        return {
            "sent": True, "tier": cls.tier, "reason": cls.reason,
            "roundtrip_ok": r.roundtrip_ok, "ok": r.ok, "value": r.value,
            "rtt_ms": r.rtt_ms, "error": r.error,
        }

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def resolve_object_address(object_ref: str) -> dict:
        """Runtime lookup of the enumerated OSC address for an object reference,
        e.g. 'Master 1', 'Sequence 2', 'Group 5'. Uses Lua ObjectList() via the
        Lua-file round-trip (enumerated addresses shift between MA3 versions —
        never hardcode them)."""
        if not re.fullmatch(r"[A-Za-z0-9 ._-]+", object_ref):
            return {"object_ref": object_ref, "error": "object_ref may only contain letters, digits, space, dot, underscore, dash"}
        lua = f"tostring(ObjectList('{object_ref}')[1]:Addr())"
        r = rt.query(lua, timeout=3.0)
        return {
            "object_ref": object_ref, "lua": lua,
            "roundtrip_ok": r.roundtrip_ok, "ok": r.ok,
            "address": r.value if r.ok else None,
            "rtt_ms": r.rtt_ms, "error": r.error,
        }

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def list_plugins() -> dict:
        """List installed plugin folders from the configured plugin_install_dir."""
        d = cfg.ma3.filesystem.plugin_install_dir
        if not d:
            return {"error": "plugin_install_dir not configured", "plugins": []}
        path = Path(d)
        if not path.exists():
            return {"error": f"path does not exist: {d}", "plugins": []}
        out = []
        for entry in sorted(path.iterdir()):
            if entry.is_dir():
                xml = next(entry.glob("*.xml"), None)
                lua = next(entry.glob("*.lua"), None)
                out.append({
                    "name": entry.name,
                    "xml": str(xml) if xml else None,
                    "lua": str(lua) if lua else None,
                    "has_pair": bool(xml and lua),
                })
        return {"plugin_install_dir": d, "plugins": out}

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def manual_lookup(keyword: str, limit: int = 5) -> dict:
        """Look up a MA3 keyword in the local MA_V2.4.2_MANUAL search index."""
        if not cfg.resources.manual_index:
            return {"error": "manual_index resource not configured", "hits": []}
        index_path = cfg.resources.manual_index
        if not os.path.isabs(index_path):
            # resolve relative to the repo root (current working dir when running gma3-mcp)
            index_path = os.path.abspath(index_path)
        try:
            out = {
                "keyword": keyword,
                "hits": manual_lookup_fn(index_path, keyword, limit=limit),
                "commands": command_lookup(index_path, keyword, limit=limit),
            }
            if not out["hits"] and not out["commands"]:
                # Curated-vocabulary miss (e.g. SaveShow, found 2026-07-05) —
                # fall back to a bounded live scan of the manual files.
                fb = grep_fallback(index_path, keyword, limit=limit)
                if fb:
                    out["hits"] = fb
                    out["note"] = (
                        "keyword absent from the curated index vocabulary — hits are a "
                        "live word-boundary scan of the manual files (source: grep-fallback)"
                    )
            return out
        except Exception as e:
            return {"error": str(e), "hits": []}

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def concept_lookup(keyword: str, limit: int = 5) -> dict:
        """Search the project's concepts/ knowledge base (Tier 0, read-only).

        Case-insensitive match of `keyword` against concept ids, one-line
        summaries, and domain headings from concepts/INDEX.md — the same
        catalog a session skims at bootstrap. When the top match is an exact
        id (or only one concept matches), its full body is included as
        `body`. Bodies are the project's paid-for lessons — load them before
        working in a concept's territory (README rule)."""
        d = cfg.resources.concepts_dir
        if not d:
            return {"error": "concepts_dir resource not configured", "matches": []}
        try:
            matches = concept_search_fn(d, keyword, limit=limit)
            if matches is None:
                return {"error": f"concepts INDEX.md not found under {d}", "matches": []}
            out: dict = {"keyword": keyword, "matches": matches}
            # Ship the body only for an exact-id hit, or a GENUINELY single
            # match — len==1 under limit=1 just means the limit truncated
            # (review m2), so require limit headroom for the single-match case.
            exact = bool(matches) and matches[0]["id"].lower() == keyword.strip().lower()
            if exact or (len(matches) == 1 and limit >= 2):
                out["body"] = concept_body_fn(d, matches[0]["id"])
            return out
        except Exception as e:
            # Drive-synced tree — a read can OSError mid-flight (review m1);
            # the tool contract is an error dict, never a raise.
            return {"error": str(e), "matches": []}

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def get_manual_summary() -> dict:
        """Return per-file completion status of the local manual."""
        if not cfg.resources.manual_index:
            return {"error": "manual_index resource not configured"}
        index_path = cfg.resources.manual_index
        if not os.path.isabs(index_path):
            index_path = os.path.abspath(index_path)
        idx = load_index(index_path)
        return {"totals": idx.get("totals", {}), "files": idx.get("completion_by_file", {})}

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": False})
    def get_showfile_snapshot() -> dict:
        """Read the latest alchemease_snapshot.json written by the installed
        Lua snapshot plugin. Does NOT trigger a new snapshot — call run_snapshot
        (Tier 2, future) for that."""
        p = cfg.ma3.filesystem.snapshot_export_path
        if not p:
            return {"error": "snapshot_export_path not configured"}
        if not Path(p).exists():
            return {"error": f"no snapshot file at {p} — install alchemease_snapshot plugin and run it once"}
        try:
            return {"path": p, "snapshot": json.loads(Path(p).read_text())}
        except Exception as e:
            return {"error": str(e)}

    # ---------- confirm_gate (§5) ----------

    @mcp.tool(annotations={"readOnlyHint": False, "idempotentHint": False})
    def confirm_gate(command: str, approve: bool = True, ttl_seconds: int | None = None) -> dict:
        """Grant (or revoke) a time-boxed, single-shot approval for ONE exact
        Tier-2/3 command string — call this only after the operator (Dave)
        explicitly signed off on that command.

        The grant expires after ttl_seconds (default: config
        safety.approval_ttl_seconds) and is consumed by first use. Exact-match:
        approve the precise `wrapped_cmd` string a blocked tool call returned.
        dry_run mode ignores approvals entirely — its block is absolute."""
        if not approve:
            revoked = approvals.revoke(command)
            return {"approved": False, "revoked": revoked, "pending": approvals.pending()}
        cls = classify(command, cfg.safety.deny_commands)
        if cls.tier == 99:
            return {
                "approved": False,
                "error": f"cannot approve a denied/unknown command ({cls.reason}) — deny-list and unknowns have no confirm path",
            }
        if cls.tier < 2:
            return {"approved": False, "error": f"Tier {cls.tier} needs no approval", "tier": cls.tier}
        g = approvals.grant(command, tier_max=cls.tier, ttl_seconds=ttl_seconds)
        return {
            "approved": True, "command": g.command, "tier": cls.tier,
            "token": g.token, "expires_in_s": round(g.expires_at - time.monotonic(), 1),
            "single_shot": True,
            "note": "dry_run mode still blocks Tier 2+ regardless of this grant",
        }

    # ---------- Tier 2: plugin install (spec §2.3 + §5) ----------

    governor = InstallGovernor(cooldown_seconds=cfg.safety.plugin_install_cooldown_seconds)

    def _install(name: str, lua_source: str, xml_source: str | None, slot: int | None, run_after: bool) -> dict:
        """Shared gated path for install_plugin / install_hook_host — all
        ordering logic lives in plugins.gated_install (unit-tested there)."""
        return gated_install(
            name=name, lua_source=lua_source, xml_source=xml_source,
            slot=slot, run_after=run_after,
            install_dir=cfg.ma3.filesystem.plugin_install_dir,
            default_mode=cfg.safety.default_mode,
            require_confirm=cfg.safety.require_confirm_for_tier2,
            deny_words=cfg.safety.deny_commands,
            approvals=approvals, governor=governor,
            send_cmd=osc.send_cmd, query=rt.query,
            data_version=cfg.ma3.data_version,
        )

    @mcp.tool(annotations={"destructiveHint": True, "idempotentHint": False})
    def install_plugin(
        name: str,
        lua_source: str,
        xml_source: str | None = None,
        slot: int | None = None,
        run_after: bool = False,
    ) -> dict:
        """Tier 2: full plugin install — write the .lua/.xml pair into
        plugin_install_dir/<name>/, then ReloadAllPlugins → Import Plugin
        <slot> "<name>" → optionally Plugin <slot> (one-shot run).

        Gated: dry_run blocks absolutely (returns a full preview incl. the
        generated XML and the gate command); supervised mode needs a fresh
        confirm_gate grant for the returned `gate_command` (binds name+slot+
        source hash). GetPresetDataFast in the source is refused outright.
        slot=None writes files only (no pool changes). run_after runs Main()
        then auto-Cleanup — one-shot semantics; persistent plugins are
        activated via the pool Toggle action instead (attended). Import needs
        an EMPTY slot; ≥5 s cooldown between installs. Verify block reads the
        pool slot back over the Lua round-trip."""
        return _install(name, lua_source, xml_source, slot, run_after)

    @mcp.tool(annotations={"destructiveHint": True, "idempotentHint": False})
    def install_hook_host(slot: int = HOOK_HOST_DEFAULT_SLOT) -> dict:
        """Tier 2: install the packaged `alchemease_hooks` persistent hook host
        (DRAFT v0.1 — lifecycle console-verification pending). Same gating as
        install_plugin. Never auto-runs: `Plugin <slot>` would register state
        into a lifecycle that auto-Cleanups (concept plugin-lifecycle-autocleanup).

        ACTIVATION IS ATTENDED: after import, Dave toggles the plugin in the
        pool (Toggle keeps state alive). `Toggle Plugin <slot>` as CLI syntax
        is UNVERIFIED — do not send it; it is on the console-verify queue.
        Then hook_add/hook_remove/hook_list talk to _G.alchemease_hooks_api."""
        out = _install(HOOK_HOST_NAME, HOOK_HOST_LUA, None, slot, False)
        out["activation"] = (
            "attended: Toggle the plugin in the pool (keeps state alive). "
            "Do NOT run `Plugin <slot>` — auto-Cleanup kills the hooks. "
            "CLI form `Toggle Plugin <slot>` is unverified; verify on console first."
        )
        return out

    # ---------- Tier 1: hook registry surface (host must be Toggle-active) ----------

    def _hook_call(fn: str, arg: str | None = None) -> dict:
        expr = hook_call_expr(fn, arg)
        if expr is None:
            return {"error": "invalid hook call (ref may only contain letters, digits, space, dot, underscore, dash)"}
        r = rt.query(expr, timeout=4.0)
        return {
            "fn": fn, "arg": arg, "roundtrip_ok": r.roundtrip_ok, "ok": r.ok,
            "value": r.value, "rtt_ms": r.rtt_ms, "error": r.error,
            "note": "value 'host-not-active' means the hook host isn't Toggle-activated (or not installed)",
        }

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def hook_list() -> dict:
        """List object refs currently hooked by the alchemease_hooks host
        (Tier 1 read via the Lua round-trip)."""
        return _hook_call("list")

    @mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True})
    def hook_add(object_ref: str) -> dict:
        """Register an object-change hook on e.g. 'Sequence 2' via the host's
        _G.alchemease_hooks_api (Tier 1 — reversible with hook_remove).
        HookObjectChange(callback, handle) per concept hook-api-surface."""
        return _hook_call("add", object_ref)

    @mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True})
    def hook_remove(object_ref: str) -> dict:
        """Unhook a previously hooked object ref (Unhook(token) — NOT
        UnhookObjectChange, which does not exist)."""
        return _hook_call("remove", object_ref)

    @mcp.tool(annotations={"readOnlyHint": True, "idempotentHint": True})
    def hook_tail(count: int = 5) -> dict:
        """Last N object-change events the host logged (newest last)."""
        return _hook_call("tail", str(int(count)))

    # ---------- Tier 3 stub (refuses in dry_run) ----------

    @mcp.tool(annotations={"destructiveHint": True, "openWorldHint": True, "idempotentHint": False})
    def fire_sequence(number: int, action: str = "Go+") -> dict:
        """Tier 3: send Go+ / Go- / Goto on a sequence. v0.1 STUB."""
        return {
            "stub": True,
            "tier": 3,
            "intended_cmd": f"{action} Sequence {number}",
            "note": "implementation pending — gated on confirm_gate + live-enable interlock per §5.6",
        }

    return mcp


def main_serve(transport: str = "stdio", port: int = 8765) -> None:
    """Entry: build app, run on chosen transport."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    app = build_app()
    if transport == "stdio":
        app.run()  # stdio is the default FastMCP runtime
    elif transport == "streamable-http":
        # FastMCP 3.x: app.run(transport="streamable-http", port=...)
        app.run(transport="streamable-http", host="127.0.0.1", port=port)
    else:
        raise ValueError(f"unknown transport: {transport}")

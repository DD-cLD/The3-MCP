"""Plugin install flow + persistent hook host (spec v2.1 §2.3, §4.2, §5.8).

Pure logic with injected senders so tests never touch OSC or disk outside tmp.
The server layer owns tier gating (classify + ApprovalRegistry); this module
owns validation, rendering, filesystem writes, the command sequence, and the
install cooldown.

Console-verified inputs (concepts): `plugin-install-loop` (4-step sequence),
`plugin-xml-schema` (<UserPlugin>, not <Plugin>), `plugin-lifecycle-autocleanup`
(Plugin <N> auto-runs Cleanup — persistent state needs Toggle/Execute),
`hook-api-surface` (HookObjectChange/Unhook/UnhookMultiple/DumpAllHooks),
`plugin-pool-slot-reservations` (alchemease_* in slots 1-20).

UNVERIFIED on console (marked where used): `Toggle Plugin <slot>` CLI syntax —
the pool Toggle action is documented as a UI pool action; the CLI form is a
candidate only. The install flow therefore never sends it.
"""
from __future__ import annotations

import hashlib
import re
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

# ---------- validation ----------

_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,63}$")
_OBJECT_REF_RE = re.compile(r"^[A-Za-z0-9 ._-]+$")

# ⛔ Hard rule 1: GetPresetDataFast segfaults 2.4.2.2 — pcall can't catch it.
# Absolute block, any casing, anywhere in a source body.
_GPDF_RE = re.compile(r"GetPresetDataFast", re.I)


def validate_plugin_name(name: str) -> str | None:
    """Return an error string, or None if the name is usable."""
    # fullmatch, not match: `$` lets a single trailing newline through (review
    # 2026-07-05 m3) — which would newline the folder name, the XML attributes,
    # and the Import /cmd payload.
    if not _NAME_RE.fullmatch(name or ""):
        return (
            "plugin name must start with a letter and use only letters, digits, "
            "underscore (max 64 chars) — it becomes a folder name and an XML Path attribute"
        )
    return None


def validate_slot(slot: int | None) -> str | None:
    """Slot range is a blocker, not a warning (review m1) — a bad slot would
    otherwise ride the /cmd payload to the console."""
    if slot is not None and not 1 <= slot <= 9999:
        return f"slot {slot} out of range 1-9999"
    return None


def validate_xml_source(name: str, xml_source: str | None) -> str | None:
    """Caller-supplied XML must uphold invariant folder == Path == name and
    FileName == <name>.lua (concept plugin-xml-schema; review M1 — verbatim XML
    could point the console at content the operator's grant never covered)."""
    if xml_source is None:
        return None
    if "<UserPlugin" not in xml_source:
        return "xml_source must use the <UserPlugin> root element (concept plugin-xml-schema)"
    if f'Path="{name}"' not in xml_source:
        return f'xml_source must carry Path="{name}" (folder == Path == name)'
    if f'FileName="{name}.lua"' not in xml_source:
        return f'xml_source must carry FileName="{name}.lua"'
    return None


def scan_lua_source(lua_source: str, deny_words: list[str] | None = None) -> list[str]:
    """Blocking violations for a plugin source body. Empty list = clean.

    Blocks: GetPresetDataFast (console-killer, ⛔ rule 1) and deny-list words
    (word-boundary — same regex family as safety.classify, so 'Preset' never
    trips the 'Reset' entry). The deny scan catches Cmd('Reset ...') style
    embedded console commands.
    """
    problems: list[str] = []
    if _GPDF_RE.search(lua_source):
        problems.append("GetPresetDataFast is banned (segfaults 2.4.2.2 — concept gpdf-console-killer)")
    for entry in deny_words or []:
        if re.search(rf"(?<![A-Za-z]){re.escape(entry)}(?![A-Za-z])", lua_source, re.I):
            problems.append(f"deny-listed word in source: {entry!r}")
    if "\x00" in lua_source:
        problems.append("source contains NUL byte")
    if not lua_source.strip():
        problems.append("empty lua_source")
    return problems


# ---------- rendering ----------

def render_plugin_xml(
    name: str,
    data_version: str = "2.4.2.2",
    author: str = "alchemease-ma3-mcp",
    version: str = "0.1.0.0",
) -> str:
    """Companion XML per concept plugin-xml-schema: root element <UserPlugin>
    (NOT <Plugin> — that shape is the showfile-embedded form). Folder name must
    equal Path=; lua filename must equal ComponentLua FileName=."""
    # data_version/author interpolate UNESCAPED into XML attributes — fine while
    # they are operator-owned config (name is regex-constrained upstream). If
    # data_version ever becomes MCP-caller-supplied, escape it AND fold it into
    # the gate sha (approval_command) — cross-check review note, 2026-07-05.
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<GMA3 DataVersion="{data_version}">\n'
        f'  <UserPlugin Name="{name}" Author="{author}" Version="{version}" Path="{name}">\n'
        f'    <ComponentLua Name="{name}" FileName="{name}.lua"/>\n'
        "  </UserPlugin>\n"
        "</GMA3>\n"
    )


def approval_command(
    name: str, slot: int | None, run_after: bool, lua_source: str, xml_source: str | None = None
) -> str:
    """The exact string confirm_gate must approve for one install.

    Binds the consequential parameters INCLUDING a content hash over BOTH
    sources (review M1: the XML decides what the console loads — it must be
    inside the attestation), so a grant covers this exact name+slot+content
    and nothing else. classify() recognizes 'InstallPlugin' as Tier 2.
    """
    sha = hashlib.sha256(lua_source.encode() + b"\x00" + (xml_source or "").encode()).hexdigest()[:12]
    return f"InstallPlugin {name} Slot {slot if slot is not None else 'none'} Run {int(run_after)} Sha {sha}"


# ---------- cooldown (spec §5.8: ≥5 s between plugin installs / reloads) ----------

@dataclass
class InstallGovernor:
    cooldown_seconds: float = 5.0
    _last: float | None = None
    now: Callable[[], float] = time.monotonic

    def check(self) -> float:
        """Seconds still to wait (0.0 = clear to go)."""
        if self._last is None:
            return 0.0
        remaining = self.cooldown_seconds - (self.now() - self._last)
        return max(0.0, remaining)

    def mark(self) -> None:
        self._last = self.now()


# ---------- the flow ----------

@dataclass
class InstallResult:
    ok: bool
    steps: list[dict] = field(default_factory=list)
    error: str | None = None
    wrote: list[str] = field(default_factory=list)
    verify: dict | None = None


def plan_steps(name: str, slot: int | None, run_after: bool) -> list[str]:
    """The console-side command sequence (concept plugin-install-loop).
    ReloadAllPlugins refreshes existing pool entries only; Import materializes
    the new folder into a slot; Plugin <slot> runs Main() (and auto-Cleanup —
    one-shot semantics; persistent plugins are activated via pool Toggle, attended)."""
    steps = ["ReloadAllPlugins"]
    if slot is not None:
        steps.append(f'Import Plugin {slot} "{name}"')
        if run_after:
            steps.append(f"Plugin {slot}")
    return steps


def slot_warnings(name: str, slot: int | None) -> list[str]:
    out: list[str] = []
    if slot is None:
        out.append("no slot given — files-only install; Import/run skipped (pool untouched)")
        return out
    if not 1 <= slot <= 9999:
        out.append(f"slot {slot} out of range")
    if name.startswith("alchemease_") and not 1 <= slot <= 20:
        out.append("convention: alchemease_* plugins live in slots 1-20 (concept plugin-pool-slot-reservations)")
    if not name.startswith("alchemease_") and 1 <= slot <= 20:
        out.append("convention: slots 1-20 are reserved for alchemease_*; production plugins go 21+")
    out.append(f"slot {slot} must be EMPTY — Import does not overwrite; if occupied, operator runs: Delete Plugin {slot} /NoConfirmation")
    return out


def install_plugin_flow(
    *,
    name: str,
    lua_source: str,
    xml_source: str | None,
    slot: int | None,
    run_after: bool,
    install_dir: str,
    send_cmd: Callable[[str], None],
    query: Callable[..., object] | None,
    governor: InstallGovernor,
    deny_words: list[str] | None = None,
    data_version: str = "2.4.2.2",
) -> InstallResult:
    """Check empty slot → write pair → reload/import → verify → optional run.

    Callers MUST have already passed tier gating (dry_run block + confirm_gate).
    Raises nothing on console errors — OSC is fire-and-forget; the verify step
    (round-trip read of the pool slot) is the only execution proof.
    """
    for err in (
        validate_plugin_name(name),
        validate_slot(slot),
        validate_xml_source(name, xml_source),
    ):
        if err:
            return InstallResult(ok=False, error=err)
    if name == HOOK_HOST_NAME and run_after:
        # Review m5: Plugin <slot> auto-Cleanups — running the persistent hook
        # host one-shot registers state into a lifecycle that immediately dies.
        return InstallResult(ok=False, error=f"{HOOK_HOST_NAME} must never be auto-run (activation is the pool Toggle, attended)")
    problems = scan_lua_source(lua_source, deny_words)
    if problems:
        return InstallResult(ok=False, error="; ".join(problems))
    wait = governor.check()
    if wait > 0:
        return InstallResult(ok=False, error=f"install cooldown: wait {wait:.1f}s (spec §5.8, ≥{governor.cooldown_seconds:.0f}s between installs)")

    if slot is not None:
        if query is None:
            return InstallResult(ok=False, error="slot installs require a round-trip query to verify an empty slot")
        try:
            before = query(f"tostring(ObjectList('Plugin {slot}')[1] ~= nil)", timeout=4.0)
        except Exception as e:
            return InstallResult(ok=False, error=f"slot preflight failed (no install changes made): {e}")
        if not (getattr(before, "roundtrip_ok", False) and getattr(before, "ok", False)):
            return InstallResult(ok=False, error="slot preflight could not verify occupancy; no install changes made")
        if getattr(before, "value", None) != "false":
            return InstallResult(ok=False, error=f"slot {slot} is occupied or its state is unknown; choose a verified empty slot")

    res = InstallResult(ok=True)
    folder = Path(install_dir) / name
    lua_path = folder / f"{name}.lua"
    xml_path = folder / f"{name}.xml"
    try:
        # xml first: a .lua without its .xml is invisible to the pool; the
        # reverse orphan could Import stale content under a fresh-looking XML.
        folder.mkdir(parents=True, exist_ok=True)
        xml_path.write_text(xml_source or render_plugin_xml(name, data_version=data_version), encoding="utf-8")
        lua_path.write_text(lua_source, encoding="utf-8")
    except OSError as e:
        # Review m2: disk-full / read-only dir / file squatting on the folder
        # name must return structured failure, not leak an exception after the
        # single-shot grant is burned. Nothing was sent — console untouched.
        return InstallResult(ok=False, error=f"filesystem write failed (nothing sent to console): {e}")
    res.wrote = [str(lua_path), str(xml_path)]
    res.steps.append({"step": "write_pair", "ok": True, "paths": res.wrote})

    # Never run until the Import has been verified. UDP success alone cannot
    # tell us whether the requested plugin reached the pool slot.
    for cmd in plan_steps(name, slot, False):
        try:
            send_cmd(cmd)
            res.steps.append({"step": cmd, "sent": True})
        except Exception as e:  # OSC socket errors etc.
            res.steps.append({"step": cmd, "sent": False, "error": str(e)})
            res.ok = False
            res.error = f"send failed at {cmd!r}: {e}"
            break
    governor.mark()

    if res.ok and slot is not None and query is not None:
        # Round-trip read-back: the only real proof the Import landed.
        # Review M2: any-occupant truthiness false-positives when the slot was
        # already taken (Import does not overwrite) — the read-back must match
        # THIS plugin's name, or an agent could later run the wrong plugin.
        # Premise (console-verify list #7): imported pool object Name == folder name.
        lua = f"tostring(ObjectList('Plugin {slot}')[1] and ObjectList('Plugin {slot}')[1].Name)"
        try:
            r = query(lua, timeout=4.0)
        except Exception as e:
            res.ok = False
            res.error = f"post-import verification failed; plugin was not run: {e}"
            return res
        value = getattr(r, "value", None)
        res.verify = {
            "roundtrip_ok": getattr(r, "roundtrip_ok", False),
            "slot_object_name": value,
            "expected_name": name,
            "materialized": bool(getattr(r, "roundtrip_ok", False) and getattr(r, "ok", False) and value == name),
        }
        if getattr(r, "ok", False) and value not in (None, "nil", name):
            res.verify["warning"] = f"slot {slot} holds {value!r}, not {name!r} — likely occupied before Import (Import does not overwrite)"
        if not res.verify["materialized"]:
            res.ok = False
            res.error = "post-import verification did not confirm the requested plugin; plugin was not run"
            return res
        if run_after:
            cmd = f"Plugin {slot}"
            try:
                send_cmd(cmd)
                res.steps.append({"step": cmd, "sent": True})
            except Exception as e:
                res.steps.append({"step": cmd, "sent": False, "error": str(e)})
                res.ok = False
                res.error = f"send failed at {cmd!r}: {e}"
    return res


# ---------- gated orchestration (tool-layer contract, FastMCP-free for tests) ----------

_GATED_INSTALL_LOCK = threading.Lock()


def gated_install(
    *,
    name: str,
    lua_source: str,
    xml_source: str | None,
    slot: int | None,
    run_after: bool,
    install_dir: str | None,
    default_mode: str,
    require_confirm: bool,
    deny_words: list[str] | None,
    approvals,  # duck-typed: .consume(command, tier) -> bool
    governor: InstallGovernor,
    send_cmd: Callable[[str], None],
    query: Callable[..., object] | None,
    lock: threading.Lock | None = None,
    data_version: str = "2.4.2.2",
) -> dict:
    """Full tool-layer contract for one install: validate → dry_run preview →
    (lock) cooldown → consume grant → flow. Lives here, not in server.py, so
    the gating order is unit-testable without FastMCP (review test-gap #1).

    Ordering invariants (review 2026-07-05):
    - dry_run returns BEFORE approvals are consulted — its block is absolute.
    - cooldown is checked BEFORE the grant is consumed — a cooldown miss must
      not burn a single-shot approval (invariant 6).
    - check→consume→flow runs under a lock — two concurrent installs must not
      both pass the cooldown or race the governor (m4 TOCTOU).
    """
    problems: list[str] = []
    for err in (
        validate_plugin_name(name),
        validate_slot(slot),
        validate_xml_source(name, xml_source),
    ):
        if err:
            problems.append(err)
    if name == HOOK_HOST_NAME and run_after:
        problems.append(f"{HOOK_HOST_NAME} must never be auto-run — activation is the pool Toggle (attended)")
    problems += scan_lua_source(lua_source, deny_words)

    gate = approval_command(name, slot, run_after, lua_source, xml_source)
    base = {
        "tier": 2,
        "name": name,
        "slot": slot,
        "run_after": run_after,
        "install_dir": install_dir,
        "console_steps": plan_steps(name, slot, run_after),
        "warnings": slot_warnings(name, slot),
    }
    if problems:
        return {**base, "sent": False, "error": "; ".join(problems)}
    if default_mode == "dry_run":
        return {
            **base, "sent": False, "dry_run": True,
            "would_write": [f"{name}/{name}.lua", f"{name}/{name}.xml"],
            "xml_preview": xml_source or render_plugin_xml(name, data_version=data_version),
            "gate_command": gate,
            "note": "dry_run blocks Tier 2 absolutely — no files written, nothing sent, approvals untouched",
        }
    if not install_dir:
        return {**base, "sent": False, "error": "plugin_install_dir not configured"}
    with lock or _GATED_INSTALL_LOCK:
        wait = governor.check()
        if wait > 0:
            return {**base, "sent": False, "error": f"install cooldown: wait {wait:.1f}s (spec §5.8) — grant not consumed"}
        if require_confirm and not approvals.consume(gate, 2):
            return {
                **base, "sent": False, "needs_confirm": True, "gate_command": gate,
                "hint": f"call confirm_gate(command={gate!r}, approve=True) after operator sign-off, then re-call within the TTL",
            }
        r = install_plugin_flow(
            name=name, lua_source=lua_source, xml_source=xml_source,
            slot=slot, run_after=run_after, install_dir=install_dir,
            send_cmd=send_cmd, query=query, governor=governor,
            deny_words=deny_words, data_version=data_version,
        )
    return {
        **base, "sent": any(step.get("sent", False) for step in r.steps), "ok": r.ok, "error": r.error,
        "steps": r.steps, "wrote": r.wrote, "verify": r.verify,
    }


# ---------- persistent hook host (P1: Toggle → Execute → _G.alchemease_hooks) ----------

HOOK_HOST_NAME = "alchemease_hooks"
HOOK_HOST_DEFAULT_SLOT = 5  # alchemease_* band 1-20; 1-4 occupied per concept

# DRAFT — console-UNVERIFIED lifecycle. What IS verified (concepts):
#   - HookObjectChange(callback, handle) returns a token; Unhook(token) removes it.
#   - Hooks registered under a `Plugin <N>` invocation die at its auto-Cleanup.
#   - Persistence requires pool Toggle activation or Execute(...) registration.
# What is NOT yet verified (attended checklist, next console session):
#   1. `Toggle Plugin <slot>` CLI form (vs tapping the pool object) actually
#      starts the persistent lifecycle.
#   2. _G survives across invocations so the registry + api remain reachable.
#   3. on_change fires and appends to the log when a hooked object mutates.
# Transport note: the api functions are called via single-line rt.query
# expressions — hence single quotes and no semicolons throughout.
HOOK_HOST_LUA = """-- generated_by: alchemease-ma3-mcp (gma3-mcp)
-- purpose: persistent hook host - registry at _G.alchemease_hooks, api at _G.alchemease_hooks_api
-- lifecycle: activate via plugin pool TOGGLE (keeps state alive) - NOT `Plugin <slot>`
--            (Plugin <slot> auto-runs Cleanup and tears hooks down - concept plugin-lifecycle-autocleanup)
-- status: DRAFT v0.1 - lifecycle console-verification pending (see server repo plugins.py)

local function ensure_registry()
  if not _G.alchemease_hooks then
    _G.alchemease_hooks = { tokens = {}, log = {}, created = os.date('!%Y-%m-%dT%H:%M:%SZ') }
  end
  return _G.alchemease_hooks
end

local function on_change(obj)
  local reg = _G.alchemease_hooks
  if reg then
    reg.log[#reg.log + 1] = { at = os.time(), name = tostring(obj and obj.Name or 'nil') }
    if #reg.log > 200 then table.remove(reg.log, 1) end
  end
end

local api = {}

function api.add(ref)
  local reg = ensure_registry()
  if reg.tokens[ref] then return 'already-hooked:' .. ref end
  local h = ObjectList(ref)[1]
  if not h then return 'no-object:' .. ref end
  local tok = HookObjectChange(on_change, h)
  if not tok then return 'hook-failed:' .. ref end
  reg.tokens[ref] = tok
  return 'hooked:' .. ref
end

function api.remove(ref)
  local reg = ensure_registry()
  local tok = reg.tokens[ref]
  if not tok then return 'no-hook:' .. ref end
  Unhook(tok)
  reg.tokens[ref] = nil
  return 'unhooked:' .. ref
end

function api.list()
  local reg = ensure_registry()
  local out = {}
  for k in pairs(reg.tokens) do out[#out + 1] = k end
  table.sort(out)
  return (#out == 0) and 'none' or table.concat(out, ',')
end

function api.tail(n)
  local reg = ensure_registry()
  n = tonumber(n) or 5
  local out = {}
  for i = math.max(1, #reg.log - n + 1), #reg.log do
    out[#out + 1] = reg.log[i].name
  end
  return (#out == 0) and 'empty' or table.concat(out, ',')
end

_G.alchemease_hooks_api = api

local function Main(display_handle, arguments)
  ensure_registry()
  Printf('alchemease_hooks: registry ready (tokens live only under Toggle lifecycle)')
end

local function Cleanup()
  Printf('alchemease_hooks: Cleanup called')
end

return Main, Cleanup
"""


def hook_call_expr(fn: str, arg: str | None = None) -> str | None:
    """Single-line, single-quote, no-semicolon rt.query expression calling the
    host api, nil-safe when the host isn't active. Returns None on a bad ref."""
    if fn not in ("add", "remove", "list", "tail"):
        return None
    if arg is not None and not _OBJECT_REF_RE.fullmatch(arg):
        return None
    call = f"_G.alchemease_hooks_api.{fn}({arg!r})" if arg is not None else f"_G.alchemease_hooks_api.{fn}()"
    # repr() gives single quotes for simple strings; guard anyway:
    if '"' in call or ";" in call or "\\" in call:
        return None
    return f"tostring(_G.alchemease_hooks_api and {call} or 'host-not-active')"

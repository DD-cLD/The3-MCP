"""Time-boxed, single-shot approvals for Tier 2/3 commands (spec §5 confirm_gate).

Model: the operator (Dave — usually relayed through cLD) grants approval for ONE
exact command string. The grant expires after `ttl_seconds` (config
`safety.approval_ttl_seconds`, default 300) and is consumed by first use.
dry_run mode never consults approvals — its block is absolute.

Exact-match by design: a grant for `Lua "Store Preset 4.106"` approves that
string and nothing else. Whitespace is normalized; nothing else is fuzzy.
"""
from __future__ import annotations

import re
import secrets
import time
from dataclasses import dataclass, field


def _normalize(command: str) -> str:
    return re.sub(r"\s+", " ", command.strip())


@dataclass
class _Grant:
    command: str
    tier_max: int
    expires_at: float
    token: str


@dataclass
class ApprovalRegistry:
    ttl_seconds: int = 300
    _grants: dict[str, _Grant] = field(default_factory=dict)

    def grant(self, command: str, tier_max: int = 2, ttl_seconds: int | None = None) -> _Grant:
        """Record approval for one exact command. Returns the grant (with token)."""
        ttl = self.ttl_seconds if ttl_seconds is None else ttl_seconds
        key = _normalize(command)
        g = _Grant(
            command=key,
            tier_max=tier_max,
            expires_at=time.monotonic() + ttl,
            token=secrets.token_hex(8),
        )
        self._grants[key] = g
        return g

    def revoke(self, command: str) -> bool:
        return self._grants.pop(_normalize(command), None) is not None

    def consume(self, command: str, tier: int) -> bool:
        """True + removes the grant if a fresh approval covers this command/tier."""
        key = _normalize(command)
        g = self._grants.get(key)
        if g is None:
            return False
        if time.monotonic() > g.expires_at:
            del self._grants[key]
            return False
        if tier > g.tier_max:
            return False
        del self._grants[key]
        return True

    def pending(self) -> list[dict]:
        """Unexpired grants (housekeeping view). Prunes expired entries."""
        now = time.monotonic()
        expired = [k for k, g in self._grants.items() if now > g.expires_at]
        for k in expired:
            del self._grants[k]
        return [
            {"command": g.command, "tier_max": g.tier_max, "expires_in_s": round(g.expires_at - now, 1)}
            for g in self._grants.values()
        ]

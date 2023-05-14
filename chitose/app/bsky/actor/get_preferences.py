# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_preferences(service: str, headers: dict[str, str]) -> bytes:
    """Get private preferences attached to the account."""
    return chitose.xrpc.call('app.bsky.actor.getPreferences', [], None, service, {} | headers)
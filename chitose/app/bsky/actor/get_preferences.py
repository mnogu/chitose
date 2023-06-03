# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_preferences(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get private preferences attached to the account."""
    return call('app.bsky.actor.getPreferences', [], None, {})
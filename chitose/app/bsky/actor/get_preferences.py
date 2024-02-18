# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_preferences(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get private preferences attached to the current account. Expected use is synchronization between multiple devices, and import/export during account migration. Requires auth."""
    return call('app.bsky.actor.getPreferences', [], None, {})
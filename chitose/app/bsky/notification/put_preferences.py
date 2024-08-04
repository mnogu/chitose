# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _put_preferences(call: chitose.xrpc.XrpcCall, priority: bool) -> bytes:
    """Set notification-related preferences for an account. Requires auth."""
    return call('app.bsky.notification.putPreferences', [], {'priority': priority}, {'Content-Type': 'application/json'})
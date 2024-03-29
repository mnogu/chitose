# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_seen(call: chitose.xrpc.XrpcCall, seen_at: str) -> bytes:
    """Notify server that the requesting account has seen notifications. Requires auth."""
    return call('app.bsky.notification.updateSeen', [], {'seenAt': seen_at}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_thread(call: chitose.xrpc.XrpcCall, root: str) -> bytes:
    """Mutes a thread preventing notifications from the thread and any of its children. Mutes are private in Bluesky. Requires auth."""
    return call('app.bsky.graph.muteThread', [], {'root': root}, {'Content-Type': 'application/json'})
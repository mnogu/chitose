# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_thread(call: chitose.xrpc.XrpcCall, root: str) -> bytes:
    """Unmutes the specified thread. Requires auth."""
    return call('app.bsky.graph.unmuteThread', [], {'root': root}, {'Content-Type': 'application/json'})
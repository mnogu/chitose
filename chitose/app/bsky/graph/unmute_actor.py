# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_actor(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Unmutes the specified account. Requires auth."""
    return call('app.bsky.graph.unmuteActor', [], {'actor': actor}, {'Content-Type': 'application/json'})
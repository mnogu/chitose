# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_actor(call: chitose.xrpc.XrpcCallable, actor: str) -> bytes:
    """Unmute an actor by did or handle."""
    return call('app.bsky.graph.unmuteActor', [], {'actor': actor}, {'Content-Type': 'application/json'})
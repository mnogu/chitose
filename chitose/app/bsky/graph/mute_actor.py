# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_actor(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Mute an actor by did or handle."""
    return call('app.bsky.graph.muteActor', [], {'actor': actor}, {'Content-Type': 'application/json'})
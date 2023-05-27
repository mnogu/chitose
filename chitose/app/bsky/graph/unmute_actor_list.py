# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_actor_list(call: chitose.xrpc.XrpcCallable, list: str) -> bytes:
    """Unmute a list of actors."""
    return call('app.bsky.graph.unmuteActorList', [], {'list': list}, {'Content-Type': 'application/json'})
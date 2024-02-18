# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_actor_list(call: chitose.xrpc.XrpcCall, list: str) -> bytes:
    """Unmutes the specified list of accounts. Requires auth."""
    return call('app.bsky.graph.unmuteActorList', [], {'list': list}, {'Content-Type': 'application/json'})
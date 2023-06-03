# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_actor_list(call: chitose.xrpc.XrpcCall, list: str) -> bytes:
    """Mute a list of actors."""
    return call('app.bsky.graph.muteActorList', [], {'list': list}, {'Content-Type': 'application/json'})
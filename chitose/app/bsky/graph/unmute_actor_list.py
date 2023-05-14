# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _unmute_actor_list(service: str, headers: dict[str, str], list: str) -> bytes:
    """Unmute a list of actors."""
    return chitose.xrpc.call('app.bsky.graph.unmuteActorList', [], {'list': list}, service, {'Content-Type': 'application/json'} | headers)
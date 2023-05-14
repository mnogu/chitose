# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_actor_list(service: str, headers: dict[str, str], list: str) -> bytes:
    """Mute a list of actors."""
    return chitose.xrpc.call('app.bsky.graph.muteActorList', [], {'list': list}, service, {'Content-Type': 'application/json'} | headers)
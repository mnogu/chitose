# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_actor_list(call: chitose.xrpc.XrpcCall, list: str) -> bytes:
    """Creates a mute relationship for the specified list of accounts. Mutes are private in Bluesky. Requires auth."""
    return call('app.bsky.graph.muteActorList', [], {'list': list}, {'Content-Type': 'application/json'})
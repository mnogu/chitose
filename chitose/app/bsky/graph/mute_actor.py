# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _mute_actor(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Creates a mute relationship for the specified account. Mutes are private in Bluesky. Requires auth."""
    return call('app.bsky.graph.muteActor', [], {'actor': actor}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_suggested_follows_by_actor(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Enumerates follows similar to a given account (actor). Expected use is to recommend additional accounts immediately after following one account."""
    return call('app.bsky.graph.getSuggestedFollowsByActor', [('actor', actor)], None, {})
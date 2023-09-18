# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_suggested_follows_by_actor(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """Get suggested follows related to a given actor."""
    return call('app.bsky.graph.getSuggestedFollowsByActor', [('actor', actor)], None, {})
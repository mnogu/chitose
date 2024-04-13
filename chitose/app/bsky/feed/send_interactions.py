# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.feed.defs

def _send_interactions(call: chitose.xrpc.XrpcCall, interactions: list[chitose.app.bsky.feed.defs.Interaction]) -> bytes:
    """Send information about interactions with feed items back to the feed generator that served them."""
    return call('app.bsky.feed.sendInteractions', [], {'interactions': interactions}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_feed_generators(call: chitose.xrpc.XrpcCall, feeds: list[str]) -> bytes:
    """Get information about a list of feed generators."""
    return call('app.bsky.feed.getFeedGenerators', [('feeds', feeds)], None, {})
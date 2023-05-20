# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_feed_generators(service: str, headers: dict[str, str], feeds: list[str]) -> bytes:
    """Get information about a list of feed generators"""
    return chitose.xrpc.call('app.bsky.feed.getFeedGenerators', [('feeds', feeds)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_feed_generator(service: str, headers: dict[str, str], feed: str) -> bytes:
    """Get information about a specific feed offered by a feed generator, such as its online status"""
    return chitose.xrpc.call('app.bsky.feed.getFeedGenerator', [('feed', feed)], None, service, {} | headers)
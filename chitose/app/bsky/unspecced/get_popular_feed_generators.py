# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_popular_feed_generators(call: chitose.xrpc.XrpcCallable) -> bytes:
    """An unspecced view of globally popular feed generators"""
    return call('app.bsky.unspecced.getPopularFeedGenerators', [], None, {})
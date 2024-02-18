# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_feed_generator(call: chitose.xrpc.XrpcCall, feed: str) -> bytes:
    """Get information about a feed generator. Implemented by AppView.


    :param feed: AT-URI of the feed generator record.
    """
    return call('app.bsky.feed.getFeedGenerator', [('feed', feed)], None, {})
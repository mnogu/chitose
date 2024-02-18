# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_posts(call: chitose.xrpc.XrpcCall, uris: list[str]) -> bytes:
    """Gets post views for a specified list of posts (by AT-URI). This is sometimes referred to as 'hydrating' a 'feed skeleton'.


    :param uris: List of post AT-URIs to return hydrated views for.
    """
    return call('app.bsky.feed.getPosts', [('uris', uris)], None, {})
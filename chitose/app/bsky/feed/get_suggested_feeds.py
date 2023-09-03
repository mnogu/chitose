# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_suggested_feeds(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of suggested feeds for the viewer."""
    return call('app.bsky.feed.getSuggestedFeeds', [('limit', limit), ('cursor', cursor)], None, {})
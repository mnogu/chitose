# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_feed_skeleton(call: chitose.xrpc.XrpcCallable, feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A skeleton of a feed provided by a feed generator"""
    return call('app.bsky.feed.getFeedSkeleton', [('feed', feed), ('limit', limit), ('cursor', cursor)], None, {})
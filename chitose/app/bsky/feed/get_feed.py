# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_feed(call: chitose.xrpc.XrpcCall, feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a hydrated feed from an actor's selected feed generator."""
    return call('app.bsky.feed.getFeed', [('feed', feed), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_popular_feed_generators(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """An unspecced view of globally popular feed generators"""
    return call('app.bsky.unspecced.getPopularFeedGenerators', [('limit', limit), ('cursor', cursor)], None, {})
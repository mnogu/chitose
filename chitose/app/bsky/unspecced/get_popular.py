# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_popular(call: chitose.xrpc.XrpcCall, include_nsfw: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """An unspecced view of globally popular items"""
    return call('app.bsky.unspecced.getPopular', [('includeNsfw', include_nsfw), ('limit', limit), ('cursor', cursor)], None, {})
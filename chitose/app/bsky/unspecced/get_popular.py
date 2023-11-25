# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_popular(call: chitose.xrpc.XrpcCall, include_nsfw: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """DEPRECATED: will be removed soon. Use a feed generator alternative."""
    return call('app.bsky.unspecced.getPopular', [('includeNsfw', include_nsfw), ('limit', limit), ('cursor', cursor)], None, {})
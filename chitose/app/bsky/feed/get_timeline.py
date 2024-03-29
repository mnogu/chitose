# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_timeline(call: chitose.xrpc.XrpcCall, algorithm: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a view of the requesting account's home timeline. This is expected to be some form of reverse-chronological feed.


    :param algorithm: Variant 'algorithm' for timeline. Implementation-specific. NOTE: most feed flexibility has been moved to feed generator mechanism.
    """
    return call('app.bsky.feed.getTimeline', [('algorithm', algorithm), ('limit', limit), ('cursor', cursor)], None, {})
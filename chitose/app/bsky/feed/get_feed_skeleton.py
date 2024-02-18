# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_feed_skeleton(call: chitose.xrpc.XrpcCall, feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a skeleton of a feed provided by a feed generator. Auth is optional, depending on provider requirements, and provides the DID of the requester. Implemented by Feed Generator Service.


    :param feed: Reference to feed generator record describing the specific feed being requested.
    """
    return call('app.bsky.feed.getFeedSkeleton', [('feed', feed), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_author_feed(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A view of an actor's feed."""
    return call('app.bsky.feed.getAuthorFeed', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_actor_likes(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A view of the posts liked by an actor."""
    return call('app.bsky.feed.getActorLikes', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
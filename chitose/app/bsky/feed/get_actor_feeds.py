# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_actor_feeds(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of feeds (feed generator records) created by the actor (in the actor's repo)."""
    return call('app.bsky.feed.getActorFeeds', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
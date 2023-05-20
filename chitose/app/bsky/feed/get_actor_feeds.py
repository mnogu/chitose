# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_actor_feeds(service: str, headers: dict[str, str], actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Retrieve a list of feeds created by a given actor"""
    return chitose.xrpc.call('app.bsky.feed.getActorFeeds', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
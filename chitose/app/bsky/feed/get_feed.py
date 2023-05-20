# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_feed(service: str, headers: dict[str, str], feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Compose and hydrate a feed from a user's selected feed generator"""
    return chitose.xrpc.call('app.bsky.feed.getFeed', [('feed', feed), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
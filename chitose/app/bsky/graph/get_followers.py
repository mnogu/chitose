# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_followers(service: str, headers: dict[str, str], actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Who is following an actor?"""
    return chitose.xrpc.call('app.bsky.graph.getFollowers', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
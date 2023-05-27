# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_follows(call: chitose.xrpc.XrpcCallable, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Who is an actor following?"""
    return call('app.bsky.graph.getFollows', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
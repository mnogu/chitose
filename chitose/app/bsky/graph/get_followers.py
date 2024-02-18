# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_followers(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates accounts which follow a specified account (actor)."""
    return call('app.bsky.graph.getFollowers', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_follows(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of who the actor follows."""
    return call('app.bsky.graph.getFollows', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
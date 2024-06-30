# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_actor_starter_packs(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of starter packs created by the actor."""
    return call('app.bsky.graph.getActorStarterPacks', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
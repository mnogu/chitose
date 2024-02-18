# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_blocks(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get mod lists that the requesting account (actor) is blocking. Requires auth."""
    return call('app.bsky.graph.getListBlocks', [('limit', limit), ('cursor', cursor)], None, {})
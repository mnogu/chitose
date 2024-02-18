# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_blocks(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates which accounts the requesting account is currently blocking. Requires auth."""
    return call('app.bsky.graph.getBlocks', [('limit', limit), ('cursor', cursor)], None, {})
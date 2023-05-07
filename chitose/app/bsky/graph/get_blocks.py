# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_blocks(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Who is the requester's account blocking?"""
    return chitose.xrpc.call('app.bsky.graph.getBlocks', [('limit', limit), ('cursor', cursor)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list(call: chitose.xrpc.XrpcCallable, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Fetch a list of actors"""
    return call('app.bsky.graph.getList', [('list', list), ('limit', limit), ('cursor', cursor)], None, {})
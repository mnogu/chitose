# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list(service: str, headers: dict[str, str], list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Fetch a list of actors"""
    return chitose.xrpc.call('app.bsky.graph.getList', [('list', list), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
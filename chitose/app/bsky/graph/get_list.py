# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list(call: chitose.xrpc.XrpcCall, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Gets a 'view' (with additional context) of a specified list.


    :param list: Reference (AT-URI) of the list record to hydrate.
    """
    return call('app.bsky.graph.getList', [('list', list), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_lists(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates the lists created by a specified account (actor).


    :param actor: The account (actor) to enumerate lists from.
    """
    return call('app.bsky.graph.getLists', [('actor', actor), ('limit', limit), ('cursor', cursor)], None, {})
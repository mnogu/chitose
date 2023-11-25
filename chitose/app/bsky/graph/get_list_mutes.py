# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_mutes(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get lists that the actor is muting."""
    return call('app.bsky.graph.getListMutes', [('limit', limit), ('cursor', cursor)], None, {})
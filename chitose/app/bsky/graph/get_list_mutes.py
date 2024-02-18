# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_mutes(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates mod lists that the requesting account (actor) currently has muted. Requires auth."""
    return call('app.bsky.graph.getListMutes', [('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_mutes(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates accounts that the requesting account (actor) currently has muted. Requires auth."""
    return call('app.bsky.graph.getMutes', [('limit', limit), ('cursor', cursor)], None, {})
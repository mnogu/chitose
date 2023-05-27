# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_suggestions(call: chitose.xrpc.XrpcCallable, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of actors suggested for following. Used in discovery UIs."""
    return call('app.bsky.actor.getSuggestions', [('limit', limit), ('cursor', cursor)], None, {})
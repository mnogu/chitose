# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_suggestions(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of actors suggested for following. Used in discovery UIs."""
    return chitose.xrpc.call('app.bsky.actor.getSuggestions', [('limit', limit), ('cursor', cursor)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_mutes(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Who does the viewer mute?"""
    return chitose.xrpc.call('app.bsky.graph.getMutes', [('limit', limit), ('cursor', cursor)], None, service, {} | headers)
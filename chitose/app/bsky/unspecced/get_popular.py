# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def _get_popular(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
    """An unspecced view of globally popular items"""
    return chitose.xrpc.call('app.bsky.unspecced.getPopular', [('limit', limit), ('cursor', cursor)], None, service, {} | headers)
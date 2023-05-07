# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_timeline(service: str, headers: dict[str, str], algorithm: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A view of the user's home timeline."""
    return chitose.xrpc.call('app.bsky.feed.getTimeline', [('algorithm', algorithm), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
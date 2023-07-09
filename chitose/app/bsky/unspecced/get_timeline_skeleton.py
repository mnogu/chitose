# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_timeline_skeleton(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A skeleton of a timeline - UNSPECCED & WILL GO AWAY SOON"""
    return call('app.bsky.unspecced.getTimelineSkeleton', [('limit', limit), ('cursor', cursor)], None, {})
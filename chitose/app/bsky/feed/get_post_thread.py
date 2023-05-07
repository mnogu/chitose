# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_post_thread(service: str, headers: dict[str, str], uri: str, depth: typing.Optional[int]=None) -> bytes:
    """"""
    return chitose.xrpc.call('app.bsky.feed.getPostThread', [('uri', uri), ('depth', depth)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_post_thread(call: chitose.xrpc.XrpcCallable, uri: str, depth: typing.Optional[int]=None) -> bytes:
    """"""
    return call('app.bsky.feed.getPostThread', [('uri', uri), ('depth', depth)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_post_thread(call: chitose.xrpc.XrpcCall, uri: str, depth: typing.Optional[int]=None, parent_height: typing.Optional[int]=None) -> bytes:
    """Get posts in a thread."""
    return call('app.bsky.feed.getPostThread', [('uri', uri), ('depth', depth), ('parentHeight', parent_height)], None, {})
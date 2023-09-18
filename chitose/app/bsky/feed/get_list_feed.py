# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_feed(call: chitose.xrpc.XrpcCall, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """A view of a recent posts from actors in a list"""
    return call('app.bsky.feed.getListFeed', [('list', list), ('limit', limit), ('cursor', cursor)], None, {})
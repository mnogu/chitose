# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_feed(call: chitose.xrpc.XrpcCall, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a feed of recent posts from a list (posts and reposts from any actors on the list). Does not require auth.


    :param list: Reference (AT-URI) to the list record.
    """
    return call('app.bsky.feed.getListFeed', [('list', list), ('limit', limit), ('cursor', cursor)], None, {})
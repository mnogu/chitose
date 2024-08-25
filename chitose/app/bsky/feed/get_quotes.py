# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_quotes(call: chitose.xrpc.XrpcCall, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of quotes for a given post.


    :param uri: Reference (AT-URI) of post record

    :param cid: If supplied, filters to quotes of specific version (by CID) of the post record.
    """
    return call('app.bsky.feed.getQuotes', [('uri', uri), ('cid', cid), ('limit', limit), ('cursor', cursor)], None, {})
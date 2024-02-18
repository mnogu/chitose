# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_post_thread(call: chitose.xrpc.XrpcCall, uri: str, depth: typing.Optional[int]=None, parent_height: typing.Optional[int]=None) -> bytes:
    """Get posts in a thread. Does not require auth, but additional metadata and filtering will be applied for authed requests.


    :param uri: Reference (AT-URI) to post record.

    :param depth: How many levels of reply depth should be included in response.

    :param parent_height: How many levels of parent (and grandparent, etc) post to include.
    """
    return call('app.bsky.feed.getPostThread', [('uri', uri), ('depth', depth), ('parentHeight', parent_height)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_posts_skeleton(call: chitose.xrpc.XrpcCall, q: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Backend Posts search, returns only skeleton


    :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.

    :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    """
    return call('app.bsky.unspecced.searchPostsSkeleton', [('q', q), ('limit', limit), ('cursor', cursor)], None, {})
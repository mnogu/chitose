# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors(call: chitose.xrpc.XrpcCall, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Find actors (profiles) matching search criteria.


    :param term: DEPRECATED: use 'q' instead

    :param q: search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended
    """
    return call('app.bsky.actor.searchActors', [('term', term), ('q', q), ('limit', limit), ('cursor', cursor)], None, {})
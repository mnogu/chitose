# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors_typeahead(call: chitose.xrpc.XrpcCall, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Find actor suggestions for a search term.


    :param term: DEPRECATED: use 'q' instead

    :param q: search query prefix; not a full query string
    """
    return call('app.bsky.actor.searchActorsTypeahead', [('term', term), ('q', q), ('limit', limit)], None, {})
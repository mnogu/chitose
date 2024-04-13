# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors_typeahead(call: chitose.xrpc.XrpcCall, term: typing.Optional[str]=None, q: typing.Optional[str]=None, viewer: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Find actor suggestions for a prefix search term. Expected use is for auto-completion during text field entry. Does not require auth.


    :param term: DEPRECATED: use 'q' instead.

    :param q: Search query prefix; not a full query string.

    :param viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.
    """
    return call('app.bsky.actor.searchActorsTypeahead', [('term', term), ('q', q), ('viewer', viewer), ('limit', limit)], None, {})
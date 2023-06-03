# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors_typeahead(call: chitose.xrpc.XrpcCall, term: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Find actor suggestions for a search term."""
    return call('app.bsky.actor.searchActorsTypeahead', [('term', term), ('limit', limit)], None, {})
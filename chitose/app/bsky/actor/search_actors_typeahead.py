# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors_typeahead(service: str, headers: dict[str, str], term: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Find actor suggestions for a search term."""
    return chitose.xrpc.call('app.bsky.actor.searchActorsTypeahead', [('term', term), ('limit', limit)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors_skeleton(call: chitose.xrpc.XrpcCall, q: str, typeahead: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Backend Actors (profile) search, returning only skeleton


    :param q: search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended. For typeahead search, only simple term match is supported, not full syntax

    :param typeahead: if true, acts as fast/simple 'typeahead' query

    :param cursor: optional pagination mechanism; may not necessarily allow scrolling through entire result set
    """
    return call('app.bsky.unspecced.searchActorsSkeleton', [('q', q), ('typeahead', typeahead), ('limit', limit), ('cursor', cursor)], None, {})
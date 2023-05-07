# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_actors(service: str, headers: dict[str, str], term: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Find actors matching search criteria."""
    return chitose.xrpc.call('app.bsky.actor.searchActors', [('term', term), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
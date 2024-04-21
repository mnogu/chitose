# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_suggestions_skeleton(call: chitose.xrpc.XrpcCall, viewer: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a skeleton of suggested actors. Intended to be called and then hydrated through app.bsky.actor.getSuggestions


    :param viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.
    """
    return call('app.bsky.unspecced.getSuggestionsSkeleton', [('viewer', viewer), ('limit', limit), ('cursor', cursor)], None, {})
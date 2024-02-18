# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_suggestions(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Get a list of suggested actors. Expected use is discovery of accounts to follow during new account onboarding."""
    return call('app.bsky.actor.getSuggestions', [('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_repos(call: chitose.xrpc.XrpcCall, term: typing.Optional[str]=None, invited_by: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Find repositories based on a search term."""
    return call('com.atproto.admin.searchRepos', [('term', term), ('invitedBy', invited_by), ('limit', limit), ('cursor', cursor)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_accounts(call: chitose.xrpc.XrpcCall, email: typing.Optional[str]=None, cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Get list of accounts that matches your search query."""
    return call('com.atproto.admin.searchAccounts', [('email', email), ('cursor', cursor), ('limit', limit)], None, {})
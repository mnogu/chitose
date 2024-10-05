# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_accounts(call: chitose.xrpc.XrpcCall, values: list[str], cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Search for accounts that match one or more threat signature values."""
    return call('tools.ozone.signature.searchAccounts', [('values', values), ('cursor', cursor), ('limit', limit)], None, {})
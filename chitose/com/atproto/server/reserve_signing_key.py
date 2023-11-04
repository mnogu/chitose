# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _reserve_signing_key(call: chitose.xrpc.XrpcCall, did: typing.Optional[str]=None) -> bytes:
    """Reserve a repo signing key for account creation.


    :param did: The did to reserve a new did:key for
    """
    return call('com.atproto.server.reserveSigningKey', [], {'did': did}, {'Content-Type': 'application/json'})
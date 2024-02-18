# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _reserve_signing_key(call: chitose.xrpc.XrpcCall, did: typing.Optional[str]=None) -> bytes:
    """Reserve a repo signing key, for use with account creation. Necessary so that a DID PLC update operation can be constructed during an account migraiton. Public and does not require auth; implemented by PDS. NOTE: this endpoint may change when full account migration is implemented.


    :param did: The DID to reserve a key for.
    """
    return call('com.atproto.server.reserveSigningKey', [], {'did': did}, {'Content-Type': 'application/json'})
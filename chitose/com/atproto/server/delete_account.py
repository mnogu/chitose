# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_account(call: chitose.xrpc.XrpcCall, did: str, password: str, token: str) -> bytes:
    """Delete an actor's account with a token and password. Can only be called after requesting a deletion token. Requires auth."""
    return call('com.atproto.server.deleteAccount', [], {'did': did, 'password': password, 'token': token}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_account(call: chitose.xrpc.XrpcCallable, did: str, password: str, token: str) -> bytes:
    """Delete a user account with a token and password."""
    return call('com.atproto.server.deleteAccount', [], {'did': did, 'password': password, 'token': token}, {'Content-Type': 'application/json'})
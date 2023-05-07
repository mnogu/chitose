# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_account(service: str, headers: dict[str, str], did: str, password: str, token: str) -> bytes:
    """Delete a user account with a token and password."""
    return chitose.xrpc.call('com.atproto.server.deleteAccount', [], {'did': did, 'password': password, 'token': token}, service, {'Content-Type': 'application/json'} | headers)
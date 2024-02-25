# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_account_password(call: chitose.xrpc.XrpcCall, did: str, password: str) -> bytes:
    """Update the password for a user account as an administrator."""
    return call('com.atproto.admin.updateAccountPassword', [], {'did': did, 'password': password}, {'Content-Type': 'application/json'})
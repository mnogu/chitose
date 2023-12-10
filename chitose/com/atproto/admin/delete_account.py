# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_account(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Delete a user account as an administrator."""
    return call('com.atproto.admin.deleteAccount', [], {'did': did}, {'Content-Type': 'application/json'})
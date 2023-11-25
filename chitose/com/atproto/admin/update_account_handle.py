# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_account_handle(call: chitose.xrpc.XrpcCall, did: str, handle: str) -> bytes:
    """Administrative action to update an account's handle."""
    return call('com.atproto.admin.updateAccountHandle', [], {'did': did, 'handle': handle}, {'Content-Type': 'application/json'})
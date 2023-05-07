# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_account_handle(service: str, headers: dict[str, str], did: str, handle: str) -> bytes:
    """Administrative action to update an account's handle"""
    return chitose.xrpc.call('com.atproto.admin.updateAccountHandle', [], {'did': did, 'handle': handle}, service, {'Content-Type': 'application/json'} | headers)
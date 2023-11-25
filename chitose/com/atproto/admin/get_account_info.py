# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_account_info(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Get details about an account."""
    return call('com.atproto.admin.getAccountInfo', [('did', did)], None, {})
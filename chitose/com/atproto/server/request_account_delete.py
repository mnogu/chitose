# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_account_delete(call: chitose.xrpc.XrpcCall) -> bytes:
    """Initiate a user account deletion via email."""
    return call('com.atproto.server.requestAccountDelete', [], {}, {})
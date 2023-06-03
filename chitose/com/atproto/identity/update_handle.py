# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_handle(call: chitose.xrpc.XrpcCall, handle: str) -> bytes:
    """Updates the handle of the account"""
    return call('com.atproto.identity.updateHandle', [], {'handle': handle}, {'Content-Type': 'application/json'})
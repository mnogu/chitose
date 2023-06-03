# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _reset_password(call: chitose.xrpc.XrpcCall, token: str, password: str) -> bytes:
    """Reset a user account password using a token."""
    return call('com.atproto.server.resetPassword', [], {'token': token, 'password': password}, {'Content-Type': 'application/json'})
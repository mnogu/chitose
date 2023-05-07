# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _reset_password(service: str, headers: dict[str, str], token: str, password: str) -> bytes:
    """Reset a user account password using a token."""
    return chitose.xrpc.call('com.atproto.server.resetPassword', [], {'token': token, 'password': password}, service, {'Content-Type': 'application/json'} | headers)
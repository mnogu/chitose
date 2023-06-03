# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_password_reset(call: chitose.xrpc.XrpcCall, email: str) -> bytes:
    """Initiate a user account password reset via email."""
    return call('com.atproto.server.requestPasswordReset', [], {'email': email}, {'Content-Type': 'application/json'})
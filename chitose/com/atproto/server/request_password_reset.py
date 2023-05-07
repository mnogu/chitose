# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_password_reset(service: str, headers: dict[str, str], email: str) -> bytes:
    """Initiate a user account password reset via email."""
    return chitose.xrpc.call('com.atproto.server.requestPasswordReset', [], {'email': email}, service, {'Content-Type': 'application/json'} | headers)
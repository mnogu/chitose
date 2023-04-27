from __future__ import annotations
import chitose

def reset_password(service: str, headers: dict[str, str], token: str, password: str):
    """Reset a user account password using a token."""
    return chitose.xrpc.call('com.atproto.server.resetPassword', [], {'token': token, 'password': password}, service, {'Content-Type': 'application/json'} | headers)
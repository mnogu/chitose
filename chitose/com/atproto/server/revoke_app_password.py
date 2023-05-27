# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _revoke_app_password(call: chitose.xrpc.XrpcCallable, name: str) -> bytes:
    """Revoke an app-specific password by name."""
    return call('com.atproto.server.revokeAppPassword', [], {'name': name}, {'Content-Type': 'application/json'})
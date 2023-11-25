# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _revoke_app_password(call: chitose.xrpc.XrpcCall, name: str) -> bytes:
    """Revoke an App Password by name."""
    return call('com.atproto.server.revokeAppPassword', [], {'name': name}, {'Content-Type': 'application/json'})
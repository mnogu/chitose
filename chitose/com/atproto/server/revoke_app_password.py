# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _revoke_app_password(service: str, headers: dict[str, str], name: str) -> bytes:
    """Revoke an app-specific password by name."""
    return chitose.xrpc.call('com.atproto.server.revokeAppPassword', [], {'name': name}, service, {'Content-Type': 'application/json'} | headers)
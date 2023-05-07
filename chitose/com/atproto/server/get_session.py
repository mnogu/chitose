# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_session(service: str, headers: dict[str, str]) -> bytes:
    """Get information about the current session."""
    return chitose.xrpc.call('com.atproto.server.getSession', [], None, service, {} | headers)
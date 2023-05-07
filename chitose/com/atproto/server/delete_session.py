# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_session(service: str, headers: dict[str, str]) -> bytes:
    """Delete the current session."""
    return chitose.xrpc.call('com.atproto.server.deleteSession', [], {}, service, {} | headers)
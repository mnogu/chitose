# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _refresh_session(service: str, headers: dict[str, str]) -> bytes:
    """Refresh an authentication session."""
    return chitose.xrpc.call('com.atproto.server.refreshSession', [], {}, service, {} | headers)
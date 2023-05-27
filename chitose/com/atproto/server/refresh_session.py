# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _refresh_session(call: chitose.xrpc.XrpcCallable) -> bytes:
    """Refresh an authentication session."""
    return call('com.atproto.server.refreshSession', [], {}, {})
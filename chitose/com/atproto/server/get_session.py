# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_session(call: chitose.xrpc.XrpcCallable) -> bytes:
    """Get information about the current session."""
    return call('com.atproto.server.getSession', [], None, {})
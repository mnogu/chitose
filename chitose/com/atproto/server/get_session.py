# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_session(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get information about the current auth session. Requires auth."""
    return call('com.atproto.server.getSession', [], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_session(call: chitose.xrpc.XrpcCallable) -> bytes:
    """Delete the current session."""
    return call('com.atproto.server.deleteSession', [], {}, {})
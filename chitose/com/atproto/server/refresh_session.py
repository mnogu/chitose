# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _refresh_session(call: chitose.xrpc.XrpcCall) -> bytes:
    """Refresh an authentication session. Requires auth using the 'refreshJwt' (not the 'accessJwt')."""
    return call('com.atproto.server.refreshSession', [], {}, {})
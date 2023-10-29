# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _reserve_signing_key(call: chitose.xrpc.XrpcCall) -> bytes:
    """Reserve a repo signing key for account creation."""
    return call('com.atproto.server.reserveSigningKey', [], {}, {})
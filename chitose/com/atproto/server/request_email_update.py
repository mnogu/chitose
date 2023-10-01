# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_email_update(call: chitose.xrpc.XrpcCall) -> bytes:
    """Request a token in order to update email."""
    return call('com.atproto.server.requestEmailUpdate', [], {}, {})
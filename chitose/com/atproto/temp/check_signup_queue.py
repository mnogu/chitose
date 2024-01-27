# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _check_signup_queue(call: chitose.xrpc.XrpcCall) -> bytes:
    """Check accounts location in signup queue."""
    return call('com.atproto.temp.checkSignupQueue', [], None, {})
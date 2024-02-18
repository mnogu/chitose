# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_handle(call: chitose.xrpc.XrpcCall, handle: str) -> bytes:
    """Updates the current account's handle. Verifies handle validity, and updates did:plc document if necessary. Implemented by PDS, and requires auth.


    :param handle: The new handle.
    """
    return call('com.atproto.identity.updateHandle', [], {'handle': handle}, {'Content-Type': 'application/json'})
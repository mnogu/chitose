# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _push_blob(call: chitose.xrpc.XrpcCall, input_: bytes) -> bytes:
    """Gets the did's repo, optionally catching up from a specific revision."""
    return call('com.atproto.temp.pushBlob', [], input_, {'Content-Type': '*/*'})
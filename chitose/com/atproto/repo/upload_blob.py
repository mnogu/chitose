# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _upload_blob(call: chitose.xrpc.XrpcCallable, input_: bytes) -> bytes:
    """Upload a new blob to be added to repo in a later request."""
    return call('com.atproto.repo.uploadBlob', [], input_, {'Content-Type': '*/*'})
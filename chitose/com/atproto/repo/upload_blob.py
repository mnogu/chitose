# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _upload_blob(service: str, headers: dict[str, str], input_: bytes) -> bytes:
    """Upload a new blob to be added to repo in a later request."""
    return chitose.xrpc.call('com.atproto.repo.uploadBlob', [], input_, service, {'Content-Type': '*/*'} | headers)
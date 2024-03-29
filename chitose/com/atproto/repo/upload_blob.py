# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _upload_blob(call: chitose.xrpc.XrpcCall, input_: bytes) -> bytes:
    """Upload a new blob, to be referenced from a repository record. The blob will be deleted if it is not referenced within a time window (eg, minutes). Blob restrictions (mimetype, size, etc) are enforced when the reference is created. Requires auth, implemented by PDS."""
    return call('com.atproto.repo.uploadBlob', [], input_, {'Content-Type': '*/*'})
from __future__ import annotations
import chitose

def upload_blob(service: str, headers: dict[str, str]):
    """Upload a new blob to be added to repo in a later request."""
    return chitose.xrpc.call('com.atproto.repo.uploadBlob', [], {}, service, {'Content-Type': '*/*'} | headers)
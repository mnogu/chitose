# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def get_blob(service: str, headers: dict[str, str], did: str, cid: str):
    """Get a blob associated with a given repo."""
    return chitose.xrpc.call('com.atproto.sync.getBlob', [('did', did), ('cid', cid)], None, service, {} | headers)
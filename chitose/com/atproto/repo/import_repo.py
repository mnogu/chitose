# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _import_repo(call: chitose.xrpc.XrpcCall, input_: bytes) -> bytes:
    """Import a repo in the form of a CAR file. Requires Content-Length HTTP header to be set."""
    return call('com.atproto.repo.importRepo', [], input_, {'Content-Type': 'application/vnd.ipld.car'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _import_repo(call: chitose.xrpc.XrpcCall, input_: bytes) -> bytes:
    """Gets the did's repo, optionally catching up from a specific revision."""
    return call('com.atproto.temp.importRepo', [], input_, {'Content-Type': 'application/vnd.ipld.car'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_blob(call: chitose.xrpc.XrpcCall, did: str, cid: str) -> bytes:
    """Get a blob associated with a given repo.


    :param did: The DID of the repo.

    :param cid: The CID of the blob to fetch
    """
    return call('com.atproto.sync.getBlob', [('did', did), ('cid', cid)], None, {})
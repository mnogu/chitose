# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_blob(service: str, headers: dict[str, str], did: str, cid: str) -> bytes:
    """Get a blob associated with a given repo.


    :param did: The DID of the repo.

    :param cid: The CID of the blob to fetch
    """
    return chitose.xrpc.call('com.atproto.sync.getBlob', [('did', did), ('cid', cid)], None, service, {} | headers)
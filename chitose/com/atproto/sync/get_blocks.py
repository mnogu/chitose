# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_blocks(call: chitose.xrpc.XrpcCall, did: str, cids: list[str]) -> bytes:
    """Get data blocks from a given repo, by CID. For example, intermediate MST nodes, or records. Does not require auth; implemented by PDS.


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getBlocks', [('did', did), ('cids', cids)], None, {})
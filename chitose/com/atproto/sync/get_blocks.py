# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_blocks(service: str, headers: dict[str, str], did: str, cids: list[str]) -> bytes:
    """Gets blocks from a given repo.


    :param did: The DID of the repo.
    """
    return chitose.xrpc.call('com.atproto.sync.getBlocks', [('did', did), ('cids', cids)], None, service, {} | headers)
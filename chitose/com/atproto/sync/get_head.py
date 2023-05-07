# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_head(service: str, headers: dict[str, str], did: str) -> bytes:
    """Gets the current HEAD CID of a repo.


    :param did: The DID of the repo.
    """
    return chitose.xrpc.call('com.atproto.sync.getHead', [('did', did)], None, service, {} | headers)
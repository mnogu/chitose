# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_head(call: chitose.xrpc.XrpcCallable, did: str) -> bytes:
    """Gets the current HEAD CID of a repo.


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getHead', [('did', did)], None, {})
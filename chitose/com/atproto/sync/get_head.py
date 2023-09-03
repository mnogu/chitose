# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_head(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """DEPRECATED - please use com.atproto.sync.getLatestCommit instead


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getHead', [('did', did)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_latest_commit(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Gets the current commit CID & revision of the repo.


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getLatestCommit', [('did', did)], None, {})
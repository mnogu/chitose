# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_repo_status(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Get the hosting status for a repository, on this server. Expected to be implemented by PDS and Relay.


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getRepoStatus', [('did', did)], None, {})
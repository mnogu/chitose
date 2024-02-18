# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _describe_repo(call: chitose.xrpc.XrpcCall, repo: str) -> bytes:
    """Get information about an account and repository, including the list of collections. Does not require auth.


    :param repo: The handle or DID of the repo.
    """
    return call('com.atproto.repo.describeRepo', [('repo', repo)], None, {})
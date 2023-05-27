# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _describe_repo(call: chitose.xrpc.XrpcCallable, repo: str) -> bytes:
    """Get information about the repo, including the list of collections.


    :param repo: The handle or DID of the repo.
    """
    return call('com.atproto.repo.describeRepo', [('repo', repo)], None, {})
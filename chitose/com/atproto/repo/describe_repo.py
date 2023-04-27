# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def describe_repo(service: str, headers: dict[str, str], repo: str):
    """Get information about the repo, including the list of collections."""
    return chitose.xrpc.call('com.atproto.repo.describeRepo', [('repo', repo)], None, service, {} | headers)
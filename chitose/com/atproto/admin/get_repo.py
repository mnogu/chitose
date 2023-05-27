# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_repo(call: chitose.xrpc.XrpcCallable, did: str) -> bytes:
    """View details about a repository."""
    return call('com.atproto.admin.getRepo', [('did', did)], None, {})
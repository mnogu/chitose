# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_repo(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Get details about a repository."""
    return call('tools.ozone.moderation.getRepo', [('did', did)], None, {})
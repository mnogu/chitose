# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_repos(call: chitose.xrpc.XrpcCall, dids: list[str]) -> bytes:
    """Get details about some repositories."""
    return call('tools.ozone.moderation.getRepos', [('dids', dids)], None, {})
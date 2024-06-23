# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_member(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """Delete a member from ozone team. Requires admin role."""
    return call('tools.ozone.team.deleteMember', [], {'did': did}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _reverse_moderation_action(call: chitose.xrpc.XrpcCall, id: int, reason: str, created_by: str) -> bytes:
    """Reverse a moderation action."""
    return call('com.atproto.admin.reverseModerationAction', [], {'id': id, 'reason': reason, 'createdBy': created_by}, {'Content-Type': 'application/json'})
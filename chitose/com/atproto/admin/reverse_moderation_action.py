# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _reverse_moderation_action(service: str, headers: dict[str, str], id: int, reason: str, created_by: str) -> bytes:
    """Reverse a moderation action."""
    return chitose.xrpc.call('com.atproto.admin.reverseModerationAction', [], {'id': id, 'reason': reason, 'createdBy': created_by}, service, {'Content-Type': 'application/json'} | headers)
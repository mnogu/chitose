# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_moderation_event(call: chitose.xrpc.XrpcCall, id: int) -> bytes:
    """Get details about a moderation event."""
    return call('com.atproto.admin.getModerationEvent', [('id', id)], None, {})
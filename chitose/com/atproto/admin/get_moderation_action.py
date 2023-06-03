# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_moderation_action(call: chitose.xrpc.XrpcCall, id: int) -> bytes:
    """View details about a moderation action."""
    return call('com.atproto.admin.getModerationAction', [('id', id)], None, {})
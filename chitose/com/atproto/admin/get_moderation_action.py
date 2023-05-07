# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_moderation_action(service: str, headers: dict[str, str], id: int) -> bytes:
    """View details about a moderation action."""
    return chitose.xrpc.call('com.atproto.admin.getModerationAction', [('id', id)], None, service, {} | headers)
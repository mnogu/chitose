# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_moderation_report(call: chitose.xrpc.XrpcCall, id: int) -> bytes:
    """Get details about a moderation report."""
    return call('com.atproto.admin.getModerationReport', [('id', id)], None, {})
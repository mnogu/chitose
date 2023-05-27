# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_moderation_report(call: chitose.xrpc.XrpcCallable, id: int) -> bytes:
    """View details about a moderation report."""
    return call('com.atproto.admin.getModerationReport', [('id', id)], None, {})
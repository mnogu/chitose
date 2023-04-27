# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def get_moderation_report(service: str, headers: dict[str, str], id: int):
    """View details about a moderation report."""
    return chitose.xrpc.call('com.atproto.admin.getModerationReport', [('id', id)], None, service, {} | headers)
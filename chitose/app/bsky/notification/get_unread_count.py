# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_unread_count(call: chitose.xrpc.XrpcCall, seen_at: typing.Optional[str]=None) -> bytes:
    """Get the count of unread notifications."""
    return call('app.bsky.notification.getUnreadCount', [('seenAt', seen_at)], None, {})
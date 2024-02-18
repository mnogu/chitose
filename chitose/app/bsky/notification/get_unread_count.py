# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_unread_count(call: chitose.xrpc.XrpcCall, seen_at: typing.Optional[str]=None) -> bytes:
    """Count the number of unread notifications for the requesting account. Requires auth."""
    return call('app.bsky.notification.getUnreadCount', [('seenAt', seen_at)], None, {})
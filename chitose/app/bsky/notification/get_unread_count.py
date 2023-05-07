# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_unread_count(service: str, headers: dict[str, str], seen_at: typing.Optional[str]=None) -> bytes:
    """"""
    return chitose.xrpc.call('app.bsky.notification.getUnreadCount', [('seenAt', seen_at)], None, service, {} | headers)
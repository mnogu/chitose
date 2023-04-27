from __future__ import annotations
import chitose
import typing

def get_unread_count(service: str, headers: dict[str, str], seen_at: typing.Optional[str]=None):
    """"""
    return chitose.xrpc.call('app.bsky.notification.getUnreadCount', [('seenAt', seen_at)], None, service, {} | headers)
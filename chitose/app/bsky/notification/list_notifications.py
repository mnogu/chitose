# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.com.atproto.label.defs
import typing

def _list_notifications(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, seen_at: typing.Optional[str]=None) -> bytes:
    """"""
    return chitose.xrpc.call('app.bsky.notification.listNotifications', [('limit', limit), ('cursor', cursor), ('seenAt', seen_at)], None, service, {} | headers)

class Notification(chitose.Object):
    """


    :param reason: Expected values are 'like', 'repost', 'follow', 'mention', 'reply', and 'quote'.
    """

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileView, reason: str, record: typing.Any, is_read: str, indexed_at: str, reason_subject: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.reason = reason
        self.record = record
        self.is_read = is_read
        self.indexed_at = indexed_at
        self.reason_subject = reason_subject
        self.labels = labels

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'reason': self.reason, 'record': self.record, 'isRead': self.is_read, 'indexedAt': self.indexed_at, 'reasonSubject': self.reason_subject, 'labels': self.labels, '$type': 'app.bsky.notification.listNotifications#notification'}
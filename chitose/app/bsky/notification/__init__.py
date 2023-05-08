# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_unread_count import _get_unread_count
from .list_notifications import _list_notifications
from .update_seen import _update_seen
import chitose
import typing

class Notification_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def update_seen(self, seen_at: str) -> bytes:
        """Notify server that the user has seen notifications."""
        return _update_seen(self.service, self.headers, seen_at)

    def list_notifications(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, seen_at: typing.Optional[str]=None) -> bytes:
        """"""
        return _list_notifications(self.service, self.headers, limit, cursor, seen_at)

    def get_unread_count(self, seen_at: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_unread_count(self.service, self.headers, seen_at)
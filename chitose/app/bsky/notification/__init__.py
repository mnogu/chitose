# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_unread_count import _get_unread_count
from .list_notifications import _list_notifications
from .put_preferences import _put_preferences
from .register_push import _register_push
from .update_seen import _update_seen
import typing

class Notification_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def update_seen(self, seen_at: str) -> bytes:
        """Notify server that the requesting account has seen notifications. Requires auth."""
        return _update_seen(self.call, seen_at)

    def get_unread_count(self, priority: typing.Optional[bool]=None, seen_at: typing.Optional[str]=None) -> bytes:
        """Count the number of unread notifications for the requesting account. Requires auth."""
        return _get_unread_count(self.call, priority, seen_at)

    def list_notifications(self, limit: typing.Optional[int]=None, priority: typing.Optional[bool]=None, cursor: typing.Optional[str]=None, seen_at: typing.Optional[str]=None) -> bytes:
        """Enumerate notifications for the requesting account. Requires auth."""
        return _list_notifications(self.call, limit, priority, cursor, seen_at)

    def put_preferences(self, priority: bool) -> bytes:
        """Set notification-related preferences for an account. Requires auth."""
        return _put_preferences(self.call, priority)

    def register_push(self, service_did: str, token: str, platform: typing.Literal['ios', 'android', 'web'], app_id: str) -> bytes:
        """Register to receive push notifications, via a specified service, for the requesting account. Requires auth."""
        return _register_push(self.call, service_did, token, platform, app_id)
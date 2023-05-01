# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_unread_count import *
from .list_notifications import *
from .update_seen import *

class _Notification:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def update_seen(self, seen_at: str):
        return update_seen(self.service, self.headers, seen_at)

    def list_notifications(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, seen_at: typing.Optional[str]=None):
        return list_notifications(self.service, self.headers, limit, cursor, seen_at)

    def get_unread_count(self, seen_at: typing.Optional[str]=None):
        return get_unread_count(self.service, self.headers, seen_at)
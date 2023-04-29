# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_unread_count import *
from .list_notifications import *
from .update_seen import *
import chitose
import chitose.app.bsky.actor.defs
import chitose.com.atproto.label.defs
import typing

class Notification:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def update_seen(self, seen_at: str):
        return update_seen(self.service, self.headers, seen_at)

    def list_notifications(self, limit: typing.Optional[int], cursor: typing.Optional[str], seen_at: typing.Optional[str]):
        return list_notifications(self.service, self.headers, limit, cursor, seen_at)

    def get_unread_count(self, seen_at: typing.Optional[str]):
        return get_unread_count(self.service, self.headers, seen_at)
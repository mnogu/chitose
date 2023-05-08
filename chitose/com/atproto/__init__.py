# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .admin import Admin_
from .identity import Identity_
from .label import Label_
from .moderation import Moderation_
from .repo import Repo_
from .server import Server_
from .sync import Sync_

class Atproto_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    @property
    def admin(self):
        return Admin_(self.service, self.headers)

    @property
    def identity(self):
        return Identity_(self.service, self.headers)

    @property
    def label(self):
        return Label_(self.service, self.headers)

    @property
    def moderation(self):
        return Moderation_(self.service, self.headers)

    @property
    def repo(self):
        return Repo_(self.service, self.headers)

    @property
    def server(self):
        return Server_(self.service, self.headers)

    @property
    def sync(self):
        return Sync_(self.service, self.headers)
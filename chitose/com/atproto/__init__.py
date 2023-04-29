# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .admin import Admin
from .identity import Identity
from .label import Label
from .moderation import Moderation
from .repo import Repo
from .server import Server
from .sync import Sync

class Atproto:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def admin(self):
        return Admin(self.service, self.headers)

    @property
    def identity(self):
        return Identity(self.service, self.headers)

    @property
    def label(self):
        return Label(self.service, self.headers)

    @property
    def moderation(self):
        return Moderation(self.service, self.headers)

    @property
    def repo(self):
        return Repo(self.service, self.headers)

    @property
    def server(self):
        return Server(self.service, self.headers)

    @property
    def sync(self):
        return Sync(self.service, self.headers)
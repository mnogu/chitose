# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .admin import _Admin
from .identity import _Identity
from .label import _Label
from .moderation import _Moderation
from .repo import _Repo
from .server import _Server
from .sync import _Sync

class _Atproto:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def admin(self):
        return _Admin(self.service, self.headers)

    @property
    def identity(self):
        return _Identity(self.service, self.headers)

    @property
    def label(self):
        return _Label(self.service, self.headers)

    @property
    def moderation(self):
        return _Moderation(self.service, self.headers)

    @property
    def repo(self):
        return _Repo(self.service, self.headers)

    @property
    def server(self):
        return _Server(self.service, self.headers)

    @property
    def sync(self):
        return _Sync(self.service, self.headers)
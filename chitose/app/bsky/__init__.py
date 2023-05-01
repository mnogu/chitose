# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .actor import _Actor
from .embed import _Embed
from .feed import _Feed
from .graph import _Graph
from .notification import _Notification
from .richtext import _Richtext
from .unspecced import _Unspecced

class _Bsky:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def actor(self):
        return _Actor(self.service, self.headers)

    @property
    def embed(self):
        return _Embed(self.service, self.headers)

    @property
    def feed(self):
        return _Feed(self.service, self.headers)

    @property
    def graph(self):
        return _Graph(self.service, self.headers)

    @property
    def notification(self):
        return _Notification(self.service, self.headers)

    @property
    def richtext(self):
        return _Richtext(self.service, self.headers)

    @property
    def unspecced(self):
        return _Unspecced(self.service, self.headers)
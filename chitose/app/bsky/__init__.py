# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .actor import Actor
from .embed import Embed
from .feed import Feed
from .graph import Graph
from .notification import Notification
from .richtext import Richtext
from .unspecced import Unspecced

class Bsky:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def actor(self):
        return Actor(self.service, self.headers)

    @property
    def embed(self):
        return Embed(self.service, self.headers)

    @property
    def feed(self):
        return Feed(self.service, self.headers)

    @property
    def graph(self):
        return Graph(self.service, self.headers)

    @property
    def notification(self):
        return Notification(self.service, self.headers)

    @property
    def richtext(self):
        return Richtext(self.service, self.headers)

    @property
    def unspecced(self):
        return Unspecced(self.service, self.headers)
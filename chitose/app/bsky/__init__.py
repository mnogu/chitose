# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .actor import Actor_
from .embed import Embed_
from .feed import Feed_
from .graph import Graph_
from .notification import Notification_
from .richtext import Richtext_
from .unspecced import Unspecced_

class Bsky_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    @property
    def actor(self):
        return Actor_(self.service, self.headers)

    @property
    def embed(self):
        return Embed_(self.service, self.headers)

    @property
    def feed(self):
        return Feed_(self.service, self.headers)

    @property
    def graph(self):
        return Graph_(self.service, self.headers)

    @property
    def notification(self):
        return Notification_(self.service, self.headers)

    @property
    def richtext(self):
        return Richtext_(self.service, self.headers)

    @property
    def unspecced(self):
        return Unspecced_(self.service, self.headers)
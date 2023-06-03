# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from chitose.xrpc import XrpcSubscribe
from .actor import Actor_
from .embed import Embed_
from .feed import Feed_
from .graph import Graph_
from .notification import Notification_
from .richtext import Richtext_
from .unspecced import Unspecced_

class Bsky_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    @property
    def actor(self):
        return Actor_(self.call, self.subscribe)

    @property
    def embed(self):
        return Embed_(self.call, self.subscribe)

    @property
    def feed(self):
        return Feed_(self.call, self.subscribe)

    @property
    def graph(self):
        return Graph_(self.call, self.subscribe)

    @property
    def notification(self):
        return Notification_(self.call, self.subscribe)

    @property
    def richtext(self):
        return Richtext_(self.call, self.subscribe)

    @property
    def unspecced(self):
        return Unspecced_(self.call, self.subscribe)
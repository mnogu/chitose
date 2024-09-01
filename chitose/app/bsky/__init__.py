# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .actor import Actor_
from .embed import Embed_
from .feed import Feed_
from .graph import Graph_
from .labeler import Labeler_
from .notification import Notification_
from .richtext import Richtext_
from .unspecced import Unspecced_
from .video import Video_

class Bsky_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    @property
    def actor(self) -> Actor_:
        return Actor_(self.call, self.subscribe)

    @property
    def embed(self) -> Embed_:
        return Embed_(self.call, self.subscribe)

    @property
    def feed(self) -> Feed_:
        return Feed_(self.call, self.subscribe)

    @property
    def graph(self) -> Graph_:
        return Graph_(self.call, self.subscribe)

    @property
    def labeler(self) -> Labeler_:
        return Labeler_(self.call, self.subscribe)

    @property
    def notification(self) -> Notification_:
        return Notification_(self.call, self.subscribe)

    @property
    def richtext(self) -> Richtext_:
        return Richtext_(self.call, self.subscribe)

    @property
    def unspecced(self) -> Unspecced_:
        return Unspecced_(self.call, self.subscribe)

    @property
    def video(self) -> Video_:
        return Video_(self.call, self.subscribe)
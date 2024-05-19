# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .actor import Actor_
from .convo import Convo_
from .moderation import Moderation_

class Bsky_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    @property
    def actor(self) -> Actor_:
        return Actor_(self.call, self.subscribe)

    @property
    def convo(self) -> Convo_:
        return Convo_(self.call, self.subscribe)

    @property
    def moderation(self) -> Moderation_:
        return Moderation_(self.call, self.subscribe)
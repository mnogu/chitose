# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from chitose.xrpc import XrpcSubscribe

class Richtext_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe
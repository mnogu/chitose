# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from .atproto import Atproto_

class Com_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable) -> None:
        self.call = call

    @property
    def atproto(self):
        return Atproto_(self.call)
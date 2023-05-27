# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from .get_popular import _get_popular
import typing

class Unspecced_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable) -> None:
        self.call = call

    def get_popular(self, include_nsfw: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular items"""
        return _get_popular(self.call, include_nsfw, limit, cursor)
# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .apply_labels import _apply_labels
from .get_popular import _get_popular
from .get_popular_feed_generators import _get_popular_feed_generators
from .get_timeline_skeleton import _get_timeline_skeleton
import chitose.com.atproto.label.defs
import typing

class Unspecced_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def apply_labels(self, labels: list[chitose.com.atproto.label.defs.Label]) -> bytes:
        """Allow a labeler to apply labels directly."""
        return _apply_labels(self.call, labels)

    def get_popular(self, include_nsfw: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular items"""
        return _get_popular(self.call, include_nsfw, limit, cursor)

    def get_popular_feed_generators(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, query: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular feed generators"""
        return _get_popular_feed_generators(self.call, limit, cursor, query)

    def get_timeline_skeleton(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """A skeleton of a timeline - UNSPECCED & WILL GO AWAY SOON"""
        return _get_timeline_skeleton(self.call, limit, cursor)
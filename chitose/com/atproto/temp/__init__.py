# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .fetch_labels import _fetch_labels
import typing

class Temp_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def fetch_labels(self, since: typing.Optional[int]=None, limit: typing.Optional[int]=None) -> bytes:
        """Fetch all labels from a labeler created after a certain date."""
        return _fetch_labels(self.call, since, limit)
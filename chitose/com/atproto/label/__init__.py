# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .query_labels import _query_labels
from .subscribe_labels import _subscribe_labels
import chitose
import typing

class Label_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def subscribe_labels(self, handler: chitose.xrpc.XrpcHandler, cursor: typing.Optional[int]=None) -> None:
        """Subscribe to stream of labels (and negations). Public endpoint implemented by mod services. Uses same sequencing scheme as repo event stream.


        :param cursor: The last known event seq number to backfill from.
        """
        _subscribe_labels(self.subscribe, handler, cursor)

    def query_labels(self, uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find labels relevant to the provided AT-URI patterns. Public endpoint for moderation services, though may return different or additional results with auth.


        :param uri_patterns: List of AT URI patterns to match (boolean 'OR'). Each may be a prefix (ending with '*'; will match inclusive of the string leading to '*'), or a full URI.

        :param sources: Optional list of label sources (DIDs) to filter on.
        """
        return _query_labels(self.call, uri_patterns, sources, limit, cursor)
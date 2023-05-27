# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from .query_labels import _query_labels
import typing

class Label_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable) -> None:
        self.call = call

    def query_labels(self, uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find labels relevant to the provided URI patterns.


        :param uri_patterns: List of AT URI patterns to match (boolean 'OR'). Each may be a prefix (ending with '*'; will match inclusive of the string leading to '*'), or a full URI

        :param sources: Optional list of label sources (DIDs) to filter on
        """
        return _query_labels(self.call, uri_patterns, sources, limit, cursor)
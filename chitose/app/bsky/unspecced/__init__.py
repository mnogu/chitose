# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_popular_feed_generators import _get_popular_feed_generators
from .get_tagged_suggestions import _get_tagged_suggestions
from .get_timeline_skeleton import _get_timeline_skeleton
from .search_actors_skeleton import _search_actors_skeleton
from .search_posts_skeleton import _search_posts_skeleton
import typing

class Unspecced_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def search_actors_skeleton(self, q: str, typeahead: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Backend Actors (profile) search, returns only skeleton.


        :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended. For typeahead search, only simple term match is supported, not full syntax.

        :param typeahead: If true, acts as fast/simple 'typeahead' query.

        :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
        """
        return _search_actors_skeleton(self.call, q, typeahead, limit, cursor)

    def search_posts_skeleton(self, q: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Backend Posts search, returns only skeleton


        :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.

        :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
        """
        return _search_posts_skeleton(self.call, q, limit, cursor)

    def get_popular_feed_generators(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, query: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular feed generators."""
        return _get_popular_feed_generators(self.call, limit, cursor, query)

    def get_tagged_suggestions(self) -> bytes:
        """Get a list of suggestions (feeds and users) tagged with categories"""
        return _get_tagged_suggestions(self.call)

    def get_timeline_skeleton(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """DEPRECATED: a skeleton of a timeline. Unspecced and will be unavailable soon."""
        return _get_timeline_skeleton(self.call, limit, cursor)
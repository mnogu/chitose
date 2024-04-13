# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_popular_feed_generators import _get_popular_feed_generators
from .get_tagged_suggestions import _get_tagged_suggestions
from .search_actors_skeleton import _search_actors_skeleton
from .search_posts_skeleton import _search_posts_skeleton
import typing

class Unspecced_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def search_actors_skeleton(self, q: str, viewer: typing.Optional[str]=None, typeahead: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Backend Actors (profile) search, returns only skeleton.


        :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended. For typeahead search, only simple term match is supported, not full syntax.

        :param viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.

        :param typeahead: If true, acts as fast/simple 'typeahead' query.

        :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
        """
        return _search_actors_skeleton(self.call, q, viewer, typeahead, limit, cursor)

    def search_posts_skeleton(self, q: str, sort: typing.Optional[typing.Literal['top', 'latest']]=None, since: typing.Optional[str]=None, until: typing.Optional[str]=None, mentions: typing.Optional[str]=None, author: typing.Optional[str]=None, lang: typing.Optional[str]=None, domain: typing.Optional[str]=None, url: typing.Optional[str]=None, tag: typing.Optional[list[str]]=None, viewer: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Backend Posts search, returns only skeleton


        :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.

        :param sort: Specifies the ranking order of results.

        :param since: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).

        :param until: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).

        :param mentions: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.

        :param author: Filter to posts by the given account. Handles are resolved to DID before query-time.

        :param lang: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.

        :param domain: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.

        :param url: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.

        :param tag: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.

        :param viewer: DID of the account making the request (not included for public/unauthenticated queries). Used for 'from:me' queries.

        :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
        """
        return _search_posts_skeleton(self.call, q, sort, since, until, mentions, author, lang, domain, url, tag, viewer, limit, cursor)

    def get_popular_feed_generators(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, query: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular feed generators."""
        return _get_popular_feed_generators(self.call, limit, cursor, query)

    def get_tagged_suggestions(self) -> bytes:
        """Get a list of suggestions (feeds and users) tagged with categories"""
        return _get_tagged_suggestions(self.call)
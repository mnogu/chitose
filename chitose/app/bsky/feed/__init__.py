# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .describe_feed_generator import _describe_feed_generator
from .get_actor_feeds import _get_actor_feeds
from .get_actor_likes import _get_actor_likes
from .get_author_feed import _get_author_feed
from .get_feed import _get_feed
from .get_feed_generator import _get_feed_generator
from .get_feed_generators import _get_feed_generators
from .get_feed_skeleton import _get_feed_skeleton
from .get_likes import _get_likes
from .get_list_feed import _get_list_feed
from .get_post_thread import _get_post_thread
from .get_posts import _get_posts
from .get_reposted_by import _get_reposted_by
from .get_suggested_feeds import _get_suggested_feeds
from .get_timeline import _get_timeline
from .search_posts import _search_posts
import typing

class Feed_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_feed_generators(self, feeds: list[str]) -> bytes:
        """Get information about a list of feed generators."""
        return _get_feed_generators(self.call, feeds)

    def get_timeline(self, algorithm: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a view of the requesting account's home timeline. This is expected to be some form of reverse-chronological feed.


        :param algorithm: Variant 'algorithm' for timeline. Implementation-specific. NOTE: most feed flexibility has been moved to feed generator mechanism.
        """
        return _get_timeline(self.call, algorithm, limit, cursor)

    def get_feed_generator(self, feed: str) -> bytes:
        """Get information about a feed generator. Implemented by AppView.


        :param feed: AT-URI of the feed generator record.
        """
        return _get_feed_generator(self.call, feed)

    def get_author_feed(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, filter: typing.Optional[typing.Literal['posts_with_replies', 'posts_no_replies', 'posts_with_media', 'posts_and_author_threads']]=None) -> bytes:
        """Get a view of an actor's 'author feed' (post and reposts by the author). Does not require auth.


        :param filter: Combinations of post/repost types to include in response.
        """
        return _get_author_feed(self.call, actor, limit, cursor, filter)

    def get_likes(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get like records which reference a subject (by AT-URI and CID).


        :param uri: AT-URI of the subject (eg, a post record).

        :param cid: CID of the subject record (aka, specific version of record), to filter likes.
        """
        return _get_likes(self.call, uri, cid, limit, cursor)

    def get_post_thread(self, uri: str, depth: typing.Optional[int]=None, parent_height: typing.Optional[int]=None) -> bytes:
        """Get posts in a thread. Does not require auth, but additional metadata and filtering will be applied for authed requests.


        :param uri: Reference (AT-URI) to post record.

        :param depth: How many levels of reply depth should be included in response.

        :param parent_height: How many levels of parent (and grandparent, etc) post to include.
        """
        return _get_post_thread(self.call, uri, depth, parent_height)

    def get_actor_likes(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a list of posts liked by an actor. Does not require auth."""
        return _get_actor_likes(self.call, actor, limit, cursor)

    def get_reposted_by(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a list of reposts for a given post.


        :param uri: Reference (AT-URI) of post record

        :param cid: If supplied, filters to reposts of specific version (by CID) of the post record.
        """
        return _get_reposted_by(self.call, uri, cid, limit, cursor)

    def describe_feed_generator(self) -> bytes:
        """Get information about a feed generator, including policies and offered feed URIs. Does not require auth; implemented by Feed Generator services (not App View)."""
        return _describe_feed_generator(self.call)

    def search_posts(self, q: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find posts matching search criteria, returning views of those posts.


        :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.

        :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
        """
        return _search_posts(self.call, q, limit, cursor)

    def get_posts(self, uris: list[str]) -> bytes:
        """Gets post views for a specified list of posts (by AT-URI). This is sometimes referred to as 'hydrating' a 'feed skeleton'.


        :param uris: List of post AT-URIs to return hydrated views for.
        """
        return _get_posts(self.call, uris)

    def get_feed(self, feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a hydrated feed from an actor's selected feed generator. Implemented by App View."""
        return _get_feed(self.call, feed, limit, cursor)

    def get_feed_skeleton(self, feed: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a skeleton of a feed provided by a feed generator. Auth is optional, depending on provider requirements, and provides the DID of the requester. Implemented by Feed Generator Service.


        :param feed: Reference to feed generator record describing the specific feed being requested.
        """
        return _get_feed_skeleton(self.call, feed, limit, cursor)

    def get_list_feed(self, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a feed of recent posts from a list (posts and reposts from any actors on the list). Does not require auth.


        :param list: Reference (AT-URI) to the list record.
        """
        return _get_list_feed(self.call, list, limit, cursor)

    def get_suggested_feeds(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a list of suggested feeds (feed generators) for the requesting account."""
        return _get_suggested_feeds(self.call, limit, cursor)

    def get_actor_feeds(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a list of feeds (feed generator records) created by the actor (in the actor's repo)."""
        return _get_actor_feeds(self.call, actor, limit, cursor)
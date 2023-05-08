# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_author_feed import _get_author_feed
from .get_likes import _get_likes
from .get_post_thread import _get_post_thread
from .get_posts import _get_posts
from .get_reposted_by import _get_reposted_by
from .get_timeline import _get_timeline
import chitose
import typing

class Feed_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def get_timeline(self, algorithm: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """A view of the user's home timeline."""
        return _get_timeline(self.service, self.headers, algorithm, limit, cursor)

    def get_author_feed(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """A view of an actor's feed."""
        return _get_author_feed(self.service, self.headers, actor, limit, cursor)

    def get_likes(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_likes(self.service, self.headers, uri, cid, limit, cursor)

    def get_post_thread(self, uri: str, depth: typing.Optional[int]=None) -> bytes:
        """"""
        return _get_post_thread(self.service, self.headers, uri, depth)

    def get_reposted_by(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_reposted_by(self.service, self.headers, uri, cid, limit, cursor)

    def get_posts(self, uris: list[str]) -> bytes:
        """A view of an actor's feed."""
        return _get_posts(self.service, self.headers, uris)
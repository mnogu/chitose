# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_author_feed import _get_author_feed
from .get_likes import _get_likes
from .get_post_thread import _get_post_thread
from .get_posts import _get_posts
from .get_reposted_by import _get_reposted_by
from .get_timeline import _get_timeline
from .defs import *
from .get_author_feed import *
from .get_likes import *
from .get_post_thread import *
from .get_posts import *
from .get_reposted_by import *
from .get_timeline import *
from .like import *
from .post import *
from .repost import *

class Feed_:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_timeline(self, algorithm: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """A view of the user's home timeline."""
        return _get_timeline(self.service, self.headers, algorithm, limit, cursor)

    def get_author_feed(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """A view of an actor's feed."""
        return _get_author_feed(self.service, self.headers, actor, limit, cursor)

    def get_likes(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """"""
        return _get_likes(self.service, self.headers, uri, cid, limit, cursor)

    def get_post_thread(self, uri: str, depth: typing.Optional[int]=None):
        """"""
        return _get_post_thread(self.service, self.headers, uri, depth)

    def get_reposted_by(self, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """"""
        return _get_reposted_by(self.service, self.headers, uri, cid, limit, cursor)

    def get_posts(self, uris: list[str]):
        """A view of an actor's feed."""
        return _get_posts(self.service, self.headers, uris)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.feed.threadgate
import typing

class Threadgate(chitose.Record):
    """"""

    def __init__(self, post: str, created_at: str, allow: typing.Optional[list[typing.Union[chitose.app.bsky.feed.threadgate.MentionRule, chitose.app.bsky.feed.threadgate.FollowingRule, chitose.app.bsky.feed.threadgate.ListRule]]]=None) -> None:
        self.post = post
        self.created_at = created_at
        self.allow = allow

    def to_dict(self) -> dict[str, typing.Any]:
        return {'post': self.post, 'createdAt': self.created_at, 'allow': self.allow, '$type': 'app.bsky.feed.threadgate'}

class MentionRule(chitose.Object):
    """"""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'app.bsky.feed.threadgate#mentionRule'}

class FollowingRule(chitose.Object):
    """"""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'app.bsky.feed.threadgate#followingRule'}

class ListRule(chitose.Object):
    """"""

    def __init__(self, list: str) -> None:
        self.list = list

    def to_dict(self) -> dict[str, typing.Any]:
        return {'list': self.list, '$type': 'app.bsky.feed.threadgate#listRule'}
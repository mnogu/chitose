# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.feed.threadgate
import typing

class Threadgate(chitose.Record):
    """


    :param post: Reference (AT-URI) to the post record.

    :param hidden_replies: List of hidden reply URIs.
    """

    def __init__(self, post: str, created_at: str, allow: typing.Optional[list[typing.Union[chitose.app.bsky.feed.threadgate.MentionRule, chitose.app.bsky.feed.threadgate.FollowingRule, chitose.app.bsky.feed.threadgate.ListRule]]]=None, hidden_replies: typing.Optional[list[str]]=None) -> None:
        self.post = post
        self.created_at = created_at
        self.allow = allow
        self.hidden_replies = hidden_replies

    def to_dict(self) -> dict[str, typing.Any]:
        return {'post': self.post, 'createdAt': self.created_at, 'allow': self.allow, 'hiddenReplies': self.hidden_replies, '$type': 'app.bsky.feed.threadgate'}

class MentionRule(chitose.Object):
    """Allow replies from actors mentioned in your post."""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'app.bsky.feed.threadgate#mentionRule'}

class FollowingRule(chitose.Object):
    """Allow replies from actors you follow."""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'app.bsky.feed.threadgate#followingRule'}

class ListRule(chitose.Object):
    """Allow replies from actors on a list."""

    def __init__(self, list: str) -> None:
        self.list = list

    def to_dict(self) -> dict[str, typing.Any]:
        return {'list': self.list, '$type': 'app.bsky.feed.threadgate#listRule'}
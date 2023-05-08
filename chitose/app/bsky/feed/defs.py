# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.app.bsky.feed.defs
import chitose.com.atproto.label.defs
import typing

class PostView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileViewBasic, record: typing.Any, indexed_at: str, embed: typing.Optional[typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View, chitose.app.bsky.embed.record.View, chitose.app.bsky.embed.record_with_media.View]]=None, reply_count: typing.Optional[int]=None, repost_count: typing.Optional[int]=None, like_count: typing.Optional[int]=None, viewer: typing.Optional[chitose.app.bsky.feed.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.record = record
        self.indexed_at = indexed_at
        self.embed = embed
        self.reply_count = reply_count
        self.repost_count = repost_count
        self.like_count = like_count
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'record': self.record, 'indexedAt': self.indexed_at, 'embed': self.embed, 'replyCount': self.reply_count, 'repostCount': self.repost_count, 'likeCount': self.like_count, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.feed.defs#postView'}

class ViewerState(chitose.Object):
    """"""

    def __init__(self, repost: typing.Optional[str]=None, like: typing.Optional[str]=None) -> None:
        self.repost = repost
        self.like = like

    def to_dict(self) -> dict:
        return {'repost': self.repost, 'like': self.like, '$type': 'app.bsky.feed.defs#viewerState'}

class FeedViewPost(chitose.Object):
    """"""

    def __init__(self, post: chitose.app.bsky.feed.defs.PostView, reply: typing.Optional[chitose.app.bsky.feed.defs.ReplyRef]=None, reason: typing.Optional[chitose.app.bsky.feed.defs.ReasonRepost]=None) -> None:
        self.post = post
        self.reply = reply
        self.reason = reason

    def to_dict(self) -> dict:
        return {'post': self.post, 'reply': self.reply, 'reason': self.reason, '$type': 'app.bsky.feed.defs#feedViewPost'}

class ReplyRef(chitose.Object):
    """"""

    def __init__(self, root: chitose.app.bsky.feed.defs.PostView, parent: chitose.app.bsky.feed.defs.PostView) -> None:
        self.root = root
        self.parent = parent

    def to_dict(self) -> dict:
        return {'root': self.root, 'parent': self.parent, '$type': 'app.bsky.feed.defs#replyRef'}

class ReasonRepost(chitose.Object):
    """"""

    def __init__(self, by: chitose.app.bsky.actor.defs.ProfileViewBasic, indexed_at: str) -> None:
        self.by = by
        self.indexed_at = indexed_at

    def to_dict(self) -> dict:
        return {'by': self.by, 'indexedAt': self.indexed_at, '$type': 'app.bsky.feed.defs#reasonRepost'}

class ThreadViewPost(chitose.Object):
    """"""

    def __init__(self, post: chitose.app.bsky.feed.defs.PostView, parent: typing.Optional[typing.Union[chitose.app.bsky.feed.defs.ThreadViewPost, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost]]=None, replies: typing.Optional[list[typing.Union[chitose.app.bsky.feed.defs.ThreadViewPost, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost]]]=None) -> None:
        self.post = post
        self.parent = parent
        self.replies = replies

    def to_dict(self) -> dict:
        return {'post': self.post, 'parent': self.parent, 'replies': self.replies, '$type': 'app.bsky.feed.defs#threadViewPost'}

class NotFoundPost(chitose.Object):
    """"""

    def __init__(self, uri: str, not_found: str) -> None:
        self.uri = uri
        self.not_found = not_found

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'notFound': self.not_found, '$type': 'app.bsky.feed.defs#notFoundPost'}

class BlockedPost(chitose.Object):
    """"""

    def __init__(self, uri: str, blocked: str) -> None:
        self.uri = uri
        self.blocked = blocked

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'blocked': self.blocked, '$type': 'app.bsky.feed.defs#blockedPost'}
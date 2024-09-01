# GENERATED CODE - DO NOT MODIFY
"""A representation of a record embedded in a Bluesky record (eg, a post). For example, a quote-post, or sharing a feed generator record."""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.app.bsky.embed.video
import chitose.app.bsky.feed.defs
import chitose.app.bsky.graph.defs
import chitose.app.bsky.labeler.defs
import chitose.com.atproto.label.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Record(chitose.Object):
    """"""

    def __init__(self, record: chitose.com.atproto.repo.strong_ref.StrongRef) -> None:
        self.record = record

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, '$type': 'app.bsky.embed.record'}

class View(chitose.Object):
    """"""

    def __init__(self, record: typing.Union[chitose.app.bsky.embed.record.ViewRecord, chitose.app.bsky.embed.record.ViewNotFound, chitose.app.bsky.embed.record.ViewBlocked, chitose.app.bsky.embed.record.ViewDetached, chitose.app.bsky.feed.defs.GeneratorView, chitose.app.bsky.graph.defs.ListView, chitose.app.bsky.labeler.defs.LabelerView, chitose.app.bsky.graph.defs.StarterPackViewBasic]) -> None:
        self.record = record

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, '$type': 'app.bsky.embed.record#view'}

class ViewRecord(chitose.Object):
    """


    :param value: The record data itself.
    """

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileViewBasic, value: typing.Any, indexed_at: str, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, reply_count: typing.Optional[int]=None, repost_count: typing.Optional[int]=None, like_count: typing.Optional[int]=None, quote_count: typing.Optional[int]=None, embeds: typing.Optional[list[typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.video.View, chitose.app.bsky.embed.external.View, chitose.app.bsky.embed.record.View, chitose.app.bsky.embed.record_with_media.View]]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.value = value
        self.indexed_at = indexed_at
        self.labels = labels
        self.reply_count = reply_count
        self.repost_count = repost_count
        self.like_count = like_count
        self.quote_count = quote_count
        self.embeds = embeds

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'value': self.value, 'indexedAt': self.indexed_at, 'labels': self.labels, 'replyCount': self.reply_count, 'repostCount': self.repost_count, 'likeCount': self.like_count, 'quoteCount': self.quote_count, 'embeds': self.embeds, '$type': 'app.bsky.embed.record#viewRecord'}

class ViewNotFound(chitose.Object):
    """"""

    def __init__(self, uri: str, not_found: bool) -> None:
        self.uri = uri
        self.not_found = not_found

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'notFound': self.not_found, '$type': 'app.bsky.embed.record#viewNotFound'}

class ViewBlocked(chitose.Object):
    """"""

    def __init__(self, uri: str, blocked: bool, author: chitose.app.bsky.feed.defs.BlockedAuthor) -> None:
        self.uri = uri
        self.blocked = blocked
        self.author = author

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'blocked': self.blocked, 'author': self.author, '$type': 'app.bsky.embed.record#viewBlocked'}

class ViewDetached(chitose.Object):
    """"""

    def __init__(self, uri: str, detached: bool) -> None:
        self.uri = uri
        self.detached = detached

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'detached': self.detached, '$type': 'app.bsky.embed.record#viewDetached'}
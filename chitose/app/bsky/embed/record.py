# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.com.atproto.label.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Record(chitose.Object):

    def __init__(self, record: chitose.com.atproto.repo.strong_ref.StrongRef) -> None:
        self.record = record

    def to_dict(self):
        return {'record': self.record}

class View(chitose.Object):

    def __init__(self, record: typing.Union[chitose.app.bsky.embed.record.ViewRecord, chitose.app.bsky.embed.record.ViewNotFound, chitose.app.bsky.embed.record.ViewBlocked]) -> None:
        self.record = record

    def to_dict(self):
        return {'record': self.record}

class ViewRecord(chitose.Object):

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileViewBasic, value: typing.Any, indexed_at: str, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, embeds: typing.Optional[list[typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View, chitose.app.bsky.embed.record.View, chitose.app.bsky.embed.record_with_media.View]]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.value = value
        self.indexed_at = indexed_at
        self.labels = labels
        self.embeds = embeds

    def to_dict(self):
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'value': self.value, 'indexedAt': self.indexed_at, 'labels': self.labels, 'embeds': self.embeds}

class ViewNotFound(chitose.Object):

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self):
        return {'uri': self.uri}

class ViewBlocked(chitose.Object):

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self):
        return {'uri': self.uri}
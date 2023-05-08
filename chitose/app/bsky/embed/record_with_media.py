# GENERATED CODE - DO NOT MODIFY
"""A representation of a record embedded in another form of content, alongside other compatible embeds"""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import typing

class RecordWithMedia(chitose.Object):
    """"""

    def __init__(self, record: chitose.app.bsky.embed.record.Record, media: typing.Union[chitose.app.bsky.embed.images.Images, chitose.app.bsky.embed.external.External]) -> None:
        self.record = record
        self.media = media

    def to_dict(self) -> dict:
        return {'record': self.record, 'media': self.media, '$type': 'app.bsky.embed.recordWithMedia'}

class View(chitose.Object):
    """"""

    def __init__(self, record: chitose.app.bsky.embed.record.View, media: typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View]) -> None:
        self.record = record
        self.media = media

    def to_dict(self) -> dict:
        return {'record': self.record, 'media': self.media, '$type': 'app.bsky.embed.recordWithMedia#view'}
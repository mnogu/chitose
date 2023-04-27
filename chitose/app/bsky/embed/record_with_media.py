from __future__ import annotations
import chitose
import chitose.app.bsky.embed
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import typing

class RecordWithMedia(chitose.Object):

    def __init__(self, record: chitose.app.bsky.embed.Record, media: typing.Union[chitose.app.bsky.embed.Images, chitose.app.bsky.embed.External]) -> None:
        self.record = record
        self.media = media

    def to_dict(self):
        return {'record': self.record, 'media': self.media}

class View(chitose.Object):

    def __init__(self, record: chitose.app.bsky.embed.record.View, media: typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View]) -> None:
        self.record = record
        self.media = media

    def to_dict(self):
        return {'record': self.record, 'media': self.media}
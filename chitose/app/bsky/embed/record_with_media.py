# GENERATED CODE - DO NOT MODIFY
"""A representation of a record embedded in a Bluesky record (eg, a post), alongside other compatible embeds. For example, a quote post and image, or a quote post and external URL card."""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.video
import typing

class RecordWithMedia(chitose.Object):
    """"""

    def __init__(self, record: chitose.app.bsky.embed.record.Record, media: typing.Union[chitose.app.bsky.embed.images.Images, chitose.app.bsky.embed.video.Video, chitose.app.bsky.embed.external.External]) -> None:
        self.record = record
        self.media = media

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, 'media': self.media, '$type': 'app.bsky.embed.recordWithMedia'}

class View(chitose.Object):
    """"""

    def __init__(self, record: chitose.app.bsky.embed.record.View, media: typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.video.View, chitose.app.bsky.embed.external.View]) -> None:
        self.record = record
        self.media = media

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, 'media': self.media, '$type': 'app.bsky.embed.recordWithMedia#view'}
# GENERATED CODE - DO NOT MODIFY
"""A video embedded in a Bluesky record (eg, a post)."""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.defs
import chitose.app.bsky.embed.video
import typing

class Video(chitose.Object):
    """


    :param alt: Alt text description of the video, for accessibility.
    """

    def __init__(self, video: chitose.Blob, captions: typing.Optional[list[chitose.app.bsky.embed.video.Caption]]=None, alt: typing.Optional[str]=None, aspect_ratio: typing.Optional[chitose.app.bsky.embed.defs.AspectRatio]=None) -> None:
        self.video = video
        self.captions = captions
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'video': self.video, 'captions': self.captions, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.video'}

class Caption(chitose.Object):
    """"""

    def __init__(self, lang: str, file: chitose.Blob) -> None:
        self.lang = lang
        self.file = file

    def to_dict(self) -> dict[str, typing.Any]:
        return {'lang': self.lang, 'file': self.file, '$type': 'app.bsky.embed.video#caption'}

class View(chitose.Object):
    """"""

    def __init__(self, cid: str, playlist: str, thumbnail: typing.Optional[str]=None, alt: typing.Optional[str]=None, aspect_ratio: typing.Optional[chitose.app.bsky.embed.defs.AspectRatio]=None) -> None:
        self.cid = cid
        self.playlist = playlist
        self.thumbnail = thumbnail
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'cid': self.cid, 'playlist': self.playlist, 'thumbnail': self.thumbnail, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.video#view'}
# GENERATED CODE - DO NOT MODIFY
"""A set of images embedded in some other form of content"""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.images
import typing

class Images(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.Image]) -> None:
        self.images = images

    def to_dict(self) -> dict:
        return {'images': self.images}

class Image(chitose.Object):
    """"""

    def __init__(self, image: typing.Any, alt: str) -> None:
        self.image = image
        self.alt = alt

    def to_dict(self) -> dict:
        return {'image': self.image, 'alt': self.alt}

class View(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.ViewImage]) -> None:
        self.images = images

    def to_dict(self) -> dict:
        return {'images': self.images}

class ViewImage(chitose.Object):
    """"""

    def __init__(self, thumb: str, fullsize: str, alt: str) -> None:
        self.thumb = thumb
        self.fullsize = fullsize
        self.alt = alt

    def to_dict(self) -> dict:
        return {'thumb': self.thumb, 'fullsize': self.fullsize, 'alt': self.alt}
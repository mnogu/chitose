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

    def to_dict(self) -> dict[str, typing.Any]:
        return {'images': self.images, '$type': 'app.bsky.embed.images'}

class Image(chitose.Object):
    """"""

    def __init__(self, image: chitose.Blob, alt: str, aspect_ratio: typing.Optional[chitose.app.bsky.embed.images.AspectRatio]=None) -> None:
        self.image = image
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'image': self.image, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.images#image'}

class AspectRatio(chitose.Object):
    """"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, '$type': 'app.bsky.embed.images#aspectRatio'}

class View(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.ViewImage]) -> None:
        self.images = images

    def to_dict(self) -> dict[str, typing.Any]:
        return {'images': self.images, '$type': 'app.bsky.embed.images#view'}

class ViewImage(chitose.Object):
    """"""

    def __init__(self, thumb: str, fullsize: str, alt: str, aspect_ratio: typing.Optional[chitose.app.bsky.embed.images.AspectRatio]=None) -> None:
        self.thumb = thumb
        self.fullsize = fullsize
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'thumb': self.thumb, 'fullsize': self.fullsize, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.images#viewImage'}
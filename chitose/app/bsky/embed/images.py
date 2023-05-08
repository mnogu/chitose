# GENERATED CODE - DO NOT MODIFY
"""A set of images embedded in some other form of content"""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.images

class Images(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.Image]) -> None:
        self.images = images

    def to_dict(self) -> dict:
        return {'images': self.images, '$type': 'app.bsky.embed.images'}

class Image(chitose.Object):
    """"""

    def __init__(self, image: chitose.Blob, alt: str) -> None:
        self.image = image
        self.alt = alt

    def to_dict(self) -> dict:
        return {'image': self.image, 'alt': self.alt, '$type': 'app.bsky.embed.images#image'}

class View(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.ViewImage]) -> None:
        self.images = images

    def to_dict(self) -> dict:
        return {'images': self.images, '$type': 'app.bsky.embed.images#view'}

class ViewImage(chitose.Object):
    """"""

    def __init__(self, thumb: str, fullsize: str, alt: str) -> None:
        self.thumb = thumb
        self.fullsize = fullsize
        self.alt = alt

    def to_dict(self) -> dict:
        return {'thumb': self.thumb, 'fullsize': self.fullsize, 'alt': self.alt, '$type': 'app.bsky.embed.images#viewImage'}
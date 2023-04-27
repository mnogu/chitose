# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

class Images(chitose.Object):

    def __init__(self, images: list[Image]) -> None:
        self.images = images

    def to_dict(self):
        return {'images': self.images}

class Image(chitose.Object):

    def __init__(self, image: typing.Any, alt: str) -> None:
        self.image = image
        self.alt = alt

    def to_dict(self):
        return {'image': self.image, 'alt': self.alt}

class View(chitose.Object):

    def __init__(self, images: list[ViewImage]) -> None:
        self.images = images

    def to_dict(self):
        return {'images': self.images}

class ViewImage(chitose.Object):

    def __init__(self, thumb: str, fullsize: str, alt: str) -> None:
        self.thumb = thumb
        self.fullsize = fullsize
        self.alt = alt

    def to_dict(self):
        return {'thumb': self.thumb, 'fullsize': self.fullsize, 'alt': self.alt}
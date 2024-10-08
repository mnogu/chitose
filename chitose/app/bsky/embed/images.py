# GENERATED CODE - DO NOT MODIFY
"""A set of images embedded in a Bluesky record (eg, a post)."""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.defs
import chitose.app.bsky.embed.images
import typing

class Images(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.Image]) -> None:
        self.images = images

    def to_dict(self) -> dict[str, typing.Any]:
        return {'images': self.images, '$type': 'app.bsky.embed.images'}

class Image(chitose.Object):
    """


    :param alt: Alt text description of the image, for accessibility.
    """

    def __init__(self, image: chitose.Blob, alt: str, aspect_ratio: typing.Optional[chitose.app.bsky.embed.defs.AspectRatio]=None) -> None:
        self.image = image
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'image': self.image, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.images#image'}

class View(chitose.Object):
    """"""

    def __init__(self, images: list[chitose.app.bsky.embed.images.ViewImage]) -> None:
        self.images = images

    def to_dict(self) -> dict[str, typing.Any]:
        return {'images': self.images, '$type': 'app.bsky.embed.images#view'}

class ViewImage(chitose.Object):
    """


    :param thumb: Fully-qualified URL where a thumbnail of the image can be fetched. For example, CDN location provided by the App View.

    :param fullsize: Fully-qualified URL where a large version of the image can be fetched. May or may not be the exact original blob. For example, CDN location provided by the App View.

    :param alt: Alt text description of the image, for accessibility.
    """

    def __init__(self, thumb: str, fullsize: str, alt: str, aspect_ratio: typing.Optional[chitose.app.bsky.embed.defs.AspectRatio]=None) -> None:
        self.thumb = thumb
        self.fullsize = fullsize
        self.alt = alt
        self.aspect_ratio = aspect_ratio

    def to_dict(self) -> dict[str, typing.Any]:
        return {'thumb': self.thumb, 'fullsize': self.fullsize, 'alt': self.alt, 'aspectRatio': self.aspect_ratio, '$type': 'app.bsky.embed.images#viewImage'}
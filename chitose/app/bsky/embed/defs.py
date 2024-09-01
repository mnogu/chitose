# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class AspectRatio(chitose.Object):
    """width:height represents an aspect ratio. It may be approximate, and may not correspond to absolute dimensions in any given unit."""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, '$type': 'app.bsky.embed.defs#aspectRatio'}
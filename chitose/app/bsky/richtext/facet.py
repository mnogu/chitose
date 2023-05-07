# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.richtext.facet
import typing

class Facet(chitose.Object):
    """"""

    def __init__(self, index: chitose.app.bsky.richtext.facet.ByteSlice, features: list[typing.Union[chitose.app.bsky.richtext.facet.Mention, chitose.app.bsky.richtext.facet.Link]]) -> None:
        self.index = index
        self.features = features

    def to_dict(self):
        return {'index': self.index, 'features': self.features}

class Mention(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self):
        return {'did': self.did}

class Link(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self):
        return {'uri': self.uri}

class ByteSlice(chitose.Object):
    """"""

    def __init__(self, byte_start: int, byte_end: int) -> None:
        self.byte_start = byte_start
        self.byte_end = byte_end

    def to_dict(self):
        return {'byteStart': self.byte_start, 'byteEnd': self.byte_end}
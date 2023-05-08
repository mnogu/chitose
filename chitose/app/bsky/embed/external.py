# GENERATED CODE - DO NOT MODIFY
"""A representation of some externally linked content, embedded in another form of content"""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.external
import typing

class External(chitose.Object):
    """"""

    def __init__(self, external: chitose.app.bsky.embed.external.ExternalExternal) -> None:
        self.external = external

    def to_dict(self) -> dict:
        return {'external': self.external, '$type': 'app.bsky.embed.external'}

class ExternalExternal(chitose.Object):
    """"""

    def __init__(self, uri: str, title: str, description: str, thumb: typing.Optional[chitose.Blob]=None) -> None:
        self.uri = uri
        self.title = title
        self.description = description
        self.thumb = thumb

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'title': self.title, 'description': self.description, 'thumb': self.thumb, '$type': 'app.bsky.embed.external#external'}

class View(chitose.Object):
    """"""

    def __init__(self, external: chitose.app.bsky.embed.external.ViewExternal) -> None:
        self.external = external

    def to_dict(self) -> dict:
        return {'external': self.external, '$type': 'app.bsky.embed.external#view'}

class ViewExternal(chitose.Object):
    """"""

    def __init__(self, uri: str, title: str, description: str, thumb: typing.Optional[str]=None) -> None:
        self.uri = uri
        self.title = title
        self.description = description
        self.thumb = thumb

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'title': self.title, 'description': self.description, 'thumb': self.thumb, '$type': 'app.bsky.embed.external#viewExternal'}
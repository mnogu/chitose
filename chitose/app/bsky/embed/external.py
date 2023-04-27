from __future__ import annotations
import chitose
import typing

class External(chitose.Object):

    def __init__(self, external: External) -> None:
        self.external = external

    def to_dict(self):
        return {'external': self.external}

class External(chitose.Object):

    def __init__(self, uri: str, title: str, description: str, thumb: typing.Optional[typing.Any]=None) -> None:
        self.uri = uri
        self.title = title
        self.description = description
        self.thumb = thumb

    def to_dict(self):
        return {'uri': self.uri, 'title': self.title, 'description': self.description, 'thumb': self.thumb}

class View(chitose.Object):

    def __init__(self, external: ViewExternal) -> None:
        self.external = external

    def to_dict(self):
        return {'external': self.external}

class ViewExternal(chitose.Object):

    def __init__(self, uri: str, title: str, description: str, thumb: typing.Optional[str]=None) -> None:
        self.uri = uri
        self.title = title
        self.description = description
        self.thumb = thumb

    def to_dict(self):
        return {'uri': self.uri, 'title': self.title, 'description': self.description, 'thumb': self.thumb}
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class SkeletonSearchPost(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'app.bsky.unspecced.defs#skeletonSearchPost'}

class SkeletonSearchActor(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'app.bsky.unspecced.defs#skeletonSearchActor'}
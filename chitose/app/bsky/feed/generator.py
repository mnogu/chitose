# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.richtext.facet
import typing

class Generator(chitose.Record):
    """"""

    def __init__(self, did: str, display_name: str, created_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[chitose.Blob]=None) -> None:
        self.did = did
        self.display_name = display_name
        self.created_at = created_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'displayName': self.display_name, 'createdAt': self.created_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, '$type': 'app.bsky.feed.generator'}
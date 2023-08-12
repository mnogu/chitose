# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.graph.defs
import chitose.app.bsky.richtext.facet
import chitose.com.atproto.label.defs
import typing

class List(chitose.Record):
    """"""

    def __init__(self, purpose: chitose.app.bsky.graph.defs.ListPurpose, name: str, created_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[chitose.Blob]=None, labels: typing.Optional[chitose.com.atproto.label.defs.SelfLabels]=None) -> None:
        self.purpose = purpose
        self.name = name
        self.created_at = created_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'purpose': self.purpose, 'name': self.name, 'createdAt': self.created_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, 'labels': self.labels, '$type': 'app.bsky.graph.list'}
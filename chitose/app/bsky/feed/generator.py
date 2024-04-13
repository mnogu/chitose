# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.richtext.facet
import chitose.com.atproto.label.defs
import typing

class Generator(chitose.Record):
    """


    :param accepts_interactions: Declaration that a feed accepts feedback interactions from a client through app.bsky.feed.sendInteractions

    :param labels: Self-label values
    """

    def __init__(self, did: str, display_name: str, created_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[chitose.Blob]=None, accepts_interactions: typing.Optional[bool]=None, labels: typing.Optional[chitose.com.atproto.label.defs.SelfLabels]=None) -> None:
        self.did = did
        self.display_name = display_name
        self.created_at = created_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar
        self.accepts_interactions = accepts_interactions
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'displayName': self.display_name, 'createdAt': self.created_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, 'acceptsInteractions': self.accepts_interactions, 'labels': self.labels, '$type': 'app.bsky.feed.generator'}
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.graph.starterpack
import chitose.app.bsky.richtext.facet
import typing

class Starterpack(chitose.Record):
    """


    :param name: Display name for starter pack; can not be empty.

    :param list: Reference (AT-URI) to the list record.
    """

    def __init__(self, name: str, list: str, created_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, feeds: typing.Optional[list[chitose.app.bsky.graph.starterpack.FeedItem]]=None) -> None:
        self.name = name
        self.list = list
        self.created_at = created_at
        self.description = description
        self.description_facets = description_facets
        self.feeds = feeds

    def to_dict(self) -> dict[str, typing.Any]:
        return {'name': self.name, 'list': self.list, 'createdAt': self.created_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'feeds': self.feeds, '$type': 'app.bsky.graph.starterpack'}

class FeedItem(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'app.bsky.graph.starterpack#feedItem'}
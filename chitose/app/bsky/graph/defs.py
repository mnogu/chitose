# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.graph.defs
import chitose.app.bsky.richtext.facet
import typing

class ListViewBasic(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, name: str, purpose: chitose.app.bsky.graph.defs.ListPurpose, avatar: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.graph.defs.ListViewerState]=None, indexed_at: typing.Optional[str]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.name = name
        self.purpose = purpose
        self.avatar = avatar
        self.viewer = viewer
        self.indexed_at = indexed_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'name': self.name, 'purpose': self.purpose, 'avatar': self.avatar, 'viewer': self.viewer, 'indexedAt': self.indexed_at, '$type': 'app.bsky.graph.defs#listViewBasic'}

class ListView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, creator: chitose.app.bsky.actor.defs.ProfileView, name: str, purpose: chitose.app.bsky.graph.defs.ListPurpose, indexed_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.graph.defs.ListViewerState]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.creator = creator
        self.name = name
        self.purpose = purpose
        self.indexed_at = indexed_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar
        self.viewer = viewer

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'creator': self.creator, 'name': self.name, 'purpose': self.purpose, 'indexedAt': self.indexed_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, 'viewer': self.viewer, '$type': 'app.bsky.graph.defs#listView'}

class ListItemView(chitose.Object):
    """"""

    def __init__(self, uri: str, subject: chitose.app.bsky.actor.defs.ProfileView) -> None:
        self.uri = uri
        self.subject = subject

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'subject': self.subject, '$type': 'app.bsky.graph.defs#listItemView'}
ListPurpose = typing.Literal['app.bsky.graph.defs#modlist', 'app.bsky.graph.defs#curatelist']
MODLIST = 'app.bsky.graph.defs#modlist'
CURATELIST = 'app.bsky.graph.defs#curatelist'

class ListViewerState(chitose.Object):
    """"""

    def __init__(self, muted: typing.Optional[bool]=None, blocked: typing.Optional[str]=None) -> None:
        self.muted = muted
        self.blocked = blocked

    def to_dict(self) -> dict[str, typing.Any]:
        return {'muted': self.muted, 'blocked': self.blocked, '$type': 'app.bsky.graph.defs#listViewerState'}
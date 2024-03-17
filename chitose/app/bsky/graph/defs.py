# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.graph.defs
import chitose.app.bsky.richtext.facet
import chitose.com.atproto.label.defs
import typing

class ListViewBasic(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, name: str, purpose: chitose.app.bsky.graph.defs.ListPurpose, avatar: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, viewer: typing.Optional[chitose.app.bsky.graph.defs.ListViewerState]=None, indexed_at: typing.Optional[str]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.name = name
        self.purpose = purpose
        self.avatar = avatar
        self.labels = labels
        self.viewer = viewer
        self.indexed_at = indexed_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'name': self.name, 'purpose': self.purpose, 'avatar': self.avatar, 'labels': self.labels, 'viewer': self.viewer, 'indexedAt': self.indexed_at, '$type': 'app.bsky.graph.defs#listViewBasic'}

class ListView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, creator: chitose.app.bsky.actor.defs.ProfileView, name: str, purpose: chitose.app.bsky.graph.defs.ListPurpose, indexed_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, viewer: typing.Optional[chitose.app.bsky.graph.defs.ListViewerState]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.creator = creator
        self.name = name
        self.purpose = purpose
        self.indexed_at = indexed_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar
        self.labels = labels
        self.viewer = viewer

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'creator': self.creator, 'name': self.name, 'purpose': self.purpose, 'indexedAt': self.indexed_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, 'labels': self.labels, 'viewer': self.viewer, '$type': 'app.bsky.graph.defs#listView'}

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

class NotFoundActor(chitose.Object):
    """indicates that a handle or DID could not be resolved"""

    def __init__(self, actor: str, not_found: bool) -> None:
        self.actor = actor
        self.not_found = not_found

    def to_dict(self) -> dict[str, typing.Any]:
        return {'actor': self.actor, 'notFound': self.not_found, '$type': 'app.bsky.graph.defs#notFoundActor'}

class Relationship(chitose.Object):
    """lists the bi-directional graph relationships between one actor (not indicated in the object), and the target actors (the DID included in the object)


    :param following: if the actor follows this DID, this is the AT-URI of the follow record

    :param followed_by: if the actor is followed by this DID, contains the AT-URI of the follow record
    """

    def __init__(self, did: str, following: typing.Optional[str]=None, followed_by: typing.Optional[str]=None) -> None:
        self.did = did
        self.following = following
        self.followed_by = followed_by

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'following': self.following, 'followedBy': self.followed_by, '$type': 'app.bsky.graph.defs#relationship'}
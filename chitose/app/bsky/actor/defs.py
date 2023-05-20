# GENERATED CODE - DO NOT MODIFY
"""A reference to an actor in the network."""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.graph.defs
import chitose.com.atproto.label.defs
import typing

class ProfileViewBasic(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, avatar: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.avatar = avatar
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'avatar': self.avatar, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileViewBasic'}

class ProfileView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[str]=None, indexed_at: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.indexed_at = indexed_at
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'indexedAt': self.indexed_at, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileView'}

class ProfileViewDetailed(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[str]=None, banner: typing.Optional[str]=None, followers_count: typing.Optional[int]=None, follows_count: typing.Optional[int]=None, posts_count: typing.Optional[int]=None, indexed_at: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.banner = banner
        self.followers_count = followers_count
        self.follows_count = follows_count
        self.posts_count = posts_count
        self.indexed_at = indexed_at
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner, 'followersCount': self.followers_count, 'followsCount': self.follows_count, 'postsCount': self.posts_count, 'indexedAt': self.indexed_at, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileViewDetailed'}

class ViewerState(chitose.Object):
    """"""

    def __init__(self, muted: typing.Optional[bool]=None, muted_by_list: typing.Optional[chitose.app.bsky.graph.defs.ListViewBasic]=None, blocked_by: typing.Optional[bool]=None, blocking: typing.Optional[str]=None, following: typing.Optional[str]=None, followed_by: typing.Optional[str]=None) -> None:
        self.muted = muted
        self.muted_by_list = muted_by_list
        self.blocked_by = blocked_by
        self.blocking = blocking
        self.following = following
        self.followed_by = followed_by

    def to_dict(self) -> dict:
        return {'muted': self.muted, 'mutedByList': self.muted_by_list, 'blockedBy': self.blocked_by, 'blocking': self.blocking, 'following': self.following, 'followedBy': self.followed_by, '$type': 'app.bsky.actor.defs#viewerState'}
Preferences = list[typing.Union['chitose.app.bsky.actor.defs.AdultContentPref', 'chitose.app.bsky.actor.defs.ContentLabelPref', 'chitose.app.bsky.actor.defs.SavedFeedsPref']]

class AdultContentPref(chitose.Object):
    """"""

    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    def to_dict(self) -> dict:
        return {'enabled': self.enabled, '$type': 'app.bsky.actor.defs#adultContentPref'}

class ContentLabelPref(chitose.Object):
    """"""

    def __init__(self, label: str, visibility: typing.Literal['show', 'warn', 'hide']) -> None:
        self.label = label
        self.visibility = visibility

    def to_dict(self) -> dict:
        return {'label': self.label, 'visibility': self.visibility, '$type': 'app.bsky.actor.defs#contentLabelPref'}

class SavedFeedsPref(chitose.Object):
    """"""

    def __init__(self, pinned: list[str], saved: list[str]) -> None:
        self.pinned = pinned
        self.saved = saved

    def to_dict(self) -> dict:
        return {'pinned': self.pinned, 'saved': self.saved, '$type': 'app.bsky.actor.defs#savedFeedsPref'}
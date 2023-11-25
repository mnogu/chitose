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

    def to_dict(self) -> dict[str, typing.Any]:
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

    def to_dict(self) -> dict[str, typing.Any]:
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

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner, 'followersCount': self.followers_count, 'followsCount': self.follows_count, 'postsCount': self.posts_count, 'indexedAt': self.indexed_at, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileViewDetailed'}

class ViewerState(chitose.Object):
    """"""

    def __init__(self, muted: typing.Optional[bool]=None, muted_by_list: typing.Optional[chitose.app.bsky.graph.defs.ListViewBasic]=None, blocked_by: typing.Optional[bool]=None, blocking: typing.Optional[str]=None, blocking_by_list: typing.Optional[chitose.app.bsky.graph.defs.ListViewBasic]=None, following: typing.Optional[str]=None, followed_by: typing.Optional[str]=None) -> None:
        self.muted = muted
        self.muted_by_list = muted_by_list
        self.blocked_by = blocked_by
        self.blocking = blocking
        self.blocking_by_list = blocking_by_list
        self.following = following
        self.followed_by = followed_by

    def to_dict(self) -> dict[str, typing.Any]:
        return {'muted': self.muted, 'mutedByList': self.muted_by_list, 'blockedBy': self.blocked_by, 'blocking': self.blocking, 'blockingByList': self.blocking_by_list, 'following': self.following, 'followedBy': self.followed_by, '$type': 'app.bsky.actor.defs#viewerState'}
Preferences = list[typing.Union['chitose.app.bsky.actor.defs.AdultContentPref', 'chitose.app.bsky.actor.defs.ContentLabelPref', 'chitose.app.bsky.actor.defs.SavedFeedsPref', 'chitose.app.bsky.actor.defs.PersonalDetailsPref', 'chitose.app.bsky.actor.defs.FeedViewPref', 'chitose.app.bsky.actor.defs.ThreadViewPref']]

class AdultContentPref(chitose.Object):
    """"""

    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    def to_dict(self) -> dict[str, typing.Any]:
        return {'enabled': self.enabled, '$type': 'app.bsky.actor.defs#adultContentPref'}

class ContentLabelPref(chitose.Object):
    """"""

    def __init__(self, label: str, visibility: typing.Literal['show', 'warn', 'hide']) -> None:
        self.label = label
        self.visibility = visibility

    def to_dict(self) -> dict[str, typing.Any]:
        return {'label': self.label, 'visibility': self.visibility, '$type': 'app.bsky.actor.defs#contentLabelPref'}

class SavedFeedsPref(chitose.Object):
    """"""

    def __init__(self, pinned: list[str], saved: list[str]) -> None:
        self.pinned = pinned
        self.saved = saved

    def to_dict(self) -> dict[str, typing.Any]:
        return {'pinned': self.pinned, 'saved': self.saved, '$type': 'app.bsky.actor.defs#savedFeedsPref'}

class PersonalDetailsPref(chitose.Object):
    """


    :param birth_date: The birth date of account owner.
    """

    def __init__(self, birth_date: typing.Optional[str]=None) -> None:
        self.birth_date = birth_date

    def to_dict(self) -> dict[str, typing.Any]:
        return {'birthDate': self.birth_date, '$type': 'app.bsky.actor.defs#personalDetailsPref'}

class FeedViewPref(chitose.Object):
    """


    :param feed: The URI of the feed, or an identifier which describes the feed.

    :param hide_replies: Hide replies in the feed.

    :param hide_replies_by_unfollowed: Hide replies in the feed if they are not by followed users.

    :param hide_replies_by_like_count: Hide replies in the feed if they do not have this number of likes.

    :param hide_reposts: Hide reposts in the feed.

    :param hide_quote_posts: Hide quote posts in the feed.
    """

    def __init__(self, feed: str, hide_replies: typing.Optional[bool]=None, hide_replies_by_unfollowed: typing.Optional[bool]=None, hide_replies_by_like_count: typing.Optional[int]=None, hide_reposts: typing.Optional[bool]=None, hide_quote_posts: typing.Optional[bool]=None) -> None:
        self.feed = feed
        self.hide_replies = hide_replies
        self.hide_replies_by_unfollowed = hide_replies_by_unfollowed
        self.hide_replies_by_like_count = hide_replies_by_like_count
        self.hide_reposts = hide_reposts
        self.hide_quote_posts = hide_quote_posts

    def to_dict(self) -> dict[str, typing.Any]:
        return {'feed': self.feed, 'hideReplies': self.hide_replies, 'hideRepliesByUnfollowed': self.hide_replies_by_unfollowed, 'hideRepliesByLikeCount': self.hide_replies_by_like_count, 'hideReposts': self.hide_reposts, 'hideQuotePosts': self.hide_quote_posts, '$type': 'app.bsky.actor.defs#feedViewPref'}

class ThreadViewPref(chitose.Object):
    """


    :param sort: Sorting mode for threads.

    :param prioritize_followed_users: Show followed users at the top of all replies.
    """

    def __init__(self, sort: typing.Optional[typing.Literal['oldest', 'newest', 'most-likes', 'random']]=None, prioritize_followed_users: typing.Optional[bool]=None) -> None:
        self.sort = sort
        self.prioritize_followed_users = prioritize_followed_users

    def to_dict(self) -> dict[str, typing.Any]:
        return {'sort': self.sort, 'prioritizeFollowedUsers': self.prioritize_followed_users, '$type': 'app.bsky.actor.defs#threadViewPref'}
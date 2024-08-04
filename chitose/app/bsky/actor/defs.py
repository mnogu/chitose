# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.graph.defs
import chitose.com.atproto.label.defs
import typing

class ProfileViewBasic(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, avatar: typing.Optional[str]=None, associated: typing.Optional[chitose.app.bsky.actor.defs.ProfileAssociated]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, created_at: typing.Optional[str]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.avatar = avatar
        self.associated = associated
        self.viewer = viewer
        self.labels = labels
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'avatar': self.avatar, 'associated': self.associated, 'viewer': self.viewer, 'labels': self.labels, 'createdAt': self.created_at, '$type': 'app.bsky.actor.defs#profileViewBasic'}

class ProfileView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[str]=None, associated: typing.Optional[chitose.app.bsky.actor.defs.ProfileAssociated]=None, indexed_at: typing.Optional[str]=None, created_at: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.associated = associated
        self.indexed_at = indexed_at
        self.created_at = created_at
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'associated': self.associated, 'indexedAt': self.indexed_at, 'createdAt': self.created_at, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileView'}

class ProfileViewDetailed(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[str]=None, banner: typing.Optional[str]=None, followers_count: typing.Optional[int]=None, follows_count: typing.Optional[int]=None, posts_count: typing.Optional[int]=None, associated: typing.Optional[chitose.app.bsky.actor.defs.ProfileAssociated]=None, joined_via_starter_pack: typing.Optional[chitose.app.bsky.graph.defs.StarterPackViewBasic]=None, indexed_at: typing.Optional[str]=None, created_at: typing.Optional[str]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.banner = banner
        self.followers_count = followers_count
        self.follows_count = follows_count
        self.posts_count = posts_count
        self.associated = associated
        self.joined_via_starter_pack = joined_via_starter_pack
        self.indexed_at = indexed_at
        self.created_at = created_at
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner, 'followersCount': self.followers_count, 'followsCount': self.follows_count, 'postsCount': self.posts_count, 'associated': self.associated, 'joinedViaStarterPack': self.joined_via_starter_pack, 'indexedAt': self.indexed_at, 'createdAt': self.created_at, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.actor.defs#profileViewDetailed'}

class ProfileAssociated(chitose.Object):
    """"""

    def __init__(self, lists: typing.Optional[int]=None, feedgens: typing.Optional[int]=None, starter_packs: typing.Optional[int]=None, labeler: typing.Optional[bool]=None, chat: typing.Optional[chitose.app.bsky.actor.defs.ProfileAssociatedChat]=None) -> None:
        self.lists = lists
        self.feedgens = feedgens
        self.starter_packs = starter_packs
        self.labeler = labeler
        self.chat = chat

    def to_dict(self) -> dict[str, typing.Any]:
        return {'lists': self.lists, 'feedgens': self.feedgens, 'starterPacks': self.starter_packs, 'labeler': self.labeler, 'chat': self.chat, '$type': 'app.bsky.actor.defs#profileAssociated'}

class ProfileAssociatedChat(chitose.Object):
    """"""

    def __init__(self, allow_incoming: typing.Literal['all', 'none', 'following']) -> None:
        self.allow_incoming = allow_incoming

    def to_dict(self) -> dict[str, typing.Any]:
        return {'allowIncoming': self.allow_incoming, '$type': 'app.bsky.actor.defs#profileAssociatedChat'}

class ViewerState(chitose.Object):
    """Metadata about the requesting account's relationship with the subject account. Only has meaningful content for authed requests."""

    def __init__(self, muted: typing.Optional[bool]=None, muted_by_list: typing.Optional[chitose.app.bsky.graph.defs.ListViewBasic]=None, blocked_by: typing.Optional[bool]=None, blocking: typing.Optional[str]=None, blocking_by_list: typing.Optional[chitose.app.bsky.graph.defs.ListViewBasic]=None, following: typing.Optional[str]=None, followed_by: typing.Optional[str]=None, known_followers: typing.Optional[chitose.app.bsky.actor.defs.KnownFollowers]=None) -> None:
        self.muted = muted
        self.muted_by_list = muted_by_list
        self.blocked_by = blocked_by
        self.blocking = blocking
        self.blocking_by_list = blocking_by_list
        self.following = following
        self.followed_by = followed_by
        self.known_followers = known_followers

    def to_dict(self) -> dict[str, typing.Any]:
        return {'muted': self.muted, 'mutedByList': self.muted_by_list, 'blockedBy': self.blocked_by, 'blocking': self.blocking, 'blockingByList': self.blocking_by_list, 'following': self.following, 'followedBy': self.followed_by, 'knownFollowers': self.known_followers, '$type': 'app.bsky.actor.defs#viewerState'}

class KnownFollowers(chitose.Object):
    """The subject's followers whom you also follow"""

    def __init__(self, count: int, followers: list[chitose.app.bsky.actor.defs.ProfileViewBasic]) -> None:
        self.count = count
        self.followers = followers

    def to_dict(self) -> dict[str, typing.Any]:
        return {'count': self.count, 'followers': self.followers, '$type': 'app.bsky.actor.defs#knownFollowers'}
Preferences = list[typing.Union['chitose.app.bsky.actor.defs.AdultContentPref', 'chitose.app.bsky.actor.defs.ContentLabelPref', 'chitose.app.bsky.actor.defs.SavedFeedsPref', 'chitose.app.bsky.actor.defs.SavedFeedsPrefV2', 'chitose.app.bsky.actor.defs.PersonalDetailsPref', 'chitose.app.bsky.actor.defs.FeedViewPref', 'chitose.app.bsky.actor.defs.ThreadViewPref', 'chitose.app.bsky.actor.defs.InterestsPref', 'chitose.app.bsky.actor.defs.MutedWordsPref', 'chitose.app.bsky.actor.defs.HiddenPostsPref', 'chitose.app.bsky.actor.defs.BskyAppStatePref', 'chitose.app.bsky.actor.defs.LabelersPref']]

class AdultContentPref(chitose.Object):
    """"""

    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    def to_dict(self) -> dict[str, typing.Any]:
        return {'enabled': self.enabled, '$type': 'app.bsky.actor.defs#adultContentPref'}

class ContentLabelPref(chitose.Object):
    """


    :param labeler_did: Which labeler does this preference apply to? If undefined, applies globally.
    """

    def __init__(self, label: str, visibility: typing.Literal['ignore', 'show', 'warn', 'hide'], labeler_did: typing.Optional[str]=None) -> None:
        self.label = label
        self.visibility = visibility
        self.labeler_did = labeler_did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'label': self.label, 'visibility': self.visibility, 'labelerDid': self.labeler_did, '$type': 'app.bsky.actor.defs#contentLabelPref'}

class SavedFeed(chitose.Object):
    """"""

    def __init__(self, id: str, type: typing.Literal['feed', 'list', 'timeline'], value: str, pinned: bool) -> None:
        self.id = id
        self.type = type
        self.value = value
        self.pinned = pinned

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'type': self.type, 'value': self.value, 'pinned': self.pinned, '$type': 'app.bsky.actor.defs#savedFeed'}

class SavedFeedsPrefV2(chitose.Object):
    """"""

    def __init__(self, items: list[chitose.app.bsky.actor.defs.SavedFeed]) -> None:
        self.items = items

    def to_dict(self) -> dict[str, typing.Any]:
        return {'items': self.items, '$type': 'app.bsky.actor.defs#savedFeedsPrefV2'}

class SavedFeedsPref(chitose.Object):
    """"""

    def __init__(self, pinned: list[str], saved: list[str], timeline_index: typing.Optional[int]=None) -> None:
        self.pinned = pinned
        self.saved = saved
        self.timeline_index = timeline_index

    def to_dict(self) -> dict[str, typing.Any]:
        return {'pinned': self.pinned, 'saved': self.saved, 'timelineIndex': self.timeline_index, '$type': 'app.bsky.actor.defs#savedFeedsPref'}

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

class InterestsPref(chitose.Object):
    """


    :param tags: A list of tags which describe the account owner's interests gathered during onboarding.
    """

    def __init__(self, tags: list[str]) -> None:
        self.tags = tags

    def to_dict(self) -> dict[str, typing.Any]:
        return {'tags': self.tags, '$type': 'app.bsky.actor.defs#interestsPref'}
MutedWordTarget = typing.Literal['content', 'tag']

class MutedWord(chitose.Object):
    """A word that the account owner has muted.


    :param value: The muted word itself.

    :param targets: The intended targets of the muted word.

    :param actor_target: Groups of users to apply the muted word to. If undefined, applies to all users.

    :param expires_at: The date and time at which the muted word will expire and no longer be applied.
    """

    def __init__(self, value: str, targets: list[chitose.app.bsky.actor.defs.MutedWordTarget], id: typing.Optional[str]=None, actor_target: typing.Optional[typing.Literal['all', 'exclude-following']]=None, expires_at: typing.Optional[str]=None) -> None:
        self.value = value
        self.targets = targets
        self.id = id
        self.actor_target = actor_target
        self.expires_at = expires_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'value': self.value, 'targets': self.targets, 'id': self.id, 'actorTarget': self.actor_target, 'expiresAt': self.expires_at, '$type': 'app.bsky.actor.defs#mutedWord'}

class MutedWordsPref(chitose.Object):
    """


    :param items: A list of words the account owner has muted.
    """

    def __init__(self, items: list[chitose.app.bsky.actor.defs.MutedWord]) -> None:
        self.items = items

    def to_dict(self) -> dict[str, typing.Any]:
        return {'items': self.items, '$type': 'app.bsky.actor.defs#mutedWordsPref'}

class HiddenPostsPref(chitose.Object):
    """


    :param items: A list of URIs of posts the account owner has hidden.
    """

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def to_dict(self) -> dict[str, typing.Any]:
        return {'items': self.items, '$type': 'app.bsky.actor.defs#hiddenPostsPref'}

class LabelersPref(chitose.Object):
    """"""

    def __init__(self, labelers: list[chitose.app.bsky.actor.defs.LabelerPrefItem]) -> None:
        self.labelers = labelers

    def to_dict(self) -> dict[str, typing.Any]:
        return {'labelers': self.labelers, '$type': 'app.bsky.actor.defs#labelersPref'}

class LabelerPrefItem(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'app.bsky.actor.defs#labelerPrefItem'}

class BskyAppStatePref(chitose.Object):
    """A grab bag of state that's specific to the bsky.app program. Third-party apps shouldn't use this.


    :param queued_nudges: An array of tokens which identify nudges (modals, popups, tours, highlight dots) that should be shown to the user.
    """

    def __init__(self, active_progress_guide: typing.Optional[chitose.app.bsky.actor.defs.BskyAppProgressGuide]=None, queued_nudges: typing.Optional[list[str]]=None) -> None:
        self.active_progress_guide = active_progress_guide
        self.queued_nudges = queued_nudges

    def to_dict(self) -> dict[str, typing.Any]:
        return {'activeProgressGuide': self.active_progress_guide, 'queuedNudges': self.queued_nudges, '$type': 'app.bsky.actor.defs#bskyAppStatePref'}

class BskyAppProgressGuide(chitose.Object):
    """If set, an active progress guide. Once completed, can be set to undefined. Should have unspecced fields tracking progress."""

    def __init__(self, guide: str) -> None:
        self.guide = guide

    def to_dict(self) -> dict[str, typing.Any]:
        return {'guide': self.guide, '$type': 'app.bsky.actor.defs#bskyAppProgressGuide'}
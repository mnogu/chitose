# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.app.bsky.feed.defs
import chitose.app.bsky.graph.defs
import chitose.app.bsky.richtext.facet
import chitose.com.atproto.label.defs
import typing

class PostView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileViewBasic, record: typing.Any, indexed_at: str, embed: typing.Optional[typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View, chitose.app.bsky.embed.record.View, chitose.app.bsky.embed.record_with_media.View]]=None, reply_count: typing.Optional[int]=None, repost_count: typing.Optional[int]=None, like_count: typing.Optional[int]=None, viewer: typing.Optional[chitose.app.bsky.feed.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, threadgate: typing.Optional[chitose.app.bsky.feed.defs.ThreadgateView]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.record = record
        self.indexed_at = indexed_at
        self.embed = embed
        self.reply_count = reply_count
        self.repost_count = repost_count
        self.like_count = like_count
        self.viewer = viewer
        self.labels = labels
        self.threadgate = threadgate

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'record': self.record, 'indexedAt': self.indexed_at, 'embed': self.embed, 'replyCount': self.reply_count, 'repostCount': self.repost_count, 'likeCount': self.like_count, 'viewer': self.viewer, 'labels': self.labels, 'threadgate': self.threadgate, '$type': 'app.bsky.feed.defs#postView'}

class ViewerState(chitose.Object):
    """Metadata about the requesting account's relationship with the subject content. Only has meaningful content for authed requests."""

    def __init__(self, repost: typing.Optional[str]=None, like: typing.Optional[str]=None, reply_disabled: typing.Optional[bool]=None) -> None:
        self.repost = repost
        self.like = like
        self.reply_disabled = reply_disabled

    def to_dict(self) -> dict[str, typing.Any]:
        return {'repost': self.repost, 'like': self.like, 'replyDisabled': self.reply_disabled, '$type': 'app.bsky.feed.defs#viewerState'}

class FeedViewPost(chitose.Object):
    """


    :param feed_context: Context provided by feed generator that may be passed back alongside interactions.
    """

    def __init__(self, post: chitose.app.bsky.feed.defs.PostView, reply: typing.Optional[chitose.app.bsky.feed.defs.ReplyRef]=None, reason: typing.Optional[chitose.app.bsky.feed.defs.ReasonRepost]=None, feed_context: typing.Optional[str]=None) -> None:
        self.post = post
        self.reply = reply
        self.reason = reason
        self.feed_context = feed_context

    def to_dict(self) -> dict[str, typing.Any]:
        return {'post': self.post, 'reply': self.reply, 'reason': self.reason, 'feedContext': self.feed_context, '$type': 'app.bsky.feed.defs#feedViewPost'}

class ReplyRef(chitose.Object):
    """"""

    def __init__(self, root: typing.Union[chitose.app.bsky.feed.defs.PostView, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost], parent: typing.Union[chitose.app.bsky.feed.defs.PostView, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost]) -> None:
        self.root = root
        self.parent = parent

    def to_dict(self) -> dict[str, typing.Any]:
        return {'root': self.root, 'parent': self.parent, '$type': 'app.bsky.feed.defs#replyRef'}

class ReasonRepost(chitose.Object):
    """"""

    def __init__(self, by: chitose.app.bsky.actor.defs.ProfileViewBasic, indexed_at: str) -> None:
        self.by = by
        self.indexed_at = indexed_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'by': self.by, 'indexedAt': self.indexed_at, '$type': 'app.bsky.feed.defs#reasonRepost'}

class ThreadViewPost(chitose.Object):
    """"""

    def __init__(self, post: chitose.app.bsky.feed.defs.PostView, parent: typing.Optional[typing.Union[chitose.app.bsky.feed.defs.ThreadViewPost, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost]]=None, replies: typing.Optional[list[typing.Union[chitose.app.bsky.feed.defs.ThreadViewPost, chitose.app.bsky.feed.defs.NotFoundPost, chitose.app.bsky.feed.defs.BlockedPost]]]=None) -> None:
        self.post = post
        self.parent = parent
        self.replies = replies

    def to_dict(self) -> dict[str, typing.Any]:
        return {'post': self.post, 'parent': self.parent, 'replies': self.replies, '$type': 'app.bsky.feed.defs#threadViewPost'}

class NotFoundPost(chitose.Object):
    """"""

    def __init__(self, uri: str, not_found: bool) -> None:
        self.uri = uri
        self.not_found = not_found

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'notFound': self.not_found, '$type': 'app.bsky.feed.defs#notFoundPost'}

class BlockedPost(chitose.Object):
    """"""

    def __init__(self, uri: str, blocked: bool, author: chitose.app.bsky.feed.defs.BlockedAuthor) -> None:
        self.uri = uri
        self.blocked = blocked
        self.author = author

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'blocked': self.blocked, 'author': self.author, '$type': 'app.bsky.feed.defs#blockedPost'}

class BlockedAuthor(chitose.Object):
    """"""

    def __init__(self, did: str, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None) -> None:
        self.did = did
        self.viewer = viewer

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'viewer': self.viewer, '$type': 'app.bsky.feed.defs#blockedAuthor'}

class GeneratorView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, did: str, creator: chitose.app.bsky.actor.defs.ProfileView, display_name: str, indexed_at: str, description: typing.Optional[str]=None, description_facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, avatar: typing.Optional[str]=None, like_count: typing.Optional[int]=None, accepts_interactions: typing.Optional[bool]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, viewer: typing.Optional[chitose.app.bsky.feed.defs.GeneratorViewerState]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.did = did
        self.creator = creator
        self.display_name = display_name
        self.indexed_at = indexed_at
        self.description = description
        self.description_facets = description_facets
        self.avatar = avatar
        self.like_count = like_count
        self.accepts_interactions = accepts_interactions
        self.labels = labels
        self.viewer = viewer

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'did': self.did, 'creator': self.creator, 'displayName': self.display_name, 'indexedAt': self.indexed_at, 'description': self.description, 'descriptionFacets': self.description_facets, 'avatar': self.avatar, 'likeCount': self.like_count, 'acceptsInteractions': self.accepts_interactions, 'labels': self.labels, 'viewer': self.viewer, '$type': 'app.bsky.feed.defs#generatorView'}

class GeneratorViewerState(chitose.Object):
    """"""

    def __init__(self, like: typing.Optional[str]=None) -> None:
        self.like = like

    def to_dict(self) -> dict[str, typing.Any]:
        return {'like': self.like, '$type': 'app.bsky.feed.defs#generatorViewerState'}

class SkeletonFeedPost(chitose.Object):
    """


    :param feed_context: Context that will be passed through to client and may be passed to feed generator back alongside interactions.
    """

    def __init__(self, post: str, reason: typing.Optional[chitose.app.bsky.feed.defs.SkeletonReasonRepost]=None, feed_context: typing.Optional[str]=None) -> None:
        self.post = post
        self.reason = reason
        self.feed_context = feed_context

    def to_dict(self) -> dict[str, typing.Any]:
        return {'post': self.post, 'reason': self.reason, 'feedContext': self.feed_context, '$type': 'app.bsky.feed.defs#skeletonFeedPost'}

class SkeletonReasonRepost(chitose.Object):
    """"""

    def __init__(self, repost: str) -> None:
        self.repost = repost

    def to_dict(self) -> dict[str, typing.Any]:
        return {'repost': self.repost, '$type': 'app.bsky.feed.defs#skeletonReasonRepost'}

class ThreadgateView(chitose.Object):
    """"""

    def __init__(self, uri: typing.Optional[str]=None, cid: typing.Optional[str]=None, record: typing.Optional[typing.Any]=None, lists: typing.Optional[list[chitose.app.bsky.graph.defs.ListViewBasic]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.record = record
        self.lists = lists

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'record': self.record, 'lists': self.lists, '$type': 'app.bsky.feed.defs#threadgateView'}

class Interaction(chitose.Object):
    """


    :param feed_context: Context on a feed item that was orginally supplied by the feed generator on getFeedSkeleton.
    """

    def __init__(self, item: typing.Optional[str]=None, event: typing.Optional[typing.Literal['app.bsky.feed.defs#requestLess', 'app.bsky.feed.defs#requestMore', 'app.bsky.feed.defs#clickthroughItem', 'app.bsky.feed.defs#clickthroughAuthor', 'app.bsky.feed.defs#clickthroughReposter', 'app.bsky.feed.defs#clickthroughEmbed', 'app.bsky.feed.defs#interactionSeen', 'app.bsky.feed.defs#interactionLike', 'app.bsky.feed.defs#interactionRepost', 'app.bsky.feed.defs#interactionReply', 'app.bsky.feed.defs#interactionQuote', 'app.bsky.feed.defs#interactionShare']]=None, feed_context: typing.Optional[str]=None) -> None:
        self.item = item
        self.event = event
        self.feed_context = feed_context

    def to_dict(self) -> dict[str, typing.Any]:
        return {'item': self.item, 'event': self.event, 'feedContext': self.feed_context, '$type': 'app.bsky.feed.defs#interaction'}
REQUEST_LESS = 'app.bsky.feed.defs#requestLess'
REQUEST_MORE = 'app.bsky.feed.defs#requestMore'
CLICKTHROUGH_ITEM = 'app.bsky.feed.defs#clickthroughItem'
CLICKTHROUGH_AUTHOR = 'app.bsky.feed.defs#clickthroughAuthor'
CLICKTHROUGH_REPOSTER = 'app.bsky.feed.defs#clickthroughReposter'
CLICKTHROUGH_EMBED = 'app.bsky.feed.defs#clickthroughEmbed'
INTERACTION_SEEN = 'app.bsky.feed.defs#interactionSeen'
INTERACTION_LIKE = 'app.bsky.feed.defs#interactionLike'
INTERACTION_REPOST = 'app.bsky.feed.defs#interactionRepost'
INTERACTION_REPLY = 'app.bsky.feed.defs#interactionReply'
INTERACTION_QUOTE = 'app.bsky.feed.defs#interactionQuote'
INTERACTION_SHARE = 'app.bsky.feed.defs#interactionShare'
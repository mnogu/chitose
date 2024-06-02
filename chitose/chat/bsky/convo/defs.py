# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.record
import chitose.app.bsky.richtext.facet
import chitose.chat.bsky.actor.defs
import chitose.chat.bsky.convo.defs
import typing

class MessageRef(chitose.Object):
    """"""

    def __init__(self, did: str, convo_id: str, message_id: str) -> None:
        self.did = did
        self.convo_id = convo_id
        self.message_id = message_id

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'convoId': self.convo_id, 'messageId': self.message_id, '$type': 'chat.bsky.convo.defs#messageRef'}

class MessageInput(chitose.Object):
    """


    :param facets: Annotations of text (mentions, URLs, hashtags, etc)
    """

    def __init__(self, text: str, facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, embed: typing.Optional[chitose.app.bsky.embed.record.Record]=None) -> None:
        self.text = text
        self.facets = facets
        self.embed = embed

    def to_dict(self) -> dict[str, typing.Any]:
        return {'text': self.text, 'facets': self.facets, 'embed': self.embed, '$type': 'chat.bsky.convo.defs#messageInput'}

class MessageView(chitose.Object):
    """


    :param facets: Annotations of text (mentions, URLs, hashtags, etc)
    """

    def __init__(self, id: str, rev: str, text: str, sender: chitose.chat.bsky.convo.defs.MessageViewSender, sent_at: str, facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, embed: typing.Optional[chitose.app.bsky.embed.record.View]=None) -> None:
        self.id = id
        self.rev = rev
        self.text = text
        self.sender = sender
        self.sent_at = sent_at
        self.facets = facets
        self.embed = embed

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'rev': self.rev, 'text': self.text, 'sender': self.sender, 'sentAt': self.sent_at, 'facets': self.facets, 'embed': self.embed, '$type': 'chat.bsky.convo.defs#messageView'}

class DeletedMessageView(chitose.Object):
    """"""

    def __init__(self, id: str, rev: str, sender: chitose.chat.bsky.convo.defs.MessageViewSender, sent_at: str) -> None:
        self.id = id
        self.rev = rev
        self.sender = sender
        self.sent_at = sent_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'rev': self.rev, 'sender': self.sender, 'sentAt': self.sent_at, '$type': 'chat.bsky.convo.defs#deletedMessageView'}

class MessageViewSender(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'chat.bsky.convo.defs#messageViewSender'}

class ConvoView(chitose.Object):
    """"""

    def __init__(self, id: str, rev: str, members: list[chitose.chat.bsky.actor.defs.ProfileViewBasic], muted: bool, unread_count: int, last_message: typing.Optional[typing.Union[chitose.chat.bsky.convo.defs.MessageView, chitose.chat.bsky.convo.defs.DeletedMessageView]]=None) -> None:
        self.id = id
        self.rev = rev
        self.members = members
        self.muted = muted
        self.unread_count = unread_count
        self.last_message = last_message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'rev': self.rev, 'members': self.members, 'muted': self.muted, 'unreadCount': self.unread_count, 'lastMessage': self.last_message, '$type': 'chat.bsky.convo.defs#convoView'}

class LogBeginConvo(chitose.Object):
    """"""

    def __init__(self, rev: str, convo_id: str) -> None:
        self.rev = rev
        self.convo_id = convo_id

    def to_dict(self) -> dict[str, typing.Any]:
        return {'rev': self.rev, 'convoId': self.convo_id, '$type': 'chat.bsky.convo.defs#logBeginConvo'}

class LogLeaveConvo(chitose.Object):
    """"""

    def __init__(self, rev: str, convo_id: str) -> None:
        self.rev = rev
        self.convo_id = convo_id

    def to_dict(self) -> dict[str, typing.Any]:
        return {'rev': self.rev, 'convoId': self.convo_id, '$type': 'chat.bsky.convo.defs#logLeaveConvo'}

class LogCreateMessage(chitose.Object):
    """"""

    def __init__(self, rev: str, convo_id: str, message: typing.Union[chitose.chat.bsky.convo.defs.MessageView, chitose.chat.bsky.convo.defs.DeletedMessageView]) -> None:
        self.rev = rev
        self.convo_id = convo_id
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'rev': self.rev, 'convoId': self.convo_id, 'message': self.message, '$type': 'chat.bsky.convo.defs#logCreateMessage'}

class LogDeleteMessage(chitose.Object):
    """"""

    def __init__(self, rev: str, convo_id: str, message: typing.Union[chitose.chat.bsky.convo.defs.MessageView, chitose.chat.bsky.convo.defs.DeletedMessageView]) -> None:
        self.rev = rev
        self.convo_id = convo_id
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'rev': self.rev, 'convoId': self.convo_id, 'message': self.message, '$type': 'chat.bsky.convo.defs#logDeleteMessage'}
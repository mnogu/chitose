# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.com.atproto.label.defs
import typing

class ProfileViewBasic(chitose.Object):
    """


    :param chat_disabled: Set to true when the actor cannot actively participate in converations
    """

    def __init__(self, did: str, handle: str, display_name: typing.Optional[str]=None, avatar: typing.Optional[str]=None, associated: typing.Optional[chitose.app.bsky.actor.defs.ProfileAssociated]=None, viewer: typing.Optional[chitose.app.bsky.actor.defs.ViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, chat_disabled: typing.Optional[bool]=None) -> None:
        self.did = did
        self.handle = handle
        self.display_name = display_name
        self.avatar = avatar
        self.associated = associated
        self.viewer = viewer
        self.labels = labels
        self.chat_disabled = chat_disabled

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'displayName': self.display_name, 'avatar': self.avatar, 'associated': self.associated, 'viewer': self.viewer, 'labels': self.labels, 'chatDisabled': self.chat_disabled, '$type': 'chat.bsky.actor.defs#profileViewBasic'}
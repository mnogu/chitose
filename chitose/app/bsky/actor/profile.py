# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.label.defs
import typing

class Profile(chitose.Record):
    """"""

    def __init__(self, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[chitose.Blob]=None, banner: typing.Optional[chitose.Blob]=None, labels: typing.Optional[chitose.com.atproto.label.defs.SelfLabels]=None) -> None:
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.banner = banner
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner, 'labels': self.labels, '$type': 'app.bsky.actor.profile'}
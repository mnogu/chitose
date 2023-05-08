# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Profile(chitose.Record):
    """"""

    def __init__(self, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[chitose.Blob]=None, banner: typing.Optional[chitose.Blob]=None) -> None:
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.banner = banner

    def to_dict(self) -> dict:
        return {'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner, '$type': 'app.bsky.actor.profile'}
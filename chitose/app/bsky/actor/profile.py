# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Profile(chitose.Record):
    """"""

    def __init__(self, display_name: typing.Optional[str]=None, description: typing.Optional[str]=None, avatar: typing.Optional[typing.Any]=None, banner: typing.Optional[typing.Any]=None) -> None:
        self.display_name = display_name
        self.description = description
        self.avatar = avatar
        self.banner = banner

    def to_dict(self):
        return {'displayName': self.display_name, 'description': self.description, 'avatar': self.avatar, 'banner': self.banner}
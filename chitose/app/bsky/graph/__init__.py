# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_blocks import _get_blocks
from .get_followers import _get_followers
from .get_follows import _get_follows
from .get_mutes import _get_mutes
from .mute_actor import _mute_actor
from .unmute_actor import _unmute_actor
from .block import *
from .follow import *
from .get_blocks import *
from .get_followers import *
from .get_follows import *
from .get_mutes import *
from .mute_actor import *
from .unmute_actor import *

class _Graph:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_followers(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _get_followers(self.service, self.headers, actor, limit, cursor)

    def mute_actor(self, actor: str):
        return _mute_actor(self.service, self.headers, actor)

    def get_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _get_mutes(self.service, self.headers, limit, cursor)

    def get_follows(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _get_follows(self.service, self.headers, actor, limit, cursor)

    def get_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _get_blocks(self.service, self.headers, limit, cursor)

    def unmute_actor(self, actor: str):
        return _unmute_actor(self.service, self.headers, actor)
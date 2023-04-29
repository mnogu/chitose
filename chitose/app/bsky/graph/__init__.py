# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .follow import *
from .get_followers import *
from .get_follows import *
from .get_mutes import *
from .mute_actor import *
from .unmute_actor import *

class Graph:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_followers(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_followers(self.service, self.headers, actor, limit, cursor)

    def mute_actor(self, actor: str):
        return mute_actor(self.service, self.headers, actor)

    def get_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_mutes(self.service, self.headers, limit, cursor)

    def get_follows(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_follows(self.service, self.headers, actor, limit, cursor)

    def unmute_actor(self, actor: str):
        return unmute_actor(self.service, self.headers, actor)
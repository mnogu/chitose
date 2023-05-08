# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_blocks import _get_blocks
from .get_followers import _get_followers
from .get_follows import _get_follows
from .get_mutes import _get_mutes
from .mute_actor import _mute_actor
from .unmute_actor import _unmute_actor
import typing

class Graph_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def get_followers(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is following an actor?"""
        return _get_followers(self.service, self.headers, actor, limit, cursor)

    def mute_actor(self, actor: str) -> bytes:
        """Mute an actor by did or handle."""
        return _mute_actor(self.service, self.headers, actor)

    def get_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who does the viewer mute?"""
        return _get_mutes(self.service, self.headers, limit, cursor)

    def get_follows(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is an actor following?"""
        return _get_follows(self.service, self.headers, actor, limit, cursor)

    def get_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is the requester's account blocking?"""
        return _get_blocks(self.service, self.headers, limit, cursor)

    def unmute_actor(self, actor: str) -> bytes:
        """Unmute an actor by did or handle."""
        return _unmute_actor(self.service, self.headers, actor)
# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_blocks import _get_blocks
from .get_followers import _get_followers
from .get_follows import _get_follows
from .get_list import _get_list
from .get_list_blocks import _get_list_blocks
from .get_list_mutes import _get_list_mutes
from .get_lists import _get_lists
from .get_mutes import _get_mutes
from .get_suggested_follows_by_actor import _get_suggested_follows_by_actor
from .mute_actor import _mute_actor
from .mute_actor_list import _mute_actor_list
from .unmute_actor import _unmute_actor
from .unmute_actor_list import _unmute_actor_list
import typing

class Graph_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_suggested_follows_by_actor(self, actor: str) -> bytes:
        """Get suggested follows related to a given actor."""
        return _get_suggested_follows_by_actor(self.call, actor)

    def unmute_actor_list(self, list: str) -> bytes:
        """Unmute a list of actors."""
        return _unmute_actor_list(self.call, list)

    def get_list_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Which lists is the requester's account blocking?"""
        return _get_list_blocks(self.call, limit, cursor)

    def mute_actor_list(self, list: str) -> bytes:
        """Mute a list of actors."""
        return _mute_actor_list(self.call, list)

    def get_lists(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Fetch a list of lists that belong to an actor"""
        return _get_lists(self.call, actor, limit, cursor)

    def get_followers(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is following an actor?"""
        return _get_followers(self.call, actor, limit, cursor)

    def mute_actor(self, actor: str) -> bytes:
        """Mute an actor by did or handle."""
        return _mute_actor(self.call, actor)

    def get_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who does the viewer mute?"""
        return _get_mutes(self.call, limit, cursor)

    def get_list_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Which lists is the requester's account muting?"""
        return _get_list_mutes(self.call, limit, cursor)

    def get_follows(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is an actor following?"""
        return _get_follows(self.call, actor, limit, cursor)

    def get_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Who is the requester's account blocking?"""
        return _get_blocks(self.call, limit, cursor)

    def unmute_actor(self, actor: str) -> bytes:
        """Unmute an actor by did or handle."""
        return _unmute_actor(self.call, actor)

    def get_list(self, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Fetch a list of actors"""
        return _get_list(self.call, list, limit, cursor)
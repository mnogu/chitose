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
from .get_relationships import _get_relationships
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
        """Enumerates follows similar to a given account (actor). Expected use is to recommend additional accounts immediately after following one account."""
        return _get_suggested_follows_by_actor(self.call, actor)

    def unmute_actor_list(self, list: str) -> bytes:
        """Unmutes the specified list of accounts. Requires auth."""
        return _unmute_actor_list(self.call, list)

    def get_list_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get mod lists that the requesting account (actor) is blocking. Requires auth."""
        return _get_list_blocks(self.call, limit, cursor)

    def mute_actor_list(self, list: str) -> bytes:
        """Creates a mute relationship for the specified list of accounts. Mutes are private in Bluesky. Requires auth."""
        return _mute_actor_list(self.call, list)

    def get_lists(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates the lists created by a specified account (actor).


        :param actor: The account (actor) to enumerate lists from.
        """
        return _get_lists(self.call, actor, limit, cursor)

    def get_followers(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates accounts which follow a specified account (actor)."""
        return _get_followers(self.call, actor, limit, cursor)

    def mute_actor(self, actor: str) -> bytes:
        """Creates a mute relationship for the specified account. Mutes are private in Bluesky. Requires auth."""
        return _mute_actor(self.call, actor)

    def get_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates accounts that the requesting account (actor) currently has muted. Requires auth."""
        return _get_mutes(self.call, limit, cursor)

    def get_list_mutes(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates mod lists that the requesting account (actor) currently has muted. Requires auth."""
        return _get_list_mutes(self.call, limit, cursor)

    def get_follows(self, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates accounts which a specified account (actor) follows."""
        return _get_follows(self.call, actor, limit, cursor)

    def get_blocks(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Enumerates which accounts the requesting account is currently blocking. Requires auth."""
        return _get_blocks(self.call, limit, cursor)

    def get_relationships(self, actor: str, others: typing.Optional[list[str]]=None) -> bytes:
        """Enumerates public relationships between one account, and a list of other accounts. Does not require auth.


        :param actor: Primary account requesting relationships for.

        :param others: List of 'other' accounts to be related back to the primary.
        """
        return _get_relationships(self.call, actor, others)

    def unmute_actor(self, actor: str) -> bytes:
        """Unmutes the specified account. Requires auth."""
        return _unmute_actor(self.call, actor)

    def get_list(self, list: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Gets a 'view' (with additional context) of a specified list.


        :param list: Reference (AT-URI) of the list record to hydrate.
        """
        return _get_list(self.call, list, limit, cursor)
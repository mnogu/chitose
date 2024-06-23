# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .add_member import _add_member
from .delete_member import _delete_member
from .list_members import _list_members
from .update_member import _update_member
import typing

class Team_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def list_members(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List all members with access to the ozone service."""
        return _list_members(self.call, limit, cursor)

    def delete_member(self, did: str) -> bytes:
        """Delete a member from ozone team. Requires admin role."""
        return _delete_member(self.call, did)

    def update_member(self, did: str, disabled: typing.Optional[bool]=None, role: typing.Optional[typing.Literal['tools.ozone.team.defs#roleAdmin', 'tools.ozone.team.defs#roleModerator', 'tools.ozone.team.defs#roleTriage']]=None) -> bytes:
        """Update a member in the ozone service. Requires admin role."""
        return _update_member(self.call, did, disabled, role)

    def add_member(self, did: str, role: typing.Literal['tools.ozone.team.defs#roleAdmin', 'tools.ozone.team.defs#roleModerator', 'tools.ozone.team.defs#roleTriage']) -> bytes:
        """Add a member to the ozone team. Requires admin role."""
        return _add_member(self.call, did, role)
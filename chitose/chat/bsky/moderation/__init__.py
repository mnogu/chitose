# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_actor_metadata import _get_actor_metadata
from .get_message_context import _get_message_context
from .update_actor_access import _update_actor_access
import typing

class Moderation_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_actor_metadata(self, actor: str) -> bytes:
        """"""
        return _get_actor_metadata(self.call, actor)

    def get_message_context(self, message_id: str, before: typing.Optional[int]=None, after: typing.Optional[int]=None) -> bytes:
        """"""
        return _get_message_context(self.call, message_id, before, after)

    def update_actor_access(self, actor: str, allow_access: bool, ref: typing.Optional[str]=None) -> bytes:
        """"""
        return _update_actor_access(self.call, actor, allow_access, ref)
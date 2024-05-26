# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .delete_message_for_self import _delete_message_for_self
from .get_convo import _get_convo
from .get_convo_for_members import _get_convo_for_members
from .get_log import _get_log
from .get_messages import _get_messages
from .leave_convo import _leave_convo
from .list_convos import _list_convos
from .mute_convo import _mute_convo
from .send_message import _send_message
from .send_message_batch import _send_message_batch
from .unmute_convo import _unmute_convo
from .update_read import _update_read
import chitose.chat.bsky.convo.defs
import chitose.chat.bsky.convo.send_message_batch
import typing

class Convo_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def list_convos(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """"""
        return _list_convos(self.call, limit, cursor)

    def unmute_convo(self, convo_id: str) -> bytes:
        """"""
        return _unmute_convo(self.call, convo_id)

    def get_log(self, cursor: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_log(self.call, cursor)

    def send_message(self, convo_id: str, message: chitose.chat.bsky.convo.defs.MessageInput) -> bytes:
        """"""
        return _send_message(self.call, convo_id, message)

    def leave_convo(self, convo_id: str) -> bytes:
        """"""
        return _leave_convo(self.call, convo_id)

    def mute_convo(self, convo_id: str) -> bytes:
        """"""
        return _mute_convo(self.call, convo_id)

    def delete_message_for_self(self, convo_id: str, message_id: str) -> bytes:
        """"""
        return _delete_message_for_self(self.call, convo_id, message_id)

    def update_read(self, convo_id: str, message_id: typing.Optional[str]=None) -> bytes:
        """"""
        return _update_read(self.call, convo_id, message_id)

    def get_convo(self, convo_id: str) -> bytes:
        """"""
        return _get_convo(self.call, convo_id)

    def get_messages(self, convo_id: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_messages(self.call, convo_id, limit, cursor)

    def get_convo_for_members(self, members: list[str]) -> bytes:
        """"""
        return _get_convo_for_members(self.call, members)

    def send_message_batch(self, items: list[chitose.chat.bsky.convo.send_message_batch.BatchItem]) -> bytes:
        """"""
        return _send_message_batch(self.call, items)
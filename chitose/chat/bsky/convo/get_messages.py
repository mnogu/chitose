# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_messages(call: chitose.xrpc.XrpcCall, convo_id: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """"""
    return call('chat.bsky.convo.getMessages', [('convoId', convo_id), ('limit', limit), ('cursor', cursor)], None, {})
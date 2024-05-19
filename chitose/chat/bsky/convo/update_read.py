# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _update_read(call: chitose.xrpc.XrpcCall, convo_id: str, message_id: typing.Optional[str]=None) -> bytes:
    """"""
    return call('chat.bsky.convo.updateRead', [], {'convoId': convo_id, 'messageId': message_id}, {'Content-Type': 'application/json'})
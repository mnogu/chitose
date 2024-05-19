# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_message_context(call: chitose.xrpc.XrpcCall, message_id: str, before: typing.Optional[int]=None, after: typing.Optional[int]=None) -> bytes:
    """"""
    return call('chat.bsky.moderation.getMessageContext', [('messageId', message_id), ('before', before), ('after', after)], None, {})
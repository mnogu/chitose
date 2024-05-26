# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_message_context(call: chitose.xrpc.XrpcCall, message_id: str, convo_id: typing.Optional[str]=None, before: typing.Optional[int]=None, after: typing.Optional[int]=None) -> bytes:
    """


    :param convo_id: Conversation that the message is from. NOTE: this field will eventually be required.
    """
    return call('chat.bsky.moderation.getMessageContext', [('messageId', message_id), ('convoId', convo_id), ('before', before), ('after', after)], None, {})
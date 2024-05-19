# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_message_for_self(call: chitose.xrpc.XrpcCall, convo_id: str, message_id: str) -> bytes:
    """"""
    return call('chat.bsky.convo.deleteMessageForSelf', [], {'convoId': convo_id, 'messageId': message_id}, {'Content-Type': 'application/json'})
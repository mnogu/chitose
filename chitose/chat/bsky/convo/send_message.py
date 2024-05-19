# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.chat.bsky.convo.defs

def _send_message(call: chitose.xrpc.XrpcCall, convo_id: str, message: chitose.chat.bsky.convo.defs.Message) -> bytes:
    """"""
    return call('chat.bsky.convo.sendMessage', [], {'convoId': convo_id, 'message': message}, {'Content-Type': 'application/json'})
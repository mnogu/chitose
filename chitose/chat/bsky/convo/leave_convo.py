# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _leave_convo(call: chitose.xrpc.XrpcCall, convo_id: str) -> bytes:
    """"""
    return call('chat.bsky.convo.leaveConvo', [], {'convoId': convo_id}, {'Content-Type': 'application/json'})
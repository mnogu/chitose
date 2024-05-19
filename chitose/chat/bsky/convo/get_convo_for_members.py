# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_convo_for_members(call: chitose.xrpc.XrpcCall, members: list[str]) -> bytes:
    """"""
    return call('chat.bsky.convo.getConvoForMembers', [('members', members)], None, {})
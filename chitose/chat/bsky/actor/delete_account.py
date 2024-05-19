# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_account(call: chitose.xrpc.XrpcCall) -> bytes:
    """"""
    return call('chat.bsky.actor.deleteAccount', [], {}, {})
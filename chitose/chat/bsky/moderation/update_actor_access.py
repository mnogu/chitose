# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _update_actor_access(call: chitose.xrpc.XrpcCall, actor: str, allow_access: bool, ref: typing.Optional[str]=None) -> bytes:
    """"""
    return call('chat.bsky.moderation.updateActorAccess', [], {'actor': actor, 'allowAccess': allow_access, 'ref': ref}, {'Content-Type': 'application/json'})
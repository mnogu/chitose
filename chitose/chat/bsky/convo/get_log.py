# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_log(call: chitose.xrpc.XrpcCall, cursor: typing.Optional[str]=None) -> bytes:
    """"""
    return call('chat.bsky.convo.getLog', [('cursor', cursor)], None, {})
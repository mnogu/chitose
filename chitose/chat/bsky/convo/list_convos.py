# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_convos(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """"""
    return call('chat.bsky.convo.listConvos', [('limit', limit), ('cursor', cursor)], None, {})
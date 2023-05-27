# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_invite_codes(call: chitose.xrpc.XrpcCallable, sort: typing.Optional[typing.Literal['recent', 'usage']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Admin view of invite codes"""
    return call('com.atproto.admin.getInviteCodes', [('sort', sort), ('limit', limit), ('cursor', cursor)], None, {})
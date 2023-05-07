# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_invite_codes(service: str, headers: dict[str, str], sort: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Admin view of invite codes"""
    return chitose.xrpc.call('com.atproto.admin.getInviteCodes', [('sort', sort), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)
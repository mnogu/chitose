# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def get_account_invite_codes(service: str, headers: dict[str, str], include_used: typing.Optional[str]=None, create_available: typing.Optional[str]=None):
    """Get all invite codes for a given account"""
    return chitose.xrpc.call('com.atproto.server.getAccountInviteCodes', [('includeUsed', include_used), ('createAvailable', create_available)], None, service, {} | headers)
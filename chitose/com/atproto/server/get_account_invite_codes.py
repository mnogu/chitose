# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_account_invite_codes(call: chitose.xrpc.XrpcCall, include_used: typing.Optional[bool]=None, create_available: typing.Optional[bool]=None) -> bytes:
    """Get all invite codes for a given account"""
    return call('com.atproto.server.getAccountInviteCodes', [('includeUsed', include_used), ('createAvailable', create_available)], None, {})
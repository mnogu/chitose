# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_invite_code(call: chitose.xrpc.XrpcCall, use_count: int, for_account: typing.Optional[str]=None) -> bytes:
    """Create an invite code."""
    return call('com.atproto.server.createInviteCode', [], {'useCount': use_count, 'forAccount': for_account}, {'Content-Type': 'application/json'})
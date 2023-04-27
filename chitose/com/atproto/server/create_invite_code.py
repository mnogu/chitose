from __future__ import annotations
import chitose
import typing

def create_invite_code(service: str, headers: dict[str, str], use_count: int, for_account: typing.Optional[str]=None):
    """Create an invite code."""
    return chitose.xrpc.call('com.atproto.server.createInviteCode', [], {'useCount': use_count, 'forAccount': for_account}, service, {'Content-Type': 'application/json'} | headers)
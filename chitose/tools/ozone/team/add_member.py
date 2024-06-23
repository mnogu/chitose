# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _add_member(call: chitose.xrpc.XrpcCall, did: str, role: typing.Literal['tools.ozone.team.defs#roleAdmin', 'tools.ozone.team.defs#roleModerator', 'tools.ozone.team.defs#roleTriage']) -> bytes:
    """Add a member to the ozone team. Requires admin role."""
    return call('tools.ozone.team.addMember', [], {'did': did, 'role': role}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _update_member(call: chitose.xrpc.XrpcCall, did: str, disabled: typing.Optional[bool]=None, role: typing.Optional[typing.Literal['tools.ozone.team.defs#roleAdmin', 'tools.ozone.team.defs#roleModerator', 'tools.ozone.team.defs#roleTriage']]=None) -> bytes:
    """Update a member in the ozone service. Requires admin role."""
    return call('tools.ozone.team.updateMember', [], {'did': did, 'disabled': disabled, 'role': role}, {'Content-Type': 'application/json'})
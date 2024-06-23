# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_members(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List all members with access to the ozone service."""
    return call('tools.ozone.team.listMembers', [('limit', limit), ('cursor', cursor)], None, {})
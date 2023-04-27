# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def resolve_handle(service: str, headers: dict[str, str], handle: typing.Optional[str]=None):
    """Provides the DID of a repo."""
    return chitose.xrpc.call('com.atproto.identity.resolveHandle', [('handle', handle)], None, service, {} | headers)
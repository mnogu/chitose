# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _resolve_handle(call: chitose.xrpc.XrpcCallable, handle: typing.Optional[str]=None) -> bytes:
    """Provides the DID of a repo.


    :param handle: The handle to resolve. If not supplied, will resolve the host's own handle.
    """
    return call('com.atproto.identity.resolveHandle', [('handle', handle)], None, {})
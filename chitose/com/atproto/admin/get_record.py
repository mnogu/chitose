# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_record(call: chitose.xrpc.XrpcCall, uri: str, cid: typing.Optional[str]=None) -> bytes:
    """Get details about a record."""
    return call('com.atproto.admin.getRecord', [('uri', uri), ('cid', cid)], None, {})
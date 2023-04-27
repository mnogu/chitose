# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def get_record(service: str, headers: dict[str, str], uri: str, cid: typing.Optional[str]=None):
    """View details about a record."""
    return chitose.xrpc.call('com.atproto.admin.getRecord', [('uri', uri), ('cid', cid)], None, service, {} | headers)
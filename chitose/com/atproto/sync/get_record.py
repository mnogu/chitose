# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def get_record(service: str, headers: dict[str, str], did: str, collection: str, rkey: str, commit: typing.Optional[str]=None):
    """Gets blocks needed for existence or non-existence of record."""
    return chitose.xrpc.call('com.atproto.sync.getRecord', [('did', did), ('collection', collection), ('rkey', rkey), ('commit', commit)], None, service, {} | headers)
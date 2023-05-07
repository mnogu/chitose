# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_record(service: str, headers: dict[str, str], did: str, collection: str, rkey: str, commit: typing.Optional[str]=None) -> bytes:
    """Gets blocks needed for existence or non-existence of record.


    :param did: The DID of the repo.

    :param commit: An optional past commit CID.
    """
    return chitose.xrpc.call('com.atproto.sync.getRecord', [('did', did), ('collection', collection), ('rkey', rkey), ('commit', commit)], None, service, {} | headers)
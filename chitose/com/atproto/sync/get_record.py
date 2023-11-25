# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_record(call: chitose.xrpc.XrpcCall, did: str, collection: str, rkey: str, commit: typing.Optional[str]=None) -> bytes:
    """Get blocks needed for existence or non-existence of record.


    :param did: The DID of the repo.

    :param commit: An optional past commit CID.
    """
    return call('com.atproto.sync.getRecord', [('did', did), ('collection', collection), ('rkey', rkey), ('commit', commit)], None, {})
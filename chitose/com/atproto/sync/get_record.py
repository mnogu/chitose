# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_record(call: chitose.xrpc.XrpcCall, did: str, collection: str, rkey: str, commit: typing.Optional[str]=None) -> bytes:
    """Get data blocks needed to prove the existence or non-existence of record in the current version of repo. Does not require auth.


    :param did: The DID of the repo.

    :param rkey: Record Key

    :param commit: DEPRECATED: referenced a repo commit by CID, and retrieved record as of that commit
    """
    return call('com.atproto.sync.getRecord', [('did', did), ('collection', collection), ('rkey', rkey), ('commit', commit)], None, {})
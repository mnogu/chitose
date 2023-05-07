# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_record(service: str, headers: dict[str, str], repo: str, collection: str, rkey: str, cid: typing.Optional[str]=None) -> bytes:
    """Get a record.


    :param repo: The handle or DID of the repo.

    :param collection: The NSID of the record collection.

    :param rkey: The key of the record.

    :param cid: The CID of the version of the record. If not specified, then return the most recent version.
    """
    return chitose.xrpc.call('com.atproto.repo.getRecord', [('repo', repo), ('collection', collection), ('rkey', rkey), ('cid', cid)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _put_record(service: str, headers: dict[str, str], repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[str]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Write a record, creating or updating it as needed.


    :param repo: The handle or DID of the repo.

    :param collection: The NSID of the record collection.

    :param rkey: The key of the record.

    :param record: The record to write.

    :param validate: Validate the record?

    :param swap_record: Compare and swap with the previous record by cid.

    :param swap_commit: Compare and swap with the previous commit by cid.
    """
    return chitose.xrpc.call('com.atproto.repo.putRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapRecord': swap_record, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)
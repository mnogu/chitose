# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_record(service: str, headers: dict[str, str], repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Create a new record.


    :param repo: The handle or DID of the repo.

    :param collection: The NSID of the record collection.

    :param record: The record to create.

    :param rkey: The key of the record.

    :param validate: Validate the record?

    :param swap_commit: Compare and swap with the previous commit by cid.
    """
    return chitose.xrpc.call('com.atproto.repo.createRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)
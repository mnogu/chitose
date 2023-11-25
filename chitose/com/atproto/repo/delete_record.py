# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _delete_record(call: chitose.xrpc.XrpcCall, repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Delete a record, or ensure it doesn't exist.


    :param repo: The handle or DID of the repo.

    :param collection: The NSID of the record collection.

    :param rkey: The key of the record.

    :param swap_record: Compare and swap with the previous record by CID.

    :param swap_commit: Compare and swap with the previous commit by CID.
    """
    return call('com.atproto.repo.deleteRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'swapRecord': swap_record, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _delete_record(call: chitose.xrpc.XrpcCall, repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Delete a repository record, or ensure it doesn't exist. Requires auth, implemented by PDS.


    :param repo: The handle or DID of the repo (aka, current account).

    :param collection: The NSID of the record collection.

    :param rkey: The Record Key.

    :param swap_record: Compare and swap with the previous record by CID.

    :param swap_commit: Compare and swap with the previous commit by CID.
    """
    return call('com.atproto.repo.deleteRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'swapRecord': swap_record, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})
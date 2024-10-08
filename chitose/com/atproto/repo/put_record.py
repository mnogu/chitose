# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _put_record(call: chitose.xrpc.XrpcCall, repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[bool]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Write a repository record, creating or updating it as needed. Requires auth, implemented by PDS.


    :param repo: The handle or DID of the repo (aka, current account).

    :param collection: The NSID of the record collection.

    :param rkey: The Record Key.

    :param record: The record to write.

    :param validate: Can be set to 'false' to skip Lexicon schema validation of record data, 'true' to require it, or leave unset to validate only for known Lexicons.

    :param swap_record: Compare and swap with the previous record by CID. WARNING: nullable and optional field; may cause problems with golang implementation

    :param swap_commit: Compare and swap with the previous commit by CID.
    """
    return call('com.atproto.repo.putRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapRecord': swap_record, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})
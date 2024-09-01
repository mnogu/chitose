# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_record(call: chitose.xrpc.XrpcCall, repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[bool]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Create a single new repository record. Requires auth, implemented by PDS.


    :param repo: The handle or DID of the repo (aka, current account).

    :param collection: The NSID of the record collection.

    :param record: The record itself. Must contain a $type field.

    :param rkey: The Record Key.

    :param validate: Can be set to 'false' to skip Lexicon schema validation of record data, 'true' to require it, or leave unset to validate only for known Lexicons.

    :param swap_commit: Compare and swap with the previous commit by CID.
    """
    return call('com.atproto.repo.createRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})
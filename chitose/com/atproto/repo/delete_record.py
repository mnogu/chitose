# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def delete_record(service: str, headers: dict[str, str], repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
    """Delete a record, or ensure it doesn't exist."""
    return chitose.xrpc.call('com.atproto.repo.deleteRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'swapRecord': swap_record, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)
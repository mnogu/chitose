# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def _put_record(service: str, headers: dict[str, str], repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[str]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
    """Write a record, creating or updating it as needed."""
    return chitose.xrpc.call('com.atproto.repo.putRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapRecord': swap_record, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)
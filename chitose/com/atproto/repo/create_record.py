# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def create_record(service: str, headers: dict[str, str], repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
    """Create a new record."""
    return chitose.xrpc.call('com.atproto.repo.createRecord', [], {'repo': repo, 'collection': collection, 'rkey': rkey, 'validate': validate, 'record': record, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)
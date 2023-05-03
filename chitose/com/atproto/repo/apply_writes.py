# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def _apply_writes(service: str, headers: dict[str, str], repo: str, writes: list[typing.Union[Create, Update, Delete]], validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
    """Apply a batch transaction of creates, updates, and deletes."""
    return chitose.xrpc.call('com.atproto.repo.applyWrites', [], {'repo': repo, 'validate': validate, 'writes': writes, 'swapCommit': swap_commit}, service, {'Content-Type': 'application/json'} | headers)

class Create(chitose.Object):

    def __init__(self, collection: str, value: typing.Any, rkey: typing.Optional[str]) -> None:
        self.collection = collection
        self.value = value
        self.rkey = rkey

    def to_dict(self):
        return {'collection': self.collection, 'value': self.value, 'rkey': self.rkey}

class Update(chitose.Object):

    def __init__(self, collection: str, rkey: str, value: typing.Any) -> None:
        self.collection = collection
        self.rkey = rkey
        self.value = value

    def to_dict(self):
        return {'collection': self.collection, 'rkey': self.rkey, 'value': self.value}

class Delete(chitose.Object):

    def __init__(self, collection: str, rkey: str) -> None:
        self.collection = collection
        self.rkey = rkey

    def to_dict(self):
        return {'collection': self.collection, 'rkey': self.rkey}
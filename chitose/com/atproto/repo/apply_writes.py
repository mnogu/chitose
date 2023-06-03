# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.repo.apply_writes
import typing

def _apply_writes(call: chitose.xrpc.XrpcCall, repo: str, writes: list[typing.Union[chitose.com.atproto.repo.apply_writes.Create, chitose.com.atproto.repo.apply_writes.Update, chitose.com.atproto.repo.apply_writes.Delete]], validate: typing.Optional[bool]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Apply a batch transaction of creates, updates, and deletes.


    :param repo: The handle or DID of the repo.

    :param validate: Validate the records?
    """
    return call('com.atproto.repo.applyWrites', [], {'repo': repo, 'validate': validate, 'writes': writes, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})

class Create(chitose.Object):
    """"""

    def __init__(self, collection: str, value: typing.Any, rkey: typing.Optional[str]=None) -> None:
        self.collection = collection
        self.value = value
        self.rkey = rkey

    def to_dict(self) -> dict:
        return {'collection': self.collection, 'value': self.value, 'rkey': self.rkey, '$type': 'com.atproto.repo.applyWrites#create'}

class Update(chitose.Object):
    """"""

    def __init__(self, collection: str, rkey: str, value: typing.Any) -> None:
        self.collection = collection
        self.rkey = rkey
        self.value = value

    def to_dict(self) -> dict:
        return {'collection': self.collection, 'rkey': self.rkey, 'value': self.value, '$type': 'com.atproto.repo.applyWrites#update'}

class Delete(chitose.Object):
    """"""

    def __init__(self, collection: str, rkey: str) -> None:
        self.collection = collection
        self.rkey = rkey

    def to_dict(self) -> dict:
        return {'collection': self.collection, 'rkey': self.rkey, '$type': 'com.atproto.repo.applyWrites#delete'}
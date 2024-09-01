# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.repo.apply_writes
import typing

def _apply_writes(call: chitose.xrpc.XrpcCall, repo: str, writes: list[typing.Union[chitose.com.atproto.repo.apply_writes.Create, chitose.com.atproto.repo.apply_writes.Update, chitose.com.atproto.repo.apply_writes.Delete]], validate: typing.Optional[bool]=None, swap_commit: typing.Optional[str]=None) -> bytes:
    """Apply a batch transaction of repository creates, updates, and deletes. Requires auth, implemented by PDS.


    :param repo: The handle or DID of the repo (aka, current account).

    :param validate: Can be set to 'false' to skip Lexicon schema validation of record data across all operations, 'true' to require it, or leave unset to validate only for known Lexicons.

    :param swap_commit: If provided, the entire operation will fail if the current repo commit CID does not match this value. Used to prevent conflicting repo mutations.
    """
    return call('com.atproto.repo.applyWrites', [], {'repo': repo, 'validate': validate, 'writes': writes, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})

class Create(chitose.Object):
    """Operation which creates a new record."""

    def __init__(self, collection: str, value: typing.Any, rkey: typing.Optional[str]=None) -> None:
        self.collection = collection
        self.value = value
        self.rkey = rkey

    def to_dict(self) -> dict[str, typing.Any]:
        return {'collection': self.collection, 'value': self.value, 'rkey': self.rkey, '$type': 'com.atproto.repo.applyWrites#create'}

class Update(chitose.Object):
    """Operation which updates an existing record."""

    def __init__(self, collection: str, rkey: str, value: typing.Any) -> None:
        self.collection = collection
        self.rkey = rkey
        self.value = value

    def to_dict(self) -> dict[str, typing.Any]:
        return {'collection': self.collection, 'rkey': self.rkey, 'value': self.value, '$type': 'com.atproto.repo.applyWrites#update'}

class Delete(chitose.Object):
    """Operation which deletes an existing record."""

    def __init__(self, collection: str, rkey: str) -> None:
        self.collection = collection
        self.rkey = rkey

    def to_dict(self) -> dict[str, typing.Any]:
        return {'collection': self.collection, 'rkey': self.rkey, '$type': 'com.atproto.repo.applyWrites#delete'}

class CreateResult(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, validation_status: typing.Optional[typing.Literal['valid', 'unknown']]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.validation_status = validation_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'validationStatus': self.validation_status, '$type': 'com.atproto.repo.applyWrites#createResult'}

class UpdateResult(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, validation_status: typing.Optional[typing.Literal['valid', 'unknown']]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.validation_status = validation_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'validationStatus': self.validation_status, '$type': 'com.atproto.repo.applyWrites#updateResult'}

class DeleteResult(chitose.Object):
    """"""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'com.atproto.repo.applyWrites#deleteResult'}
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.sync.subscribe_repos
import typing

def _subscribe_repos(subscribe: chitose.xrpc.XrpcSubscribe, handler: chitose.xrpc.XrpcHandler, cursor: typing.Optional[int]=None) -> None:
    """Repository event stream, aka Firehose endpoint. Outputs repo commits with diff data, and identity update events, for all repositories on the current server. See the atproto specifications for details around stream sequencing, repo versioning, CAR diff format, and more. Public and does not require auth; implemented by PDS and Relay.


    :param cursor: The last known event seq number to backfill from.
    """
    subscribe('com.atproto.sync.subscribeRepos', [('cursor', cursor)], handler)

class Commit(chitose.Object):
    """Represents an update of repository state. Note that empty commits are allowed, which include no repo data changes, but an update to rev and signature.


    :param seq: The stream sequence number of this message.

    :param rebase: DEPRECATED -- unused

    :param too_big: Indicates that this commit contained too many ops, or data size was too large. Consumers will need to make a separate request to get missing data.

    :param repo: The repo this event comes from.

    :param commit: Repo commit object CID.

    :param rev: The rev of the emitted commit. Note that this information is also in the commit object included in blocks, unless this is a tooBig event.

    :param since: The rev of the last emitted commit from this repo (if any).

    :param blocks: CAR file containing relevant blocks, as a diff since the previous repo state.

    :param time: Timestamp of when this message was originally broadcast.

    :param prev: DEPRECATED -- unused. WARNING -- nullable and optional; stick with optional to ensure golang interoperability.
    """

    def __init__(self, seq: int, rebase: bool, too_big: bool, repo: str, commit: typing.Any, rev: str, since: str, blocks: typing.Any, ops: list[chitose.com.atproto.sync.subscribe_repos.RepoOp], blobs: list[typing.Any], time: str, prev: typing.Optional[typing.Any]=None) -> None:
        self.seq = seq
        self.rebase = rebase
        self.too_big = too_big
        self.repo = repo
        self.commit = commit
        self.rev = rev
        self.since = since
        self.blocks = blocks
        self.ops = ops
        self.blobs = blobs
        self.time = time
        self.prev = prev

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'rebase': self.rebase, 'tooBig': self.too_big, 'repo': self.repo, 'commit': self.commit, 'rev': self.rev, 'since': self.since, 'blocks': self.blocks, 'ops': self.ops, 'blobs': self.blobs, 'time': self.time, 'prev': self.prev, '$type': 'com.atproto.sync.subscribeRepos#commit'}

class Identity(chitose.Object):
    """Represents a change to an account's identity. Could be an updated handle, signing key, or pds hosting endpoint. Serves as a prod to all downstream services to refresh their identity cache."""

    def __init__(self, seq: int, did: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#identity'}

class Handle(chitose.Object):
    """Represents an update of the account's handle, or transition to/from invalid state. NOTE: Will be deprecated in favor of #identity."""

    def __init__(self, seq: int, did: str, handle: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.handle = handle
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'handle': self.handle, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#handle'}

class Migrate(chitose.Object):
    """Represents an account moving from one PDS instance to another. NOTE: not implemented; account migration uses #identity instead"""

    def __init__(self, seq: int, did: str, migrate_to: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.migrate_to = migrate_to
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'migrateTo': self.migrate_to, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#migrate'}

class Tombstone(chitose.Object):
    """Indicates that an account has been deleted. NOTE: may be deprecated in favor of #identity or a future #account event"""

    def __init__(self, seq: int, did: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#tombstone'}

class Info(chitose.Object):
    """"""

    def __init__(self, name: typing.Literal['OutdatedCursor',], message: typing.Optional[str]=None) -> None:
        self.name = name
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'name': self.name, 'message': self.message, '$type': 'com.atproto.sync.subscribeRepos#info'}

class RepoOp(chitose.Object):
    """A repo operation, ie a mutation of a single record.


    :param cid: For creates and updates, the new record CID. For deletions, null.
    """

    def __init__(self, action: typing.Literal['create', 'update', 'delete'], path: str, cid: typing.Any) -> None:
        self.action = action
        self.path = path
        self.cid = cid

    def to_dict(self) -> dict[str, typing.Any]:
        return {'action': self.action, 'path': self.path, 'cid': self.cid, '$type': 'com.atproto.sync.subscribeRepos#repoOp'}
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.sync.subscribe_repos
import typing

class Commit(chitose.Object):
    """


    :param blocks: CAR file containing relevant blocks
    """

    def __init__(self, seq: int, rebase: str, too_big: str, repo: str, commit: typing.Any, prev: typing.Any, blocks: typing.Any, ops: list[chitose.com.atproto.sync.subscribe_repos.RepoOp], blobs: list[typing.Any], time: str) -> None:
        self.seq = seq
        self.rebase = rebase
        self.too_big = too_big
        self.repo = repo
        self.commit = commit
        self.prev = prev
        self.blocks = blocks
        self.ops = ops
        self.blobs = blobs
        self.time = time

    def to_dict(self) -> dict:
        return {'seq': self.seq, 'rebase': self.rebase, 'tooBig': self.too_big, 'repo': self.repo, 'commit': self.commit, 'prev': self.prev, 'blocks': self.blocks, 'ops': self.ops, 'blobs': self.blobs, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#commit'}

class Handle(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, handle: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.handle = handle
        self.time = time

    def to_dict(self) -> dict:
        return {'seq': self.seq, 'did': self.did, 'handle': self.handle, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#handle'}

class Migrate(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, migrate_to: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.migrate_to = migrate_to
        self.time = time

    def to_dict(self) -> dict:
        return {'seq': self.seq, 'did': self.did, 'migrateTo': self.migrate_to, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#migrate'}

class Tombstone(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.time = time

    def to_dict(self) -> dict:
        return {'seq': self.seq, 'did': self.did, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#tombstone'}

class Info(chitose.Object):
    """"""

    def __init__(self, name: str, message: typing.Optional[str]=None) -> None:
        self.name = name
        self.message = message

    def to_dict(self) -> dict:
        return {'name': self.name, 'message': self.message, '$type': 'com.atproto.sync.subscribeRepos#info'}

class RepoOp(chitose.Object):
    """"""

    def __init__(self, action: str, path: str, cid: typing.Any) -> None:
        self.action = action
        self.path = path
        self.cid = cid

    def to_dict(self) -> dict:
        return {'action': self.action, 'path': self.path, 'cid': self.cid, '$type': 'com.atproto.sync.subscribeRepos#repoOp'}
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_repos(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List dids and root cids of hosted repos"""
    return call('com.atproto.sync.listRepos', [('limit', limit), ('cursor', cursor)], None, {})

class Repo(chitose.Object):
    """"""

    def __init__(self, did: str, head: str) -> None:
        self.did = did
        self.head = head

    def to_dict(self) -> dict:
        return {'did': self.did, 'head': self.head, '$type': 'com.atproto.sync.listRepos#repo'}
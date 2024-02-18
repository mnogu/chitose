# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_repos(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Enumerates all the DID, rev, and commit CID for all repos hosted by this service. Does not require auth; implemented by PDS and Relay."""
    return call('com.atproto.sync.listRepos', [('limit', limit), ('cursor', cursor)], None, {})

class Repo(chitose.Object):
    """


    :param head: Current repo commit CID
    """

    def __init__(self, did: str, head: str, rev: str) -> None:
        self.did = did
        self.head = head
        self.rev = rev

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'head': self.head, 'rev': self.rev, '$type': 'com.atproto.sync.listRepos#repo'}
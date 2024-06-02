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

    :param status: If active=false, this optional field indicates a possible reason for why the account is not active. If active=false and no status is supplied, then the host makes no claim for why the repository is no longer being hosted.
    """

    def __init__(self, did: str, head: str, rev: str, active: typing.Optional[bool]=None, status: typing.Optional[typing.Literal['takendown', 'suspended', 'deactivated']]=None) -> None:
        self.did = did
        self.head = head
        self.rev = rev
        self.active = active
        self.status = status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'head': self.head, 'rev': self.rev, 'active': self.active, 'status': self.status, '$type': 'com.atproto.sync.listRepos#repo'}
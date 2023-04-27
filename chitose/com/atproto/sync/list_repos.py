# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def list_repos(service: str, headers: dict[str, str], limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
    """List dids and root cids of hosted repos"""
    return chitose.xrpc.call('com.atproto.sync.listRepos', [('limit', limit), ('cursor', cursor)], None, service, {} | headers)

class Repo(chitose.Object):

    def __init__(self, did: str, head: str) -> None:
        self.did = did
        self.head = head

    def to_dict(self):
        return {'did': self.did, 'head': self.head}
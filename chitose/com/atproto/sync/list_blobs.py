from __future__ import annotations
import chitose
import typing

def list_blobs(service: str, headers: dict[str, str], did: str, latest: typing.Optional[str]=None, earliest: typing.Optional[str]=None):
    """List blob cids for some range of commits"""
    return chitose.xrpc.call('com.atproto.sync.listBlobs', [('did', did), ('latest', latest), ('earliest', earliest)], None, service, {} | headers)
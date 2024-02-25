# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_missing_blobs(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Returns a list of missing blobs for the requesting account. Intended to be used in the account migration flow."""
    return call('com.atproto.repo.listMissingBlobs', [('limit', limit), ('cursor', cursor)], None, {})

class RecordBlob(chitose.Object):
    """"""

    def __init__(self, cid: str, record_uri: str) -> None:
        self.cid = cid
        self.record_uri = record_uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'cid': self.cid, 'recordUri': self.record_uri, '$type': 'com.atproto.repo.listMissingBlobs#recordBlob'}
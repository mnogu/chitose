# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose
import typing

def list_records(service: str, headers: dict[str, str], repo: str, collection: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, rkey_start: typing.Optional[str]=None, rkey_end: typing.Optional[str]=None, reverse: typing.Optional[str]=None):
    """List a range of records in a collection."""
    return chitose.xrpc.call('com.atproto.repo.listRecords', [('repo', repo), ('collection', collection), ('limit', limit), ('cursor', cursor), ('rkeyStart', rkey_start), ('rkeyEnd', rkey_end), ('reverse', reverse)], None, service, {} | headers)

class Record(chitose.Object):

    def __init__(self, uri: str, cid: str, value: typing.Any) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value

    def to_dict(self):
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value}
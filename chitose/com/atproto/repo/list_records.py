# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_records(call: chitose.xrpc.XrpcCall, repo: str, collection: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, rkey_start: typing.Optional[str]=None, rkey_end: typing.Optional[str]=None, reverse: typing.Optional[bool]=None) -> bytes:
    """List a range of records in a collection.


    :param repo: The handle or DID of the repo.

    :param collection: The NSID of the record type.

    :param limit: The number of records to return.

    :param rkey_start: DEPRECATED: The lowest sort-ordered rkey to start from (exclusive)

    :param rkey_end: DEPRECATED: The highest sort-ordered rkey to stop at (exclusive)

    :param reverse: Reverse the order of the returned records?
    """
    return call('com.atproto.repo.listRecords', [('repo', repo), ('collection', collection), ('limit', limit), ('cursor', cursor), ('rkeyStart', rkey_start), ('rkeyEnd', rkey_end), ('reverse', reverse)], None, {})

class Record(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, value: typing.Any) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, '$type': 'com.atproto.repo.listRecords#record'}
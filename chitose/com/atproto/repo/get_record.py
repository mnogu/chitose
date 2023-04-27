from __future__ import annotations
import chitose
import typing

def get_record(service: str, headers: dict[str, str], repo: str, collection: str, rkey: str, cid: typing.Optional[str]=None):
    """Get a record."""
    return chitose.xrpc.call('com.atproto.repo.getRecord', [('repo', repo), ('collection', collection), ('rkey', rkey), ('cid', cid)], None, service, {} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_blobs(call: chitose.xrpc.XrpcCall, did: str, since: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List blob CIDs for an account, since some repo revision. Does not require auth; implemented by PDS.


    :param did: The DID of the repo.

    :param since: Optional revision of the repo to list blobs since.
    """
    return call('com.atproto.sync.listBlobs', [('did', did), ('since', since), ('limit', limit), ('cursor', cursor)], None, {})
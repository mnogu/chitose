# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_repo(call: chitose.xrpc.XrpcCall, did: str, since: typing.Optional[str]=None) -> bytes:
    """Download a repository export as CAR file. Optionally only a 'diff' since a previous revision. Does not require auth; implemented by PDS.


    :param did: The DID of the repo.

    :param since: The revision ('rev') of the repo to create a diff from.
    """
    return call('com.atproto.sync.getRepo', [('did', did), ('since', since)], None, {})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_repo(call: chitose.xrpc.XrpcCall, did: str, earliest: typing.Optional[str]=None, latest: typing.Optional[str]=None) -> bytes:
    """Gets the repo state.


    :param did: The DID of the repo.

    :param earliest: The earliest commit in the commit range (not inclusive)

    :param latest: The latest commit in the commit range (inclusive)
    """
    return call('com.atproto.sync.getRepo', [('did', did), ('earliest', earliest), ('latest', latest)], None, {})
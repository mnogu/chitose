# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_repo(call: chitose.xrpc.XrpcCall, did: str, since: typing.Optional[str]=None) -> bytes:
    """Gets the did's repo, optionally catching up from a specific revision.


    :param did: The DID of the repo.

    :param since: The revision of the repo to catch up from.
    """
    return call('com.atproto.sync.getRepo', [('did', did), ('since', since)], None, {})
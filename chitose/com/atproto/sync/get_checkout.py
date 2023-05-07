# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_checkout(service: str, headers: dict[str, str], did: str, commit: typing.Optional[str]=None) -> bytes:
    """Gets the repo state.


    :param did: The DID of the repo.

    :param commit: The commit to get the checkout from. Defaults to current HEAD.
    """
    return chitose.xrpc.call('com.atproto.sync.getCheckout', [('did', did), ('commit', commit)], None, service, {} | headers)
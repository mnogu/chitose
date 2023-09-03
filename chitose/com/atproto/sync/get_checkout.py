# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_checkout(call: chitose.xrpc.XrpcCall, did: str) -> bytes:
    """DEPRECATED - please use com.atproto.sync.getRepo instead


    :param did: The DID of the repo.
    """
    return call('com.atproto.sync.getCheckout', [('did', did)], None, {})
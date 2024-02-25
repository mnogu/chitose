# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_service_auth(call: chitose.xrpc.XrpcCall, aud: str) -> bytes:
    """Get a signed token on behalf of the requesting DID for the requested service.


    :param aud: The DID of the service that the token will be used to authenticate with
    """
    return call('com.atproto.server.getServiceAuth', [('aud', aud)], None, {})
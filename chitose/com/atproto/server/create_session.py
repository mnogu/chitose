# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _create_session(call: chitose.xrpc.XrpcCall, identifier: str, password: str) -> bytes:
    """Create an authentication session.


    :param identifier: Handle or other identifier supported by the server for the authenticating user.
    """
    return call('com.atproto.server.createSession', [], {'identifier': identifier, 'password': password}, {'Content-Type': 'application/json'})
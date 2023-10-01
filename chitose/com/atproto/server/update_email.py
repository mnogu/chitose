# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _update_email(call: chitose.xrpc.XrpcCall, email: str, token: typing.Optional[str]=None) -> bytes:
    """Update an account's email.


    :param token: Requires a token from com.atproto.sever.requestEmailUpdate if the account's email has been confirmed.
    """
    return call('com.atproto.server.updateEmail', [], {'email': email, 'token': token}, {'Content-Type': 'application/json'})
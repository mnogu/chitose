# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_service_auth(call: chitose.xrpc.XrpcCall, aud: str, exp: typing.Optional[int]=None, lxm: typing.Optional[str]=None) -> bytes:
    """Get a signed token on behalf of the requesting DID for the requested service.


    :param aud: The DID of the service that the token will be used to authenticate with

    :param exp: The time in Unix Epoch seconds that the JWT expires. Defaults to 60 seconds in the future. The service may enforce certain time bounds on tokens depending on the requested scope.

    :param lxm: Lexicon (XRPC) method to bind the requested token to
    """
    return call('com.atproto.server.getServiceAuth', [('aud', aud), ('exp', exp), ('lxm', lxm)], None, {})
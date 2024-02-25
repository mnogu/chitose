# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _sign_plc_operation(call: chitose.xrpc.XrpcCall, token: typing.Optional[str]=None, rotation_keys: typing.Optional[list[str]]=None, also_known_as: typing.Optional[list[str]]=None, verification_methods: typing.Optional[typing.Any]=None, services: typing.Optional[typing.Any]=None) -> bytes:
    """Signs a PLC operation to update some value(s) in the requesting DID's document.


    :param token: A token received through com.atproto.identity.requestPlcOperationSignature
    """
    return call('com.atproto.identity.signPlcOperation', [], {'token': token, 'rotationKeys': rotation_keys, 'alsoKnownAs': also_known_as, 'verificationMethods': verification_methods, 'services': services}, {'Content-Type': 'application/json'})
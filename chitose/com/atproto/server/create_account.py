# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_account(call: chitose.xrpc.XrpcCall, handle: str, email: typing.Optional[str]=None, did: typing.Optional[str]=None, invite_code: typing.Optional[str]=None, password: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None, plc_op: typing.Optional[typing.Any]=None) -> bytes:
    """Create an account."""
    return call('com.atproto.server.createAccount', [], {'email': email, 'handle': handle, 'did': did, 'inviteCode': invite_code, 'password': password, 'recoveryKey': recovery_key, 'plcOp': plc_op}, {'Content-Type': 'application/json'})
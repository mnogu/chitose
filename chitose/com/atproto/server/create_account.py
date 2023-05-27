# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_account(call: chitose.xrpc.XrpcCallable, email: str, handle: str, password: str, did: typing.Optional[str]=None, invite_code: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None) -> bytes:
    """Create an account."""
    return call('com.atproto.server.createAccount', [], {'email': email, 'handle': handle, 'did': did, 'inviteCode': invite_code, 'password': password, 'recoveryKey': recovery_key}, {'Content-Type': 'application/json'})
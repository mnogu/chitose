# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_account(service: str, headers: dict[str, str], email: str, handle: str, password: str, invite_code: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None) -> bytes:
    """Create an account."""
    return chitose.xrpc.call('com.atproto.server.createAccount', [], {'email': email, 'handle': handle, 'inviteCode': invite_code, 'password': password, 'recoveryKey': recovery_key}, service, {'Content-Type': 'application/json'} | headers)
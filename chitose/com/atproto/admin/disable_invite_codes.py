# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _disable_invite_codes(call: chitose.xrpc.XrpcCallable, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None) -> bytes:
    """Disable some set of codes and/or all codes associated with a set of users"""
    return call('com.atproto.admin.disableInviteCodes', [], {'codes': codes, 'accounts': accounts}, {'Content-Type': 'application/json'})
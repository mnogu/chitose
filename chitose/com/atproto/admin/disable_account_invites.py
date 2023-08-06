# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _disable_account_invites(call: chitose.xrpc.XrpcCall, account: str, note: typing.Optional[str]=None) -> bytes:
    """Disable an account from receiving new invite codes, but does not invalidate existing codes


    :param note: Additionally add a note describing why the invites were disabled
    """
    return call('com.atproto.admin.disableAccountInvites', [], {'account': account, 'note': note}, {'Content-Type': 'application/json'})
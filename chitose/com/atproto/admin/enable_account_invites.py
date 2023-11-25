# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _enable_account_invites(call: chitose.xrpc.XrpcCall, account: str, note: typing.Optional[str]=None) -> bytes:
    """Re-enable an account's ability to receive invite codes.


    :param note: Optional reason for enabled invites.
    """
    return call('com.atproto.admin.enableAccountInvites', [], {'account': account, 'note': note}, {'Content-Type': 'application/json'})
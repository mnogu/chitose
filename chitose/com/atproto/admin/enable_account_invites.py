# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _enable_account_invites(call: chitose.xrpc.XrpcCall, account: str, note: typing.Optional[str]=None) -> bytes:
    """Re-enable an accounts ability to receive invite codes


    :param note: Additionally add a note describing why the invites were enabled
    """
    return call('com.atproto.admin.enableAccountInvites', [], {'account': account, 'note': note}, {'Content-Type': 'application/json'})
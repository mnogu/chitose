# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_account_email(call: chitose.xrpc.XrpcCall, account: str, email: str) -> bytes:
    """Administrative action to update an account's email


    :param account: The handle or DID of the repo.
    """
    return call('com.atproto.admin.updateAccountEmail', [], {'account': account, 'email': email}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _update_account_email(service: str, headers: dict[str, str], account: str, email: str) -> bytes:
    """Administrative action to update an account's email


    :param account: The handle or DID of the repo.
    """
    return chitose.xrpc.call('com.atproto.admin.updateAccountEmail', [], {'account': account, 'email': email}, service, {'Content-Type': 'application/json'} | headers)
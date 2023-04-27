# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def update_account_email(service: str, headers: dict[str, str], account: str, email: str):
    """Administrative action to update an account's email"""
    return chitose.xrpc.call('com.atproto.admin.updateAccountEmail', [], {'account': account, 'email': email}, service, {'Content-Type': 'application/json'} | headers)
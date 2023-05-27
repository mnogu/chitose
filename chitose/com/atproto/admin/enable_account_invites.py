# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _enable_account_invites(call: chitose.xrpc.XrpcCallable, account: str) -> bytes:
    """Re-enable an accounts ability to receive invite codes"""
    return call('com.atproto.admin.enableAccountInvites', [], {'account': account}, {'Content-Type': 'application/json'})
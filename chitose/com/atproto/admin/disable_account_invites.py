# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _disable_account_invites(call: chitose.xrpc.XrpcCall, account: str) -> bytes:
    """Disable an account from receiving new invite codes, but does not invalidate existing codes"""
    return call('com.atproto.admin.disableAccountInvites', [], {'account': account}, {'Content-Type': 'application/json'})
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _disable_account_invites(service: str, headers: dict[str, str], account: str) -> bytes:
    """Disable an account from receiving new invite codes, but does not invalidate existing codes"""
    return chitose.xrpc.call('com.atproto.admin.disableAccountInvites', [], {'account': account}, service, {'Content-Type': 'application/json'} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _enable_account_invites(service: str, headers: dict[str, str], account: str) -> bytes:
    """Re-enable an accounts ability to receive invite codes"""
    return chitose.xrpc.call('com.atproto.admin.enableAccountInvites', [], {'account': account}, service, {'Content-Type': 'application/json'} | headers)
# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _activate_account(call: chitose.xrpc.XrpcCall) -> bytes:
    """Activates a currently deactivated account. Used to finalize account migration after the account's repo is imported and identity is setup."""
    return call('com.atproto.server.activateAccount', [], {}, {})
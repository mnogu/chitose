# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _check_account_status(call: chitose.xrpc.XrpcCall) -> bytes:
    """Returns the status of an account, especially as pertaining to import or recovery. Can be called many times over the course of an account migration. Requires auth and can only be called pertaining to oneself."""
    return call('com.atproto.server.checkAccountStatus', [], None, {})
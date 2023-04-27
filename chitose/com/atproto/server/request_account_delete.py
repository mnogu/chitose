# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def request_account_delete(service: str, headers: dict[str, str]):
    """Initiate a user account deletion via email."""
    return chitose.xrpc.call('com.atproto.server.requestAccountDelete', [], {}, service, {} | headers)
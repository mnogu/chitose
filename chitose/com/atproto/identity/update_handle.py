# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def update_handle(service: str, headers: dict[str, str], handle: str):
    """Updates the handle of the account"""
    return chitose.xrpc.call('com.atproto.identity.updateHandle', [], {'handle': handle}, service, {'Content-Type': 'application/json'} | headers)
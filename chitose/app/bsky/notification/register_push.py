# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _register_push(call: chitose.xrpc.XrpcCall, service_did: str, token: str, platform: typing.Literal['ios', 'android', 'web'], app_id: str) -> bytes:
    """Register to receive push notifications, via a specified service, for the requesting account. Requires auth."""
    return call('app.bsky.notification.registerPush', [], {'serviceDid': service_did, 'token': token, 'platform': platform, 'appId': app_id}, {'Content-Type': 'application/json'})
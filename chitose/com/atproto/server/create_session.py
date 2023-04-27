# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def create_session(service: str, headers: dict[str, str], identifier: str, password: str):
    """Create an authentication session."""
    return chitose.xrpc.call('com.atproto.server.createSession', [], {'identifier': identifier, 'password': password}, service, {'Content-Type': 'application/json'} | headers)
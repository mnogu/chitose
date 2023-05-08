# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _create_app_password(service: str, headers: dict[str, str], name: str) -> bytes:
    """Create an app-specific password."""
    return chitose.xrpc.call('com.atproto.server.createAppPassword', [], {'name': name}, service, {'Content-Type': 'application/json'} | headers)

class AppPassword(chitose.Object):
    """"""

    def __init__(self, name: str, password: str, created_at: str) -> None:
        self.name = name
        self.password = password
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {'name': self.name, 'password': self.password, 'createdAt': self.created_at, '$type': 'com.atproto.server.createAppPassword#appPassword'}
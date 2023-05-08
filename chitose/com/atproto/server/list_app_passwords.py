# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _list_app_passwords(service: str, headers: dict[str, str]) -> bytes:
    """List all app-specific passwords."""
    return chitose.xrpc.call('com.atproto.server.listAppPasswords', [], None, service, {} | headers)

class AppPassword(chitose.Object):
    """"""

    def __init__(self, name: str, created_at: str) -> None:
        self.name = name
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {'name': self.name, 'createdAt': self.created_at, '$type': 'com.atproto.server.listAppPasswords#appPassword'}
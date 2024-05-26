# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_app_password(call: chitose.xrpc.XrpcCall, name: str, privileged: typing.Optional[bool]=None) -> bytes:
    """Create an App Password.


    :param name: A short name for the App Password, to help distinguish them.

    :param privileged: If an app password has 'privileged' access to possibly sensitive account state. Meant for use with trusted clients.
    """
    return call('com.atproto.server.createAppPassword', [], {'name': name, 'privileged': privileged}, {'Content-Type': 'application/json'})

class AppPassword(chitose.Object):
    """"""

    def __init__(self, name: str, password: str, created_at: str, privileged: typing.Optional[bool]=None) -> None:
        self.name = name
        self.password = password
        self.created_at = created_at
        self.privileged = privileged

    def to_dict(self) -> dict[str, typing.Any]:
        return {'name': self.name, 'password': self.password, 'createdAt': self.created_at, 'privileged': self.privileged, '$type': 'com.atproto.server.createAppPassword#appPassword'}
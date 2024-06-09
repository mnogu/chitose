# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_config(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get details about ozone's server configuration."""
    return call('tools.ozone.server.getConfig', [], None, {})

class ServiceConfig(chitose.Object):
    """"""

    def __init__(self, url: typing.Optional[str]=None) -> None:
        self.url = url

    def to_dict(self) -> dict[str, typing.Any]:
        return {'url': self.url, '$type': 'tools.ozone.server.getConfig#serviceConfig'}

class ViewerConfig(chitose.Object):
    """"""

    def __init__(self, role: typing.Optional[typing.Literal['tools.ozone.team.defs#roleAdmin', 'tools.ozone.team.defs#roleModerator', 'tools.ozone.team.defs#roleTriage']]=None) -> None:
        self.role = role

    def to_dict(self) -> dict[str, typing.Any]:
        return {'role': self.role, '$type': 'tools.ozone.server.getConfig#viewerConfig'}
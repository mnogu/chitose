# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _describe_server(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get a document describing the service's accounts configuration."""
    return call('com.atproto.server.describeServer', [], None, {})

class Links(chitose.Object):
    """"""

    def __init__(self, privacy_policy: typing.Optional[str]=None, terms_of_service: typing.Optional[str]=None) -> None:
        self.privacy_policy = privacy_policy
        self.terms_of_service = terms_of_service

    def to_dict(self) -> dict[str, typing.Any]:
        return {'privacyPolicy': self.privacy_policy, 'termsOfService': self.terms_of_service, '$type': 'com.atproto.server.describeServer#links'}
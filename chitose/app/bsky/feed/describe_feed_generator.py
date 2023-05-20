# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _describe_feed_generator(service: str, headers: dict[str, str]) -> bytes:
    """Returns information about a given feed generator including TOS & offered feed URIs"""
    return chitose.xrpc.call('app.bsky.feed.describeFeedGenerator', [], None, service, {} | headers)

class Feed(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict:
        return {'uri': self.uri, '$type': 'app.bsky.feed.describeFeedGenerator#feed'}

class Links(chitose.Object):
    """"""

    def __init__(self, privacy_policy: typing.Optional[str]=None, terms_of_service: typing.Optional[str]=None) -> None:
        self.privacy_policy = privacy_policy
        self.terms_of_service = terms_of_service

    def to_dict(self) -> dict:
        return {'privacyPolicy': self.privacy_policy, 'termsOfService': self.terms_of_service, '$type': 'app.bsky.feed.describeFeedGenerator#links'}
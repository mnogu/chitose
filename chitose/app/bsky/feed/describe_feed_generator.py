# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _describe_feed_generator(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get information about a feed generator, including policies and offered feed URIs. Does not require auth; implemented by Feed Generator services (not App View)."""
    return call('app.bsky.feed.describeFeedGenerator', [], None, {})

class Feed(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'app.bsky.feed.describeFeedGenerator#feed'}

class Links(chitose.Object):
    """"""

    def __init__(self, privacy_policy: typing.Optional[str]=None, terms_of_service: typing.Optional[str]=None) -> None:
        self.privacy_policy = privacy_policy
        self.terms_of_service = terms_of_service

    def to_dict(self) -> dict[str, typing.Any]:
        return {'privacyPolicy': self.privacy_policy, 'termsOfService': self.terms_of_service, '$type': 'app.bsky.feed.describeFeedGenerator#links'}
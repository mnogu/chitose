# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_actor_metadata(call: chitose.xrpc.XrpcCall, actor: str) -> bytes:
    """"""
    return call('chat.bsky.moderation.getActorMetadata', [('actor', actor)], None, {})

class Metadata(chitose.Object):
    """"""

    def __init__(self, messages_sent: int, messages_received: int, convos: int, convos_started: int) -> None:
        self.messages_sent = messages_sent
        self.messages_received = messages_received
        self.convos = convos
        self.convos_started = convos_started

    def to_dict(self) -> dict[str, typing.Any]:
        return {'messagesSent': self.messages_sent, 'messagesReceived': self.messages_received, 'convos': self.convos, 'convosStarted': self.convos_started, '$type': 'chat.bsky.moderation.getActorMetadata#metadata'}
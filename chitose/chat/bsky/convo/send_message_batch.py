# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.chat.bsky.convo.defs
import chitose.chat.bsky.convo.send_message_batch
import typing

def _send_message_batch(call: chitose.xrpc.XrpcCall, items: list[chitose.chat.bsky.convo.send_message_batch.BatchItem]) -> bytes:
    """"""
    return call('chat.bsky.convo.sendMessageBatch', [], {'items': items}, {'Content-Type': 'application/json'})

class BatchItem(chitose.Object):
    """"""

    def __init__(self, convo_id: str, message: chitose.chat.bsky.convo.defs.Message) -> None:
        self.convo_id = convo_id
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'convoId': self.convo_id, 'message': self.message, '$type': 'chat.bsky.convo.sendMessageBatch#batchItem'}
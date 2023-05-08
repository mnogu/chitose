# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.label.defs
import typing

class Labels(chitose.Object):
    """"""

    def __init__(self, seq: int, labels: list[chitose.com.atproto.label.defs.Label]) -> None:
        self.seq = seq
        self.labels = labels

    def to_dict(self) -> dict:
        return {'seq': self.seq, 'labels': self.labels, '$type': 'com.atproto.label.subscribeLabels#labels'}

class Info(chitose.Object):
    """"""

    def __init__(self, name: str, message: typing.Optional[str]=None) -> None:
        self.name = name
        self.message = message

    def to_dict(self) -> dict:
        return {'name': self.name, 'message': self.message, '$type': 'com.atproto.label.subscribeLabels#info'}
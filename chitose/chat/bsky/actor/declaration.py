# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Declaration(chitose.Record):
    """"""

    def __init__(self, allow_incoming: typing.Literal['all', 'none', 'following']) -> None:
        self.allow_incoming = allow_incoming

    def to_dict(self) -> dict[str, typing.Any]:
        return {'allowIncoming': self.allow_incoming, '$type': 'chat.bsky.actor.declaration'}
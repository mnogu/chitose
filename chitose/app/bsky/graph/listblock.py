# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Listblock(chitose.Record):
    """


    :param subject: Reference (AT-URI) to the mod list record.
    """

    def __init__(self, subject: str, created_at: str) -> None:
        self.subject = subject
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subject': self.subject, 'createdAt': self.created_at, '$type': 'app.bsky.graph.listblock'}
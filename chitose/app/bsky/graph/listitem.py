# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Listitem(chitose.Record):
    """


    :param subject: The account which is included on the list.

    :param list: Reference (AT-URI) to the list record (app.bsky.graph.list).
    """

    def __init__(self, subject: str, list: str, created_at: str) -> None:
        self.subject = subject
        self.list = list
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subject': self.subject, 'list': self.list, 'createdAt': self.created_at, '$type': 'app.bsky.graph.listitem'}
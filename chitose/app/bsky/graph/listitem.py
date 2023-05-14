# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

class Listitem(chitose.Record):
    """"""

    def __init__(self, subject: str, list: str, created_at: str) -> None:
        self.subject = subject
        self.list = list
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {'subject': self.subject, 'list': self.list, 'createdAt': self.created_at, '$type': 'app.bsky.graph.listitem'}
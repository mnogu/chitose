# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class CommitMeta(chitose.Object):
    """"""

    def __init__(self, cid: str, rev: str) -> None:
        self.cid = cid
        self.rev = rev

    def to_dict(self) -> dict[str, typing.Any]:
        return {'cid': self.cid, 'rev': self.rev, '$type': 'com.atproto.repo.defs#commitMeta'}
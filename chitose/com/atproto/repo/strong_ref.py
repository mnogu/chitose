# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

class StrongRef(chitose.Object):

    def __init__(self, uri: str, cid: str) -> None:
        self.uri = uri
        self.cid = cid

    def to_dict(self):
        return {'uri': self.uri, 'cid': self.cid}
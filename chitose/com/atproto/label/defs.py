# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class Label(chitose.Object):

    def __init__(self, src: str, uri: str, val: str, cts: str, cid: typing.Optional[str]=None, neg: typing.Optional[str]=None) -> None:
        self.src = src
        self.uri = uri
        self.val = val
        self.cts = cts
        self.cid = cid
        self.neg = neg

    def to_dict(self):
        return {'src': self.src, 'uri': self.uri, 'val': self.val, 'cts': self.cts, 'cid': self.cid, 'neg': self.neg}
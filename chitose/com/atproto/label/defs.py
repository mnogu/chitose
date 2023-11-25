# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.label.defs
import typing

class Label(chitose.Object):
    """Metadata tag on an atproto resource (eg, repo or record).


    :param src: DID of the actor who created this label.

    :param uri: AT URI of the record, repository (account), or other resource that this label applies to.

    :param val: The short string name of the value or type of this label.

    :param cts: Timestamp when this label was created.

    :param cid: Optionally, CID specifying the specific version of 'uri' resource this label applies to.

    :param neg: If true, this is a negation label, overwriting a previous label.
    """

    def __init__(self, src: str, uri: str, val: str, cts: str, cid: typing.Optional[str]=None, neg: typing.Optional[bool]=None) -> None:
        self.src = src
        self.uri = uri
        self.val = val
        self.cts = cts
        self.cid = cid
        self.neg = neg

    def to_dict(self) -> dict[str, typing.Any]:
        return {'src': self.src, 'uri': self.uri, 'val': self.val, 'cts': self.cts, 'cid': self.cid, 'neg': self.neg, '$type': 'com.atproto.label.defs#label'}

class SelfLabels(chitose.Object):
    """Metadata tags on an atproto record, published by the author within the record."""

    def __init__(self, values: list[chitose.com.atproto.label.defs.SelfLabel]) -> None:
        self.values = values

    def to_dict(self) -> dict[str, typing.Any]:
        return {'values': self.values, '$type': 'com.atproto.label.defs#selfLabels'}

class SelfLabel(chitose.Object):
    """Metadata tag on an atproto record, published by the author within the record. Note that schemas should use #selfLabels, not #selfLabel.


    :param val: The short string name of the value or type of this label.
    """

    def __init__(self, val: str) -> None:
        self.val = val

    def to_dict(self) -> dict[str, typing.Any]:
        return {'val': self.val, '$type': 'com.atproto.label.defs#selfLabel'}
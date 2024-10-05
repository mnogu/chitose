# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class SigDetail(chitose.Object):
    """"""

    def __init__(self, property: str, value: str) -> None:
        self.property = property
        self.value = value

    def to_dict(self) -> dict[str, typing.Any]:
        return {'property': self.property, 'value': self.value, '$type': 'tools.ozone.signature.defs#sigDetail'}
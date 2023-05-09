# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .atproto import Atproto_

class Com_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    @property
    def atproto(self):
        return Atproto_(self.service, self.headers)
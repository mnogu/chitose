# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .bsky import Bsky_

class App_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    @property
    def bsky(self):
        return Bsky_(self.service, self.headers)
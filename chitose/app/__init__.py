# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .bsky import Bsky_

class App_:

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    @property
    def bsky(self):
        return Bsky_(self.service, self.headers)
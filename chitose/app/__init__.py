# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .bsky import _Bsky

class _App:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def bsky(self):
        return _Bsky(self.service, self.headers)
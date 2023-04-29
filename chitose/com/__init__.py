# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .atproto import Atproto

class Com:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    @property
    def atproto(self):
        return Atproto(self.service, self.headers)
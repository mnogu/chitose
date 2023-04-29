# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_popular import *
import chitose
import typing

class Unspecced:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_popular(self, limit: typing.Optional[int], cursor: typing.Optional[str]):
        return get_popular(self.service, self.headers, limit, cursor)
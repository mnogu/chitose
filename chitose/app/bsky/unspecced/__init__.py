# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_popular import _get_popular
from .get_popular import *

class Unspecced:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_popular(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """An unspecced view of globally popular items"""
        return _get_popular(self.service, self.headers, limit, cursor)
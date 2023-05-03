# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .query_labels import _query_labels
from .defs import *
from .query_labels import *
from .subscribe_labels import *

class _Label:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def query_labels(self, uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _query_labels(self.service, self.headers, uri_patterns, sources, limit, cursor)
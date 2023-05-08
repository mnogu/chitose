# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_popular import _get_popular
import typing

class Unspecced_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def get_popular(self, include_nsfw: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """An unspecced view of globally popular items"""
        return _get_popular(self.service, self.headers, include_nsfw, limit, cursor)
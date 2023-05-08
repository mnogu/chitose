# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .resolve_handle import _resolve_handle
from .update_handle import _update_handle
import typing

class Identity_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def update_handle(self, handle: str) -> bytes:
        """Updates the handle of the account"""
        return _update_handle(self.service, self.headers, handle)

    def resolve_handle(self, handle: typing.Optional[str]=None) -> bytes:
        """Provides the DID of a repo.


        :param handle: The handle to resolve. If not supplied, will resolve the host's own handle.
        """
        return _resolve_handle(self.service, self.headers, handle)
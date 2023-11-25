# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .resolve_handle import _resolve_handle
from .update_handle import _update_handle

class Identity_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def update_handle(self, handle: str) -> bytes:
        """Updates the handle of the account."""
        return _update_handle(self.call, handle)

    def resolve_handle(self, handle: str) -> bytes:
        """Provides the DID of a repo.


        :param handle: The handle to resolve.
        """
        return _resolve_handle(self.call, handle)